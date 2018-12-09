import hello_pb2 as hello
import  hello_pb2_grpc as hpg
import grpc
import grpc_tools
from   google.protobuf import  wrappers_pb2 as wrap

def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    # stub=hello
    stub=hpg.HelloWorldStub(channel)
    person=hello.Person(name="liming")
    msg=wrap.StringValue(value="are you ok")

    tobeGreed=hello.ToBeGreeted(person=person,msg=msg)

    response=stub.SayHello(tobeGreed)
    print("Greeter client received: " + response.message)

    # stub = hello_pb2_grpc.GreeterStub(channel)
    # response = stub.SayHello(hello_pb2_grpc.HelloRequest(name='czl'))
    # print("Greeter client received: " + response.message)
    # response = stub.SayHelloAgain(hello.HelloRequest(name='daydaygo'))
    # print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()

