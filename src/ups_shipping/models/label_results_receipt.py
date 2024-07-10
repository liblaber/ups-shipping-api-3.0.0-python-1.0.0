# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .receipt_image import ReceiptImage


@JsonMap({"html_image": "HTMLImage", "image": "Image", "url": "URL"})
class LabelResultsReceipt(BaseModel):
    """Container for the HTML receipt and the receipt link.

    :param html_image: Base 64 encoded html browser image., defaults to None
    :type html_image: str, optional
    :param image: Container for the receipt in the format other than HTML., defaults to None
    :type image: ReceiptImage, optional
    :param url: Receipt's url  Applicable for following types of shipments: Print/Electronic Return Label Print/Electronic Import Control Label, defaults to None
    :type url: str, optional
    """

    def __init__(
        self, html_image: str = None, image: ReceiptImage = None, url: str = None
    ):
        if html_image is not None:
            self.html_image = html_image
        if image is not None:
            self.image = self._define_object(image, ReceiptImage)
        if url is not None:
            self.url = url