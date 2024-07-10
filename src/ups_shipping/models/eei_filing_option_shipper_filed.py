# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "code": "Code",
        "description": "Description",
        "pre_departure_itn_number": "PreDepartureITNNumber",
        "exemption_legend": "ExemptionLegend",
        "eei_shipment_reference_number": "EEIShipmentReferenceNumber",
    }
)
class EeiFilingOptionShipperFiled(BaseModel):
    """Indicates the EEI Shipper Filed option or AES Direct. (Option 1 or 2).  Applicable for EEI form.

    :param code: Indicates the EEI Shipper sub option.  Applicable for EEI form and is required. Valid value is: A- requires the ITN; B- requires the Exemption Legend; C- requires the post departure filing citation.
    :type code: str
    :param description: Description of ShipperFiled Code.  Applicable for EEI form., defaults to None
    :type description: str, optional
    :param pre_departure_itn_number: Input for Shipper Filed option A and AES Direct. The format is available from AESDirect website.  Valid and Required for Shipper Filed option A. EEI form only., defaults to None
    :type pre_departure_itn_number: str, optional
    :param exemption_legend: Input for Shipper Filed option B. 30.2(d)(2), 30.26(a), 30.36, 30.37(a), 30.37(b), 30.37(c), 30.37(d), 30.37(e), 30.37(f), 30.37(h), 30.37(i), 30.30(j), 30.37(k), 30.37(i), 30.37(j), 30.37(k), 30.37(l), 30.37(m), 30.37(n), 30.37(o), 30.37(p), 30.37(q), 30.37(r), 30.37(s), 30.37(t), 30.37(u), 30.37(x), 30.37(y)(1), 30.37(y)(2), 30.37(y)(3), 30.37(y)(4), 30.37(y)(5), 30.37(y)(6), 30.39, 30.40(a), 30.40(b), 30.40(c), 30.40(d), 30.8(b)  Valid and Required for Shipper Filed option B. EEI form only., defaults to None
    :type exemption_legend: str, optional
    :param eei_shipment_reference_number: Shipment Reference Number for use during interaction with AES. Valid for EEI form for Shipper Filed option 'C' and AES Direct Filed., defaults to None
    :type eei_shipment_reference_number: str, optional
    """

    def __init__(
        self,
        code: str,
        description: str = None,
        pre_departure_itn_number: str = None,
        exemption_legend: str = None,
        eei_shipment_reference_number: str = None,
    ):
        self.code = code
        if description is not None:
            self.description = description
        if pre_departure_itn_number is not None:
            self.pre_departure_itn_number = pre_departure_itn_number
        if exemption_legend is not None:
            self.exemption_legend = exemption_legend
        if eei_shipment_reference_number is not None:
            self.eei_shipment_reference_number = eei_shipment_reference_number