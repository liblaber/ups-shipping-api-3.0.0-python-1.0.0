# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"prime_code": "PrimeCode", "sub_code": "SubCode"})
class CommodityNmfc(BaseModel):
    """Container to hold the NMFC codes.

    :param prime_code: Specifies the Commodity's NMFC prime code.  Required if NMFC Container is present.
    :type prime_code: str
    :param sub_code: Specifies the Commodity's NMFC sub code.  Needs to be provided when the SubCode associated with the PrimeCode is other than 00. UPS defaults the sub value to 00 if not provided. If provided the Sub Code should be associated with the PrimeCode of the NMFC., defaults to None
    :type sub_code: str, optional
    """

    def __init__(self, prime_code: str, sub_code: str = None):
        self.prime_code = prime_code
        if sub_code is not None:
            self.sub_code = sub_code
