from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class BotUser(models.Model):
    telegram_id = models.PositiveBigIntegerField(_('ID Telegram'), db_index=True, unique=True)
    username = models.CharField(_('Username'), max_length=150, blank=True, null=True)
    first_name = models.CharField(_('Name'), max_length=150, blank=True, null=True)
    last_name = models.CharField(_('Surname'), max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.telegram_id}: {self.username}'

    class Meta:
        verbose_name = 'Bot User'
        verbose_name_plural = 'Bot Users'

class TelegramChat (models.Model):
    bot_user = models.ForeignKey(BotUser, verbose_name= _('Bot User'), on_delete=models.CASCADE)
    name = models.CharField(_('Channel Name'), max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.bot_user}: {self.name}'

    class Meta:
        verbose_name = 'Telegram Channel'
        verbose_name_plural = 'Telegram Channels'

class InviteLink(models.Model):
    telegram_chat = models.ForeignKey(TelegramChat, verbose_name=_('Telegram Channel'), on_delete=models.CASCADE)
    creates_join_request = models.BooleanField(_('Request to Add'), default=False)

    creator = models.CharField(_('Creator'), max_length=250, blank=True, null=True)
    expire_date = models.CharField(_('Expire date'), max_length=150, blank=True, null=True)

    link = models. CharField(_('Link'), max_length=150, blank=True, null=True)
    is_primary = models.BooleanField(_('Is primary'), blank=True, null=True)
    is_revoked = models.BooleanField(_('Is revoked'), blank=True, null=True)

    member_limit = models.IntegerField(_('Subscription limit'), blank=True, null=True)
    name = models.CharField(_('Name'), max_length=150, blank=True, null=True)
    pending_join_request_count = models.IntegerField(_('pending_join_request_count'), blank=True, null=True)

    class Meta:
        verbose_name = 'Invitation Link'
        verbose_name_plural = 'Invitation Links'

class TelegramSubscriber (models.Model):
    invite_link = models.ForeignKey(TelegramChat, verbose_name = _('Invitation Link'), on_delete = models.CASCADE)
    telegram_id = models.PositiveBigIntegerField(_('ID Telegram'), db_index=True, unique=True)
    username = models.CharField(_('Username'), max_length=150, blank=True, null=True)
    first_name = models.CharField(_('Name'), max_length=150, blank=True, null=True)
    last_name = models. CharField(_('Surname'), max_length=150, blank=True, null=True)
    subscribed = models.BooleanField(_('Subscribed'), default=False)
    datetime_subscribe = models.DateTimeField(_('Subscription time'), blank=True, null=True)
    datetime_unsubscribe = models.DateTimeField(_('Unsubscription time'), blank=True, null=True)

    def __str__(self):
        return f'{self.telegram_id}: {self.username}'

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'