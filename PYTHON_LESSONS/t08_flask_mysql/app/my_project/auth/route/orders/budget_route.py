"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import budget_controller
from t08_flask_mysql.app.my_project.auth.domain import Budget

budget_bp = Blueprint('budget', __name__, url_prefix='/budget')


@budget_bp.get('')
def get_all_budget() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(budget_controller.find_all()), HTTPStatus.OK)


@budget_bp.post('')
def create_budget() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    budget = Budget.create_from_dto(content)
    budget_controller.create(budget)
    return make_response(jsonify(budget.put_into_dto()), HTTPStatus.CREATED)


@budget_bp.get('/<int:budget_id>')
def get_budget(budget_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(budget_controller.find_by_id(abudget_id)), HTTPStatus.OK)


@budget_bp.put('/<int:budget_id>')
def update_budget(budget_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    budget = Budget.create_from_dto(content)
    budget_controller.update(budget_id, budget)
    return make_response("budget updated", HTTPStatus.OK)


@budget_bp.patch('/<int:budget_id>')
def patch_budget(budget_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    budget_controller.patch(budget_id, content)
    return make_response("budget updated", HTTPStatus.OK)


@budget_bp.delete('/<int:budget_id>')
def delete_budget(budget_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    budget_controller.delete(budget_id)
    return make_response("budget deleted", HTTPStatus.OK)
