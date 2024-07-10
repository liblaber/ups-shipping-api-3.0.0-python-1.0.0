# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .label_recovery_response import LabelRecoveryResponse


@JsonMap({"label_recovery_response": "LabelRecoveryResponse"})
class LabelrecoveryResponseWrapper(BaseModel):
    """N/A

    :param label_recovery_response: Response for the Label recovery request  Validates the date range and label being present. Also if the shipment is return or not
    :type label_recovery_response: LabelRecoveryResponse
    """

    def __init__(self, label_recovery_response: LabelRecoveryResponse):
        self.label_recovery_response = self._define_object(
            label_recovery_response, LabelRecoveryResponse
        )