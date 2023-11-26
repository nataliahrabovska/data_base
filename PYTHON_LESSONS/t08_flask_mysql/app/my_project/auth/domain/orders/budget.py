"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Budget(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "budget"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actors_fee = db.Column(db.Integer)
    team_salary = db.Column(db.Integer)
    post_production = db.Column(db.Integer)
    marketing = db.Column(db.Integer)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))

    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Budget({self.id}, '{self.actors_fee}', '{self.team_salary}', '{self.post_production}', '{self.film_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "actors_fee": self.actors_fee,
            "team_salary": self.team_salary,
            "post_production": self.post_production,
            "marketing": self.marketing,
            "film_id": self.film_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Budget:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Budget(
            actors_fee=dto_dict.get("actors_fee"),
            team_salary=dto_dict.get("team_salary"),
            post_production=dto_dict.get("post_production"),
            marketing=dto_dict.get("marketing"),
            film_id=dto_dict.get("film_id"),
        )
        return obj
