# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .high_value_report_image import HighValueReportImage


@JsonMap({"image": "Image"})
class ShipmentResultsHighValueReport(BaseModel):
    """Container for the High Value Report generated for ImportControl or Return shipments with high package declared value.

    :param image: Container tag for the High Value Report image.
    :type image: HighValueReportImage
    """

    def __init__(self, image: HighValueReportImage):
        self.image = self._define_object(image, HighValueReportImage)