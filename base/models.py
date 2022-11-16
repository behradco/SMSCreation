from flask_login import UserMixin
from base import login_manager

@login_manager.user_loader
def load_user(id):
    return User(id=id)

def validation(username, password):
    return str.__eq__(username, "behrad") and str.__eq__(password, "behrad")

class User(UserMixin):
    id = 1
    username = None
    password = None

    def __init__(self, id=None, username=None, password=None):
        if id:
            self.id = id
        elif username and password:
            self.username = username
            self.password = password
