from django.apps import AppConfig


class BaseConfig(AppConfig):
    """Base configuration for this app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
