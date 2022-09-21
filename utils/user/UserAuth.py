from exceptions import FailedToLoginException, ServerNotResponds, ServerError
from guild import RoleManager, UserManager
from utils.services import UserService
import re


class UserAuth:

    @staticmethod
    async def auth(guild, member, login, password):
        try:
            user_info = await UserService.login(login, password)
        except FailedToLoginException:
            await member.send("Неверный логин или пароль. Попробуйте пройти авторизацию еще раз")
            return

        except (ServerNotResponds, ServerError):
            await member.send("Авторизация в данный момент не доступна. Попробуйте позже")
            return

        if user_info['department'] != "5dd48623-77d5-11e9-940d-000c29c02919":
            await member.send(
                "Вы должны быть с кафедры Информационные системы и технологии, чтобы авторизоваться на этом сервере")
            return


        nickname = f"{user_info['surname']} {user_info['name']}"

        studentRole = RoleManager.getRole(guild, "student")
        await UserManager.addRoles(member, studentRole, reason="Added by bot, adding new user role")

        role = RoleManager.getRole(guild, user_info['group'])
        if not role:
            role = await RoleManager.createRole(guild, user_info['group'])
            await RoleManager.sortRoles(guild)

        if len(member.roles) >= 3:
            old_roles_list = []
            for old_role in member.roles:
                if re.fullmatch("\d+-\d+", old_role.name):
                    old_roles_list.append(old_role)

            await member.remove_roles(*old_roles_list)

        await UserManager.addRoles(member, role, reason="Added by bot, adding new user role")

        try:
            await UserManager.changeNickname(member, nick=nickname, reason="Changed by bot, authenticating new user")
        except Exception:
            pass

        await member.send(f"Вы успешно авторизованы, {user_info['name']}!")
        return user_info
