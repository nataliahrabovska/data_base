"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Cast(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "cast"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    salary = db.Column(db.Integer)
    screen_time = db.Column(db.Integer)
    role = db.Column(db.String(300))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'))

    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Cast({self.id}, '{self.salary}', '{self.role}', '{self.film_id}', '{self.actor_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "salary": self.salary,
            "screen_time": self.screen_time,
            "role": self.role,
            "film_id": self.film_id,
            "actor_id": self.actor_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Cast:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Cast(
            salary=dto_dict.get("salary"),
            screen_time=dto_dict.get("screen_time"),
            role=dto_dict.get("role"),
            film_id=dto_dict.get("film_id"),
            actor_id=dto_dict.get("actor_id"),
        )
        return obj
