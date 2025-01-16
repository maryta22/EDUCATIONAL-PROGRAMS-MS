from swagger_server.database_models.models import Program, ProgramSellers, SalesAdvisor
import logging
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

    def get_all_programs(self, state=None):
        session = self.Session()
        try:
            query = session.query(Program).options(
                joinedload(Program.program_sellers).joinedload(ProgramSellers.sales_advisor).joinedload(SalesAdvisor.user)
            )

            # Aplica el filtro de estado si se proporciona
            if state is not None:
                query = query.filter(Program.state == state)

            programs = query.all()
            print([program.to_dict() for program in programs])
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

    def update_program(self, program_id, name, description, state, advisors):
        session = self.Session()
        try:
            print("program_id:", program_id)
            program = session.query(Program).filter(Program.id == program_id).one_or_none()
            if not program:
                raise Exception("Program not found")

            if name:
                program.name = name
            if description:
                program.description = description
            if state is not None:
                program.state = state

            # Actualizar los asesores asociados al programa
            if advisors is not None:
                # Eliminar los asesores actuales
                session.query(ProgramSellers).filter(ProgramSellers.id_academic_program == program_id).delete()
                # Insertar los nuevos asesores
                program_sellers = [
                    ProgramSellers(
                        id_academic_program=program_id,
                        id_sales_advisor=advisor_id,
                        state=1  # Estado activo por defecto
                    )
                    for advisor_id in advisors
                ]
                session.bulk_save_objects(program_sellers)

            session.commit()
            return program.to_dict()
        except Exception as e:
            session.rollback()
            logging.error(f"Error updating program: {e}")
            raise
        finally:
            session.close()

    def get_program_by_id(self, id):
        session = self.Session()
        try:
            program = session.query(Program).options(
                joinedload(Program.program_sellers).joinedload(ProgramSellers.sales_advisor).joinedload(SalesAdvisor.user)
            ).filter(Program.id == id).one_or_none()
            if not program:
                raise Exception("Program not found")
            return program.to_dict()
        except Exception as e:
            logging.error(f"Error retrieving program: {e}")
            raise
        finally:
            session.close()

    def get_programs_by_sales_advisor(self, advisor_id):
        session = self.Session()
        try:
            programs = session.query(Program).join(ProgramSellers).filter(
                ProgramSellers.id_sales_advisor == advisor_id
            ).options(
                joinedload(Program.program_sellers).joinedload(ProgramSellers.sales_advisor).joinedload(
                    SalesAdvisor.user)
            ).all()

            return programs
        except Exception as e:
            logging.error(f"Error retrieving programs for sales advisor {advisor_id}: {e}")
            raise
        finally:
            session.close()
