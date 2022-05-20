import datetime

from database.manager import DBManager
from request_.service_request import MyRequest
from service.message_manager import MessageManager
from service.time_manager import TimeManager
from telegram.manager import TelegramManager


class TableManager(MyRequest):

    def __init__(self):
        self.message_manager = MessageManager()
        self.telegram_manager = TelegramManager()
        self.db_manager: DBManager = DBManager()
        self.time_manager = TimeManager()
        self._course_usd: int | None = None
        self._table: list[list] | None = None

    def set_raw_table(self):
        self._table = self.get_google_sheet_table()

    def set_course_usd(self):
        self._course_usd = self.get_course_usd_from_cb()

    def get_table(self) -> list[list]:
        return self._table

    def add_rub_to_table(self) -> list[list]:
        """
         Добавляет значение в рублях.
        """
        for row in self._table:
            try:
                row[0] = int(row[0])
                row[1] = int(row[1])
                row[2] = int(row[2])
                row[3] = datetime.datetime.strptime(row[3], "%d.%m.%Y").date()
                rub = row[2] * self._course_usd
                row.append(rub)
            except IndexError:
                continue

        return self._table



