# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"currency_code": "CurrencyCode", "monetary_value": "MonetaryValue"})
class ShipmentServiceOptionsAccessPointCod(BaseModel):
    """Access Point COD indicates COD is requested for a shipment.  Valid only for "01 - Hold For Pickup At UPS Access Point" Shipment Indication type. Shipment Access Point COD is valid only for countries or territories within E.U.
    Not valid with (Shipment) COD.
    Not available to shipment with return service.

    :param currency_code: Access Point COD Currency Code.
    :type currency_code: str
    :param monetary_value: Access Point COD Monetary Value.
    :type monetary_value: str
    """

    def __init__(self, currency_code: str, monetary_value: str):
        self.currency_code = currency_code
        self.monetary_value = monetary_value
