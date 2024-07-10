# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lr_response_response_status import LrResponseResponseStatus
from .response_alert import ResponseAlert
from .lr_response_transaction_reference import LrResponseTransactionReference


@JsonMap(
    {
        "response_status": "ResponseStatus",
        "alert": "Alert",
        "transaction_reference": "TransactionReference",
    }
)
class LabelRecoveryResponseResponse(BaseModel):
    """Response Container

    :param response_status: Response Status container
    :type response_status: LrResponseResponseStatus
    :param alert: Alert Container. There can be zero to many alert containers with code and description., defaults to None
    :type alert: ResponseAlert, optional
    :param transaction_reference: Transaction Reference Container, defaults to None
    :type transaction_reference: LrResponseTransactionReference, optional
    """

    def __init__(
        self,
        response_status: LrResponseResponseStatus,
        alert: ResponseAlert = None,
        transaction_reference: LrResponseTransactionReference = None,
    ):
        self.response_status = self._define_object(
            response_status, LrResponseResponseStatus
        )
        if alert is not None:
            self.alert = self._define_object(alert, ResponseAlert)
        if transaction_reference is not None:
            self.transaction_reference = self._define_object(
                transaction_reference, LrResponseTransactionReference
            )
