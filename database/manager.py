from database.models import Orders, get_db, Session


class DBManager:
    def __init__(self):
        self.db: Session = get_db()

    def add_table_to_db(self, table: list[list]):
        for raw in table:
            try:
                obj = Orders(id=raw[0],
                             order_id=raw[1],
                             price_usd=raw[2],
                             delivery_time=raw[3],
                             price_rub=raw[4])
            except IndexError:
                continue
            self.db.merge(obj)
            self.db.commit()

    def get_order_from_db_by_id(self, id_: int) -> Orders:
        return self.db.query(Orders).filter(Orders.id == id_)

    def get_order_from_db_all(self) -> list[Orders]:
        return self.db.query(Orders).all()
