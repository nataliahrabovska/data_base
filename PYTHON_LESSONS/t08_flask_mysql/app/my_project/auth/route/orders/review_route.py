"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import review_controller
from t08_flask_mysql.app.my_project.auth.domain import Review

review_bp = Blueprint('review', __name__, url_prefix='/review')


@review_bp.get('')
def get_all_review() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)


@review_bp.post('')
def create_review() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@review_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(review_controller.find_by_id(review_id)), HTTPStatus.OK)


@review_bp.put('/<int:review_id>')
def update_review(director_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.update(director_id, review)
    return make_response("review updated", HTTPStatus.OK)


@review_bp.patch('/<int:review_id>')
def patch_review(review_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    review_controller.patch(review_id, content)
    return make_response("review updated", HTTPStatus.OK)


@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    review_controller.delete(review_id)
    return make_response("review deleted", HTTPStatus.OK)
