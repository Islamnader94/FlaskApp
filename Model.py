from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, ValidationError
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), unique=True, nullable=False)
    details = db.relationship('Detailes', backref=db.backref('user', lazy=True))

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Detailes(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, unique=True, nullable=False)
    address = db.Column(db.String(150), unique=True, nullable=False)
    country_origin = db.Column(db.String(150), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __init__(self, age, address, country_origin):
        self.age = age
        self.address = address
        self.country_origin = country_origin


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name  = fields.String(required=True)


class DetailesSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    age = fields.Integer(required=True)
    address = fields.String(required=True)
    country_origin = fields.String(required=True)
    user_id = fields.Integer(required=False)
