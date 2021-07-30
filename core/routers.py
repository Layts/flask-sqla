from flask import request, Blueprint, make_response
from core.models import Ticket, Comment

app_route = Blueprint('route', __name__)


@app_route.route('/ticket', methods=['POST'])
def add_ticket():
    input_data = request.json
    if not input_data:
        res = make_response("Empty body", 400)
    else:
        ticket = Ticket(**input_data)
        ticket.save_to_db()
        res = make_response("Success", 200)
    return res


@app_route.route('/ticket/set_state', methods=['PUT'])
def set_ticket_state():
    input_data = request.json
    if not input_data:
        res = make_response("Empty body", 400)
    else:
        new_state = input_data.get("state_id")
        ticket = Ticket.query.filter_by(id=input_data.get("ticket_id")).first()
        if ticket.check_permission(new_state):
            ticket.status = new_state
            ticket.save_to_db()
            res = make_response("Success", 200)
        else:
            res = make_response("invalid status", 400)
    return res


@app_route.route('/comment', methods=['POST'])
def add_comment():
    input_data = request.json
    if not input_data:
        res = make_response("Empty body", 400)
    else:
        ticket = Ticket.query.filter_by(id=input_data.get("ticket_id")).first()
        if not ticket:
            res = make_response("Invalid ticket_id", 400)
        elif not ticket.check_permission():
            res = make_response("invalid status", 400)
        else:
            comment = Comment(**input_data)
            comment.save_to_db()
            res = make_response("Success", 200)
    return res


@app_route.route('/ticket/<int:ticket_id>')
def get_ticket(ticket_id):
    entry = Ticket.query.filter_by(id=ticket_id).first()
    if not entry:
        res = make_response("Invalid ticket_id", 400)
    else:
        res = make_response(entry.row2dict())
    return res

