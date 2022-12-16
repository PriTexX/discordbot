import json
import requests

from config import API_URL
from exceptions import FailedToLoginException, ErrorSavingUser, UserAlreadyExists, ServerError
from utils.services import RequestService


class UserService:
    login_url = API_URL + '/login'
    user_url = API_URL + '/user'

    @staticmethod
    async def login(username, password):
        credentials = {"ulogin": username, "upassword": password}
        resp = requests.post("https://e.mospolytech.ru/old/lk_api.php", data=credentials, verify=False)

        if resp.status_code != 200:
            raise FailedToLoginException("Wrong username or password")

        resp = requests.get(f"https://e.mospolytech.ru/old/lk_api.php/?getUser&token={resp.json()['token']}", verify=False)

        if resp.status_code != 200:
            raise FailedToLoginException("Wrong username or password")

        userInfo = resp.json()["user"]

        departament = ""
        if userInfo["specialty"] == "09.03.02 Информационные системы и технологии":
            departament = "5dd48623-77d5-11e9-940d-000c29c02919"

        return {"department": departament, "group": userInfo["group"],
                "surname": userInfo["surname"], "name": userInfo["name"],
                "oneCGuid": "Authenticated through the LK"}

    @staticmethod
    async def saveUser(discordUserId, oneCId):
        discordUser = {"discorduserid": discordUserId, "oneCGuid": oneCId}

        statuscode, data = await RequestService.post(UserService.user_url, data=discordUser)
        if statuscode == 500:
            raise ErrorSavingUser("Problem occurred in saving user")
        if statuscode == 422:
            raise UserAlreadyExists("User with same id already exists")

        return statuscode
