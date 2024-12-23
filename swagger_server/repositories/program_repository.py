from swagger_server.database_models.models import Program, ProgramSellers, SalesAdvisor

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