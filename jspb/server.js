var services = require('./hello_grpc_pb.js');
var messages = require('./hello_pb.js');
var grpc = require('grpc')
var hello = function(call, callback) {
    var response=new messages.Greeting()
         // var response = new messages.HelloResponse();
   response.setHellostring
        response.setHellostring("hello," + call.request.getMsg());
    callback(null, response);
}
var server = new grpc.Server();
server.addService(
    s
  services.HelloWorldServiceService,
  {
    hello:hello
  }
);
server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
server.start(function(err,data){
  console.log(err);
  console.log(data);
});
