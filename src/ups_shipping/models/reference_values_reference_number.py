# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"value": "Value"})
class ReferenceValuesReferenceNumber(BaseModel):
    """Container for reference number

    :param value: Required if TrackingNumber or Mail Innovations Tracking Number is not populated. Customer supplied reference number. Supports up to 2 customer supplied combinations of Reference code- value combinations.
    :type value: str
    """

    def __init__(self, value: str):
        self.value = value