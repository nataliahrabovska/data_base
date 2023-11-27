"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.actor_controller import ActorController
from .orders.film_controller import FilmController
from .orders.budget_controller import BudgetController
from .orders.cast_controller import CastController
from .orders.director_controller import DirectorController
from .orders.film_has_director_controller import FilmHasDirectorController
from .orders.movie_description_controller import MovieDescriptionController
from .orders.client_type_controller import ClientTypeController

actor_controller = ActorController()
film_controller = FilmController()
budget_controller = BudgetController()
cast_controller = CastController()
director_controller = DirectorController()
film_has_director_controller = FilmHasDirectorController()
movie_description_controller = MovieDescriptionController()
client_type_controller = ClientTypeController()
