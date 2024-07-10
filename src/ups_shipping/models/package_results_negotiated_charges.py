# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .negotiated_charges_itemized_charges import NegotiatedChargesItemizedCharges


@JsonMap({"itemized_charges": "ItemizedCharges"})
class PackageResultsNegotiatedCharges(BaseModel):
    """Negotiated Rates Charge Container.  These charges are returned when:
    1) Subversion is greater than or equal to 1607
    2) If negotiated rates were requested for GFP shipments and account number is eligible to receive negotiated rates.

    :param itemized_charges: Negotiated Itemized Accessorial and SurCharges. Negotiated itemized charges are only returned for certain contract-only shipments as well as Worldwide Express Freight, Ground Freight Pricing, and Hazmat movements. Negotiated Itemized Accessorial and Sur Charges are returned only when the subversion element is present and greater than or equal to 1607. Package level itemized charges are only returned for US domestic movements **NOTE:** For versions >= v2403, this element will always be returned as an array. For requests using versions < v2403, this element will be returned as an array if there is more than one object and a single object if there is only 1. , defaults to None
    :type itemized_charges: List[NegotiatedChargesItemizedCharges], optional
    """

    def __init__(self, itemized_charges: List[NegotiatedChargesItemizedCharges] = None):
        if itemized_charges is not None:
            self.itemized_charges = self._define_list(
                itemized_charges, NegotiatedChargesItemizedCharges
            )