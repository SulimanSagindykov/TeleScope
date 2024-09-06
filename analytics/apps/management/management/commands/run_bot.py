from django.core.management.base import BaseCommand, CommandError
from analytics.apps.bot.main_bot import bot
import asyncio

class Command(BaseCommand):
    help = "Running bot"

    def handle(self, *args, **options):
        asyncio.run(bot.polling())