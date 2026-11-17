import os

from bottle import Bottle, TEMPLATE_PATH, run

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Diz ao Bottle onde ficam os templates (.tpl) da camada View
TEMPLATE_PATH.insert(0, os.path.join(BASE_DIR, "views"))

from controllers.auth_controller import register_routes  # noqa: E402

app = Bottle()
register_routes(app, BASE_DIR)

if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8080, debug=True, reloader=True)