from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto
from lab4.app.my_project.auth.domain.orders.client import Client


class Account(db.Model):
    __bind_key__ = 'accounts_db'
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Account:
        obj = Client(**dto_dict)
        return obj