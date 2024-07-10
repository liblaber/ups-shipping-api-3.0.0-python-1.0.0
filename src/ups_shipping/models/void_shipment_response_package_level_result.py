# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .package_level_result_status import PackageLevelResultStatus


@JsonMap({"tracking_number": "TrackingNumber", "status": "Status"})
class VoidShipmentResponsePackageLevelResult(BaseModel):
    """VoidShipmentResponsePackageLevelResult

    :param tracking_number: The package's identification number
    :type tracking_number: str
    :param status: Contains the status code tags.
    :type status: PackageLevelResultStatus
    """

    def __init__(self, tracking_number: str, status: PackageLevelResultStatus):
        self.tracking_number = tracking_number
        self.status = self._define_object(status, PackageLevelResultStatus)
