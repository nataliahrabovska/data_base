"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Review


class ReviewDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Review

