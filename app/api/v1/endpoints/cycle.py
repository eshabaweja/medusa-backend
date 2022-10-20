from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.cycle import Cycles
from crud.cycle_crud import cycle_crud
from schema import cycle
from api.deps import get_db

router = APIRouter()

DATE_FORMAT = "%d %m %Y"


@router.post("/start")
def _create_new_cycle(request_body: cycle.StartCycle, db: Session = Depends(get_db)):
    start_date_obj = datetime.strptime(request_body.start_date, DATE_FORMAT)

    id = cycle_crud.create(db, start_date_obj)

    return {"id": id}
