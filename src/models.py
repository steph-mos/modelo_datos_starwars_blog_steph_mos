from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
        __tablename__= 'user'
        id: Mapped[int] = mapped_column(primary_key=True)
        email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
        password: Mapped[str] = mapped_column(nullable=False)
        is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
        
        favorite_character: Mapped[list['FavoriteCharacters']] = relationship(
             back_populates ='user', cascade='all, delete-orphan')
        favorite_planet: Mapped[list['FavoritePlanets']] = relationship(
             back_populates = 'user', cascade='all, delete-orphan')
        favorite_starship: Mapped[list['FavoriteStarships']] = relationship(
             back_populates = 'user', cascade='all, delete-orphan')

class Characters (db.Model):
    __tablename__= 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    height: Mapped[str] = mapped_column(Integer)
    weight: Mapped[str] = mapped_column(Integer)
    favorite_by: Mapped[list['FavoriteCharacters']] = relationship(
         back_populates='characters', cascade='all, delete-orphan')
    


class FavoriteCharacters (db.Model):
    __tablename__='favoritecharacters'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped[User] = relationship(back_populates='favorite_character')
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'))
    characters: Mapped[Characters] = relationship(
         back_populates='favorites_by', cascade='all, delete-orphan')


class Planets(db.Model):
    __tablename__= 'planets'
    id: Mapped[int]= mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    population: Mapped[int]= mapped_column(Integer)
    diameter: Mapped[int] = mapped_column(Integer)
    favorite_by: Mapped[list['FavoritePlanets']] = relationship(
         back_populates='planets'
    )

class FavoritePlanets(db.Model):
     __tablename__='favoriteplanets'
     id: Mapped[int] = mapped_column(primary_key=True)
     user_id:Mapped[int] = mapped_column(ForeignKey('user.id'))
     user: Mapped[User] = relationship(back_populates='favorite_planet')
     planets_id: Mapped[int] = mapped_column(ForeignKey('planets.id'))
     planets: Mapped[Planets] = relationship(
        back_populates='favorite_by')



class Starships(db.Model):
    __tablename__ = 'starships'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    favorite_by: Mapped[list['FavoriteStarships']] = relationship(back_populates='starships')

class FavoriteStarships(db.Model):
     __tablename__='favoritestarships'
     id: Mapped[int] = mapped_column(primary_key=True)
     user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
     user: Mapped[User] = relationship(back_populates='favorite_starship')
     starships_id: Mapped[int] = mapped_column(ForeignKey('starships.id'))
     starships: Mapped[Starships] = relationship(back_populates='favorite_by')




def serialize(self):
    return {
        "id": self.id,
        "email": self.email,
        # do not serialize the password, its a security breach
        }
