import aiohttp
import json


class RequestService:
    headers = {"Content-type": "application/json"}

    @staticmethod
    def toJson(data):
        return json.dumps(data)

    @staticmethod
    async def get(url):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.request("GET", url, connector=conn, headers=RequestService.headers) as response:
            await conn.close()
            return response.status, await response.text()

    @staticmethod
    async def post(url, data):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.request("POST", url, connector=conn, data=RequestService.toJson(data), headers=RequestService.headers) as response:
            await conn.close()
            return response.status, await response.text()



