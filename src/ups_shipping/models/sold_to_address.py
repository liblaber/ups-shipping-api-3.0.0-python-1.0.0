# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "address_line": "AddressLine",
        "city": "City",
        "state_province_code": "StateProvinceCode",
        "town": "Town",
        "postal_code": "PostalCode",
        "country_code": "CountryCode",
    }
)
class SoldToAddress(BaseModel):
    """Sold To Address Container.  Applies to NAFTA CO.

    :param address_line: SoldTo location's street address.  Applies to NAFTA CO.
    :type address_line: List[str]
    :param city: SoldTo location's city.
    :type city: str
    :param state_province_code: SoldTo location's state or province code.  Required for certain countries or territories., defaults to None
    :type state_province_code: str, optional
    :param town: SoldTo location's town code., defaults to None
    :type town: str, optional
    :param postal_code: SoldTo location's postal code., defaults to None
    :type postal_code: str, optional
    :param country_code: SoldTo location's country or territory code.
    :type country_code: str
    """

    def __init__(
        self,
        address_line: List[str],
        city: str,
        country_code: str,
        state_province_code: str = None,
        town: str = None,
        postal_code: str = None,
    ):
        self.address_line = address_line
        self.city = city
        if state_province_code is not None:
            self.state_province_code = state_province_code
        if town is not None:
            self.town = town
        if postal_code is not None:
            self.postal_code = postal_code
        self.country_code = country_code