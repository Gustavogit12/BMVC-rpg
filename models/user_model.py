from models.rpg_engine import ChildOfHades, ChildOfPoseidon, ChildOfZeus


class UserModel:
    """Guarda os usuários e confere login e senha."""

    users = {
        "thalia": {"password": "raio123", "character": ChildOfZeus("Thalia")},
        "percy": {"password": "mar123", "character": ChildOfPoseidon("Percy")},
        "nico": {"password": "sombra123", "character": ChildOfHades("Nico")},
    }

    @staticmethod
    def authenticate(username, password):
        user = UserModel.users.get(username.lower())
        if user is not None and user["password"] == password:
            return True
        return False

    @staticmethod
    def get_character(username):
        user = UserModel.users.get(username)
        if user is None:
            return None
        return user["character"]

    @staticmethod
    def test_credentials():
        result = []
        for username in UserModel.users:
            result.append({
                "username": username,
                "password": UserModel.users[username]["password"],
            })
        return result