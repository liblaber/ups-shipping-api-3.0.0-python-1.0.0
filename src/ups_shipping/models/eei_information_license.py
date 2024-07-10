# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "number": "Number",
        "code": "Code",
        "license_line_value": "LicenseLineValue",
        "eccn_number": "ECCNNumber",
    }
)
class EeiInformationLicense(BaseModel):
    """Licence information for SDL commodity.  Applies to EEI form only.

    :param number: Represents any one of the following values: export license number, exception code, CFR citation, KPC Number, ACM Number.  Applies to EEI form only. Refer to EEI License Types and Exemptions in the Appendix  for valid values and formats., defaults to None
    :type number: str, optional
    :param code: The standard license code published by US government.  Refer to EEI License Codes in the Appendix for valid values.  Applies to EEI form only. It is required for EEIFilingOption code 3. It is optionally required for all other filing types; however, it is used to categorize each product as SDL or non-SDL.  It is also used to identify which piece of information is applicable., defaults to None
    :type code: str, optional
    :param license_line_value: The export monetary amount allowed per license. Required for a licensable product when the EEI form is selected. Format: Whole numbers only.  Applies to EEI form only. Required if EEIFilingOption code 1A (only for SDL shipments) or 3., defaults to None
    :type license_line_value: str, optional
    :param eccn_number: Product ECCN Number issued by BIS (Bureau of Industry and Security). If the license number is a commerce license, ECCN must be provided. The format is #A### or EAR99  Applies to EEI forms only. It is required for EEIFilingOption code 3. ECCN is required one of the following License Exception Codes is entered: CIV, CTP, ENC, GBS, KMI, LVS, TSR, defaults to None
    :type eccn_number: str, optional
    """

    def __init__(
        self,
        number: str = None,
        code: str = None,
        license_line_value: str = None,
        eccn_number: str = None,
    ):
        if number is not None:
            self.number = number
        if code is not None:
            self.code = code
        if license_line_value is not None:
            self.license_line_value = license_line_value
        if eccn_number is not None:
            self.eccn_number = eccn_number