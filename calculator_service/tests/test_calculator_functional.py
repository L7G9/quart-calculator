import unittest
import json

from calculator_service import app as tested_app
from calculator_service.views.calculator_blueprints import (
    PARAM_1_KEY,
    PARAM_2_KEY,
    LIST_KEY,
    RESULT_KEY,
)


class TestApp(unittest.IsolatedAsyncioTestCase):
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    ab_data = {PARAM_1_KEY: 9, PARAM_2_KEY: 3}

    list_data = {LIST_KEY: [1, 2, 3, 4, 5]}

    async def test_add_data(self):
        app = tested_app.test_client()
        result = await app.get(
            "/add", headers=self.headers, data=json.dumps(self.ab_data)
        )
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 12)

    async def test_add_query(self):
        app = tested_app.test_client()
        result = await app.get("/add?a=9&b=3")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 12)

    async def test_subtract_data(self):
        app = tested_app.test_client()
        result = await app.get(
            "/subtract", headers=self.headers, data=json.dumps(self.ab_data)
        )
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 6)

    async def test_subtract_query(self):
        app = tested_app.test_client()
        result = await app.get("/subtract?a=9&b=3")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 6)

    async def test_multiply_data(self):
        app = tested_app.test_client()
        result = await app.get(
            "/multiply", headers=self.headers, data=json.dumps(self.ab_data)
        )
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 27)

    async def test_multiply_query(self):
        app = tested_app.test_client()
        result = await app.get("/multiply?a=9&b=3")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 27)

    async def test_divide_data(self):
        app = tested_app.test_client()
        result = await app.get(
            "/divide", headers=self.headers, data=json.dumps(self.ab_data)
        )
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 3)

    async def test_divide_query(self):
        app = tested_app.test_client()
        result = await app.get("/divide?a=9&b=3")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 3)

    async def test_sum(self):
        app = tested_app.test_client()
        result = await app.get(
            "/sum", headers=self.headers, data=json.dumps(self.list_data)
        )
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 15)

    async def test_mean(self):
        app = tested_app.test_client()
        result = await app.get(
            "/mean", headers=self.headers, data=json.dumps(self.list_data)
        )
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body[RESULT_KEY], 3)


if __name__ == "__main__":
    unittest.main()
