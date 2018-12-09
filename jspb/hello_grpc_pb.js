// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var hello_pb = require('./hello_pb.js');
var google_protobuf_wrappers_pb = require('google-protobuf/google/protobuf/wrappers_pb.js');

function serialize_com_zh_all_Greeting(arg) {
  if (!(arg instanceof hello_pb.Greeting)) {
    throw new Error('Expected argument of type com.zh.all.Greeting');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_com_zh_all_Greeting(buffer_arg) {
  return hello_pb.Greeting.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_com_zh_all_ToBeGreeted(arg) {
  if (!(arg instanceof hello_pb.ToBeGreeted)) {
    throw new Error('Expected argument of type com.zh.all.ToBeGreeted');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_com_zh_all_ToBeGreeted(buffer_arg) {
  return hello_pb.ToBeGreeted.deserializeBinary(new Uint8Array(buffer_arg));
}


//
// Returns a greeting for the given person optionally including a custom message.
var HelloWorldService = exports.HelloWorldService = {
  sayHello: {
    path: '/com.zh.all.HelloWorld/SayHello',
    requestStream: false,
    responseStream: false,
    requestType: hello_pb.ToBeGreeted,
    responseType: hello_pb.Greeting,
    requestSerialize: serialize_com_zh_all_ToBeGreeted,
    requestDeserialize: deserialize_com_zh_all_ToBeGreeted,
    responseSerialize: serialize_com_zh_all_Greeting,
    responseDeserialize: deserialize_com_zh_all_Greeting,
  },
};

exports.HelloWorldClient = grpc.makeGenericClientConstructor(HelloWorldService);
