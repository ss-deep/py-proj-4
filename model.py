from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    
    __tablename__="user"

    id = db.column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(255), unitque=True, nullable=False)
    password=db.column(db.String(255),nullable=False)