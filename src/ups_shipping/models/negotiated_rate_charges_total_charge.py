# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"currency_code": "CurrencyCode", "monetary_value": "MonetaryValue"})
class NegotiatedRateChargesTotalCharge(BaseModel):
    """Total charges container. Account Based Rates info. Total charges are only returned for ABR eligible shipper account/UserId combinations when the user includes the NegotiatedRatesIndicator in the request.

    :param currency_code: Total charges currency code.
    :type currency_code: str
    :param monetary_value: Total charges monetary value.  Valid values are from 0 to 9999999999999999.99
    :type monetary_value: str
    """

    def __init__(self, currency_code: str, monetary_value: str):
        self.currency_code = currency_code
        self.monetary_value = monetary_value