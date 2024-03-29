"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from . import message_pb2 as message__pb2
from . import onchain_event_pb2 as onchain__event__pb2
from . import hub_event_pb2 as hub__event__pb2
from . import username_proof_pb2 as username__proof__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16request_response.proto\x1a\rmessage.proto\x1a\x13onchain_event.proto\x1a\x0fhub_event.proto\x1a\x14username_proof.proto"\x07\n\x05Empty"X\n\x10SubscribeRequest\x12"\n\x0bevent_types\x18\x01 \x03(\x0e2\r.HubEventType\x12\x14\n\x07from_id\x18\x02 \x01(\x04H\x00\x88\x01\x01B\n\n\x08_from_id"\x1a\n\x0cEventRequest\x12\n\n\x02id\x18\x01 \x01(\x04""\n\x0eHubInfoRequest\x12\x10\n\x08db_stats\x18\x01 \x01(\x08"\xa1\x01\n\x0fHubInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x12\n\nis_syncing\x18\x02 \x01(\x08\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\x11\n\troot_hash\x18\x04 \x01(\t\x12\x1a\n\x08db_stats\x18\x05 \x01(\x0b2\x08.DbStats\x12\x0e\n\x06peerId\x18\x06 \x01(\t\x12\x18\n\x10hub_operator_fid\x18\x07 \x01(\x04"Q\n\x07DbStats\x12\x14\n\x0cnum_messages\x18\x01 \x01(\x04\x12\x16\n\x0enum_fid_events\x18\x02 \x01(\x04\x12\x18\n\x10num_fname_events\x18\x03 \x01(\x04"3\n\x11SyncStatusRequest\x12\x13\n\x06peerId\x18\x01 \x01(\tH\x00\x88\x01\x01B\t\n\x07_peerId"b\n\x12SyncStatusResponse\x12\x12\n\nis_syncing\x18\x01 \x01(\x08\x12 \n\x0bsync_status\x18\x02 \x03(\x0b2\x0b.SyncStatus\x12\x16\n\x0eengine_started\x18\x03 \x01(\x08"\xc8\x01\n\nSyncStatus\x12\x0e\n\x06peerId\x18\x01 \x01(\t\x12\x0e\n\x06inSync\x18\x02 \x01(\t\x12\x12\n\nshouldSync\x18\x03 \x01(\x08\x12\x18\n\x10divergencePrefix\x18\x04 \x01(\t\x12\x1c\n\x14divergenceSecondsAgo\x18\x05 \x01(\x05\x12\x15\n\rtheirMessages\x18\x06 \x01(\x04\x12\x13\n\x0bourMessages\x18\x07 \x01(\x04\x12\x13\n\x0blastBadSync\x18\x08 \x01(\x03\x12\r\n\x05score\x18\t \x01(\x03"{\n\x18TrieNodeMetadataResponse\x12\x0e\n\x06prefix\x18\x01 \x01(\x0c\x12\x14\n\x0cnum_messages\x18\x02 \x01(\x04\x12\x0c\n\x04hash\x18\x03 \x01(\t\x12+\n\x08children\x18\x04 \x03(\x0b2\x19.TrieNodeMetadataResponse"l\n\x18TrieNodeSnapshotResponse\x12\x0e\n\x06prefix\x18\x01 \x01(\x0c\x12\x17\n\x0fexcluded_hashes\x18\x02 \x03(\t\x12\x14\n\x0cnum_messages\x18\x03 \x01(\x04\x12\x11\n\troot_hash\x18\x04 \x01(\t" \n\x0eTrieNodePrefix\x12\x0e\n\x06prefix\x18\x01 \x01(\x0c"\x1b\n\x07SyncIds\x12\x10\n\x08sync_ids\x18\x01 \x03(\x0c"\x89\x01\n\nFidRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12\x16\n\tpage_size\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x17\n\npage_token\x18\x03 \x01(\x0cH\x01\x88\x01\x01\x12\x14\n\x07reverse\x18\x04 \x01(\x08H\x02\x88\x01\x01B\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse"}\n\x0bFidsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x17\n\npage_token\x18\x02 \x01(\x0cH\x01\x88\x01\x01\x12\x14\n\x07reverse\x18\x03 \x01(\x08H\x02\x88\x01\x01B\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse"N\n\x0cFidsResponse\x12\x0c\n\x04fids\x18\x01 \x03(\x04\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\x0cH\x00\x88\x01\x01B\x12\n\x10_next_page_token"`\n\x10MessagesResponse\x12\x1a\n\x08messages\x18\x01 \x03(\x0b2\x08.Message\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\x0cH\x00\x88\x01\x01B\x12\n\x10_next_page_token"\xc9\x01\n\x14CastsByParentRequest\x12!\n\x0eparent_cast_id\x18\x01 \x01(\x0b2\x07.CastIdH\x00\x12\x14\n\nparent_url\x18\x05 \x01(\tH\x00\x12\x16\n\tpage_size\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x17\n\npage_token\x18\x03 \x01(\x0cH\x02\x88\x01\x01\x12\x14\n\x07reverse\x18\x04 \x01(\x08H\x03\x88\x01\x01B\x08\n\x06parentB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse"\x87\x01\n\x0fReactionRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12$\n\rreaction_type\x18\x02 \x01(\x0e2\r.ReactionType\x12!\n\x0etarget_cast_id\x18\x03 \x01(\x0b2\x07.CastIdH\x00\x12\x14\n\ntarget_url\x18\x04 \x01(\tH\x00B\x08\n\x06target"\xd1\x01\n\x15ReactionsByFidRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12)\n\rreaction_type\x18\x02 \x01(\x0e2\r.ReactionTypeH\x00\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x02\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x03\x88\x01\x01B\x10\n\x0e_reaction_typeB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse"\x8a\x02\n\x18ReactionsByTargetRequest\x12!\n\x0etarget_cast_id\x18\x01 \x01(\x0b2\x07.CastIdH\x00\x12\x14\n\ntarget_url\x18\x06 \x01(\tH\x00\x12)\n\rreaction_type\x18\x02 \x01(\x0e2\r.ReactionTypeH\x01\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x03\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x04\x88\x01\x01B\x08\n\x06targetB\x10\n\x0e_reaction_typeB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse"E\n\x0fUserDataRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12%\n\x0euser_data_type\x18\x02 \x01(\x0e2\r.UserDataType"(\n\x18NameRegistryEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\x0c"(\n\x19RentRegistryEventsRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04"\xb9\x01\n\x13OnChainEventRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12%\n\nevent_type\x18\x02 \x01(\x0e2\x11.OnChainEventType\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x00\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x01\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x02\x88\x01\x01B\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse"g\n\x14OnChainEventResponse\x12\x1d\n\x06events\x18\x01 \x03(\x0b2\r.OnChainEvent\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\x0cH\x00\x88\x01\x01B\x12\n\x10_next_page_token"E\n\x15StorageLimitsResponse\x12\x1d\n\x06limits\x18\x01 \x03(\x0b2\r.StorageLimit\x12\r\n\x05units\x18\x02 \x01(\r"\x8a\x01\n\x0cStorageLimit\x12\x1e\n\nstore_type\x18\x01 \x01(\x0e2\n.StoreType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x04\x12\x0c\n\x04used\x18\x04 \x01(\x04\x12\x19\n\x11earliestTimestamp\x18\x05 \x01(\x04\x12\x14\n\x0cearliestHash\x18\x06 \x01(\x0c"$\n\x14UsernameProofRequest\x12\x0c\n\x04name\x18\x01 \x01(\x0c"8\n\x16UsernameProofsResponse\x12\x1e\n\x06proofs\x18\x01 \x03(\x0b2\x0e.UserNameProof"3\n\x13VerificationRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12\x0f\n\x07address\x18\x02 \x01(\x0c",\n\rSignerRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12\x0e\n\x06signer\x18\x02 \x01(\x0c"M\n\x0bLinkRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12\x11\n\tlink_type\x18\x02 \x01(\t\x12\x14\n\ntarget_fid\x18\x03 \x01(\x04H\x00B\x08\n\x06target"\xb6\x01\n\x11LinksByFidRequest\x12\x0b\n\x03fid\x18\x01 \x01(\x04\x12\x16\n\tlink_type\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x02\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x03\x88\x01\x01B\x0c\n\n_link_typeB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse"\xcc\x01\n\x14LinksByTargetRequest\x12\x14\n\ntarget_fid\x18\x01 \x01(\x04H\x00\x12\x16\n\tlink_type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x17\n\npage_token\x18\x04 \x01(\x0cH\x03\x88\x01\x01\x12\x14\n\x07reverse\x18\x05 \x01(\x08H\x04\x88\x01\x01B\x08\n\x06targetB\x0c\n\n_link_typeB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\n\n\x08_reverse"2\n\x1fIdRegistryEventByAddressRequest\x12\x0f\n\x07address\x18\x01 \x01(\x0c">\n\x12ValidationResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x19\n\x07message\x18\x02 \x01(\x0b2\x08.Message*\xbe\x01\n\tStoreType\x12\x13\n\x0fSTORE_TYPE_NONE\x10\x00\x12\x14\n\x10STORE_TYPE_CASTS\x10\x01\x12\x14\n\x10STORE_TYPE_LINKS\x10\x02\x12\x18\n\x14STORE_TYPE_REACTIONS\x10\x03\x12\x18\n\x14STORE_TYPE_USER_DATA\x10\x04\x12\x1c\n\x18STORE_TYPE_VERIFICATIONS\x10\x05\x12\x1e\n\x1aSTORE_TYPE_USERNAME_PROOFS\x10\x06b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'request_response_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_STORETYPE']._serialized_start = 3876
    _globals['_STORETYPE']._serialized_end = 4066
    _globals['_EMPTY']._serialized_start = 101
    _globals['_EMPTY']._serialized_end = 108
    _globals['_SUBSCRIBEREQUEST']._serialized_start = 110
    _globals['_SUBSCRIBEREQUEST']._serialized_end = 198
    _globals['_EVENTREQUEST']._serialized_start = 200
    _globals['_EVENTREQUEST']._serialized_end = 226
    _globals['_HUBINFOREQUEST']._serialized_start = 228
    _globals['_HUBINFOREQUEST']._serialized_end = 262
    _globals['_HUBINFORESPONSE']._serialized_start = 265
    _globals['_HUBINFORESPONSE']._serialized_end = 426
    _globals['_DBSTATS']._serialized_start = 428
    _globals['_DBSTATS']._serialized_end = 509
    _globals['_SYNCSTATUSREQUEST']._serialized_start = 511
    _globals['_SYNCSTATUSREQUEST']._serialized_end = 562
    _globals['_SYNCSTATUSRESPONSE']._serialized_start = 564
    _globals['_SYNCSTATUSRESPONSE']._serialized_end = 662
    _globals['_SYNCSTATUS']._serialized_start = 665
    _globals['_SYNCSTATUS']._serialized_end = 865
    _globals['_TRIENODEMETADATARESPONSE']._serialized_start = 867
    _globals['_TRIENODEMETADATARESPONSE']._serialized_end = 990
    _globals['_TRIENODESNAPSHOTRESPONSE']._serialized_start = 992
    _globals['_TRIENODESNAPSHOTRESPONSE']._serialized_end = 1100
    _globals['_TRIENODEPREFIX']._serialized_start = 1102
    _globals['_TRIENODEPREFIX']._serialized_end = 1134
    _globals['_SYNCIDS']._serialized_start = 1136
    _globals['_SYNCIDS']._serialized_end = 1163
    _globals['_FIDREQUEST']._serialized_start = 1166
    _globals['_FIDREQUEST']._serialized_end = 1303
    _globals['_FIDSREQUEST']._serialized_start = 1305
    _globals['_FIDSREQUEST']._serialized_end = 1430
    _globals['_FIDSRESPONSE']._serialized_start = 1432
    _globals['_FIDSRESPONSE']._serialized_end = 1510
    _globals['_MESSAGESRESPONSE']._serialized_start = 1512
    _globals['_MESSAGESRESPONSE']._serialized_end = 1608
    _globals['_CASTSBYPARENTREQUEST']._serialized_start = 1611
    _globals['_CASTSBYPARENTREQUEST']._serialized_end = 1812
    _globals['_REACTIONREQUEST']._serialized_start = 1815
    _globals['_REACTIONREQUEST']._serialized_end = 1950
    _globals['_REACTIONSBYFIDREQUEST']._serialized_start = 1953
    _globals['_REACTIONSBYFIDREQUEST']._serialized_end = 2162
    _globals['_REACTIONSBYTARGETREQUEST']._serialized_start = 2165
    _globals['_REACTIONSBYTARGETREQUEST']._serialized_end = 2431
    _globals['_USERDATAREQUEST']._serialized_start = 2433
    _globals['_USERDATAREQUEST']._serialized_end = 2502
    _globals['_NAMEREGISTRYEVENTREQUEST']._serialized_start = 2504
    _globals['_NAMEREGISTRYEVENTREQUEST']._serialized_end = 2544
    _globals['_RENTREGISTRYEVENTSREQUEST']._serialized_start = 2546
    _globals['_RENTREGISTRYEVENTSREQUEST']._serialized_end = 2586
    _globals['_ONCHAINEVENTREQUEST']._serialized_start = 2589
    _globals['_ONCHAINEVENTREQUEST']._serialized_end = 2774
    _globals['_ONCHAINEVENTRESPONSE']._serialized_start = 2776
    _globals['_ONCHAINEVENTRESPONSE']._serialized_end = 2879
    _globals['_STORAGELIMITSRESPONSE']._serialized_start = 2881
    _globals['_STORAGELIMITSRESPONSE']._serialized_end = 2950
    _globals['_STORAGELIMIT']._serialized_start = 2953
    _globals['_STORAGELIMIT']._serialized_end = 3091
    _globals['_USERNAMEPROOFREQUEST']._serialized_start = 3093
    _globals['_USERNAMEPROOFREQUEST']._serialized_end = 3129
    _globals['_USERNAMEPROOFSRESPONSE']._serialized_start = 3131
    _globals['_USERNAMEPROOFSRESPONSE']._serialized_end = 3187
    _globals['_VERIFICATIONREQUEST']._serialized_start = 3189
    _globals['_VERIFICATIONREQUEST']._serialized_end = 3240
    _globals['_SIGNERREQUEST']._serialized_start = 3242
    _globals['_SIGNERREQUEST']._serialized_end = 3286
    _globals['_LINKREQUEST']._serialized_start = 3288
    _globals['_LINKREQUEST']._serialized_end = 3365
    _globals['_LINKSBYFIDREQUEST']._serialized_start = 3368
    _globals['_LINKSBYFIDREQUEST']._serialized_end = 3550
    _globals['_LINKSBYTARGETREQUEST']._serialized_start = 3553
    _globals['_LINKSBYTARGETREQUEST']._serialized_end = 3757
    _globals['_IDREGISTRYEVENTBYADDRESSREQUEST']._serialized_start = 3759
    _globals['_IDREGISTRYEVENTBYADDRESSREQUEST']._serialized_end = 3809
    _globals['_VALIDATIONRESPONSE']._serialized_start = 3811
    _globals['_VALIDATIONRESPONSE']._serialized_end = 3873