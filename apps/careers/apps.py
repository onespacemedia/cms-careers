from cms.models import PageBaseSearchAdapter
from django.apps import AppConfig
from watson import search as watson


class CareersConfig(AppConfig):
    name = 'careers'

    def ready(self):
        Career = self.get_model('Career')
        watson.register(Career, adapter_cls=PageBaseSearchAdapter)
