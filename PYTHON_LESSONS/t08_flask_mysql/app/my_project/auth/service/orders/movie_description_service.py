"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import movie_description_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class MovieDescriptionService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = movie_description_dao
