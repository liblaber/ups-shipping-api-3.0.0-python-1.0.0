# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class LabelRecoveryLabelSpecificationLabelImageFormat(BaseModel):
    """The file format of the label and receipt. Defaults to HTML format if this node does not exist.

    :param code: File type that the label is to be generated in. Valid values are: - GIF -- label is in HTML format. - PDF -- label is in PDF format. - ZPL -- Thermal label in ZPL format. - EPL -- Thermal label in EPL2 format. - SPL -- Thermal label in SPL format. Default is GIF
    :type code: str
    :param description: Description of the label image format code., defaults to None
    :type description: str, optional
    """

    def __init__(self, code: str, description: str = None):
        self.code = code
        if description is not None:
            self.description = description
