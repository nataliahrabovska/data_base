"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Director(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "director"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    age = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    nationality = db.Column(db.String(30))
    gender = db.Column(db.String(30))

    director_films = db.relationship("FilmHasDirector", backref="director")

    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Actor({self.id}, '{self.name}', '{self.surname}', '{self.age}', '{self.experience}', '{self.nationality}', '{self.gender}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        films_list = [directorFilmPair.film.put_into_dto() for directorFilmPair in self.director_films]

        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "nationality": self.nationality,
            "experience": self.experience,
            "gender": self.gender,
            "films_list": films_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Director:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Director(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            age=dto_dict.get("age"),
            nationality=dto_dict.get("nationality"),
            experience=dto_dict.get("experience"),
            gender=dto_dict.get("gender"),
        )
        return obj
