from pprint import pprint

from service.table_manager import TableManager


def main():
    table_manager = TableManager()
    table_manager.set_raw_table()
    table_manager.set_course_usd()
    table_manager.add_rub_to_table()
    table = table_manager.get_table()
    table_manager.db_manager.add_table_to_db(table)


def check_orders_date():
    table_manager = TableManager()
    orders = table_manager.db_manager.get_order_from_db_all()
    overdue_orders = table_manager.time_manager.check_overdue_orders(orders)
    if overdue_orders:
        message = table_manager.message_manager.prepare_message(overdue_orders)
        table_manager.telegram_manager.send_message(message)
