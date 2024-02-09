import grpc
import json
import logging
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

from dotenv import load_dotenv
from fff.grpc import rpc_pb2_grpc as hub
from fff.grpc.request_response_pb2 import LinksByTargetRequest, MessagesResponse, UserDataRequest
from fff.grpc.message_pb2 import MESSAGE_TYPE_LINK_ADD, MESSAGE_TYPE_LINK_REMOVE, FARCASTER_NETWORK_MAINNET, USER_DATA_TYPE_DISPLAY
from io import BytesIO

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def from_json_data(data: dict) -> pd.Series:
    follower_counts = dict()
    follower_count = 0

    messages = data['messages']
    logger.info(f'Loaded {len(messages)} messages')

    for message in messages:
        data = message['data']
        if data['network'] != 'FARCASTER_NETWORK_MAINNET':
            logger.warn(f'Skipping message for network {data['network']} in {message}')
            continue

        message_type = data['type']
        if message_type == 'MESSAGE_TYPE_LINK_ADD':
            follower_count += 1
        elif message_type == 'MESSAGE_TYPE_LINK_REMOVE':
            follower_count -= 1
        else:
            logger.warn(f'Unknown message type {message_type} in {message}')

        if follower_count < 0:
            logger.error(f'Negative follower count: {follower_count}')

        timestamp = pd.to_datetime(data['timestamp'], unit='s')
        follower_counts[timestamp] = follower_count

    # turn into a pandas series and sort by index
    return pd.Series(follower_counts).sort_index()


def from_json_file(input_filename: str) -> pd.Series:
    with open(input_filename) as f:
        data = json.load(f)
        return from_json_data(data)


def from_grpc_data(response: MessagesResponse, follower_count = 0) -> pd.Series:
    follower_counts = dict()

    messages = response.messages
    logger.info(f'Loaded {len(messages)} messages')

    for message in messages:
        data = message.data

        if data.network != FARCASTER_NETWORK_MAINNET:
            logger.warn(f'Skipping message for network {data.network} in {message}')
            continue

        message_type = data.type
        if message_type == MESSAGE_TYPE_LINK_ADD:
            follower_count += 1
        elif message_type == MESSAGE_TYPE_LINK_REMOVE:
            logger.info(f'lost a follower in {message}')
            follower_count -= 1
        else:
            logger.warn(f'Unknown message type {message_type} in {message}')

        if follower_count < 0:
            logger.error(f'Negative follower count: {follower_count}')

        timestamp = pd.to_datetime(data.timestamp, unit='s')
        follower_counts[timestamp] = follower_count

    # turn into a pandas series and sort by index
    return pd.Series(follower_counts).sort_index()


def get_hub_rpc() -> str:
    hub_rpc = os.getenv('HUB_RPC', None)
    if not hub_rpc:
        raise ValueError('HUB_RPC environment variable not set')

    return hub_rpc


def from_grpc(fid: int) -> pd.Series:
    series = []
    with grpc.insecure_channel(get_hub_rpc()) as channel:
        stub = hub.HubServiceStub(channel)
        page_token = None
        follower_count = 0

        while True:
            request = LinksByTargetRequest(target_fid=fid, page_token=page_token)
            response: MessagesResponse = stub.GetLinksByTarget(request)
            series.append(from_grpc_data(response, follower_count))

            if page_token := response.next_page_token:
                follower_count += len(response.messages)
                continue

            break

    return pd.concat(series)


def generate_png(data: pd.Series, title: str) -> BytesIO:
    sns.set_style("whitegrid")
    sns.set_context("talk")
    sns.despine(left=True, bottom=True)

    # Create the plot
    figure_size_inches = 8
    plt.figure(figsize=(figure_size_inches, figure_size_inches))
    plt.fill_between(data.index, data, color="green", alpha=0.3)  # Fill under the line
    plt.plot(data.index, data, color="green", linewidth=2)  # Smooth line

    plt.title(title)
    # plt.gca().set_facecolor('#333333')  # Set background color
    plt.grid(False)  # No grid
    plt.xticks([])  # No x-axis ticks
    plt.box(False)  # No box around the plot

    plt.tight_layout()

    # Target size in pixels divided by figure size in inches
    dpi = 1024 / figure_size_inches

    buffer = BytesIO()
    plt.savefig(buffer, dpi=dpi, bbox_inches='tight', format='png')
    buffer.seek(0)
    return buffer


# example response:
#
#   data {
#     type: MESSAGE_TYPE_USER_DATA_ADD
#     fid: 10502
#     timestamp: 97867817
#     network: FARCASTER_NETWORK_MAINNET
#     user_data_body {
#       type: USER_DATA_TYPE_DISPLAY
#       value: "karmacoma"
#     }
#   }
#
def get_username(fid: int) -> str:
    with grpc.insecure_channel(get_hub_rpc()) as channel:
        stub = hub.HubServiceStub(channel)
        request = UserDataRequest(fid=fid, user_data_type=USER_DATA_TYPE_DISPLAY)
        response = stub.GetUserData(request)
        return response.data.user_data_body.value


def main():
    import sys

    user_input = sys.argv[1]
    dataset = from_json_file(user_input) if os.path.exists(user_input) else from_grpc(int(user_input))

    title = f'Follower count for {user_input}'
    output_filename = user_input.replace('.json', '.png')

    buffer = generate_png(dataset, title)
    with open(output_filename, 'wb') as f:
        f.write(buffer.read())
    print(f'Output written to {output_filename}')


if __name__ == '__main__':
    main()

