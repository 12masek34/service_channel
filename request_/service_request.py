import os

import requests
from dotenv import load_dotenv

from sheet.google_sheet import service, spreadsheet_id

load_dotenv()


class MyRequest:
    MAX_ROWS = 1000

    @staticmethod
    def get_course_usd_from_cb() -> int:
        """
        Получает курс доллара.
        """
        response = requests.get(os.getenv('URL_USD_COURSE')).json()
        usd_course = response['Valute']['USD']['Value']
        return int(usd_course)

    def get_google_sheet_table(self) -> list[list]:
        """
        Получает таблицу google sheets.
        """
        values = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=f'A1:E{self.MAX_ROWS}',
            majorDimension='ROWS'
        ).execute()

        return values['values'][1:]
