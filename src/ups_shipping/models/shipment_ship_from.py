# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ship_from_tax_id_type import ShipFromTaxIdType
from .ship_from_phone import ShipFromPhone
from .ship_from_address import ShipFromAddress
from .ship_from_vendor_info import ShipFromVendorInfo


@JsonMap(
    {
        "name": "Name",
        "attention_name": "AttentionName",
        "company_displayable_name": "CompanyDisplayableName",
        "tax_identification_number": "TaxIdentificationNumber",
        "tax_id_type": "TaxIDType",
        "phone": "Phone",
        "fax_number": "FaxNumber",
        "address": "Address",
        "vendor_info": "VendorInfo",
    }
)
class ShipmentShipFrom(BaseModel):
    """Ship From Container.  Required for return shipment.

    Required if pickup location is different from the shipper's address.

    :param name: The ship from location's name or company name.  35 characters are accepted, but for return Shipment only 30 characters will be printed on the label.  Required if ShipFrom tag is in the XML.
    :type name: str
    :param attention_name: The ship from Attention name.  35 characters are accepted, but for return Shipment only 30 characters will be printed on the label.  Required if ShipFrom tag is in the XML and Invoice or CO International forms is requested. If not present, will default to the Shipper Attention Name., defaults to None
    :type attention_name: str, optional
    :param company_displayable_name: Not applicable for ShipFrom., defaults to None
    :type company_displayable_name: str, optional
    :param tax_identification_number: Company's Tax Identification Number at the pick up location.  Conditionally required if EEI form (International forms) is requested.  Applies to EEI Form only., defaults to None
    :type tax_identification_number: str, optional
    :param tax_id_type: Tax Identification Container.  Applies to EEI form only., defaults to None
    :type tax_id_type: ShipFromTaxIdType, optional
    :param phone: Container for Phone Number.  If ShipFrom country or territory is US, PR, CA, and VI, the layout is: area code, 7 digit phone number or  area code, 7 digit phone number, 4 digit extension number. For other countries or territories, the layout is: country or territory code, area code, 7 digit number.   If ShipFrom tag is in the XML and International forms is requested., defaults to None
    :type phone: ShipFromPhone, optional
    :param fax_number: The Ship from fax number.  If Ship from country or territory is US 10 digits allowed, otherwise 1-15 digits allowed., defaults to None
    :type fax_number: str, optional
    :param address: Ship from Address Container.  The package will be originating from or being shipped from this address. The shipment will be rated from this origin address to the destination ship to address.
    :type address: ShipFromAddress
    :param vendor_info: Vendor Information Container, defaults to None
    :type vendor_info: ShipFromVendorInfo, optional
    """

    def __init__(
        self,
        name: str,
        address: ShipFromAddress,
        attention_name: str = None,
        company_displayable_name: str = None,
        tax_identification_number: str = None,
        tax_id_type: ShipFromTaxIdType = None,
        phone: ShipFromPhone = None,
        fax_number: str = None,
        vendor_info: ShipFromVendorInfo = None,
    ):
        self.name = name
        if attention_name is not None:
            self.attention_name = attention_name
        if company_displayable_name is not None:
            self.company_displayable_name = company_displayable_name
        if tax_identification_number is not None:
            self.tax_identification_number = tax_identification_number
        if tax_id_type is not None:
            self.tax_id_type = self._define_object(tax_id_type, ShipFromTaxIdType)
        if phone is not None:
            self.phone = self._define_object(phone, ShipFromPhone)
        if fax_number is not None:
            self.fax_number = fax_number
        self.address = self._define_object(address, ShipFromAddress)
        if vendor_info is not None:
            self.vendor_info = self._define_object(vendor_info, ShipFromVendorInfo)