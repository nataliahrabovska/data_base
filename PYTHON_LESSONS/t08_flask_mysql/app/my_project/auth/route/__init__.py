"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.actor_route import actor_bp
    from .orders.film_route import film_bp
    from .orders.budget_route import budget_bp
    from .orders.cast_route import cast_bp
    from .orders.director_route import director_bp
    from .orders.film_has_director_route import film_has_director_bp
    from .orders.movie_description_route import movie_description_bp
    from .orders.client_type_route import client_type_bp

    app.register_blueprint(actor_bp)
    app.register_blueprint(film_bp)
    app.register_blueprint(budget_bp)
    app.register_blueprint(cast_bp)
    app.register_blueprint(director_bp)
    app.register_blueprint(film_has_director_bp)
    app.register_blueprint(movie_description_bp)
    app.register_blueprint(client_type_bp)
