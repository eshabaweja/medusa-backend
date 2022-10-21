from pydantic import BaseModel


class StartCycle(BaseModel):
    start_date: str
