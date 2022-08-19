from exceptions import FailedToLoginException, ServerNotResponds, ServerError
from guild import RoleManager, UserManager
from utils.services import UserService


class UserAuth:

    @staticmethod
    async def auth(guild, member, login, password):
        try:
            user_info = await UserService.login(login, password)
        except FailedToLoginException as exception:
            print(exception.details)
            await member.send("Неверный логин или пароль")
            return

        except (ServerNotResponds, ServerError):
            await member.send("Авторизация в данный момент не доступна. Попробуйте позже")
            return

        if user_info['department'] != "5dd48625-77d5-11e9-940d-000c29c02919":
            await member.send(
                "Вы должны быть с кафедры Информационные системы и технологии, чтобы авторизоваться на этом сервере")
            return

        role = RoleManager.getRole(guild, user_info['group'])
        studentRole = RoleManager.getRole(guild, "student")

        if not role:
            role = await RoleManager.createRole(guild, user_info['group'])

        nickname = f"{user_info['surname']} {user_info['name']}"

        await UserManager.addRoles(member, role, reason="Added by bot, adding new user role")
        await UserManager.addRoles(member, studentRole, reason="Added by bot, adding new user role")

        try:
            await UserManager.changeNickname(member, nick=nickname, reason="Changed by bot, authenticating new user")
        except Exception:
            pass

        await member.send(f"Вы успешно авторизованы, {user_info['name']}!")
        return user_info
