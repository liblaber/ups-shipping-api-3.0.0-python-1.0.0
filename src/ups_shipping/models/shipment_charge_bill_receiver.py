# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .bill_receiver_address import BillReceiverAddress


@JsonMap({"account_number": "AccountNumber", "address": "Address"})
class ShipmentChargeBillReceiver(BaseModel):
    """Container for the BillReceiver billing option.  This element or its sibling element, BillShipper, BillThirdParty or Consignee Billed, must be present but no more than one can be present. For a return shipment, Bill Receiver is invalid for Transportation charges.

    :param account_number: The UPS account number.  The account must be a valid UPS account number that is active.  For US, PR and CA accounts, the account must be a daily pickup account, an occasional account, a customer B.I.N account, or a dropper shipper account.  All other accounts must be either a daily pickup account, an occasional account, a drop shipper account, or a non-shipping account.
    :type account_number: str
    :param address: Container for additional information for the bill receiver's UPS accounts address., defaults to None
    :type address: BillReceiverAddress, optional
    """

    def __init__(self, account_number: str, address: BillReceiverAddress = None):
        self.account_number = account_number
        if address is not None:
            self.address = self._define_object(address, BillReceiverAddress)
