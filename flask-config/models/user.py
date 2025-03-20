from models.timestamp import TimestampModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class UserModel(TimestampModel):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String(75), nullable=False, unique=True)