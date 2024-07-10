# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class PackageLevelResultStatus(BaseModel):
    """Contains the status code tags.

    :param code: The Package Level void status code.  A numeric value that describes the status code. 1 = Voided or Already Voided;  0 = Not Voided
    :type code: str
    :param description: A text description of the status code.
    :type description: str
    """

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description