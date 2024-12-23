from datetime import date, datetime  # noqa: F401

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Program(Base):
    __tablename__ = 'academic_program'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    state = Column(Integer, nullable=False)

    program_sellers = relationship("ProgramSellers", back_populates="academic_program")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "state": self.state
        }

class ProgramSellers(Base):
    __tablename__ = 'academic_program_sales_advisor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_academic_program = Column(Integer, ForeignKey('academic_program.id'), nullable=False)
    id_sales_advisor = Column(Integer, ForeignKey('sales_advisor.id'), nullable=False)
    state = Column(Integer, nullable=False)

    academic_program = relationship("Program", back_populates="program_sellers")
    sales_advisor = relationship("Seller", back_populates="program_sellers")

    def to_dict(self):
        return {
            "id": self.id,
            "id_academic_program": self.id_academic_program,
            "id_sales_advisor": self.id_sales_advisor,
            "state": self.state
        }

class Seller(Base):
    __tablename__ = 'sales_advisor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    state = Column(Integer, nullable=False)

    program_sellers = relationship("ProgramSellers", back_populates="sales_advisor")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "state": self.state
        }