import unittest
import json

from calculator_service import app as tested_app

class TestApp(unittest.IsolatedAsyncioTestCase):
    async def test_add(self):
        app = tested_app.test_client()
        result = await app.get("/add?a=9&b=3")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body["result"], 12)

    async def test_subtract(self):
        app = tested_app.test_client()
        result = await app.get("/subtract?a=9&b=3")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body["result"], 6)

    async def test_multiply(self):
        app = tested_app.test_client()
        result = await app.get("/multiply?a=9&b=3")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body["result"], 27)

    async def test_divide(self):
        app = tested_app.test_client()
        result = await app.get("/divide?a=9&b=3")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body["result"], 3)

    async def test_sum(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {"list": [1, 2, 3, 4, 5]}
        app = tested_app.test_client()
        result = await app.get("/sum", headers = headers, data = json.dumps(data))
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body["result"], 15)

if __name__ == "__main__":
    unittest.main()

