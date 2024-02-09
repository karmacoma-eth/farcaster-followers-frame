"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from . import username_proof_pb2 as username__proof__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x1a\x14username_proof.proto"\xcc\x01\n\x07Message\x12\x1a\n\x04data\x18\x01 \x01(\x0b2\x0c.MessageData\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12 \n\x0bhash_scheme\x18\x03 \x01(\x0e2\x0b.HashScheme\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12*\n\x10signature_scheme\x18\x05 \x01(\x0e2\x10.SignatureScheme\x12\x0e\n\x06signer\x18\x06 \x01(\x0c\x12\x17\n\ndata_bytes\x18\x07 \x01(\x0cH\x00\x88\x01\x01B\r\n\x0b_data_bytes"\x9b\x04\n\x0bMessageData\x12\x1a\n\x04type\x18\x01 \x01(\x0e2\x0c.MessageType\x12\x0b\n\x03fid\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\r\x12"\n\x07network\x18\x04 \x01(\x0e2\x11.FarcasterNetwork\x12%\n\rcast_add_body\x18\x05 \x01(\x0b2\x0c.CastAddBodyH\x00\x12+\n\x10cast_remove_body\x18\x06 \x01(\x0b2\x0f.CastRemoveBodyH\x00\x12&\n\rreaction_body\x18\x07 \x01(\x0b2\r.ReactionBodyH\x00\x12D\n\x1dverification_add_address_body\x18\t \x01(\x0b2\x1b.VerificationAddAddressBodyH\x00\x12;\n\x18verification_remove_body\x18\n \x01(\x0b2\x17.VerificationRemoveBodyH\x00\x12\'\n\x0euser_data_body\x18\x0c \x01(\x0b2\r.UserDataBodyH\x00\x12\x1e\n\tlink_body\x18\x0e \x01(\x0b2\t.LinkBodyH\x00\x12-\n\x13username_proof_body\x18\x0f \x01(\x0b2\x0e.UserNameProofH\x00\x12-\n\x11frame_action_body\x18\x10 \x01(\x0b2\x10.FrameActionBodyH\x00B\x06\n\x04body":\n\x0cUserDataBody\x12\x1b\n\x04type\x18\x01 \x01(\x0e2\r.UserDataType\x12\r\n\x05value\x18\x02 \x01(\t";\n\x05Embed\x12\r\n\x03url\x18\x01 \x01(\tH\x00\x12\x1a\n\x07cast_id\x18\x02 \x01(\x0b2\x07.CastIdH\x00B\x07\n\x05embed"\xbf\x01\n\x0bCastAddBody\x12\x19\n\x11embeds_deprecated\x18\x01 \x03(\t\x12\x10\n\x08mentions\x18\x02 \x03(\x04\x12!\n\x0eparent_cast_id\x18\x03 \x01(\x0b2\x07.CastIdH\x00\x12\x14\n\nparent_url\x18\x07 \x01(\tH\x00\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x1a\n\x12mentions_positions\x18\x05 \x03(\r\x12\x16\n\x06embeds\x18\x06 \x03(\x0b2\x06.EmbedB\x08\n\x06parent"%\n\x0eCastRemoveBody\x12\x13\n\x0btarget_hash\x18\x01 \x01(\x0c"#\n\x06CastId\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12\x0c\n\x04hash\x18\x02 \x01(\x0c"n\n\x0cReactionBody\x12\x1b\n\x04type\x18\x01 \x01(\x0e2\r.ReactionType\x12!\n\x0etarget_cast_id\x18\x02 \x01(\x0b2\x07.CastIdH\x00\x12\x14\n\ntarget_url\x18\x03 \x01(\tH\x00B\x08\n\x06target"\xa4\x01\n\x1aVerificationAddAddressBody\x12\x0f\n\x07address\x18\x01 \x01(\x0c\x12\x17\n\x0fclaim_signature\x18\x02 \x01(\x0c\x12\x12\n\nblock_hash\x18\x03 \x01(\x0c\x12\x19\n\x11verification_type\x18\x04 \x01(\r\x12\x10\n\x08chain_id\x18\x05 \x01(\r\x12\x1b\n\x08protocol\x18\x07 \x01(\x0e2\t.Protocol"F\n\x16VerificationRemoveBody\x12\x0f\n\x07address\x18\x01 \x01(\x0c\x12\x1b\n\x08protocol\x18\x02 \x01(\x0e2\t.Protocol"l\n\x08LinkBody\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x1d\n\x10displayTimestamp\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x14\n\ntarget_fid\x18\x03 \x01(\x04H\x00B\x08\n\x06targetB\x13\n\x11_displayTimestamp"b\n\x0fFrameActionBody\x12\x0b\n\x03url\x18\x01 \x01(\x0c\x12\x14\n\x0cbutton_index\x18\x02 \x01(\r\x12\x18\n\x07cast_id\x18\x03 \x01(\x0b2\x07.CastId\x12\x12\n\ninput_text\x18\x04 \x01(\x0c*:\n\nHashScheme\x12\x14\n\x10HASH_SCHEME_NONE\x10\x00\x12\x16\n\x12HASH_SCHEME_BLAKE3\x10\x01*g\n\x0fSignatureScheme\x12\x19\n\x15SIGNATURE_SCHEME_NONE\x10\x00\x12\x1c\n\x18SIGNATURE_SCHEME_ED25519\x10\x01\x12\x1b\n\x17SIGNATURE_SCHEME_EIP712\x10\x02*\x8c\x03\n\x0bMessageType\x12\x15\n\x11MESSAGE_TYPE_NONE\x10\x00\x12\x19\n\x15MESSAGE_TYPE_CAST_ADD\x10\x01\x12\x1c\n\x18MESSAGE_TYPE_CAST_REMOVE\x10\x02\x12\x1d\n\x19MESSAGE_TYPE_REACTION_ADD\x10\x03\x12 \n\x1cMESSAGE_TYPE_REACTION_REMOVE\x10\x04\x12\x19\n\x15MESSAGE_TYPE_LINK_ADD\x10\x05\x12\x1c\n\x18MESSAGE_TYPE_LINK_REMOVE\x10\x06\x12-\n)MESSAGE_TYPE_VERIFICATION_ADD_ETH_ADDRESS\x10\x07\x12$\n MESSAGE_TYPE_VERIFICATION_REMOVE\x10\x08\x12\x1e\n\x1aMESSAGE_TYPE_USER_DATA_ADD\x10\x0b\x12\x1f\n\x1bMESSAGE_TYPE_USERNAME_PROOF\x10\x0c\x12\x1d\n\x19MESSAGE_TYPE_FRAME_ACTION\x10\r*\x8a\x01\n\x10FarcasterNetwork\x12\x1a\n\x16FARCASTER_NETWORK_NONE\x10\x00\x12\x1d\n\x19FARCASTER_NETWORK_MAINNET\x10\x01\x12\x1d\n\x19FARCASTER_NETWORK_TESTNET\x10\x02\x12\x1c\n\x18FARCASTER_NETWORK_DEVNET\x10\x03*\xa8\x01\n\x0cUserDataType\x12\x17\n\x13USER_DATA_TYPE_NONE\x10\x00\x12\x16\n\x12USER_DATA_TYPE_PFP\x10\x01\x12\x1a\n\x16USER_DATA_TYPE_DISPLAY\x10\x02\x12\x16\n\x12USER_DATA_TYPE_BIO\x10\x03\x12\x16\n\x12USER_DATA_TYPE_URL\x10\x05\x12\x1b\n\x17USER_DATA_TYPE_USERNAME\x10\x06*X\n\x0cReactionType\x12\x16\n\x12REACTION_TYPE_NONE\x10\x00\x12\x16\n\x12REACTION_TYPE_LIKE\x10\x01\x12\x18\n\x14REACTION_TYPE_RECAST\x10\x02*6\n\x08Protocol\x12\x15\n\x11PROTOCOL_ETHEREUM\x10\x00\x12\x13\n\x0fPROTOCOL_SOLANA\x10\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_HASHSCHEME']._serialized_start = 1740
    _globals['_HASHSCHEME']._serialized_end = 1798
    _globals['_SIGNATURESCHEME']._serialized_start = 1800
    _globals['_SIGNATURESCHEME']._serialized_end = 1903
    _globals['_MESSAGETYPE']._serialized_start = 1906
    _globals['_MESSAGETYPE']._serialized_end = 2302
    _globals['_FARCASTERNETWORK']._serialized_start = 2305
    _globals['_FARCASTERNETWORK']._serialized_end = 2443
    _globals['_USERDATATYPE']._serialized_start = 2446
    _globals['_USERDATATYPE']._serialized_end = 2614
    _globals['_REACTIONTYPE']._serialized_start = 2616
    _globals['_REACTIONTYPE']._serialized_end = 2704
    _globals['_PROTOCOL']._serialized_start = 2706
    _globals['_PROTOCOL']._serialized_end = 2760
    _globals['_MESSAGE']._serialized_start = 40
    _globals['_MESSAGE']._serialized_end = 244
    _globals['_MESSAGEDATA']._serialized_start = 247
    _globals['_MESSAGEDATA']._serialized_end = 786
    _globals['_USERDATABODY']._serialized_start = 788
    _globals['_USERDATABODY']._serialized_end = 846
    _globals['_EMBED']._serialized_start = 848
    _globals['_EMBED']._serialized_end = 907
    _globals['_CASTADDBODY']._serialized_start = 910
    _globals['_CASTADDBODY']._serialized_end = 1101
    _globals['_CASTREMOVEBODY']._serialized_start = 1103
    _globals['_CASTREMOVEBODY']._serialized_end = 1140
    _globals['_CASTID']._serialized_start = 1142
    _globals['_CASTID']._serialized_end = 1177
    _globals['_REACTIONBODY']._serialized_start = 1179
    _globals['_REACTIONBODY']._serialized_end = 1289
    _globals['_VERIFICATIONADDADDRESSBODY']._serialized_start = 1292
    _globals['_VERIFICATIONADDADDRESSBODY']._serialized_end = 1456
    _globals['_VERIFICATIONREMOVEBODY']._serialized_start = 1458
    _globals['_VERIFICATIONREMOVEBODY']._serialized_end = 1528
    _globals['_LINKBODY']._serialized_start = 1530
    _globals['_LINKBODY']._serialized_end = 1638
    _globals['_FRAMEACTIONBODY']._serialized_start = 1640
    _globals['_FRAMEACTIONBODY']._serialized_end = 1738