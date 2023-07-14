from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Permission:
    CHAT_BOT = 0x01
    SEARCH_USER = 0x02
    REQUEST_FRIEND = 0x04
    CHAT_UNKNOWN = 0x08
    EDIT_OWN = 0x10
    CHAT_ALL = 0x20
    EDIT_ALL = 0x40


class Profile(db.Model):
    id = db.Column(db.UUID, primary_key=True, server_default=db.text("uuid_generate_v4()"))
    name = db.Column(db.VARCHAR(30), nullable=False)
    privileges = db.Column(db.INTEGER)

    users = db.relationship("Users", backref="profile")

    def __repr__(self):
        return f"<profile: {self.name}>"


class Verification(db.Model):
    user_id = db.Column(db.UUID, db.ForeignKey("users.id"), primary_key=True)
    code = db.Column(db.UUID, nullable=False, server_default=db.text("uuid_generate_v4()"))

    def __repr__(self):
        return f"<verification: {self.user}>"


class Gender(db.Model):
    id = db.Column(db.UUID, primary_key=True, server_default=db.text('uuid_generate_v4()'))
    name = db.Column(db.VARCHAR(15), nullable=False)

    users = db.relationship("Users", backref="gender")

    def __repr__(self):
        return f"<gender: {self.name}>"


class RelationType(db.Model):
    __tablename__ = "relation_type"

    id = db.Column(db.UUID, primary_key=True, server_default=db.text("uuid_generate_v4()"))
    name = db.Column(db.VARCHAR(15), nullable=False)

    def __repr__(self):
        return f"<relation_type: {self.name}>"


class Relation(db.Model):
    user_id_1 = db.Column(db.UUID, db.ForeignKey("users.id"), primary_key=True, nullable=False)
    user_id_2 = db.Column(db.UUID, db.ForeignKey("users.id"), primary_key=True, nullable=False)
    connection_time = db.Column(db.DateTime, nullable=False)
    relation_type_id = db.Column(db.UUID, db.ForeignKey("relation_type.id"), nullable=False)

    def __repr__(self):
        return f"<relation: {self.user_id_1}, {self.user_id_2}>"


class Chat(db.Model):
    id = db.Column(db.UUID, primary_key=True, server_default=db.text("uuid_generate_v4()"))
    message = db.Column(db.TEXT)
    sender_id = db.Column(db.UUID, db.ForeignKey("users.id"), nullable=False)
    receiver_id = db.Column(db.UUID, db.ForeignKey("users.id"), nullable=False)
    sent_time = db.Column(db.DateTime, nullable=False)
    seen = db.Column(db.BOOLEAN, nullable=False)

    def __repr__(self):
        return f"<chat: {self.sender_id}, {self.receiver_id}>"


class Users(db.Model):
    id = db.Column(db.UUID, primary_key=True, server_default=db.text("uuid_generate_v4()"))
    session_id = db.Column(db.UUID, server_default=db.text("uuid_generate_v4()"))
    tag = db.Column(db.INTEGER, nullable=False)
    username = db.Column(db.VARCHAR(60), nullable=False)
    age = db.Column(db.INTEGER)
    email = db.Column(db.VARCHAR(120), nullable=False)
    password_hash = db.Column(db.VARCHAR(120), nullable=False)
    creation_time = db.Column(db.DateTime)
    image_id = db.Column(db.UUID, server_default=db.text("uuid_generate_v4()"))

    gender_id = db.Column(db.UUID, db.ForeignKey("gender.id"), nullable=False)
    profile_id = db.Column(db.UUID, db.ForeignKey("profile.id"), nullable=False)

    verification = db.relationship("Verification", backref="user")

    @property
    def password(self):
        return "Not readable"

    @password.setter
    def password(self, data):
        self.password_hash = generate_password_hash(data)

    def verify_password(self, data):
        return check_password_hash(data, self.password_hash)

    def __repr__(self):
        return f"<users: {self.username}>"
