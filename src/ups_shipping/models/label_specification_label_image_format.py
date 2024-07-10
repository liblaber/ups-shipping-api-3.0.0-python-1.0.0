# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class LabelSpecificationLabelImageFormat(BaseModel):
    """LabelImageFormat Container.

    :param code: Label print method code determines the format in which Labels are to be generated. For EPL2 formatted Labels use EPL, for SPL formatted Labels use SPL, for ZPL formatted Labels use ZPL and for image formats use GIF.  For shipments without return service the valid value is GIF, ZPL, EPL and SPL. For shipments with PRL return service, the valid values are EPL, ZPL, SPL and GIF. For UPS Premier Silver shipment only ZPL is supported.
    :type code: str
    :param description: Description of the label image format code., defaults to None
    :type description: str, optional
    """

    def __init__(self, code: str, description: str = None):
        self.code = code
        if description is not None:
            self.description = description