import aiohttp
import json
from exceptions import ServerNotResponds


class RequestService:
    headers = {"Content-type": "application/json"}

    @staticmethod
    def toJson(data):
        return json.dumps(data)

    @staticmethod
    async def get(url):
        try:
            conn = aiohttp.TCPConnector(verify_ssl=False)
            async with aiohttp.request("GET", url,
                                       connector=conn,
                                       headers=RequestService.headers) as response:
                await conn.close()
                return response.status, await response.text()
        except aiohttp.ClientConnectorError:
            raise ServerNotResponds("Сервер в данный момент не доступен.")

    @staticmethod
    async def post(url, data):
        try:
            conn = aiohttp.TCPConnector(verify_ssl=False)
            async with aiohttp.request("POST", url,
                                       connector=conn,
                                       data=RequestService.toJson(data),
                                       headers=RequestService.headers) as response:
                await conn.close()
                return response.status, await response.text()
        except aiohttp.ClientConnectorError:
            raise ServerNotResponds("Сервер в данный момент не доступен.")



