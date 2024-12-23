from swagger_server.database_models.models import Program, ProgramSellers, SalesAdvisor
from swagger_server.models.custom_program_request import CustomProgramRequest
import logging
from datetime import datetime

from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()

class ProgramRepository:
    def __init__(self):
        pass_sam = os.getenv('DB_PASSWORD')
        self.engine = create_engine(f'mysql+pymysql://root:{pass_sam}@localhost:3306/espae_prospections')
        self.Session = sessionmaker(bind=self.engine)

    def get_all_programs(self):
        session = self.Session()
        try:
            programs = session.query(Program).options(
                joinedload(Program.program_sellers).joinedload(ProgramSellers.sales_advisor)
            ).all()
            return [program.to_dict() for program in programs]
        except Exception as e:
            logging.error(f"Error retrieving programs: {e}")
            raise
        finally:
            session.close()

    def create_program(self, program_request: CustomProgramRequest):
        session = self.Session()
        try:
            # Crear el nuevo programa
            new_program = Program(
                name=program_request.nombre,
                description=program_request.descripcion,
                state=1 if program_request.estado == 'Activo' else 0
            )
            session.add(new_program)
            session.flush()  # Para obtener el ID del nuevo programa

            # Añadir registros en ProgramSellers si hay asesores
            if program_request.advisors:
                self.update_program_sellers(session, new_program.id, program_request.advisors)

            session.commit()
            return new_program.to_dict()
        except Exception as e:
            session.rollback()
            logging.error(f"Error creating program: {e}")
            raise
        finally:
            session.close()

    def update_program_sellers(self, session, program_id, advisors):
        try:
            for advisor_id in advisors:
                new_program_seller = ProgramSellers(
                    id_academic_program=program_id,
                    id_sales_advisor=advisor_id,
                    state=1  # Asumimos que el estado es activo por defecto
                )
                session.add(new_program_seller)
        except Exception as e:
            logging.error(f"Error updating program sellers: {e}")
            raise