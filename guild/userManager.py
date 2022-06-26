import discord


class UserManager:

    @staticmethod
    async def addRoles(user: discord.Member, roles, reason="Added by bot"):
        await user.add_roles(roles, reason=reason)

    @staticmethod
    async def changeNickname(user: discord.Member, nick, reason="Edited by bot"):
        await user.edit(nick=nick, reason=reason)

    @staticmethod
    async def removeRoles(user: discord.Member, *roles, reason="Removed by bot"):
        await user.remove_roles(roles, reason=reason)
