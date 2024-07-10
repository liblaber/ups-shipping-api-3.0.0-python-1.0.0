# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .summary_result_status import SummaryResultStatus


@JsonMap({"status": "Status"})
class VoidShipmentResponseSummaryResult(BaseModel):
    """Container for the Summary Result

    :param status: Container for the status of the Summary Result
    :type status: SummaryResultStatus
    """

    def __init__(self, status: SummaryResultStatus):
        self.status = self._define_object(status, SummaryResultStatus)