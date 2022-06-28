class EventHandler:
    def __init__(self, id, handler_func):
        self.id = id
        self.handler_func = handler_func

    async def execute(self, *args, **kwargs):
        await self.handler_func(*args, **kwargs)