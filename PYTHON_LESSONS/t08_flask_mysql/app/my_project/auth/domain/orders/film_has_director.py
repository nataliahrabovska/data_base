from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class FilmHasDirector(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "film_has_director"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    salary = db.Column(db.Integer)
    the_number_of_films_made = db.Column(db.Integer)
    awards = db.Column(db.String(3000))

    # Define foreign keys
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))

    # # Define relationships
    # film = db.relationship("Film", backref='film_has_director')
    # director = db.relationship("Director", backref='film_has_director')

    def __repr__(self) -> str:
        return f"FilmHasDirector({self.id}, '{self.salary}', '{self.the_number_of_films_made}', '{self.awards}', '{self.film_id}', '{self.director_id}',)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "salary": self.salary,
            "the_number_of_films_made": self.the_number_of_films_made,
            "awards": self.awards,
            "film_id": self.film_id,
            "film_info": self.film.name,
            "director_id": self.director_id,
            "director_info": self.director.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> FilmHasDirector:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = FilmHasDirector(
            salary=dto_dict.get("salary"),
            the_number_of_films_made=dto_dict.get("the_number_of_films_made"),
            awards=dto_dict.get("awards"),
            film_id=dto_dict.get("film_id"),
            director_id=dto_dict.get("director_id"),
        )
        return obj
