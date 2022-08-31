"""Base Models Module"""
from flask_sqlalchemy import SQLAlchemy
db: SQLAlchemy = SQLAlchemy()

class BaseModelMixin:
    """Base Model Class"""

    def save(self):
        """Save model data in database"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete(cls, obj_id: int):
        """Delete model data from database"""
        is_successful = cls.query.filter_by(id=obj_id).delete()
        db.session.commit()
        return bool(is_successful)
