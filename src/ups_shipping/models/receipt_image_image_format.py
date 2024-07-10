# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class ReceiptImageImageFormat(BaseModel):
    """Container for the format of the receipt.

    :param code: Code representing the format in which a receipt is returned. Valid values: - HTML = HTML format - PDF = pdf
    :type code: str
    :param description: Description of the form image format code., defaults to None
    :type description: str, optional
    """

    def __init__(self, code: str, description: str = None):
        self.code = code
        if description is not None:
            self.description = description
