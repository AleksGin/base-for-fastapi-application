from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import Base
from .mixins.int_id_primary_key import IntIdPkMixin


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    likes: Mapped[int]
    posts: Mapped[int]

    __table_args__ = (
        UniqueConstraint("likes", "posts"),
    )
