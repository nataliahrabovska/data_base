"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import film_has_director_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class FilmHasDirectorService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = film_has_director_dao
