import datetime

from database.models import Orders


class TimeManager:

    @staticmethod
    def check_overdue_orders(orders: list[Orders]) -> list:
        """
        Проверяет дату. Возвращает все просроченные ордера.
        """
        overdue_orders = []
        for order in orders:
            if order.delivery_time < datetime.datetime.now():
                overdue_orders.append(order)
        return overdue_orders
