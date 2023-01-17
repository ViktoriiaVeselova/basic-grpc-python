import grpc

# import the generated classes
import ping_pb2
import ping_pb2_grpc


# open a gRPC channel
channel = grpc.insecure_channel('127.0.0.1:8081')

# create a stub (client)
stub = ping_pb2_grpc.PingServiceStub(channel)

# create a valid request message
request = ping_pb2.PingRequest(message="Ping")

# make the call
response = stub.getResponse(request)

# et voilà
print(response.message)