"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


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

    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Film({self.id}, '{self.name}', '{self.duration}', '{self.release_year}', '{self.genre}', '{self.country}',)"

    def put_into_dto(self) -> Dict[str, Any]:

        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

        budget = [budget.put_into_dto() for budget in self.budget]
        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "release_year": self.release_year,
            "genre": self.genre,
            "experience": self.experience,
            "country": self.country,
            "budget": budget,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Film:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Film(
            name=dto_dict.get("name"),
            duration=dto_dict.get("duration"),
            release_year=dto_dict.get("release_year"),
            genre=dto_dict.get("genre"),
            experience=dto_dict.get("experience"),
            country=dto_dict.get("country"),
            budget=dto_dict.get("budget"),
        )
        return obj
