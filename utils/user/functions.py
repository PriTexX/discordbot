from .UserAuth import UserAuth
from models.user import User


def getUser(token):
    userInfo = UserAuth.getUserInfo(token)

    return User(userInfo["surname"] + ' ' + userInfo["name"], userInfo["group"])