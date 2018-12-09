# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='com.zh.all',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bhello.proto\x12\ncom.zh.all\x1a\x1egoogle/protobuf/wrappers.proto\"\x16\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\"\\\n\x0bToBeGreeted\x12\"\n\x06person\x18\x01 \x01(\x0b\x32\x12.com.zh.all.Person\x12)\n\x03msg\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x1b\n\x08Greeting\x12\x0f\n\x07message\x18\x01 \x01(\t2I\n\nHelloWorld\x12;\n\x08SayHello\x12\x17.com.zh.all.ToBeGreeted\x1a\x14.com.zh.all.Greeting\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='com.zh.all.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.zh.all.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  ],
  serialized_start=59,
  serialized_end=81,
)


_TOBEGREETED = _descriptor.Descriptor(
  name='ToBeGreeted',
  full_name='com.zh.all.ToBeGreeted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='com.zh.all.ToBeGreeted.person', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='com.zh.all.ToBeGreeted.msg', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  ],
  serialized_start=83,
  serialized_end=175,
)


_GREETING = _descriptor.Descriptor(
  name='Greeting',
  full_name='com.zh.all.Greeting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='com.zh.all.Greeting.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  ],
  serialized_start=177,
  serialized_end=204,
)

_TOBEGREETED.fields_by_name['person'].message_type = _PERSON
_TOBEGREETED.fields_by_name['msg'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['ToBeGreeted'] = _TOBEGREETED
DESCRIPTOR.message_types_by_name['Greeting'] = _GREETING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:com.zh.all.Person)
  ))
_sym_db.RegisterMessage(Person)

ToBeGreeted = _reflection.GeneratedProtocolMessageType('ToBeGreeted', (_message.Message,), dict(
  DESCRIPTOR = _TOBEGREETED,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:com.zh.all.ToBeGreeted)
  ))
_sym_db.RegisterMessage(ToBeGreeted)

Greeting = _reflection.GeneratedProtocolMessageType('Greeting', (_message.Message,), dict(
  DESCRIPTOR = _GREETING,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:com.zh.all.Greeting)
  ))
_sym_db.RegisterMessage(Greeting)



_HELLOWORLD = _descriptor.ServiceDescriptor(
  name='HelloWorld',
  full_name='com.zh.all.HelloWorld',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=206,
  serialized_end=279,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='com.zh.all.HelloWorld.SayHello',
    index=0,
    containing_service=None,
    input_type=_TOBEGREETED,
    output_type=_GREETING,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLOWORLD)

DESCRIPTOR.services_by_name['HelloWorld'] = _HELLOWORLD

# @@protoc_insertion_point(module_scope)
