from quart import Blueprint
from quart import request
from calculator_service.calculator import Calculator

PARAM_1_KEY = 'a'
PARAM_2_KEY = 'b'
LIST_KEY = 'list'
RESULT_KEY = 'result'

async def get_a_and_b():
    json_data = await request.get_json()
    if json_data != None:
        a = json_data[PARAM_1_KEY]
        b = json_data[PARAM_2_KEY]
    else:
        a = request.args.get(PARAM_1_KEY)
        b = request.args.get(PARAM_2_KEY)
    return int(a), int(b)

async def get_list():
    json_data = await request.get_json()
    return json_data[LIST_KEY]

calculator = Calculator()

add = Blueprint("add", __name__)
@add.route("/add")
async def calculate_add():
    a, b = await get_a_and_b()
    return {RESULT_KEY: calculator.add(a, b)}

subtract = Blueprint("subtract", __name__)
@add.route("/subtract")
async def calculate_subtract():
    a, b = await get_a_and_b()
    return {"result": calculator.subtract(a, b)}

multiply = Blueprint("multiply", __name__)
@add.route("/multiply")
async def calculate_multiply():
    a, b = await get_a_and_b()
    return {"result": calculator.multiply(a, b)}

divide = Blueprint("divide", __name__)
@add.route("/divide")
async def calculate_divide():
    a, b = await get_a_and_b()
    return {"result": calculator.divide(a, b)}

sum = Blueprint("sum", __name__)
@add.route("/sum")
async def calculate_sum():
    list = await get_list()
    return {"result": calculator.sum(list)}

mean = Blueprint('mean', __name__)
@add.route("/mean")
async def calculate_mean():
    list = await get_list()
    return {"result": calculator.mean(list)}

