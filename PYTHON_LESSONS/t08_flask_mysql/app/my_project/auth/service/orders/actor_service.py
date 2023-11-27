"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import actor_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ActorService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = actor_dao
