# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .label_results_label_image import LabelResultsLabelImage
from .label_results_mail_innovations_label_image import (
    LabelResultsMailInnovationsLabelImage,
)
from .label_results_receipt import LabelResultsReceipt
from .label_results_form import LabelResultsForm


@JsonMap(
    {
        "tracking_number": "TrackingNumber",
        "label_image": "LabelImage",
        "mail_innovations_tracking_number": "MailInnovationsTrackingNumber",
        "mail_innovations_label_image": "MailInnovationsLabelImage",
        "receipt": "Receipt",
        "form": "Form",
    }
)
class LabelRecoveryResponseLabelResults(BaseModel):
    """Container that stores the label results. Information containing the results of the user's Label Recovery Request.

    :param tracking_number: Package Tracking number.  Package 1Z number. Returned only if TrackingNumber or Combination of Reference Number and Shipper Number present in request., defaults to None
    :type tracking_number: str, optional
    :param label_image: The elements needed to render a label on a printer or in a browser. Specifies the format in which GraphicImage is represented. If LabelImageFormat is GIF, LabelImage contains GraphicImage and HTMLImage. Otherwise, it contains only GraphicImage. If LabelImageFormat is PDF, LabelImage is only returned at the first package result. If entered in the request, the response mirrors, else the default values are returned.  Returned only if TrackingNumber or Combination of Reference Number and Shipper Number present in request., defaults to None
    :type label_image: LabelResultsLabelImage, optional
    :param mail_innovations_tracking_number: Mail Innovations Tracking Number.  Applicable for Single Mail Innovations Returns and Dual Mail Innovations Returns shipment. Returned only if MailInnovationsTrackingNumber is provided in request., defaults to None
    :type mail_innovations_tracking_number: str, optional
    :param mail_innovations_label_image: Container to hold Mail Innovations shipments label. The elements needed to render a label on a printer or in a browser. Specifies the format in which GraphicImage is represented. If LabelImageFormat is GIF, LabelImage contains GraphicImage and HTMLImage. Otherwise, it contains only GraphicImage.   Applicable for Single Mail Innovations Returns and Dual Mail Innovations Returns shipment. Returned only if MailInnovationsTrackingNumber is provided in request. If LabelImageFormat requested was PDF and TrackingNumber was present along with MailInnovationsTrackingNumber in the request, only LabelImage container is returned. MailInnovationsLabelImage will not be returned. In that case, the labels for Small Package Tracking Number and Mail Innovations Tracking Number will be stitched in single PDF file., defaults to None
    :type mail_innovations_label_image: LabelResultsMailInnovationsLabelImage, optional
    :param receipt: Container for the HTML receipt and the receipt link., defaults to None
    :type receipt: LabelResultsReceipt, optional
    :param form: Container tag for the International Forms. Currently, represents UPS Premium Care Form for Electronic Returns Label and Electronic Import Control Label. UPS  Premium Care Form for Forward shipment if Subverion is 1903 or greater  Applicable for Electronic Return Label and Electronic Import Control Label shipments only. Applies only for Canada domestic shipments. Returned for request with SubVersion greater than or equal to 1707.  UPS  Premium Care Form for Forward shipment if Subverion is 1903 or greater, defaults to None
    :type form: LabelResultsForm, optional
    """

    def __init__(
        self,
        tracking_number: str = None,
        label_image: LabelResultsLabelImage = None,
        mail_innovations_tracking_number: str = None,
        mail_innovations_label_image: LabelResultsMailInnovationsLabelImage = None,
        receipt: LabelResultsReceipt = None,
        form: LabelResultsForm = None,
    ):
        if tracking_number is not None:
            self.tracking_number = tracking_number
        if label_image is not None:
            self.label_image = self._define_object(label_image, LabelResultsLabelImage)
        if mail_innovations_tracking_number is not None:
            self.mail_innovations_tracking_number = mail_innovations_tracking_number
        if mail_innovations_label_image is not None:
            self.mail_innovations_label_image = self._define_object(
                mail_innovations_label_image, LabelResultsMailInnovationsLabelImage
            )
        if receipt is not None:
            self.receipt = self._define_object(receipt, LabelResultsReceipt)
        if form is not None:
            self.form = self._define_object(form, LabelResultsForm)