"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import film_controller
from t08_flask_mysql.app.my_project.auth.domain import Film

film_bp = Blueprint('film', __name__, url_prefix='/film')


@film_bp.get('')
def get_all_films() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(film_controller.find_all()), HTTPStatus.OK)


@film_bp.post('')
def film_actor() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    film = Film.create_from_dto(content)
    film_controller.create(film)
    return make_response(jsonify(film.put_into_dto()), HTTPStatus.CREATED)


@film_bp.get('/<int:film_id>')
def get_film(film_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(film_controller.find_by_id(film_id)), HTTPStatus.OK)


@film_bp.put('/<int:film_id>')
def update_film(film_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    film = Film.create_from_dto(content)
    film_controller.update(film_id, film)
    return make_response("film updated", HTTPStatus.OK)


@film_bp.patch('/<int:film_id>')
def patch_film(film_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    film_controller.patch(film_id, content)
    return make_response("film updated", HTTPStatus.OK)


@film_bp.delete('/<int:film_id>')
def delete_film(film_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    film_controller.delete(film_id)
    return make_response("Film deleted", HTTPStatus.OK)
