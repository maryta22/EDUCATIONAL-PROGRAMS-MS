# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AssignProgramRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, program_id: int=None):  # noqa: E501
        """AssignProgramRequest - a model defined in Swagger

        :param program_id: The program_id of this AssignProgramRequest.  # noqa: E501
        :type program_id: int
        """
        self.swagger_types = {
            'program_id': int
        }

        self.attribute_map = {
            'program_id': 'programId'
        }
        self._program_id = program_id

    @classmethod
    def from_dict(cls, dikt) -> 'AssignProgramRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssignProgramRequest of this AssignProgramRequest.  # noqa: E501
        :rtype: AssignProgramRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def program_id(self) -> int:
        """Gets the program_id of this AssignProgramRequest.


        :return: The program_id of this AssignProgramRequest.
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id: int):
        """Sets the program_id of this AssignProgramRequest.


        :param program_id: The program_id of this AssignProgramRequest.
        :type program_id: int
        """

        self._program_id = program_id
