# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .bill_third_party_address import BillThirdPartyAddress


@JsonMap(
    {
        "account_number": "AccountNumber",
        "certified_electronic_mail": "CertifiedElectronicMail",
        "interchange_system_code": "InterchangeSystemCode",
        "address": "Address",
    }
)
class ShipmentChargeBillThirdParty(BaseModel):
    """Container for the third party billing option.  This element or its sibling element, BillShipper, BillReceiver or Consignee Billed, must be present but no more than one can be present.

    :param account_number: The UPS account number of the third party shipper.  The account must be a valid UPS account number that is active.  For US, PR and CA accounts, the account must be either a daily pickup account, an occasional account, or a customer B.I.N account, or a drop shipper account.  All other accounts must be either a daily pickup account, an occasional account, a drop shipper account, or a non-shipping account., defaults to None
    :type account_number: str, optional
    :param certified_electronic_mail: Posta Elettronica Certificata (PEC) which is the recipient code for the customers certified electronic mail value., defaults to None
    :type certified_electronic_mail: str, optional
    :param interchange_system_code: Sistema Di Interscambio(SDI) which is the recipient code for the customer's interchange value or Interchange System Code, defaults to None
    :type interchange_system_code: str, optional
    :param address: Container for additional information for the third party UPS accounts address.
    :type address: BillThirdPartyAddress
    """

    def __init__(
        self,
        address: BillThirdPartyAddress,
        account_number: str = None,
        certified_electronic_mail: str = None,
        interchange_system_code: str = None,
    ):
        if account_number is not None:
            self.account_number = account_number
        if certified_electronic_mail is not None:
            self.certified_electronic_mail = certified_electronic_mail
        if interchange_system_code is not None:
            self.interchange_system_code = interchange_system_code
        self.address = self._define_object(address, BillThirdPartyAddress)