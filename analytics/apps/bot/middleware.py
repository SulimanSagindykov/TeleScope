from telebot import BaseMiddleware

class CustomMiddleware(BaseMiddleware) :
    def __init__(self):
        super(CustomMiddleware, self).__init__()
        self.update_sensitive = True
        self.update_types = ['message', 'edited_message']

    async def pre_process_message(self, message, data):
        pass
    async def post_process_message(self, message, data, exception):
        pass
    async def pre_process_edited_message(self, message, data):
        pass
    async def post_process_edited_message(self, message, data, exception):
        pass