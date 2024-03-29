"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from . import message_pb2 as message__pb2
from . import onchain_event_pb2 as onchain__event__pb2
from . import username_proof_pb2 as username__proof__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fhub_event.proto\x1a\rmessage.proto\x1a\x13onchain_event.proto\x1a\x14username_proof.proto"Q\n\x10MergeMessageBody\x12\x19\n\x07message\x18\x01 \x01(\x0b2\x08.Message\x12"\n\x10deleted_messages\x18\x02 \x03(\x0b2\x08.Message"-\n\x10PruneMessageBody\x12\x19\n\x07message\x18\x01 \x01(\x0b2\x08.Message".\n\x11RevokeMessageBody\x12\x19\n\x07message\x18\x01 \x01(\x0b2\x08.Message">\n\x15MergeOnChainEventBody\x12%\n\x0eon_chain_event\x18\x01 \x01(\x0b2\r.OnChainEvent"\xcc\x01\n\x16MergeUserNameProofBody\x12&\n\x0eusername_proof\x18\x01 \x01(\x0b2\x0e.UserNameProof\x12.\n\x16deleted_username_proof\x18\x02 \x01(\x0b2\x0e.UserNameProof\x12(\n\x16username_proof_message\x18\x03 \x01(\x0b2\x08.Message\x120\n\x1edeleted_username_proof_message\x18\x04 \x01(\x0b2\x08.Message"\xcb\x02\n\x08HubEvent\x12\x1b\n\x04type\x18\x01 \x01(\x0e2\r.HubEventType\x12\n\n\x02id\x18\x02 \x01(\x04\x12/\n\x12merge_message_body\x18\x03 \x01(\x0b2\x11.MergeMessageBodyH\x00\x12/\n\x12prune_message_body\x18\x04 \x01(\x0b2\x11.PruneMessageBodyH\x00\x121\n\x13revoke_message_body\x18\x05 \x01(\x0b2\x12.RevokeMessageBodyH\x00\x12<\n\x19merge_username_proof_body\x18\x08 \x01(\x0b2\x17.MergeUserNameProofBodyH\x00\x12;\n\x19merge_on_chain_event_body\x18\x0b \x01(\x0b2\x16.MergeOnChainEventBodyH\x00B\x06\n\x04body*\xe0\x01\n\x0cHubEventType\x12\x17\n\x13HUB_EVENT_TYPE_NONE\x10\x00\x12 \n\x1cHUB_EVENT_TYPE_MERGE_MESSAGE\x10\x01\x12 \n\x1cHUB_EVENT_TYPE_PRUNE_MESSAGE\x10\x02\x12!\n\x1dHUB_EVENT_TYPE_REVOKE_MESSAGE\x10\x03\x12\'\n#HUB_EVENT_TYPE_MERGE_USERNAME_PROOF\x10\x06\x12\'\n#HUB_EVENT_TYPE_MERGE_ON_CHAIN_EVENT\x10\tb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hub_event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_HUBEVENTTYPE']._serialized_start = 861
    _globals['_HUBEVENTTYPE']._serialized_end = 1085
    _globals['_MERGEMESSAGEBODY']._serialized_start = 77
    _globals['_MERGEMESSAGEBODY']._serialized_end = 158
    _globals['_PRUNEMESSAGEBODY']._serialized_start = 160
    _globals['_PRUNEMESSAGEBODY']._serialized_end = 205
    _globals['_REVOKEMESSAGEBODY']._serialized_start = 207
    _globals['_REVOKEMESSAGEBODY']._serialized_end = 253
    _globals['_MERGEONCHAINEVENTBODY']._serialized_start = 255
    _globals['_MERGEONCHAINEVENTBODY']._serialized_end = 317
    _globals['_MERGEUSERNAMEPROOFBODY']._serialized_start = 320
    _globals['_MERGEUSERNAMEPROOFBODY']._serialized_end = 524
    _globals['_HUBEVENT']._serialized_start = 527
    _globals['_HUBEVENT']._serialized_end = 858