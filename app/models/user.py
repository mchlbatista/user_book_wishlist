import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(128))
    created_at = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.utcnow, nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=datetime.datetime.utcnow,
        default=datetime.datetime.utcnow,
        nullable=False,
    )

    wishlists = db.relationship("Wishlist", backref="user", lazy="select")

    def save(self):
        db.session.add(self)
        db.session.commit()
