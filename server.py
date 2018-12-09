from concurrent import futures
import time
import grpc
import hello_pb2 as hello
import hello_pb2_grpc as hg

# 实现 proto 文件中定义的 GreeterServicer

class Greeter(hg.HelloWorldServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def SayHello(self, request, context):
        print("someone request me python")
        return hello.Greeting(message = 'hello {name} {msg}'.format(name=request.person.name,msg = request.msg))
        #return hello.HelloReply(message = 'hello {msg}'.format(msg = request.name))

    # def SayHelloAgain(self, request, context):
    #     return helloworld_pb2.HelloReply(message='hello {msg}'.format(msg = request.name))

def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hg.add_HelloWorldServicer_to_server(Greeter(),server)
   # hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    print("running server grpc python")
    serve()

