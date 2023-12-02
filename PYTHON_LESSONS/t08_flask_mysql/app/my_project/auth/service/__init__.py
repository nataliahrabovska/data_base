"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.actor_service import ActorService
from .orders.film_service import FilmService
from .orders.budget_service import BudgetService
from .orders.cast_service import CastService
from .orders.director_service import DirectorService
from .orders.film_has_director_service import FilmHasDirectorService
from .orders.movie_description_service import MovieDescriptionService

actor_service = ActorService()
film_service = FilmService()
budget_service = BudgetService()
cast_service = CastService()
director_service = DirectorService()
film_has_director_service = FilmHasDirectorService()
movie_description_service = MovieDescriptionService()
