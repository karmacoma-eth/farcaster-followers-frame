"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from . import message_pb2 as message__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cgossip.proto\x1a\rmessage.proto"T\n\x11GossipAddressInfo\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\x0e\n\x06family\x18\x02 \x01(\r\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x10\n\x08dns_name\x18\x04 \x01(\t"\xf6\x01\n\x16ContactInfoContentBody\x12*\n\x0egossip_address\x18\x01 \x01(\x0b2\x12.GossipAddressInfo\x12\'\n\x0brpc_address\x18\x02 \x01(\x0b2\x12.GossipAddressInfo\x12\x17\n\x0fexcluded_hashes\x18\x03 \x03(\t\x12\r\n\x05count\x18\x04 \x01(\r\x12\x13\n\x0bhub_version\x18\x05 \x01(\t\x12"\n\x07network\x18\x06 \x01(\x0e2\x11.FarcasterNetwork\x12\x13\n\x0bapp_version\x18\x07 \x01(\t\x12\x11\n\ttimestamp\x18\x08 \x01(\x04"\xe4\x02\n\x12ContactInfoContent\x12*\n\x0egossip_address\x18\x01 \x01(\x0b2\x12.GossipAddressInfo\x12\'\n\x0brpc_address\x18\x02 \x01(\x0b2\x12.GossipAddressInfo\x12\x17\n\x0fexcluded_hashes\x18\x03 \x03(\t\x12\r\n\x05count\x18\x04 \x01(\r\x12\x13\n\x0bhub_version\x18\x05 \x01(\t\x12"\n\x07network\x18\x06 \x01(\x0e2\x11.FarcasterNetwork\x12\x13\n\x0bapp_version\x18\x07 \x01(\t\x12\x11\n\ttimestamp\x18\x08 \x01(\x04\x12%\n\x04body\x18\t \x01(\x0b2\x17.ContactInfoContentBody\x12\x11\n\tsignature\x18\n \x01(\x0c\x12\x0e\n\x06signer\x18\x0b \x01(\x0c\x12\x17\n\ndata_bytes\x18\x0c \x01(\x0cH\x00\x88\x01\x01B\r\n\x0b_data_bytes"F\n\x0fPingMessageBody\x12\x1b\n\x13ping_origin_peer_id\x18\x01 \x01(\x0c\x12\x16\n\x0eping_timestamp\x18\x02 \x01(\x04"x\n\x0eAckMessageBody\x12\x1b\n\x13ping_origin_peer_id\x18\x01 \x01(\x0c\x12\x1a\n\x12ack_origin_peer_id\x18\x02 \x01(\x0c\x12\x16\n\x0eping_timestamp\x18\x03 \x01(\x04\x12\x15\n\rack_timestamp\x18\x04 \x01(\x04"q\n\x15NetworkLatencyMessage\x12(\n\x0cping_message\x18\x02 \x01(\x0b2\x10.PingMessageBodyH\x00\x12&\n\x0back_message\x18\x03 \x01(\x0b2\x0f.AckMessageBodyH\x00B\x06\n\x04body"\xe9\x01\n\rGossipMessage\x12\x1b\n\x07message\x18\x01 \x01(\x0b2\x08.MessageH\x00\x123\n\x14contact_info_content\x18\x03 \x01(\x0b2\x13.ContactInfoContentH\x00\x129\n\x17network_latency_message\x18\x07 \x01(\x0b2\x16.NetworkLatencyMessageH\x00\x12\x0e\n\x06topics\x18\x04 \x03(\t\x12\x0f\n\x07peer_id\x18\x05 \x01(\x0c\x12\x1f\n\x07version\x18\x06 \x01(\x0e2\x0e.GossipVersionB\t\n\x07content*?\n\rGossipVersion\x12\x15\n\x11GOSSIP_VERSION_V1\x10\x00\x12\x17\n\x13GOSSIP_VERSION_V1_1\x10\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gossip_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_GOSSIPVERSION']._serialized_start = 1270
    _globals['_GOSSIPVERSION']._serialized_end = 1333
    _globals['_GOSSIPADDRESSINFO']._serialized_start = 31
    _globals['_GOSSIPADDRESSINFO']._serialized_end = 115
    _globals['_CONTACTINFOCONTENTBODY']._serialized_start = 118
    _globals['_CONTACTINFOCONTENTBODY']._serialized_end = 364
    _globals['_CONTACTINFOCONTENT']._serialized_start = 367
    _globals['_CONTACTINFOCONTENT']._serialized_end = 723
    _globals['_PINGMESSAGEBODY']._serialized_start = 725
    _globals['_PINGMESSAGEBODY']._serialized_end = 795
    _globals['_ACKMESSAGEBODY']._serialized_start = 797
    _globals['_ACKMESSAGEBODY']._serialized_end = 917
    _globals['_NETWORKLATENCYMESSAGE']._serialized_start = 919
    _globals['_NETWORKLATENCYMESSAGE']._serialized_end = 1032
    _globals['_GOSSIPMESSAGE']._serialized_start = 1035
    _globals['_GOSSIPMESSAGE']._serialized_end = 1268