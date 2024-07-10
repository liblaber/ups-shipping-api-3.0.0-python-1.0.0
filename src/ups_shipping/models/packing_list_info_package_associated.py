# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "package_number": "PackageNumber",
        "product_amount": "ProductAmount",
        "product_note": "ProductNote",
    }
)
class PackingListInfoPackageAssociated(BaseModel):
    """Data Container holding package/product related information that will break up the product into each package on the packing list.  Total product amount must equal the product unit value above. Required for packaging list and Air Freight Packing list.                                                      Packaging list max allowed : 20
    Air Freight Packaging list max allowed: 200

    :param package_number: Package number the product should be allocated to ont he packing list.  Required for packaging list and Air Freight Packing list.
    :type package_number: str
    :param product_amount: Amount of Product associated with a package.  Required for packaging list and Air Freight Packing list.
    :type product_amount: str
    :param product_note: Product Note., defaults to None
    :type product_note: str, optional
    """

    def __init__(
        self, package_number: str, product_amount: str, product_note: str = None
    ):
        self.package_number = package_number
        self.product_amount = product_amount
        if product_note is not None:
            self.product_note = product_note