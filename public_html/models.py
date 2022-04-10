from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .view import app
# Create database connection object
db = SQLAlchemy(app)

class Patient():
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db(String(20), nullable=False))
    prenom = db.Column(db.String(20), nullable=False)

class Critere():
    id = db.Column(db.Integer, primary_key=True)
    valeur = db.Column(db(String(20), nullable=False))

class Diagnostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    criteres = db.Column(db.Criteres, nullable=False)
    #idPatient = db.Column(db.Patient.id, nullable=False)

    def __init__(self, criteres):
        self.criteres = criteres


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("What's your favorite scary movie?", Gender['female']))
    db.session.commit()
    lg.warning('Database initialized!')
