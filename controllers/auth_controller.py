import os

from bottle import redirect, request, response, static_file, template

from models.user_model import UserModel

SECRET = "segredo-do-meu-projeto"


def get_logged_user():
    return request.get_cookie("user", secret=SECRET)


def index():
    if get_logged_user():
        redirect("/dashboard")
    redirect("/login")


def login_get():
    return template("login", error=None, username="",
                    test_users=UserModel.test_credentials())


def login_post():
    username = request.forms.get("username", "").strip().lower()
    password = request.forms.get("password", "")

    if UserModel.authenticate(username, password):
        response.set_cookie("user", username, secret=SECRET, path="/")
        redirect("/dashboard")

    return template("login", error="Usuário ou senha inválidos.", username=username,
                    test_users=UserModel.test_credentials())


def dashboard():
    username = get_logged_user()
    if not username:
        redirect("/login")
    character = UserModel.get_character(username)
    return template("dashboard", personagem=character)


def logout():
    response.delete_cookie("user", path="/")
    redirect("/login")


def register_routes(app, base_dir):
    static_folder = os.path.join(base_dir, "static")

    def serve_static(filepath):
        return static_file(filepath, root=static_folder)

    app.route("/", method="GET", callback=index)
    app.route("/login", method="GET", callback=login_get)
    app.route("/login", method="POST", callback=login_post)
    app.route("/dashboard", method="GET", callback=dashboard)
    app.route("/logout", method="POST", callback=logout)
    app.route("/static/<filepath:path>", method="GET", callback=serve_static)