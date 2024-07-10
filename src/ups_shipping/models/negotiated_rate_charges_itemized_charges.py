# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "code": "Code",
        "description": "Description",
        "currency_code": "CurrencyCode",
        "monetary_value": "MonetaryValue",
        "sub_type": "SubType",
    }
)
class NegotiatedRateChargesItemizedCharges(BaseModel):
    """NegotiatedRateChargesItemizedCharges

    :param code: Identification code for itemized charge.
    :type code: str
    :param description: Description of Itemized Charge that had been charged., defaults to None
    :type description: str, optional
    :param currency_code: Itemized Charges currency code type. The currency code used in the Shipment request is returned.
    :type currency_code: str
    :param monetary_value: Itemized Charges value amount.  Valid values are from 0 to 99999999999999.99
    :type monetary_value: str
    :param sub_type: The sub-type of ItemizedCharges type., defaults to None
    :type sub_type: str, optional
    """

    def __init__(
        self,
        code: str,
        currency_code: str,
        monetary_value: str,
        description: str = None,
        sub_type: str = None,
    ):
        self.code = code
        if description is not None:
            self.description = description
        self.currency_code = currency_code
        self.monetary_value = monetary_value
        if sub_type is not None:
            self.sub_type = sub_type