import datetime
from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    isbn = db.Column(db.String(255))
    date_publication = db.Column(db.Date)
    created_at = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.utcnow, nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow,
        nullable=False,
    )

    def save(self):
        db.session.add(self)
        db.session.commit()
