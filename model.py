import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app=Flask(__name__)

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

class Team(db.Model):

    __tablename__="teams"

    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    team_name=db.Column(db.String(255), unique=True,nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

class Project(db.Model):

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)


if __name__=="__main__":
    connect_to_db(app)
    with app.app_context():
        db.create_all()
        print("Connected to db!")