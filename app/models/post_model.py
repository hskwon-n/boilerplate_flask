from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import db


class PostModel(db.Model):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    views: Mapped[int] = mapped_column(Integer)
