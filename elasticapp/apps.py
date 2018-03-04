from django.apps import AppConfig


class ElasticappConfig(AppConfig):
    name = 'elasticapp'

    def ready(self):
        import elasticapp.signals
