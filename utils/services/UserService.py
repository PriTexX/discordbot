from constants import API_REQUEST_STRING
from exceptions import WrongCredentials, ErrorSavingUser
from utils.services import RequestService


class UserService:
    login_url = API_REQUEST_STRING + 'login/'
    user_url = API_REQUEST_STRING + 'user/'

    @staticmethod
    async def login(username, password):
        credentials = {"login": username, "password": password}

        statuscode, data = await RequestService.post(UserService.login_url, data=credentials)
        if statuscode == 400:
            raise WrongCredentials("Wrong username or password")

        if statuscode == 200:
            return data

    @staticmethod
    async def saveUser(discordUserId, activeDirectoryId, oneCId):
        discordUser = {"discorduserid": discordUserId, "activeDirectoryGuid": activeDirectoryId, "oneCGuid": oneCId}

        statuscode = await RequestService.post(UserService.user_url, data=discordUser)
        if statuscode == 500:
            raise ErrorSavingUser("Problem occurred in saving user")

        return statuscode

    @staticmethod
    async def getUser(discordUserId):
        statuscode, data = await RequestService.get(UserService.user_url + f"?discordUserId={discordUserId}")
        print(statuscode, data)