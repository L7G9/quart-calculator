from quart import Blueprint
from quart import request
from calculator_service.calculator import Calculator

calculator = Calculator()

add = Blueprint("add", __name__)
@add.route("/add")
def calculate_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return {"result": calculator.add(a, b)}

subtract = Blueprint("subtract", __name__)
@add.route("/subtract")
def calculate_subtract():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return {"result": calculator.subtract(a, b)}

multiply = Blueprint("multiply", __name__)
@add.route("/multiply")
def calculate_multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return {"result": calculator.multiply(a, b)}

divide = Blueprint("divide", __name__)
@add.route("/divide")
def calculate_divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return {"result": calculator.divide(a, b)}

sum = Blueprint("sum", __name__)
@add.route("/sum")
async def calculate_sum():
    json_data = await request.get_json()
    list = json_data['list']
    return {"result": calculator.sum(list)}
