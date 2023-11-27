"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import cast_controller
from t08_flask_mysql.app.my_project.auth.domain import Cast

cast_bp = Blueprint('cast', __name__, url_prefix='/cast')


@cast_bp.get('')
def get_all_cast() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(cast_controller.find_all()), HTTPStatus.OK)


@cast_bp.post('')
def create_cast() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    cast = Cast.create_from_dto(content)
    cast_controller.create(cast)
    return make_response(jsonify(cast.put_into_dto()), HTTPStatus.CREATED)


@cast_bp.get('/<int:cast_id>')
def get_cast(cast_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(cast_controller.find_by_id(cast_id)), HTTPStatus.OK)


@cast_bp.put('/<int:cast_id>')
def update_cast(cast_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    cast = Cast.create_from_dto(content)
    cast_controller.update(cast_id, cast)
    return make_response("cast updated", HTTPStatus.OK)


@cast_bp.patch('/<int:cast_id>')
def patch_cast(cast_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    cast_controller.patch(cast_id, content)
    return make_response("budget updated", HTTPStatus.OK)


@cast_bp.delete('/<int:cast_id>')
def delete_cast(cast_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    cast_controller.delete(cast_id)
    return make_response("cast deleted", HTTPStatus.OK)
