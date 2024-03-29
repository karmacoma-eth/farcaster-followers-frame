"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13onchain_event.proto"\xca\x03\n\x0cOnChainEvent\x12\x1f\n\x04type\x18\x01 \x01(\x0e2\x11.OnChainEventType\x12\x10\n\x08chain_id\x18\x02 \x01(\r\x12\x14\n\x0cblock_number\x18\x03 \x01(\r\x12\x12\n\nblock_hash\x18\x04 \x01(\x0c\x12\x17\n\x0fblock_timestamp\x18\x05 \x01(\x04\x12\x18\n\x10transaction_hash\x18\x06 \x01(\x0c\x12\x11\n\tlog_index\x18\x07 \x01(\r\x12\x0b\n\x03fid\x18\x08 \x01(\x04\x12-\n\x11signer_event_body\x18\t \x01(\x0b2\x10.SignerEventBodyH\x00\x12>\n\x1asigner_migrated_event_body\x18\n \x01(\x0b2\x18.SignerMigratedEventBodyH\x00\x126\n\x16id_register_event_body\x18\x0b \x01(\x0b2\x14.IdRegisterEventBodyH\x00\x128\n\x17storage_rent_event_body\x18\x0c \x01(\x0b2\x15.StorageRentEventBodyH\x00\x12\x10\n\x08tx_index\x18\r \x01(\r\x12\x0f\n\x07version\x18\x0e \x01(\rB\x06\n\x04body"\x7f\n\x0fSignerEventBody\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x10\n\x08key_type\x18\x02 \x01(\r\x12$\n\nevent_type\x18\x03 \x01(\x0e2\x10.SignerEventType\x12\x10\n\x08metadata\x18\x04 \x01(\x0c\x12\x15\n\rmetadata_type\x18\x05 \x01(\r"-\n\x17SignerMigratedEventBody\x12\x12\n\nmigratedAt\x18\x01 \x01(\r"s\n\x13IdRegisterEventBody\x12\n\n\x02to\x18\x01 \x01(\x0c\x12(\n\nevent_type\x18\x02 \x01(\x0e2\x14.IdRegisterEventType\x12\x0c\n\x04from\x18\x03 \x01(\x0c\x12\x18\n\x10recovery_address\x18\x04 \x01(\x0c"D\n\x14StorageRentEventBody\x12\r\n\x05payer\x18\x01 \x01(\x0c\x12\r\n\x05units\x18\x02 \x01(\r\x12\x0e\n\x06expiry\x18\x03 \x01(\r*\x97\x01\n\x10OnChainEventType\x12\x13\n\x0fEVENT_TYPE_NONE\x10\x00\x12\x15\n\x11EVENT_TYPE_SIGNER\x10\x01\x12\x1e\n\x1aEVENT_TYPE_SIGNER_MIGRATED\x10\x02\x12\x1a\n\x16EVENT_TYPE_ID_REGISTER\x10\x03\x12\x1b\n\x17EVENT_TYPE_STORAGE_RENT\x10\x04*\x89\x01\n\x0fSignerEventType\x12\x1a\n\x16SIGNER_EVENT_TYPE_NONE\x10\x00\x12\x19\n\x15SIGNER_EVENT_TYPE_ADD\x10\x01\x12\x1c\n\x18SIGNER_EVENT_TYPE_REMOVE\x10\x02\x12!\n\x1dSIGNER_EVENT_TYPE_ADMIN_RESET\x10\x03*\xac\x01\n\x13IdRegisterEventType\x12\x1f\n\x1bID_REGISTER_EVENT_TYPE_NONE\x10\x00\x12#\n\x1fID_REGISTER_EVENT_TYPE_REGISTER\x10\x01\x12#\n\x1fID_REGISTER_EVENT_TYPE_TRANSFER\x10\x02\x12*\n&ID_REGISTER_EVENT_TYPE_CHANGE_RECOVERY\x10\x03b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'onchain_event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_ONCHAINEVENTTYPE']._serialized_start = 848
    _globals['_ONCHAINEVENTTYPE']._serialized_end = 999
    _globals['_SIGNEREVENTTYPE']._serialized_start = 1002
    _globals['_SIGNEREVENTTYPE']._serialized_end = 1139
    _globals['_IDREGISTEREVENTTYPE']._serialized_start = 1142
    _globals['_IDREGISTEREVENTTYPE']._serialized_end = 1314
    _globals['_ONCHAINEVENT']._serialized_start = 24
    _globals['_ONCHAINEVENT']._serialized_end = 482
    _globals['_SIGNEREVENTBODY']._serialized_start = 484
    _globals['_SIGNEREVENTBODY']._serialized_end = 611
    _globals['_SIGNERMIGRATEDEVENTBODY']._serialized_start = 613
    _globals['_SIGNERMIGRATEDEVENTBODY']._serialized_end = 658
    _globals['_IDREGISTEREVENTBODY']._serialized_start = 660
    _globals['_IDREGISTEREVENTBODY']._serialized_end = 775
    _globals['_STORAGERENTEVENTBODY']._serialized_start = 777
    _globals['_STORAGERENTEVENTBODY']._serialized_end = 845