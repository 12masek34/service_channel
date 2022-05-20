from database.models import Orders


class MessageManager:

    @staticmethod
    def prepare_message(orders: list[Orders]):
        message = ''
        for order in orders:
            message += f'Заказ №{order.order_id} истек срок поставки {order.delivery_time}\n'
        return message
