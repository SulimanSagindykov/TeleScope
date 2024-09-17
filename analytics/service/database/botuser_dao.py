from asgiref.sync import sync_to_async


@sync_to_async
def update_or_create_tg_user():
    