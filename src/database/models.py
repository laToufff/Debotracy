from sqlalchemy import Column, Integer, BigInteger, String, Boolean, ForeignKey, DateTime
from .base import Base


class Guild(Base) :
    __tablename__ = 'guilds'

    id = Column(BigInteger, primary_key=True, index=True)
    votes_channel = Column(BigInteger)
    vote_results_channel = Column(BigInteger)

class Vote(Base) :
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    guild_id = Column(BigInteger, ForeignKey('guilds.id'), index=True)
    author_id = Column(BigInteger, index=True)
    name = Column(String)
    description = Column(String)
    multiple_choices = Column(Boolean)
    time_created = Column(DateTime)
    time_closed = Column(DateTime)
    time_edited = Column(DateTime)
    is_open = Column(Boolean)

    def __repr__(self) :
        return f"<Vote id={self.id} guild_id={self.guild_id} author_id={self.author_id} name='{self.name}' description='{self.description}' multiple_choices={self.multiple_choices} time_created={self.time_created} time_closed={self.time_closed} time_edited={self.time_edited} is_open={self.is_open}>"

class VoteMessage(Base) :
    __tablename__ = 'vote_messages'

    id = Column(BigInteger, primary_key=True, index=True)
    vote_id = Column(Integer, ForeignKey('votes.id'), index=True)

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
    user_id = Column(BigInteger)