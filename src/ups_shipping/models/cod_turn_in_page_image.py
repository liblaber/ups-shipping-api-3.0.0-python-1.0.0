# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .cod_turn_in_page_image_image_format import CodTurnInPageImageImageFormat


@JsonMap({"image_format": "ImageFormat", "graphic_image": "GraphicImage"})
class CodTurnInPageImage(BaseModel):
    """The container of the image for COD Turn In Page.

    :param image_format: The container for format of COD Turn In Page.
    :type image_format: CodTurnInPageImageImageFormat
    :param graphic_image: Base 64 encoded html browser image rendering software
    :type graphic_image: str
    """

    def __init__(self, image_format: CodTurnInPageImageImageFormat, graphic_image: str):
        self.image_format = self._define_object(
            image_format, CodTurnInPageImageImageFormat
        )
        self.graphic_image = graphic_image
