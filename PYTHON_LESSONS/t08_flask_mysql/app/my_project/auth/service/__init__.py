"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.client_service import ActorService
from .orders.film_service import FilmService
from .orders.budget_service import BudgetService
from .orders.client_type_service import ClientTypeService

actor_service = ActorService()
film_service = FilmService()
budget_service = BudgetService()
client_type_service = ClientTypeService()
