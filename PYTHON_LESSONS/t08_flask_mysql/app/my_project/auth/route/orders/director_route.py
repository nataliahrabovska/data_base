"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import director_controller
from t08_flask_mysql.app.my_project.auth.domain import Director

director_bp = Blueprint('director', __name__, url_prefix='/director')


@director_bp.get('')
def get_all_director() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(director_controller.find_all()), HTTPStatus.OK)


@director_bp.post('')
def create_director() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    director = Director.create_from_dto(content)
    director_controller.create(director)
    return make_response(jsonify(director.put_into_dto()), HTTPStatus.CREATED)


@director_bp.get('/<int:director_id>')
def get_director(director_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(director_controller.find_by_id(director_id)), HTTPStatus.OK)


@director_bp.put('/<int:director_id>')
def update_director(director_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    director = Director.create_from_dto(content)
    director_controller.update(director_id, director)
    return make_response("director updated", HTTPStatus.OK)


@director_bp.patch('/<int:director_id>')
def patch_director(director_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    director_controller.patch(director_id, content)
    return make_response("director updated", HTTPStatus.OK)


@director_bp.delete('/<int:director_id>')
def delete_director(director_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    director_controller.delete(director_id)
    return make_response("director deleted", HTTPStatus.OK)
