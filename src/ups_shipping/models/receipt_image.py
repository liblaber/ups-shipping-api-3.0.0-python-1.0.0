# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .receipt_image_image_format import ReceiptImageImageFormat


@JsonMap({"image_format": "ImageFormat", "graphic_image": "GraphicImage"})
class ReceiptImage(BaseModel):
    """Container for the receipt in the format other than HTML.

    :param image_format: Container for the format of the receipt.
    :type image_format: ReceiptImageImageFormat
    :param graphic_image: Base 64 encoded graphic image
    :type graphic_image: str
    """

    def __init__(self, image_format: ReceiptImageImageFormat, graphic_image: str):
        self.image_format = self._define_object(image_format, ReceiptImageImageFormat)
        self.graphic_image = graphic_image
