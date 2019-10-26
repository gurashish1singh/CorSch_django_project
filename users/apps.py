from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Importing signals so that we make a profile of a new user automatically -> see signals.py
    def ready(self):
        import users.signals
