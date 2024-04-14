#!/usr/bin/python3
""" Module that Defines a City mode and Inherits from SQLAlchemy\
        Base and links to the MySQL table cities."""

    from sqlalchemy import Column, ForiegnKey, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()


    class City(Base):
        """Represents a city for a MySQL database.

        Atrributes:
            id (str): The city's id.
            name (sqllchemy.Integer): The city's name.
            state_id (sqlalchemy.String): The city's state id.
        """
        __tablename__ = "cities"
        id = Column(Integer, primary_key=True)
        id = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
