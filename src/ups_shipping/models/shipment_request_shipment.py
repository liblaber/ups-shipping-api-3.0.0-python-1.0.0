# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .shipment_return_service import ShipmentReturnService
from .shipment_shipper import ShipmentShipper
from .shipment_ship_to import ShipmentShipTo
from .shipment_alternate_delivery_address import ShipmentAlternateDeliveryAddress
from .shipment_ship_from import ShipmentShipFrom
from .shipment_payment_information import ShipmentPaymentInformation
from .shipment_frs_payment_information import ShipmentFrsPaymentInformation
from .shipment_freight_shipment_information import ShipmentFreightShipmentInformation
from .shipment_promotional_discount_information import (
    ShipmentPromotionalDiscountInformation,
)
from .shipment_dg_signatory_info import ShipmentDgSignatoryInfo
from .shipment_shipment_rating_options import ShipmentShipmentRatingOptions
from .shipment_reference_number import ShipmentReferenceNumber
from .shipment_service import ShipmentService
from .shipment_invoice_line_total import ShipmentInvoiceLineTotal
from .shipment_shipment_indication_type import ShipmentShipmentIndicationType
from .shipment_shipment_service_options import ShipmentShipmentServiceOptions
from .shipment_package import ShipmentPackage


@JsonMap(
    {
        "description": "Description",
        "return_service": "ReturnService",
        "documents_only_indicator": "DocumentsOnlyIndicator",
        "shipper": "Shipper",
        "ship_to": "ShipTo",
        "alternate_delivery_address": "AlternateDeliveryAddress",
        "ship_from": "ShipFrom",
        "payment_information": "PaymentInformation",
        "frs_payment_information": "FRSPaymentInformation",
        "freight_shipment_information": "FreightShipmentInformation",
        "goods_not_in_free_circulation_indicator": "GoodsNotInFreeCirculationIndicator",
        "promotional_discount_information": "PromotionalDiscountInformation",
        "dg_signatory_info": "DGSignatoryInfo",
        "shipment_rating_options": "ShipmentRatingOptions",
        "movement_reference_number": "MovementReferenceNumber",
        "reference_number": "ReferenceNumber",
        "service": "Service",
        "invoice_line_total": "InvoiceLineTotal",
        "num_of_pieces_in_shipment": "NumOfPiecesInShipment",
        "usps_endorsement": "USPSEndorsement",
        "mi_label_cn22_indicator": "MILabelCN22Indicator",
        "sub_classification": "SubClassification",
        "cost_center": "CostCenter",
        "cost_center_barcode_indicator": "CostCenterBarcodeIndicator",
        "package_id": "PackageID",
        "package_id_barcode_indicator": "PackageIDBarcodeIndicator",
        "irregular_indicator": "IrregularIndicator",
        "shipment_indication_type": "ShipmentIndicationType",
        "mi_dual_return_shipment_key": "MIDualReturnShipmentKey",
        "mi_dual_return_shipment_indicator": "MIDualReturnShipmentIndicator",
        "rating_method_requested_indicator": "RatingMethodRequestedIndicator",
        "tax_information_indicator": "TaxInformationIndicator",
        "shipment_service_options": "ShipmentServiceOptions",
        "locale": "Locale",
        "shipment_value_threshold_code": "ShipmentValueThresholdCode",
        "master_carton_id": "MasterCartonID",
        "master_carton_indicator": "MasterCartonIndicator",
        "shipment_date": "ShipmentDate",
        "package": "Package",
    }
)
class ShipmentRequestShipment(BaseModel):
    """Shipment Container

    :param description: The Description of Goods for the shipment. Applies to international and domestic shipments.  Provide a detailed description of items being shipped for documents and non-documents.  Examples: "annual reports" and "9 mm steel screws".  Required if all of the listed conditions are true:  ShipFrom and ShipTo countries or territories are not the same; The packaging type is not UPS Letter; The ShipFrom and or ShipTo countries or territories are not in the European Union or the ShipFrom and ShipTo countries or territories are both in the European Union and the shipments service type is not UPS Standard., defaults to None
    :type description: str, optional
    :param return_service: Type of Return service. When this container exists, the shipment is a return shipment., defaults to None
    :type return_service: ShipmentReturnService, optional
    :param documents_only_indicator: Indicates a shipment contains written, typed, or printed communication of no commercial value.  If DocumentsOnly is not specified then it implies that the shipment contains non documents or documents of commercial value.  Default is a shipment contains non- documents or documents of commercial value.  This is an empty tag, any value inside is ignored.  Valid only for shipments with different origin and destination countries or territories. The origin country or territory is not US, and the destination country or territory is not CA, PR or MX., defaults to None
    :type documents_only_indicator: str, optional
    :param shipper: Container for the Shipper's information.
    :type shipper: ShipmentShipper
    :param ship_to: Ship To Container.
    :type ship_to: ShipmentShipTo
    :param alternate_delivery_address: AlternateDeliveryAddress Container.  Alternate Delivery Address (UPS Access Point Address) required if ShipmentIndicationType is 01 or 02., defaults to None
    :type alternate_delivery_address: ShipmentAlternateDeliveryAddress, optional
    :param ship_from: Ship From Container.  Required for return shipment.  Required if pickup location is different from the shipper's address., defaults to None
    :type ship_from: ShipmentShipFrom, optional
    :param payment_information: Payment information container for detailed shipment charges. The two shipment charges that are available for specification are Transportation charges and Duties and Taxes.  It is required for non-Ground Freight Pricing shipments only., defaults to None
    :type payment_information: ShipmentPaymentInformation, optional
    :param frs_payment_information: Container to hold the Payment information for the Ground Freight Pricing Shipments.  Required for Ground Freight Pricing Shipments only., defaults to None
    :type frs_payment_information: ShipmentFrsPaymentInformation, optional
    :param freight_shipment_information: Container to hold Freight Shipment information., defaults to None
    :type freight_shipment_information: ShipmentFreightShipmentInformation, optional
    :param goods_not_in_free_circulation_indicator: Goods Not In Free Circulation indicator.  This is an empty tag, any value inside is ignored. This indicator is invalid for a package type of UPS Letter and DocumentsOnly., defaults to None
    :type goods_not_in_free_circulation_indicator: str, optional
    :param promotional_discount_information: PromotionalDiscountInformation container. This container contains discount information that the customer wants to request each time while placing a shipment., defaults to None
    :type promotional_discount_information: ShipmentPromotionalDiscountInformation, optional
    :param dg_signatory_info: DGSignatoryInfo Container  DGPaperImage will be returned if DGSignatoryInfo container present, defaults to None
    :type dg_signatory_info: ShipmentDgSignatoryInfo, optional
    :param shipment_rating_options: ShipmentRatingOptions container., defaults to None
    :type shipment_rating_options: ShipmentShipmentRatingOptions, optional
    :param movement_reference_number: Movement Reference Number (MRN) information.  Must contain alphanumeric characters only. Must be a length of 18 characters. The 3rd and 4th Characters must be the Shipper country or territory ISO Code., defaults to None
    :type movement_reference_number: str, optional
    :param reference_number: reference_number, defaults to None
    :type reference_number: List[ShipmentReferenceNumber], optional
    :param service: UPS service type.
    :type service: ShipmentService
    :param invoice_line_total: Container to hold InvoiceLineTotal Information.  Required for forward shipments whose origin is the US and destination is Puerto Rico or Canada. Not available for any other shipments. FOR OTHER DESTINATIONS the InvoiceLineTotal in the International Forms Container must be used., defaults to None
    :type invoice_line_total: ShipmentInvoiceLineTotal, optional
    :param num_of_pieces_in_shipment: Total number of pieces in all pallets in a UPS Worldwide Express Freight Shipment.  It is required for UPS Worldwide Express Freight and UPS Worldwide Express Freight Midday Shipment. Valid values are 1 to 99999., defaults to None
    :type num_of_pieces_in_shipment: str, optional
    :param usps_endorsement: USPS Endorsement. Valid values:  1 = Return Service Requested  2 = Forwarding Service Requested  3 = Address Service Requested  4 = Change Service Requested and  5 = No Service Selected.  Note: For International Mail Innovations shipments use No Service Selected. International Mail Innovations shipments are applicable for Priority Mail Innovations and Mail Innovations Economy Mail Innovations services only.  Required for Mail Innovations forward shipments., defaults to None
    :type usps_endorsement: str, optional
    :param mi_label_cn22_indicator: Indicates single label with both MI label and CN22 form.  International CN22 form is required., defaults to None
    :type mi_label_cn22_indicator: str, optional
    :param sub_classification: A component encoded on the barcode of the Mail Innovations label.   Valid values:  IR = Irregular MA = Machineable SubClass is only required if the customer's contract have them subclass the package not UPS., defaults to None
    :type sub_classification: str, optional
    :param cost_center: Customer assigned identifier for report and billing summarization displays to the right of the Cost Center title.  Required for Mail Innovations Return shipments. It is shown on the bottom of the shipping label as reference 2. Cost Center length is alphanumeric with a max length of 30 for Mail Innovations forward shipments. Cost Center length is numeric with a max length of 4 for Mail Innovations Return shipments., defaults to None
    :type cost_center: str, optional
    :param cost_center_barcode_indicator: Presence/Absence indicator. Presence of this indicator means that the customer is requesting for the CostCenter field to be barcoded at the bottom of the label., defaults to None
    :type cost_center_barcode_indicator: str, optional
    :param package_id: Customer-assigned unique piece identifier that returns visibility events.  Required only for Mail Innovations forward shipments. Alpha numeric values only. It is shown on the bottom of the shipping label as reference 1., defaults to None
    :type package_id: str, optional
    :param package_id_barcode_indicator: Presence/Absence indicator. Presence of this indicator means that the customer is requesting for the PackageID field to be barcoded at the bottom of the label., defaults to None
    :type package_id_barcode_indicator: str, optional
    :param irregular_indicator: Mail classification defined by the USPS.   Valid values:  1 = Balloon 2 = Oversize 3 = Not Applicable, defaults to None
    :type irregular_indicator: str, optional
    :param shipment_indication_type: shipment_indication_type, defaults to None
    :type shipment_indication_type: List[ShipmentShipmentIndicationType], optional
    :param mi_dual_return_shipment_key: MIDualReturnShipmentKey is unique key required to process Mail Innovations Dual Return Shipment.  The unique identifier (key) would be returned in response of first phase of Mail Innovations Dual Return Shipments.  This unique identifier (key) would be part of request for second phase of Mail Innovations Dual Return Shipments. Format:  For Package return shipments, the package tracking number is concatenated with the system time (YYYY-MM-DDHH.MM.SS.NNN), followed by service code.  For MI Return shipments, the Mail Manifest ID (MMI) is concatenated with the system time.  The unique identifier (key) is required to link the package and the Mail Innovations portion of Dual Return shipment.  If unique identifier (key) is empty in the request for UPS Mail Innovations Return Service, the request will be treated as the first phase of the Mail Innovations Dual Returns Request.  If the MIDualReturnShipmentIndicator is present with empty or null MIDualReturnShipmentKey in UPS Package Return Shipment, the request will be treated as the first phase of Dual MI Return Label Shipment.  This field would be ignored if MIDualReturnShipmentIndicator is not present in UPS Package Return Shipment request., defaults to None
    :type mi_dual_return_shipment_key: str, optional
    :param mi_dual_return_shipment_indicator: MIDualReturnShipmentIndicator is an indicator to identify a Package Shipment is part of UPS Mail Innovations Dual Label Shipment.  Its presence means Package Shipment is part of UPS Mail Innovations Dual Label shipment.  If the indicator is present in Package Shipment request, shipment would be considered as part of a Dual Mail Innovations Returns.  This indicator is not valid with UPS Mail Innovations Returns Service code., defaults to None
    :type mi_dual_return_shipment_indicator: str, optional
    :param rating_method_requested_indicator: Presence/Absence Indicator. Any value inside is ignored. RatingMethodRequestedIndicator is an indicator. If present, Billable Weight Calculation method information and Rating Method information would be returned in response., defaults to None
    :type rating_method_requested_indicator: str, optional
    :param tax_information_indicator: Presence/Absence Indicator. Any value inside is ignored. TaxInformationIndicator is an indicator. If present, any taxes that may be applicable to a shipment would be returned in response. If this indicator is requested with NegotiatedRatesIndicator, Tax related information, if applicable, would be returned only for Negotiated Rates and not for Published Rates. The Tax related information includes any type of Taxes, corresponding Monetary Values, Total Charges with Taxes and disclaimers (if applicable) would be returned in response., defaults to None
    :type tax_information_indicator: str, optional
    :param shipment_service_options: Container for Shipment Service Options., defaults to None
    :type shipment_service_options: ShipmentShipmentServiceOptions, optional
    :param locale: Represents 5 character ISO Locale that allows the user to request Reference Number Code on Label, Label instructions and Receipt instructions (if applicable) in desired language.  Locale is specified by the combination of language code and country or territory code - 2 character language code and 2 character country or territory code seperated by an underscore ('_') character.  If Locale element is requested along with LabelLinksIndicator, the URL to retrieve Label and Receipts (if applicable) will be returned in the requested Locale. Please note only LabelURL and ReceiptURL (if applicable) will be returned. LocalLanguageLabelURL and LocalLanguageReceiptURL will not be returned if Locale element is present in request. Queen's English (en_GB) is the default, defaults to None
    :type locale: str, optional
    :param shipment_value_threshold_code: Shipment Value Threshold Code. 01 = Shipment value is below or equals to threshold value 02 = Shipment value is above threshold value.     NA = Not Applicable, defaults to None
    :type shipment_value_threshold_code: str, optional
    :param master_carton_id: Master Carton ID. If Economy Service (17 or 72) : Economy Shipment will be associated with given Master Carton ID. If Non-Economy Service: Master Carton Shipment will be created for given Master Carton ID., defaults to None
    :type master_carton_id: str, optional
    :param master_carton_indicator: Master Carton Indicator. Presence of the indicator means Master Carton ID will be created and returned to client.  This is an empty tag, any value inside is ignored.                                                                  MasterCartonIndicator is only valid with Econmoy Shipment (Service Code 17 or 72). Will be ignored if master carton id present., defaults to None
    :type master_carton_indicator: str, optional
    :param shipment_date: User can send up to 7 days in the future with current date as day zero. Format: YYYYMMDD, defaults to None
    :type shipment_date: str, optional
    :param package: package
    :type package: List[ShipmentPackage]
    """

    def __init__(
        self,
        shipper: ShipmentShipper,
        ship_to: ShipmentShipTo,
        service: ShipmentService,
        package: List[ShipmentPackage],
        description: str = None,
        return_service: ShipmentReturnService = None,
        documents_only_indicator: str = None,
        alternate_delivery_address: ShipmentAlternateDeliveryAddress = None,
        ship_from: ShipmentShipFrom = None,
        payment_information: ShipmentPaymentInformation = None,
        frs_payment_information: ShipmentFrsPaymentInformation = None,
        freight_shipment_information: ShipmentFreightShipmentInformation = None,
        goods_not_in_free_circulation_indicator: str = None,
        promotional_discount_information: ShipmentPromotionalDiscountInformation = None,
        dg_signatory_info: ShipmentDgSignatoryInfo = None,
        shipment_rating_options: ShipmentShipmentRatingOptions = None,
        movement_reference_number: str = None,
        reference_number: List[ShipmentReferenceNumber] = None,
        invoice_line_total: ShipmentInvoiceLineTotal = None,
        num_of_pieces_in_shipment: str = None,
        usps_endorsement: str = None,
        mi_label_cn22_indicator: str = None,
        sub_classification: str = None,
        cost_center: str = None,
        cost_center_barcode_indicator: str = None,
        package_id: str = None,
        package_id_barcode_indicator: str = None,
        irregular_indicator: str = None,
        shipment_indication_type: List[ShipmentShipmentIndicationType] = None,
        mi_dual_return_shipment_key: str = None,
        mi_dual_return_shipment_indicator: str = None,
        rating_method_requested_indicator: str = None,
        tax_information_indicator: str = None,
        shipment_service_options: ShipmentShipmentServiceOptions = None,
        locale: str = None,
        shipment_value_threshold_code: str = None,
        master_carton_id: str = None,
        master_carton_indicator: str = None,
        shipment_date: str = None,
    ):
        if description is not None:
            self.description = description
        if return_service is not None:
            self.return_service = self._define_object(
                return_service, ShipmentReturnService
            )
        if documents_only_indicator is not None:
            self.documents_only_indicator = documents_only_indicator
        self.shipper = self._define_object(shipper, ShipmentShipper)
        self.ship_to = self._define_object(ship_to, ShipmentShipTo)
        if alternate_delivery_address is not None:
            self.alternate_delivery_address = self._define_object(
                alternate_delivery_address, ShipmentAlternateDeliveryAddress
            )
        if ship_from is not None:
            self.ship_from = self._define_object(ship_from, ShipmentShipFrom)
        if payment_information is not None:
            self.payment_information = self._define_object(
                payment_information, ShipmentPaymentInformation
            )
        if frs_payment_information is not None:
            self.frs_payment_information = self._define_object(
                frs_payment_information, ShipmentFrsPaymentInformation
            )
        if freight_shipment_information is not None:
            self.freight_shipment_information = self._define_object(
                freight_shipment_information, ShipmentFreightShipmentInformation
            )
        if goods_not_in_free_circulation_indicator is not None:
            self.goods_not_in_free_circulation_indicator = (
                goods_not_in_free_circulation_indicator
            )
        if promotional_discount_information is not None:
            self.promotional_discount_information = self._define_object(
                promotional_discount_information, ShipmentPromotionalDiscountInformation
            )
        if dg_signatory_info is not None:
            self.dg_signatory_info = self._define_object(
                dg_signatory_info, ShipmentDgSignatoryInfo
            )
        if shipment_rating_options is not None:
            self.shipment_rating_options = self._define_object(
                shipment_rating_options, ShipmentShipmentRatingOptions
            )
        if movement_reference_number is not None:
            self.movement_reference_number = movement_reference_number
        if reference_number is not None:
            self.reference_number = self._define_list(
                reference_number, ShipmentReferenceNumber
            )
        self.service = self._define_object(service, ShipmentService)
        if invoice_line_total is not None:
            self.invoice_line_total = self._define_object(
                invoice_line_total, ShipmentInvoiceLineTotal
            )
        if num_of_pieces_in_shipment is not None:
            self.num_of_pieces_in_shipment = num_of_pieces_in_shipment
        if usps_endorsement is not None:
            self.usps_endorsement = usps_endorsement
        if mi_label_cn22_indicator is not None:
            self.mi_label_cn22_indicator = mi_label_cn22_indicator
        if sub_classification is not None:
            self.sub_classification = sub_classification
        if cost_center is not None:
            self.cost_center = cost_center
        if cost_center_barcode_indicator is not None:
            self.cost_center_barcode_indicator = cost_center_barcode_indicator
        if package_id is not None:
            self.package_id = package_id
        if package_id_barcode_indicator is not None:
            self.package_id_barcode_indicator = package_id_barcode_indicator
        if irregular_indicator is not None:
            self.irregular_indicator = irregular_indicator
        if shipment_indication_type is not None:
            self.shipment_indication_type = self._define_list(
                shipment_indication_type, ShipmentShipmentIndicationType
            )
        if mi_dual_return_shipment_key is not None:
            self.mi_dual_return_shipment_key = mi_dual_return_shipment_key
        if mi_dual_return_shipment_indicator is not None:
            self.mi_dual_return_shipment_indicator = mi_dual_return_shipment_indicator
        if rating_method_requested_indicator is not None:
            self.rating_method_requested_indicator = rating_method_requested_indicator
        if tax_information_indicator is not None:
            self.tax_information_indicator = tax_information_indicator
        if shipment_service_options is not None:
            self.shipment_service_options = self._define_object(
                shipment_service_options, ShipmentShipmentServiceOptions
            )
        if locale is not None:
            self.locale = locale
        if shipment_value_threshold_code is not None:
            self.shipment_value_threshold_code = shipment_value_threshold_code
        if master_carton_id is not None:
            self.master_carton_id = master_carton_id
        if master_carton_indicator is not None:
            self.master_carton_indicator = master_carton_indicator
        if shipment_date is not None:
            self.shipment_date = shipment_date
        self.package = self._define_list(package, ShipmentPackage)
