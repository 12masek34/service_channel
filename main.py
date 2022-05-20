from time import sleep

from database.models import create_db
from app import main, check_and_send_orders_to_telegram

ONE_DAY = 1440
ONE_MINUTE = 60

if __name__ == '__main__':

    create_db()
    count_minutes = 0

    while True:
        main()
        sleep(ONE_MINUTE)
        count_minutes += 1

        if count_minutes == ONE_DAY:
            check_and_send_orders_to_telegram()
