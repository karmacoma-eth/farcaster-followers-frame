"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsync_trie.proto"J\n\nDbTrieNode\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x12\n\nchildChars\x18\x02 \x03(\r\x12\r\n\x05items\x18\x03 \x01(\r\x12\x0c\n\x04hash\x18\x04 \x01(\x0cb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sync_trie_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_DBTRIENODE']._serialized_start = 19
    _globals['_DBTRIENODE']._serialized_end = 93