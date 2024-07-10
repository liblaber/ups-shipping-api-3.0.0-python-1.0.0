# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"currency_code": "CurrencyCode", "monetary_value": "MonetaryValue"})
class ShipmentChargesBaseServiceCharge(BaseModel):
    """Base Service Charge container.
    Transportation charge = BaseServiceCharge + Fuel charge  Returned only if Subversion >=1701.

    :param currency_code: BaseServiceCharge currency code type. The currency code used in the Shipment request is returned.
    :type currency_code: str
    :param monetary_value: Base Service Charge value amount.  Valid values are from 0 to 99999999999999.99
    :type monetary_value: str
    """

    def __init__(self, currency_code: str, monetary_value: str):
        self.currency_code = currency_code
        self.monetary_value = monetary_value