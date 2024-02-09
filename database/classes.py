from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .base import Base


class Guild(Base) :
    __tablename__ = 'guilds'

    id = Column(Integer, primary_key=True, index=True)
    votes_channel = Column(Integer)
    vote_results_channel = Column(Integer)

class Vote(Base) :
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    guild_id = Column(Integer, ForeignKey('guilds.id'))
    author_id = Column(Integer)
    msg_id = Column(Integer)
    name = Column(String)
    description = Column(String)
    multiple_choices = Column(Boolean)
    time_created = Column(Integer)
    time_closed = Column(Integer)
    time_edited = Column(Integer)
    is_open = Column(Boolean)

class VoteOption(Base) :
    __tablename__ = 'vote_options'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    vote_id = Column(Integer, ForeignKey('votes.id'))
    emoji = Column(String)
    description = Column(String)

class VoteChoice(Base) :
    __tablename__ = 'vote_choices'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    vote_id = Column(Integer, ForeignKey('votes.id'))
    option_id = Column(Integer, ForeignKey('vote_options.id'))

class VoteUser(Base) :
    __tablename__ = 'vote_users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    choice_id = Column(Integer, ForeignKey('vote_choices.id'))
    user_id = Column(Integer)