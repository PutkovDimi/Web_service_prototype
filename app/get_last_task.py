from app import db, models
from sqlalchemy import func


def get_last_task():
    qry = db.session.query(func.max(models.Task.id).label("last_number"))
    res = qry.one()
    return res.last_number if res.last_number else 0
