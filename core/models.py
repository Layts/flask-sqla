from core.app import db
import datetime
from core.srv.config import TicketStatus, TICKET_STATUS_ROUTERS


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modified_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    text = db.Column(db.String(500))
    topic = db.Column(db.String(500))
    email = db.Column(db.String(50))
    status = db.Column(db.Integer(), default=TicketStatus.OPEN.value
    )
    comments = db.relationship('Comment')

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))
        return d

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def check_permission(self, new_status: int) -> bool:
        if new_status in TICKET_STATUS_ROUTERS.get(self.status):
            return True
        else:
            return False


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer(), db.ForeignKey('ticket.id'))
    text = db.Column(db.String(500))
    email = db.Column(db.String(50))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()