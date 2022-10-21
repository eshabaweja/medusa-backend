from pprint import pprint
from sqlalchemy.orm import Session
from datetime import datetime

from models.cycle import Cycles


class CycleCRUD:
    def create(self, db: Session, start_date: datetime) -> int:
        new_cycle = Cycles(start=start_date)
        try:
            db.add(new_cycle)
            db.flush()

            db.refresh()

            id = new_cycle.id

        except Exception as e:
            pprint(e)
            id = -1

        return id


cycle_crud = CycleCRUD()
