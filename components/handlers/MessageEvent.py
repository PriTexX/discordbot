import discord

from components import EventHandler


class MessageEvent:
    def __init__(self):
        self.handlers = []

    def registerHandler(self, handler: EventHandler):
        self.handlers.append(handler)

    def removeHandler(self, handler_id):
        for handler in self.handlers:
            if handler.id == handler_id:
                del handler
                return True
        return False

    async def handle(self, message: discord.Message):
        for handler in self.handlers:
            await handler.execute(message)