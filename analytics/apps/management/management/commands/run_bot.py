from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import util

from analytics.apps.bot.main_bot import bot

import asyncio
import logging

logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = "Running bot"

    def handle(self, *args, **options):
        try:
            asyncio.run(bot.infinity_polling(logger_level=settings.LOG_LEVEL, allowed_updates=util.update_types))
        except Exception as e:
            logger.error(f"Exception while running bot: {e}")
