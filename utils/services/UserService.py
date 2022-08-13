import json

from config import API_REQUEST_STRING
from exceptions import FailedToLoginException, ErrorSavingUser, UserAlreadyExists
from utils.services import RequestService


class UserService:
    login_url = API_REQUEST_STRING + 'login/'
    user_url = API_REQUEST_STRING + 'user/'

    @staticmethod
    async def login(username, password):
        credentials = {"login": username, "password": password}

        statuscode, data = await RequestService.post(UserService.login_url, data=credentials)
        if statuscode == 400:
            raise FailedToLoginException("Wrong username or password")

        if statuscode == 200:
            return json.loads(data)
        raise FailedToLoginException("Some problem occurred during login")

    @staticmethod
    async def saveUser(discordUserId, oneCId):
        discordUser = {"discorduserid": discordUserId, "oneCGuid": oneCId}

        statuscode, data = await RequestService.post(UserService.user_url, data=discordUser)
        if statuscode == 500:
            raise ErrorSavingUser("Problem occurred in saving user")
        if statuscode == 422:
            raise UserAlreadyExists("User with same id already exists")

        return statuscode

    @staticmethod
    async def getUser(discordUserId):
        statuscode, data = await RequestService.get(UserService.user_url + f"?discordUserId={discordUserId}")
        print(statuscode, data)