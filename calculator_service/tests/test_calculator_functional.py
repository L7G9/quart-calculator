import unittest
import json

from calculator_service import app as tested_app

class TestApp(unittest.IsolatedAsyncioTestCase):
    async def test_add(self):
        app = tested_app.test_client()
        result = await app.get("/add?a=3&b=9")
        body = json.loads(str(await result.get_data(), "utf8"))
        self.assertEqual(body["result"], 12)

if __name__ == "__main__":
    unittest.main()

