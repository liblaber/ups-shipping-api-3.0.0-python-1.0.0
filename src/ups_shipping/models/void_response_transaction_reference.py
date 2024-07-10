# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"customer_context": "CustomerContext"})
class VoidResponseTransactionReference(BaseModel):
    """Transaction Reference Container.

    :param customer_context: The CustomerContext Information which will be echoed during response., defaults to None
    :type customer_context: str, optional
    """

    def __init__(self, customer_context: str = None):
        if customer_context is not None:
            self.customer_context = customer_context
