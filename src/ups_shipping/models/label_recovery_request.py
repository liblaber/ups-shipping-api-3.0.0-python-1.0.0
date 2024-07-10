# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .label_recovery_request_request import LabelRecoveryRequestRequest
from .label_recovery_request_label_specification import (
    LabelRecoveryRequestLabelSpecification,
)
from .label_recovery_request_translate import LabelRecoveryRequestTranslate
from .label_recovery_request_label_delivery import LabelRecoveryRequestLabelDelivery
from .label_recovery_request_reference_values import LabelRecoveryRequestReferenceValues
from .label_recovery_request_ups_premium_care_form import (
    LabelRecoveryRequestUpsPremiumCareForm,
)


@JsonMap(
    {
        "request": "Request",
        "label_specification": "LabelSpecification",
        "translate": "Translate",
        "label_delivery": "LabelDelivery",
        "tracking_number": "TrackingNumber",
        "mail_innovations_tracking_number": "MailInnovationsTrackingNumber",
        "reference_values": "ReferenceValues",
        "locale": "Locale",
        "ups_premium_care_form": "UPSPremiumCareForm",
    }
)
class LabelRecoveryRequest(BaseModel):
    """Request for obtaining the Label for the return shipment.

    :param request: Request Container.
    :type request: LabelRecoveryRequestRequest
    :param label_specification: Container that is used to define the properties required by the user to print and/ or display the UPS shipping label.  Required for the shipment without return service, or shipment with PRL return service., defaults to None
    :type label_specification: LabelRecoveryRequestLabelSpecification, optional
    :param translate: Translate container allows the user to specify the language he/she would like a specific portion of response to return.  The language is specified by the combination of language code and dialect code.  Valid combinations are: LanguageCode + DialectCode.  Either Translate container or Locale element can be present in a given request. Both can't be requested together in same request. Combinations:  eng GB = Queen's English  Spa 97 = Castilian Spanish  ita 97 = Italian  fra 97 = France French  fra CA = Canadian French  deu 97 = German  por 97 = Portugal Portuguese  nld 97 = Dutch  dan 97 = Danish  fin 97 = Finnish  swe 97 = Swedish  eng CA = Canadian English  Eng US = US English  Default language is Queen's English  If the Ship from country or territory is Canada, the Language defaults to Canadian English.  If the ship from country or territory is US, the language defaults to US English. If shipping from some other country or territory, the language defaults to Queens English., defaults to None
    :type translate: LabelRecoveryRequestTranslate, optional
    :param label_delivery: Container for the Label Delivery accessorial. One Label Delivery per shipment., defaults to None
    :type label_delivery: LabelRecoveryRequestLabelDelivery, optional
    :param tracking_number: Small Package Tracking Number. Required if Mail Innovations Tracking Number or ReferenceNumber/Value and ShipperNumber is not provided.  If only TrackingNumber is provided, the request will be treated as Small Package Shipment. Label Recovery will return label for Small Package Tracking Number. If both, TrackingNumber and MailInnovationsTrackingNumber are provided, the request will be treated as Dual Mail Innovations Return Shipment. Label Recovery will return two labels one each for - Small Package Tracking Number and Mail Innovations Return Tracking Number., defaults to None
    :type tracking_number: str, optional
    :param mail_innovations_tracking_number: Mail Innovations Tracking Number.  Required if Tracking Number or ReferenceNumber/Value is not populated.  If only MailInnovationsTrackingNumber is provided, the request will be treated as Single Mail Innovations Return Shipment. Label Recovery will return label for Mail Innovations Return Tracking Number. If both, TrackingNumber and MailInnovationsTrackingNumber are provided, the request will be treated as Dual Mail Innovations Return Shipment. Label Recovery will return two labels one each for - Small Package Tracking Number and Mail Innovations Return Tracking Number., defaults to None
    :type mail_innovations_tracking_number: str, optional
    :param reference_values: Container that holds reference number and shipper number  If tracking number is not present use reference Number, defaults to None
    :type reference_values: LabelRecoveryRequestReferenceValues, optional
    :param locale: Represents 5 character ISO Locale that allows the user to request Reference Number Code on Label, Label instructions, Receipt instructions (if available for given tracking number) and High Value Report (if available for given tracking number) in desired language.  Locale is specified by the combination of language code and country or territory code - 2 character language code and 2 character country code seperated by an underscore ('_') character. Example - de_DE. Please refer to Appendix for supported values for Locale.  Either Translate container or Locale element can be present in a given request. Both can't be requested together in same request., defaults to None
    :type locale: str, optional
    :param ups_premium_care_form: UPS Premium Care Form container.  Default is PDF when container is not provided.    Valid only for Canada to Canada movements. UPS Premium Care Form will be returned in  both US English and Canadian French language., defaults to None
    :type ups_premium_care_form: LabelRecoveryRequestUpsPremiumCareForm, optional
    """

    def __init__(
        self,
        request: LabelRecoveryRequestRequest,
        label_specification: LabelRecoveryRequestLabelSpecification = None,
        translate: LabelRecoveryRequestTranslate = None,
        label_delivery: LabelRecoveryRequestLabelDelivery = None,
        tracking_number: str = None,
        mail_innovations_tracking_number: str = None,
        reference_values: LabelRecoveryRequestReferenceValues = None,
        locale: str = None,
        ups_premium_care_form: LabelRecoveryRequestUpsPremiumCareForm = None,
    ):
        self.request = self._define_object(request, LabelRecoveryRequestRequest)
        if label_specification is not None:
            self.label_specification = self._define_object(
                label_specification, LabelRecoveryRequestLabelSpecification
            )
        if translate is not None:
            self.translate = self._define_object(
                translate, LabelRecoveryRequestTranslate
            )
        if label_delivery is not None:
            self.label_delivery = self._define_object(
                label_delivery, LabelRecoveryRequestLabelDelivery
            )
        if tracking_number is not None:
            self.tracking_number = tracking_number
        if mail_innovations_tracking_number is not None:
            self.mail_innovations_tracking_number = mail_innovations_tracking_number
        if reference_values is not None:
            self.reference_values = self._define_object(
                reference_values, LabelRecoveryRequestReferenceValues
            )
        if locale is not None:
            self.locale = locale
        if ups_premium_care_form is not None:
            self.ups_premium_care_form = self._define_object(
                ups_premium_care_form, LabelRecoveryRequestUpsPremiumCareForm
            )
