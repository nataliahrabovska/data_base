"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import movie_description_controller
from t08_flask_mysql.app.my_project.auth.domain import MovieDescription

movie_description_bp = Blueprint('movie_description', __name__, url_prefix='/moviedescription')


@movie_description_bp.get('')
def get_all_movie_description() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(movie_description_controller.find_all()), HTTPStatus.OK)


@movie_description_bp.post('')
def create_movie_description() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    movie_description = request.get_json()
    film = MovieDescription.create_from_dto(movie_description)
    movie_description_controller.create(movie_description)
    return make_response(jsonify(movie_description.put_into_dto()), HTTPStatus.CREATED)


@movie_description_bp.get('/<int:movie_description_id>')
def get_movie_description(movie_description_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(movie_description_controller.find_by_id(movie_description_id)), HTTPStatus.OK)


@movie_description_bp.put('/<int:movie_description_id>')
def update_movie_description(movie_description_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    movie_description = MovieDescription.create_from_dto(content)
    movie_description_controller.update(movie_description_id, movie_description)
    return make_response("movie description updated", HTTPStatus.OK)


@movie_description_bp.patch('/<int:movie_description_id>')
def patch_movie_description(movie_description_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    movie_description_controller.patch(movie_description_id, content)
    return make_response("movie description updated", HTTPStatus.OK)


@movie_description_bp.delete('/<int:movie_description_id>')
def delete_movie_description(movie_description_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    movie_description_controller.delete(movie_description_id)
    return make_response("movie description deleted", HTTPStatus.OK)
