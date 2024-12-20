# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.assign_program_request import AssignProgramRequest  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.program_request import ProgramRequest  # noqa: E501
from swagger_server.models.program_update import ProgramUpdate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_programs_get(self):
        """Test case for programs_get

        Obtener todos los programas académicos
        """
        response = self.client.open(
            '/programs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_programs_id_delete(self):
        """Test case for programs_id_delete

        Eliminar un programa académico
        """
        response = self.client.open(
            '/programs/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_programs_id_get(self):
        """Test case for programs_id_get

        Obtener un programa académico por ID
        """
        response = self.client.open(
            '/programs/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_programs_id_patch(self):
        """Test case for programs_id_patch

        Actualizar parcialmente un programa académico
        """
        body = ProgramUpdate()
        response = self.client.open(
            '/programs/{id}'.format(id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_programs_post(self):
        """Test case for programs_post

        Crear un nuevo programa académico
        """
        body = ProgramRequest()
        response = self.client.open(
            '/programs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vendors_programs_delete(self):
        """Test case for vendors_programs_delete

        Quitar un programa de un vendedor
        """
        response = self.client.open(
            '/vendors/{vendorId}/programs/{programId}'.format(vendor_id=56, program_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vendors_programs_get(self):
        """Test case for vendors_programs_get

        Obtener programas asignados a un vendedor
        """
        response = self.client.open(
            '/vendors/{vendorId}/programs'.format(vendor_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vendors_programs_post(self):
        """Test case for vendors_programs_post

        Asignar un programa a un vendedor
        """
        body = AssignProgramRequest()
        response = self.client.open(
            '/vendors/{vendorId}/programs'.format(vendor_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
