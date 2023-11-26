"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.client_dao import ActorDAO
from .orders.film_dao import FilmDAO
from .orders.budget_dao import BudgetDAO
from .orders.client_type_dao import ClientTypeDAO

actor_dao = ActorDAO()
film_dao = FilmDAO()
budget_dao = BudgetDAO()
client_type_dao = ClientTypeDAO()
