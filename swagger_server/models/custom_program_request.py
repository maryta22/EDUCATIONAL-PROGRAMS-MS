from swagger_server.models.program_request import ProgramRequest

class CustomProgramRequest(ProgramRequest):
    def __init__(self, nombre: str=None, descripcion: str=None, estado: int=None, advisors: list=None):  # noqa: E501
        super().__init__(nombre, descripcion, estado)
        self._advisors = advisors

    @property
    def advisors(self) -> list:
        """Gets the advisors of this CustomProgramRequest.

        :return: The advisors of this CustomProgramRequest.
        :rtype: list
        """
        return self._advisors

    @advisors.setter
    def advisors(self, advisors: list):
        """Sets the advisors of this CustomProgramRequest.

        :param advisors: The advisors of this CustomProgramRequest.
        :type advisors: list
        """
        self._advisors = advisors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super().to_dict()
        result['advisors'] = self._advisors
        return result