from discord_components import Interaction
from components import  EventHandler


class ButtonPressEventHandler:
    def __init__(self):
        self.handlers = {}

    def registerHandler(self, btn_id, handler: EventHandler):
        if self.handlers.get(btn_id, False):
            self.handlers[btn_id].append(handler)
        else:
            self.handlers[btn_id] = [handler]

    def removeHandler(self, btn_id, handler_id):
        for handler in self.handlers[btn_id]:
            if handler.id == handler_id:
                del handler
                return True
        return False

    async def handle(self, btn_id, interaction: Interaction):
        for handler in self.handlers[btn_id]:
            await handler.execute(interaction)