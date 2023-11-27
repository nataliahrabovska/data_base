"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.actor_dao import ActorDAO
from .orders.film_dao import FilmDAO
from .orders.budget_dao import BudgetDAO
from .orders.cast_dao import CastDAO
from .orders.director_dao import DirectorDAO
from .orders.film_has_director_dao import FilmHasDirectorDAO
from .orders.movie_description_dao import MovieDescriptionDAO
from .orders.client_type_dao import ClientTypeDAO

actor_dao = ActorDAO()
film_dao = FilmDAO()
budget_dao = BudgetDAO()
cast_dao = CastDAO()
director_dao = DirectorDAO()
film_has_director_dao = FilmHasDirectorDAO()
movie_description_dao = MovieDescriptionDAO()
client_type_dao = ClientTypeDAO()
