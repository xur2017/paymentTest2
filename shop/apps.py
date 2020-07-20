from django.apps import AppConfig


#class ShopConfig(AppConfig):
#    name = 'shop'

class EcommerceAppConfig(AppConfig):
    name = 'shop'
 
    def ready(self):
        # import signal handlers
        import shop.signals