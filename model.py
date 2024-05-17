import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app=Flask(__name__)

app.app_context().push()

db=SQLAlchemy()
load_dotenv()

POSTGRES_URI=os.getenv("POSTGRES_URI")

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

class User(db.Model):
    
    __tablename__="users"

    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password=db.Column(db.String(255),nullable=False)

    teams=db.relationship("Team",backref="user",lazy=True)
    

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

class Team(db.Model):

    __tablename__="teams"

    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    team_name=db.Column(db.String(255), unique=True,nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    project=db.relationship("Project",backref="teams",lazy=True)

    def __init__(self,team_name,user_id):
        self.team_name=team_name
        self.user_id=user_id

class Project(db.Model):

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)

    def __init__(self,project_name,description,completed,team_id):
        self.project_name=project_name
        self.description=description
        self.completed=completed
        self.team_id=team_id


if __name__=="__main__":
    connect_to_db(app)
    with app.app_context():
        db.create_all()
        print("Connected to db!")