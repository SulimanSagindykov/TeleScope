import logging

import telebot
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
from analytics.apps.bot.middleware import CustomMiddleware

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')
telebot.logger.setLevel(settings.LOG_LEVEL)
# Handle '/start' and '/help'
logger = logging.getLogger(__name__)

bot.setup_middleware(CustomMiddleware())

@bot.chat_member_handler()
async def chat_member_handler_bot(message):
    status = message.difference.get('status')
    invite_link = message.invite_link
    full_name = message.from_user.full_name
    username = message.from_user.username
    id = message.from_user.id
    invite_link_name = ''
    invite_link_url = ''
    try:
        invite_link_name = getattr(invite_link, 'name')
        invite_link_url = getattr(invite_link, 'invite_link')
    except AttributeError as e:
        logger.info(f'Did not get an invite link: {e}')
    current_subscriber_status = status[1]
    if current_subscriber_status == 'member':
        status_text = '💥Subscribed'
    elif current_subscriber_status == 'left':
        status_text = '🫡Unsubscribed'
    else:
        status_text = '🫣Not found'
    text_message = (f'Status: {status_text}\n'
                    f'Name: {full_name}\n'
                    f'ID: {id}')
    if username:
        text_message += f'\n<b>Nickname</b>: @{username}'
    if invite_link_name:
        text_message += f'\nInvite Link Name: {invite_link_name}'
    if invite_link_url:
        text_message += f'\n<b>URL</b>: {invite_link_url}'

    await bot.send_message(chat_id=settings.ADMIN_ID, text=text_message)

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, 'Салем')
    await bot.send_message(message.chat.id, message.chat.id)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)
