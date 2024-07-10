# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"height": "Height", "width": "Width"})
class LabelSpecificationLabelStockSize(BaseModel):
    """Container for the EPL2, ZPL or SPL label size.  Valid for EPL2, ZPL and SPL Labels.

    :param height: Height of the label image. For IN, use whole inches.  For EPL2, ZPL and SPL Labels. Only valid values are 6 or 8. Note: Label Image will only scale up to 4 X 6, even when requesting 4 X 8.
    :type height: str
    :param width: Width of the label image. For IN, use whole inches.  For EPL2, ZPL and SPL Labels. Valid value is 4. Note: Label Image will only scale up to 4 X 6, even when requesting 4 X 8.
    :type width: str
    """

    def __init__(self, height: str, width: str):
        self.height = height
        self.width = width
