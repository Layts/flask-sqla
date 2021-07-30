import enum


class TicketStatus(enum.Enum):
    OPEN = 0
    ANSWERED = 1
    WAITING = 2
    CLOSED = 3


TICKET_STATUS_ROUTERS = {
    TicketStatus.OPEN.value: [TicketStatus.ANSWERED.value, TicketStatus.CLOSED.value],
    TicketStatus.ANSWERED.value: [TicketStatus.WAITING.value, TicketStatus.CLOSED.value],
    TicketStatus.WAITING.value: [TicketStatus.CLOSED.value],
    TicketStatus.CLOSED: []

}
DB_USER = "postgres"
DB_PWD = "postgres"
DB_URL = f"postgresql://{DB_USER}:{DB_PWD}@localhost:5432/testdb"