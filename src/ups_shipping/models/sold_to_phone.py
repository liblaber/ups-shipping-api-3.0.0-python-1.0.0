# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"number": "Number", "extension": "Extension"})
class SoldToPhone(BaseModel):
    """Phone Container.

    :param number: Sold To contacts phone number.
    :type number: str
    :param extension: Sold To contacts phone extension., defaults to None
    :type extension: str, optional
    """

    def __init__(self, number: str, extension: str = None):
        self.number = number
        if extension is not None:
            self.extension = extension
