from sqlalchemy import Column, Integer, Boolean, BigInteger

from base import Base


class GroupSetting(Base):
    __tablename__ = "group_settings"

    tele_id = Column(BigInteger, primary_key=True)
    join_timer = Column(Integer)
    pass_timer = Column(Integer)
    money_mode = Column(Boolean)
