import services_pb2 as messages
import services_pb2_grpc as services


def getCalculated(result: int, operation: str, error: int) -> messages.Calculated:
    """Generates serizalized Calculated object.

    Args:
        result (int): result of a calculation
        operation (str): operation
        error (int): 1 if error occured, 0 otherwise

    Returns:
        Calculated: serialized fields
    """
    return messages.Calculated(result=result, operation=operation, error=error)


class exprEval(services.exprEvalServicer):
    def Eval(self, expression: messages.Expr, context) -> messages.Calculated:
        lhs = expression.lhs
        rhs = expression.rhs
        op = expression.operation
        match op:
            case "+":
                return getCalculated(lhs + rhs, op, 0)
            case "-":
                return getCalculated(lhs - rhs, op, 0)
            case "/":
                return getCalculated(lhs // rhs, op, 0)
            case "%":
                return getCalculated(lhs % rhs, op, 0)
            case "**":
                return getCalculated(lhs**rhs, op, 0)
            case _:
                return getCalculated(0, op, 1)
