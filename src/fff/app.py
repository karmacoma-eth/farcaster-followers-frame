import json
import logging
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

MESSAGE_TYPE_LINK_ADD = 'MESSAGE_TYPE_LINK_ADD'
MESSAGE_TYPE_LINK_REMOVE = 'MESSAGE_TYPE_LINK_REMOVE'
FARCASTER_NETWORK_MAINNET = 'FARCASTER_NETWORK_MAINNET'

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    import sys

    input_file = sys.argv[1]

    follower_counts = dict()
    follower_count = 0

    with open(input_file) as f:
        data = json.load(f)
        messages = data['messages']
        logger.info(f'Loaded {len(messages)} messages')
        for item in messages:
            data = item['data']

            if data['network'] != FARCASTER_NETWORK_MAINNET:
                continue

            item_type = data['type']
            if item_type == MESSAGE_TYPE_LINK_ADD:
                follower_count += 1
            elif item_type == MESSAGE_TYPE_LINK_REMOVE:
                follower_count -= 1
            else:
                logger.warn(f'Unknown message type {item_type} in {item}')

            if follower_count < 0:
                logger.error(f'Negative follower count: {follower_count}')

            timestamp = pd.to_datetime(data['timestamp'], unit='s')
            follower_counts[timestamp] = follower_count

    # turn into a pandas series and sort by index
    dataset = pd.Series(follower_counts).sort_index()

    sns.set_style("whitegrid")
    sns.set_context("talk")
    # sns.lineplot(data=dataset, marker=None)
    sns.despine(left=True, bottom=True)

    # Create the plot
    figure_size_inches = 8
    plt.figure(figsize=(figure_size_inches, figure_size_inches))
    plt.fill_between(dataset.index, dataset, color="green", alpha=0.3)  # Fill under the line
    plt.plot(dataset.index, dataset, color="green", linewidth=2)  # Smooth line

    plt.title("karma's followers")  # Title of the graph
    # plt.gca().set_facecolor('#333333')  # Set background color
    plt.grid(False)  # No grid
    plt.xticks([])  # No x-axis ticks
    # plt.yticks([])  # No y-axis ticks
    plt.box(False)  # No box around the plot

    plt.tight_layout()

    # Target size in pixels divided by figure size in inches
    dpi = 1024 / figure_size_inches
    output_filename = input_file.replace('.json', '.png')
    plt.savefig(output_filename, dpi=dpi, bbox_inches='tight', format='png')
    print(f'Output written to {output_filename}')
    # plt.show()


if __name__ == '__main__':
    main()
