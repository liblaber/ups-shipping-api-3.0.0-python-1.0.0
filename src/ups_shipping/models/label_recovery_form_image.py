# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .label_recovery_image_image_format import LabelRecoveryImageImageFormat


@JsonMap({"image_format": "ImageFormat", "graphic_image": "GraphicImage"})
class LabelRecoveryFormImage(BaseModel):
    """Container tag for the International Forms image.

    :param image_format: Container tag for the International forms image format information.
    :type image_format: LabelRecoveryImageImageFormat
    :param graphic_image: Base 64 encoded International Forms image.
    :type graphic_image: str
    """

    def __init__(self, image_format: LabelRecoveryImageImageFormat, graphic_image: str):
        self.image_format = self._define_object(
            image_format, LabelRecoveryImageImageFormat
        )
        self.graphic_image = graphic_image
