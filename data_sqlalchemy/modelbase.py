"""
Use extra module to prevent circular imports
"""
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()
