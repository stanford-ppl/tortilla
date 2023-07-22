# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tortilla.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ops_pb2 as ops__pb2
import stream_pb2 as stream__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tortilla.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0etortilla.proto\x1a\tops.proto\x1a\x0cstream.proto\"O\n\x0cProgramGraph\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\toperators\x18\x02 \x03(\x0b\x32\n.OperationB\x07\n\x05_nameJ\x04\x08\x03\x10\x0b\x62\x06proto3'
  ,
  dependencies=[ops__pb2.DESCRIPTOR,stream__pb2.DESCRIPTOR,])




_PROGRAMGRAPH = _descriptor.Descriptor(
  name='ProgramGraph',
  full_name='ProgramGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ProgramGraph.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operators', full_name='ProgramGraph.operators', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_name', full_name='ProgramGraph._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=43,
  serialized_end=122,
)

_PROGRAMGRAPH.fields_by_name['operators'].message_type = ops__pb2._OPERATION
_PROGRAMGRAPH.oneofs_by_name['_name'].fields.append(
  _PROGRAMGRAPH.fields_by_name['name'])
_PROGRAMGRAPH.fields_by_name['name'].containing_oneof = _PROGRAMGRAPH.oneofs_by_name['_name']
DESCRIPTOR.message_types_by_name['ProgramGraph'] = _PROGRAMGRAPH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProgramGraph = _reflection.GeneratedProtocolMessageType('ProgramGraph', (_message.Message,), {
  'DESCRIPTOR' : _PROGRAMGRAPH,
  '__module__' : 'tortilla_pb2'
  # @@protoc_insertion_point(class_scope:ProgramGraph)
  })
_sym_db.RegisterMessage(ProgramGraph)


# @@protoc_insertion_point(module_scope)
