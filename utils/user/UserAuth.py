from exceptions import FailedToLoginException
from guild import RoleManager, UserManager
from utils.services import UserService


class UserAuth:

    @staticmethod
    async def auth(guild, member, login, password):
        try:
            user_info = await UserService.login(login, password)
        except FailedToLoginException:
            await member.send("Неверный логин или пароль")
            return

        if user_info['department'] != "Институт принтмедиа и информационных технологий":
            await member.send(
                "Вы должны быть с кафедры Информационные системы и технологии, чтобы авторизоваться на этом сервере")
            return

        role = RoleManager.getRole(guild, user_info['group'])

        if not role:
            role = await RoleManager.createRole(guild, user_info['group'])

        nickname = f"{user_info['surname']} {user_info['name']}"

        await UserManager.addRoles(member, role, reason="Added by bot, adding new user role")

        try: # remove this try/except block in production
            await UserManager.changeNickname(member, nick=nickname, reason="Changed by bot, authenticating new user")
        except:
            pass

        await member.send(f"Вы успешно авторизованы, {user_info['name']}!")
        return user_info
