import json

from config import API_URL
from exceptions import FailedToLoginException, ErrorSavingUser, UserAlreadyExists, ServerError
from utils.services import RequestService


class UserService:
    login_url = API_URL + '/login'
    user_url = API_URL + '/user'

    @staticmethod
    async def login(username, password):
        credentials = {"login": username, "password": password}

        statuscode, data = await RequestService.post(UserService.login_url, data=credentials)
        if statuscode == 400:
            raise FailedToLoginException("Wrong username or password")

        if statuscode == 200:
            return json.loads(data)

        if statuscode == 500:
            raise ServerError("Some problem on server side occurred")

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