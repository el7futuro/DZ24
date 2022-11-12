import os

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app import DATA_DIR
from request import BatchRequestSchema
from utils import query_action, check_file

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/perform_query", methods=['POST'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    try:
        action_list = BatchRequestSchema().load(data=request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    if check_file():
        raise FileNotFoundError(400)



    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос

    result = None
    for query in action_list['queries']:
        result = query_action(cmd=query['cmd'], value=query['value'], data=result)
    # вернуть пользователю сформированный результат
    return jsonify(result)
