import logging
import connexion
import six
from flask import request, jsonify

from swagger_server.models.assign_program_request import AssignProgramRequest  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.program_update import ProgramUpdate  # noqa: E501
from swagger_server import util
from swagger_server.repositories.program_repository import ProgramRepository  # Importar el repositorio

program_repository = ProgramRepository()

def programs_get():  # noqa: E501
    """Obtener todos los programas académicos

    :rtype: List[Program]
    """
    try:
        # Lee el parámetro 'state' de la consulta (query parameter)
        state = request.args.get('state', type=int)

        # Llama al repositorio con el filtro de estado
        programs = program_repository.get_all_programs(state=state)
        return jsonify(programs), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500



def programs_id_delete(id_):  # noqa: E501
    """Eliminar un programa académico

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def programs_id_get(id_):  # noqa: E501
    """Obtener programa por id

    :rtype: Program
    """
    try:
        program = program_repository.get_program_by_id(id_)
        return jsonify(program), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def programs_id_patch(id_):  # noqa: E501
    """Actualizar parcialmente un programa académico

    :param id: 
    :type id: int

    :rtype: Program
    """
    try:
        # Obtener el cuerpo de la solicitud
        data = request.get_json()

        # Procesar datos del programa
        name = data.get('nombre')
        description = data.get('descripcion')
        state = data.get('estado')
        advisors = data.get('advisors', [])  # Extraer el array de asesores

        # Llamar al repositorio para actualizar el programa
        updated_program = program_repository.update_program(id_, name, description, state, advisors)
        return jsonify(updated_program), 200
    except Exception as e:
        logging.error(f"Error updating program: {e}")
        return jsonify({"message": "Error updating program"}), 500


def programs_post():
    try:
        # Obtener el cuerpo de la solicitud
        data = request.get_json()

        # Procesar datos del programa
        name = data.get('nombre')
        description = data.get('descripcion')
        state = data.get('estado')
        advisors = data.get('advisors', [])  # Extraer el array de asesores

        # Llamar al repositorio para crear el programa
        new_program = program_repository.create_program(name, description, state, advisors)
        return new_program, 201
    except Exception as e:
        logging.error(f"Error creating program: {e}")
        return {"message": "Error creating program"}, 500

def vendors_programs_delete(vendor_id, program_id):  # noqa: E501
    """Quitar un programa de un vendedor

     # noqa: E501

    :param vendor_id: 
    :type vendor_id: int
    :param program_id: 
    :type program_id: int

    :rtype: None
    """
    return 'do some magic!'


def vendors_programs_get(vendor_id):  # noqa: E501
    """Obtener programas asignados a un vendedor

     # noqa: E501

    :param vendor_id: 
    :type vendor_id: int

    :rtype: List[Program]
    """
    return 'do some magic!'


def vendors_programs_post(body, vendor_id):  # noqa: E501
    """Asignar un programa a un vendedor

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param vendor_id: 
    :type vendor_id: int

    :rtype: None
    """
    if request.is_json:
        body = AssignProgramRequest.from_dict(request.get_json())  # noqa: E501
    return 'do some magic!'

def sales_advisors_programs_get(advisor_id):
    """
    Obtener programas asignados a un asesor de ventas
    :param advisor_id: ID del asesor de ventas
    :type advisor_id: int
    :rtype: List[Program]
    """
    try:
        programs = program_repository.get_programs_by_sales_advisor(advisor_id)
        print(programs)
        if not programs:
            return jsonify({"message": "Asesor de ventas no encontrado o sin programas asignados"}), 404
        return jsonify([program.to_dict() for program in programs]), 200
    except Exception as e:
        logging.error(f"Error retrieving programs for advisor {advisor_id}: {e}")
        return jsonify({"message": str(e)}), 500
