"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import director_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class DirectorService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = director_dao
