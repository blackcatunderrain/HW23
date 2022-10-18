from flask import Blueprint, request
from marshmallow import ValidationError

from models import RequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        data = RequestParams().load(request.json)
    except ValidationError as e:
        return e.messages, 400
    print(data)

    return data
