# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ping.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nping.proto\x12 com.epam.grpchometask.stubs.ping\"\x1e\n\x0bPingRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0cPingResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2{\n\x0bPingService\x12l\n\x0bgetResponse\x12-.com.epam.grpchometask.stubs.ping.PingRequest\x1a..com.epam.grpchometask.stubs.ping.PingResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ping_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PINGREQUEST._serialized_start=48
  _PINGREQUEST._serialized_end=78
  _PINGRESPONSE._serialized_start=80
  _PINGRESPONSE._serialized_end=111
  _PINGSERVICE._serialized_start=113
  _PINGSERVICE._serialized_end=236
# @@protoc_insertion_point(module_scope)