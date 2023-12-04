"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import event

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.movie_description import MovieDescription


class Film(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "film"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300))
    duration = db.Column(db.Integer)
    release_year = db.Column(db.Integer)
    genre = db.Column(db.String(300))
    country = db.Column(db.String(300))
    budget = db.relationship("Budget", backref='film')
    movie_description_id = db.Column(db.Integer, db.ForeignKey('movie_description.id'), nullable=True)

    film_directors = db.relationship("FilmHasDirector", backref="film")

    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Film({self.id}, '{self.name}', '{self.duration}', '{self.release_year}', '{self.genre}', '{self.country}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

        budget = [budget.put_into_dto() for budget in self.budget]

        directors_list = [
            {
                "id": directorFilmPair.director.id,
                "name": directorFilmPair.director.name,
                "surname": directorFilmPair.director.surname,
                "age": directorFilmPair.director.age,
                "nationality": directorFilmPair.director.nationality,
                "experience": directorFilmPair.director.experience,
                "gender": directorFilmPair.director.gender,
            } for directorFilmPair in self.film_directors]

        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "release_year": self.release_year,
            "genre": self.genre,
            "country": self.country,
            "budget": budget,
            "movie_description_info": {
                "id": self.movie_description_info.id,
                "plot": self.movie_description_info.plot,
                "scene": self.movie_description_info.scene,
                "action_time": self.movie_description_info.action_time,
                "awards": self.movie_description_info.awards,
                "age_group": self.movie_description_info.age_group}
            ,
            "directors-list": directors_list

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Film:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        movie_description_info_dict = dto_dict.get("movie_description_info", {})

        movie_description_info = MovieDescription.create_from_dto(movie_description_info_dict)

        obj = Film(
            name=dto_dict.get("name"),
            duration=dto_dict.get("duration"),
            release_year=dto_dict.get("release_year"),
            genre=dto_dict.get("genre"),
            country=dto_dict.get("country"),
            budget=dto_dict.get("budget"),
            movie_description_info=movie_description_info  # Assign the created MovieDescription instance
        )
        return obj


def receive_after_insert_review(mapper, connection, target):
    film_id = target.film_id
    film = db.session.query(Film).get(film_id)
    if film:
        film_reviews = film.reviews if hasattr(film, 'reviews') else []
        film_reviews.append(target)


