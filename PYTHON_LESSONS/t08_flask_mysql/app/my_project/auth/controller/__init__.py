"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.client_controller import ActorController
from .orders.film_controller import FilmController
from .orders.budget_controller import BudgetController
from .orders.client_type_controller import ClientTypeController

actor_controller = ActorController()
film_controller = FilmController()
budget_controller = BudgetController()
client_type_controller = ClientTypeController()
