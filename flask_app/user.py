from flask_login import UserMixin

from flask_app import db


class User(UserMixin, db.Model):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
