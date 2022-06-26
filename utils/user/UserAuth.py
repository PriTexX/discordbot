import requests
from models import User
from exceptions import FailedToLoginException


class UserAuth:

    @staticmethod
    def auth(login, password):
        resp = requests.post("https://e.mospolytech.ru/old/lk_api.php", data={
            'ulogin': login,
            'upassword': password,
        }, verify=False)

        if resp.status_code == 400:
            raise FailedToLoginException("Неверно указан логин или пароль")

        return resp.json()['token']

    @staticmethod
    def getUserInfo(token):
        userInfo = requests.get(
            f"https://e.mospolytech.ru/old/lk_api.php/?getUser&token={token}",
            verify=False
        ).json()

        return userInfo['user']
