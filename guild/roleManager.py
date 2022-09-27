import re

import discord
from math import cos, sin, e


def sortRolesFunc(role):
    roleName = role.name

    if len(roleName) == 7:
        return int(roleName[:3]+roleName[4:])

    return int(roleName[:3]+roleName[4:-1]) + int(roleName[-1:]) + 10



def getPermissions():
    permissions = discord.Permissions(
        view_channel=True,
    )

    permissions.value |= 1 << 10
    permissions.value |= 1 << 11
    permissions.value |= 1 << 14
    permissions.value |= 1 << 15
    permissions.value |= 1 << 16
    permissions.value |= 1 << 38
    permissions.value |= 1 << 35
    permissions.value |= 1 << 36
    permissions.value |= 1 << 6
    permissions.value |= 1 << 18
    permissions.value |= 1 << 37
    permissions.value |= 1 << 31
    permissions.value |= 1 << 20
    permissions.value |= 1 << 21
    permissions.value |= 1 << 9
    permissions.value |= 1 << 25

    return permissions


class RoleManager:

    @staticmethod
    async def createRole(guild: discord.Guild, name) -> discord.Role:
        number_year = int(name[:2])
        color = discord.Color.from_rgb(int(sin(number_year * 1.43) * 127 + 127),
                                       int(cos(number_year * e ** 3.31) * 127 + 127),
                                       int(sin(number_year * e ** 10.55) * 127 + 127))
        permissions = getPermissions()
        role = await guild.create_role(name=name, permissions=permissions, color=color, hoist=True, mentionable=True,
                                       reason="Created by bot")
        all_roles = await guild.fetch_roles()
        pos = max([rl.position for rl in all_roles if re.fullmatch("\[ПД\].*", rl.name)])
        await role.edit(position=pos + 1)
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

    @staticmethod
    async def sortRoles(guild: discord.Guild):
        roles, start_pos = await RoleManager.__getSortedRoles(guild)
        roles_to_position = RoleManager.__makeDictFromSortedRoles(roles, start_pos)
        await guild.edit_role_positions(roles_to_position)

    @staticmethod
    async def __getSortedRoles(guild: discord.Guild):
        idx_from = -1
        idx_to = -1
        start_pos = -1

        all_roles = sorted(await guild.fetch_roles(), key=lambda x: x.position)
        for i in range(len(all_roles) - 1, 1, -1):
            if all_roles[i].name == "student" or re.fullmatch("\[ПД\].*", all_roles[i].name):
                idx_from = i + 1
                start_pos = all_roles[i].position
                break

        for i in range(len(all_roles) - 1, 1, -1):
            if all_roles[i].name == "ОЛДЫ":
                idx_to = i
                break

        return all_roles[idx_from:idx_to], start_pos

    @staticmethod
    def __makeDictFromSortedRoles(roles, stud_pos):
        role_to_pos = {}

        master_roles = [role for role in roles if re.fullmatch("[0-9]{2}4[0-9]{0,}-[0-9]{3,}", role.name)]
        bachelor_roles = [role for role in roles if re.fullmatch("[0-9]{2}[123][0-9]{0,}-[0-9]{3,}", role.name)]

        for role in sorted(bachelor_roles, key=sortRolesFunc, reverse=True):
            stud_pos += 1
            role_to_pos[role] = stud_pos

        for role in sorted(master_roles, key=sortRolesFunc, reverse=True):
            stud_pos += 1
            role_to_pos[role] = stud_pos

        return role_to_pos
