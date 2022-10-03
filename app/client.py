import grpc
import services_pb2 as messages
import services_pb2_grpc as services


def getExpr(a: int, b: int, o: str) -> messages.Expr:
    """Generates serialized Expr object"""
    return messages.Expr(lhs=a, rhs=b, operation=o)


def run(a: int, b: int, o: str) -> messages.Calculated:
    """Evaluates basic expression on server from http://localhost:50051 via gRPC and returns serialized response.

    Args:
        a (int): left argument of an expression
        b (int): right argument of an expression
        o (str): operation

    Returns:
        Calculated: serialized response from server -- {.result, .operation, .error} -- evaluated result, operation and error code (0 if no errors, 1 otherwise)
    """
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = services.exprEvalStub(channel)
        response = stub.Eval(getExpr(a, b, o))
    return response


if __name__ == "__main__":
    a, b = map(int, input().split())
    c = input()
    print(run(a, b, c))
