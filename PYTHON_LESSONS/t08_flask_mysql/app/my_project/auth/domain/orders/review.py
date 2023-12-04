"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Review(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.String(300))
    plot = db.Column(db.String(300))
    acting = db.Column(db.String(300))
    music = db.Column(db.String(300))
    graphics = db.Column(db.String(300))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))

    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Budget({self.id}, '{self.rating}', '{self.plot}', '{self.acting}', '{self.music}', '{self.graphics}', '{self.film_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "rating": self.rating,
            "plot": self.plot,
            "acting": self.acting,
            "music": self.music,
            "graphics": self.graphics,
            "film_id": self.film_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Review(
            rating=dto_dict.get("rating"),
            plot=dto_dict.get("plot"),
            acting=dto_dict.get("acting"),
            music=dto_dict.get("music"),
            graphics=dto_dict.get("graphics"),
            film_id=dto_dict.get("film_id"),
        )
        return obj
