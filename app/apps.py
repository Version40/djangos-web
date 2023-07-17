from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        import app.signals
        from django.contrib.auth.models import User

        def get_order_count(self):
            from .models import OrderItem
            order_items = OrderItem.objects.filter(order__is_paid=False, order__user=self)
            total_count = order_items.count()

            return total_count

        User.add_to_class('get_order_count', get_order_count)

