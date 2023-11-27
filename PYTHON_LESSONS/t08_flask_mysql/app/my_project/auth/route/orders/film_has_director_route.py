"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import film_has_director_controller
from t08_flask_mysql.app.my_project.auth.domain import FilmHasDirector

film_has_director_bp = Blueprint('film_has_director', __name__, url_prefix='/filmdirector')


@film_has_director_bp.get('')
def get_all_film_has_director() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(film_has_director_controller.find_all()), HTTPStatus.OK)


@film_has_director_bp.post('')
def create_film_has_director() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    film_has_director = FilmHasDirector.create_from_dto(content)
    film_has_director_controller.create(film_has_director)
    return make_response(jsonify(film_has_director.put_into_dto()), HTTPStatus.CREATED)


@film_has_director_bp.get('/<int:film_has_director_id>')
def get_film_has_director(film_has_director_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(film_has_director_controller.find_by_id(film_has_director_id)), HTTPStatus.OK)


@film_has_director_bp.put('/<int:film_has_director_id>')
def update_film_has_director(film_has_director_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    film_has_director = FilmHasDirector.create_from_dto(content)
    film_has_director_controller.update(film_has_director_id, film_has_director)
    return make_response("film has director updated", HTTPStatus.OK)


@film_has_director_bp.patch('/<int:film_has_director_id>')
def patch_film_has_director(film_has_director_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    film_has_director_controller.patch(film_has_director_id, content)
    return make_response("film director updated", HTTPStatus.OK)


@film_has_director_bp.delete('/<int:film_has_director_id>')
def delete_film_has_director(film_has_director_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    film_has_director_controller.delete(film_has_director_id)
    return make_response("Film director deleted", HTTPStatus.OK)
