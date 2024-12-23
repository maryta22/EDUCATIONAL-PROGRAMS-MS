import connexion
import six
from flask import request, jsonify

from swagger_server.models.assign_program_request import AssignProgramRequest  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.custom_program_request import CustomProgramRequest
from swagger_server.models.program_update import ProgramUpdate  # noqa: E501
from swagger_server import util
from swagger_server.repositories.program_repository import ProgramRepository  # Importar el repositorio

program_repository = ProgramRepository()

def programs_get():  # noqa: E501
    """Obtener todos los programas académicos

     # noqa: E501


    :rtype: List[Program]
    """
    return program_repository.get_all_programs()


def programs_id_delete(id):  # noqa: E501
    """Eliminar un programa académico

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def programs_id_get(id):  # noqa: E501
    """Obtener un programa académico por ID

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Program
    """
    return 'do some magic!'


def programs_id_patch(body, id):  # noqa: E501
    """Actualizar parcialmente un programa académico

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: Program
    """
    if request.is_json:
        body = ProgramUpdate.from_dict(request.get_json())  # noqa: E501
    return 'do some magic!'


def programs_post():  # noqa: E501
    """Crear un nuevo programa académico

    :rtype: Program
    """
    if request.is_json:
        body = CustomProgramRequest.from_dict(request.get_json())  # noqa: E501
        try:
            new_program = program_repository.create_program(body)
            return jsonify(new_program), 201
        except Exception as e:
            return jsonify({"message": str(e)}), 500
    return jsonify({"message": "Invalid input"}), 400

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
