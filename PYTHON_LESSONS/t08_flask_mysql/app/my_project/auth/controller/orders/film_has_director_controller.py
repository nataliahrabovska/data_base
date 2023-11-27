"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import film_has_director_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class FilmHasDirectorController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = film_has_director_service
