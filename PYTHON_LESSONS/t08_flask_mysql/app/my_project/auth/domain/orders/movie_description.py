"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class MovieDescription(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "movie_description"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plot = db.Column(db.String(300))
    scene = db.Column(db.String(30))
    action_time = db.Column(db.String(30))
    awards = db.Column(db.String(30))
    age_group = db.Column(db.String(30))

    film_info = db.relationship("Film", backref="movie_description_info")

    # # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"MovieDescription({self.id}, '{self.plot}', '{self.scene}', '{self.action_time}', '{self.awards}', '{self.age_group}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "plot": self.plot,
            "scene": self.scene,
            "action_time": self.action_time,
            "awards": self.awards,
            "age_group": self.age_group,
            "film_info": [{
                "id": film.id,
                "name": film.name,
                "duration": film.duration,
                "release_year": film.release_year,
                "genre": film.genre,
                "country": film.country}
                for film in self.film_info],

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MovieDescription:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = MovieDescription(
            plot=dto_dict.get("plot"),
            scene=dto_dict.get("scene"),
            action_time=dto_dict.get("action_time"),
            awards=dto_dict.get("awards"),
            age_group=dto_dict.get("age_group"),
            film_info=dto_dict.get("film_info")
        )
        return obj
