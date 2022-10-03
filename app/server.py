import grpc
from concurrent import futures
import services_pb2_grpc as services
import exprEval as exprEval

global port, server
port = "50051"


def serve():
    """Starts gRPC server on port specified in {port} global variable and listens to incoming requests"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_exprEvalServicer_to_server(exprEval.exprEval(), server)
    server.add_insecure_port("[::]:{}".format(port))
    server.start()
    print("Server started listening on port {}".format(port))
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
