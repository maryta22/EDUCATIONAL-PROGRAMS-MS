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
                joinedload(Program.program_sellers).joinedload(ProgramSellers.sales_advisor).joinedload(SalesAdvisor.user)
            ).all()
            return [program.to_dict() for program in programs]
        except Exception as e:
            logging.error(f"Error retrieving programs: {e}")
            raise
        finally:
            session.close()

    def create_program(self, name, description, state, advisors):
        session = self.Session()
        try:
            # Crear el nuevo programa
            new_program = Program(
                name=name,
                description=description,
                state=state
            )
            session.add(new_program)
            session.flush()  # Obtiene el ID del nuevo programa

            # Insertar los asesores asociados al programa
            if advisors:
                program_sellers = [
                    ProgramSellers(
                        id_academic_program=new_program.id,
                        id_sales_advisor=advisor_id,
                        state=1  # Estado activo por defecto
                    )
                    for advisor_id in advisors
                ]
                session.bulk_save_objects(program_sellers)

            session.commit()
            return new_program.to_dict()
        except Exception as e:
            session.rollback()
            logging.error(f"Error creating program: {e}")
            raise
        finally:
            session.close()
