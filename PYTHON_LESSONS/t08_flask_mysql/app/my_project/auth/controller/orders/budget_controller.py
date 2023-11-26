"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import budget_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class BudgetController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = budget_service
