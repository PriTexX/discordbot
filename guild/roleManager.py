import discord
from random import randint


class RoleManager:

    @staticmethod
    async def createRole(guild: discord.Guild, name) -> discord.Role:
        colour = discord.Color.from_rgb(randint(0,255), randint(0,255), randint(0,255))
        role = await guild.create_role(name=name, colour=colour, hoist=True, mentionable=True, reason="Created by bot")
        return role

    @staticmethod
    async def deleteRole(guild: discord.Guild, roleName) -> None:
        roleToDelete = discord.utils.find(lambda r: r.name == roleName, guild.roles)

        if roleToDelete:
            await roleToDelete.delete()

    @staticmethod
    def checkRoleExists(guild: discord.Guild, roleName) -> bool:
        role = discord.utils.find(lambda r: r.name == roleName, guild.roles)
        return bool(role)

    @staticmethod
    async def changeRolePosition(role: discord.Role, position):
        await role.edit(position=position)

    @staticmethod
    def getRole(guild: discord.Guild, roleName):
        return discord.utils.find(lambda r: r.name == roleName, guild.roles)


