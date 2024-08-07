# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .international_forms_user_created_form import InternationalFormsUserCreatedForm
from .international_forms_ups_premium_care_form import (
    InternationalFormsUpsPremiumCareForm,
)
from .international_forms_cn22_form import InternationalFormsCn22Form
from .international_forms_eei_filing_option import InternationalFormsEeiFilingOption
from .international_forms_contacts import InternationalFormsContacts
from .international_forms_product import InternationalFormsProduct
from .international_forms_discount import InternationalFormsDiscount
from .international_forms_freight_charges import InternationalFormsFreightCharges
from .international_forms_insurance_charges import InternationalFormsInsuranceCharges
from .international_forms_other_charges import InternationalFormsOtherCharges
from .international_forms_blanket_period import InternationalFormsBlanketPeriod


@JsonMap(
    {
        "form_type": "FormType",
        "user_created_form": "UserCreatedForm",
        "ups_premium_care_form": "UPSPremiumCareForm",
        "cn22_form": "CN22Form",
        "additional_document_indicator": "AdditionalDocumentIndicator",
        "form_group_id_name": "FormGroupIdName",
        "eei_filing_option": "EEIFilingOption",
        "contacts": "Contacts",
        "product": "Product",
        "invoice_number": "InvoiceNumber",
        "invoice_date": "InvoiceDate",
        "purchase_order_number": "PurchaseOrderNumber",
        "terms_of_shipment": "TermsOfShipment",
        "reason_for_export": "ReasonForExport",
        "comments": "Comments",
        "declaration_statement": "DeclarationStatement",
        "discount": "Discount",
        "freight_charges": "FreightCharges",
        "insurance_charges": "InsuranceCharges",
        "other_charges": "OtherCharges",
        "currency_code": "CurrencyCode",
        "blanket_period": "BlanketPeriod",
        "export_date": "ExportDate",
        "exporting_carrier": "ExportingCarrier",
        "carrier_id": "CarrierID",
        "in_bond_code": "InBondCode",
        "entry_number": "EntryNumber",
        "point_of_origin": "PointOfOrigin",
        "point_of_origin_type": "PointOfOriginType",
        "mode_of_transport": "ModeOfTransport",
        "port_of_export": "PortOfExport",
        "port_of_unloading": "PortOfUnloading",
        "loading_pier": "LoadingPier",
        "parties_to_transaction": "PartiesToTransaction",
        "routed_export_transaction_indicator": "RoutedExportTransactionIndicator",
        "containerized_indicator": "ContainerizedIndicator",
        "override_paperless_indicator": "OverridePaperlessIndicator",
        "shipper_memo": "ShipperMemo",
        "hazardous_materials_indicator": "HazardousMaterialsIndicator",
    }
)
class ShipmentServiceOptionsInternationalForms(BaseModel):
    """International Forms information.

    :param form_type: Indicates the name of the International Form requested. Valid values: - 01 - Invoice - 03 - CO - 04 - NAFTA CO - 05 - Partial Invoice - 06 - Packinglist - 07 - Customer Generated Forms - 08 â€“ Air Freight Packing List - 09 - CN22 Form - 10 â€“ UPS Premium Care Form - 11 - EEI For shipment with return service, 05 or 10 are the only valid values. Note: 01 and 05 are mutually exclusive and 05 are only valid for return shipments only.
    :type form_type: List[str]
    :param user_created_form: Data container for DocumentID(s).  Required if Form Type is 07., defaults to None
    :type user_created_form: InternationalFormsUserCreatedForm, optional
    :param ups_premium_care_form: UPS Premium Care Form is required if UPS Premium Care Indicator is present on a package.  Valid only for Canada to Canada movements., defaults to None
    :type ups_premium_care_form: InternationalFormsUpsPremiumCareForm, optional
    :param cn22_form: Container for the CN22 form.  Required if the customer wants to use the UPS generated CN22., defaults to None
    :type cn22_form: InternationalFormsCn22Form, optional
    :param additional_document_indicator: Presence of the indicator means user will supply additional document, such as EEI, NAFTA_CO or CO.  This indicator should be set when the shipper intends to utilize UPS paperless invoice functionality AND the shipper has SELF-PREPARED other International Forms (EEI, CO, NAFTACO) to accompany the shipment.  It is evaluated only when:  1. Account is paperless enabled.  2. Movement requires an invoice. 3. Destination country or territory accepts paperless invoice.  4. Invoice data is supplied by the client and the data passes validation., defaults to None
    :type additional_document_indicator: str, optional
    :param form_group_id_name: Contains description text which identifies the group of International forms. This element does not appear on the forms., defaults to None
    :type form_group_id_name: str, optional
    :param eei_filing_option: EEI Filing option.  Applicable for EEI form and is required., defaults to None
    :type eei_filing_option: InternationalFormsEeiFilingOption, optional
    :param contacts: Holds the contact information of various parties.  Applicable for EEI and NAFTA CO only. Required for NAFTA CO and EEI. Ultimate consignee contact information is required for EEI.  Producer contact information is required for NAFTA CO, defaults to None
    :type contacts: InternationalFormsContacts, optional
    :param product: product
    :type product: List[InternationalFormsProduct]
    :param invoice_number: Commercial Invoice number assigned by the exporter.  Applies to Invoice and Partial Invoice forms only. Required for Invoice forms and optional for Partial Invoice., defaults to None
    :type invoice_number: str, optional
    :param invoice_date: Date when the Invoice is created. Ideally this is the same as the ship date.  Applies to Invoice and Partial Invoice forms only. Required for Invoice forms and optional for Partial Invoice. Required for Invoice form for forward shipments. For shipment with return service, the user input will be ignored, and the field will be blank on the invoice. Format is yyyyMMdd., defaults to None
    :type invoice_date: str, optional
    :param purchase_order_number: The customer's order reference number.  Applies to Invoice and Partial Invoice forms only., defaults to None
    :type purchase_order_number: str, optional
    :param terms_of_shipment: Indicates the rights to the seller from the buyer. Also, it refers to Terms of Sale.  Applies to Invoice and Partial Invoice forms only.  Valid values:  CFR: Cost and Freight  CIF: Cost Insurance and Freight  CIP: Carriage and Insurance Paid  CPT: Carriage Paid To  DAF: Delivered at Frontier  DDP: Delivery Duty Paid  DDU: Delivery Duty Unpaid  DEQ: Delivered Ex Quay  DES: Delivered Ex Ship  EXW: Ex Works  FAS: Free Alongside Ship  FCA: Free Carrier  FOB: Free On Board, defaults to None
    :type terms_of_shipment: str, optional
    :param reason_for_export: A reason to export the current international shipment. Valid values: SALE, GIFT, SAMPLE, RETURN, REPAIR, INTERCOMPANYDATA, Any other reason.  Applies to Invoice and Partial Invoice forms only. Required for Invoice forms and Optional for Partial Invoice. No validation., defaults to None
    :type reason_for_export: str, optional
    :param comments: Any extra information about the current shipment.  Applies to Invoice and Partial Invoice forms only., defaults to None
    :type comments: str, optional
    :param declaration_statement: This is the legal explanation, used by Customs, for the delivering of this shipment. It must be identical to the set of declarations actually used by Customs. Examples of declarations that might be entered in this field are: I hereby certify that the goods covered by this shipment qualify as originating goods for purposes of preferential tariff treatment under the NAFTA. I hereby certify that the information on this invoice is true and correct and the contents and value of this shipment is as stated above.  EEA statement:  The exporter of the products covered by this document declares that except where otherwise clearly indicated these products are of EEA preferential origin.  Applies to Invoice and Partial Invoice forms only. On the invoice for return shipment, the verbiage is as follows (user input is ignored): The exporter of the products covered by this document declares that except where otherwise clearly indicated these products are of EEA preferential origin, defaults to None
    :type declaration_statement: str, optional
    :param discount: Container tag that holds the discount.  Applies to Invoice and Partial Invoice forms only., defaults to None
    :type discount: InternationalFormsDiscount, optional
    :param freight_charges: Container tag that holds the Freight Charges.  Applies to Invoice and Partial Invoice forms only., defaults to None
    :type freight_charges: InternationalFormsFreightCharges, optional
    :param insurance_charges: Container tag that holds the Insurance Charges.  Applies to Invoice and Partial Invoice forms only., defaults to None
    :type insurance_charges: InternationalFormsInsuranceCharges, optional
    :param other_charges: Container tag that holds the information of amount that covers additional charges not already listed on the invoice.  Applies to Invoice and Partial Invoice forms only., defaults to None
    :type other_charges: InternationalFormsOtherCharges, optional
    :param currency_code: Currency code for all the monetary values of the Invoice form.  Applies to Invoice and Partial Invoice forms only., defaults to None
    :type currency_code: str, optional
    :param blanket_period: This field should be entered if the  NAFTA Certificate covers multiple shipments of identical goods as described in the Description of Goods field that are imported into a NAFTA country or territory for a specified period of up to one year (the blanket period). The importation of a good for which preferential treatment is claimed based on this certificate must occur between these dates.  Applies to NAFTA CO form only. Required for NAFTA CO.  This is not valid for a paperless shipment., defaults to None
    :type blanket_period: InternationalFormsBlanketPeriod, optional
    :param export_date: The date the goods will be exiting the country or territory.  Applies to CO and EEI forms only. Required for CO and EEI forms. Format is yyyyMMdd., defaults to None
    :type export_date: str, optional
    :param exporting_carrier: The name of the carrier that is exporting the shipment. The vessels flag number should also be entered, if the carrier is a vessel. If value is empty, it will be set to default value as 'UPS' for EEI forms.  Applies to CO and EEI forms only. Required for CO forms. , defaults to None
    :type exporting_carrier: str, optional
    :param carrier_id: The four-character Standard Carrier Alpha Code (SCAC) for vessel, rail, and truck shipments. For air shipment, enter the two or three character International Air Transport Association (IATA) code.  Applies to EEI forms only. No Validations., defaults to None
    :type carrier_id: str, optional
    :param in_bond_code: The two-character In Bond Code.  Applies to EEI forms only. Required for EEI forms. Valid values for EEI are: 70: Not in bond; 67: IE from a FTZ; 68: T&E from a FTZ., defaults to None
    :type in_bond_code: str, optional
    :param entry_number: The Import Entry Number when the export transaction is used as proof of export for import transactions (examples: In Bond, Temporary Import Bond or Drawbacks).  Applies to EEI forms only. Conditionally Required for EEI forms when In bond code value is other than 70 (Not In Bond), defaults to None
    :type entry_number: str, optional
    :param point_of_origin: Contains one of the following:  The two-digit U.S. Postal Service abbreviation for the state from which the goods were shipped to the port of export. The state that is the source for the good with the highest value. The state of consolidation. The Foreign Trade Zone number of the zone from where the exports are leaving.  If the goods were shipped from Puerto Rico, enter PR.  Applies to EEI forms only. Required for EEI., defaults to None
    :type point_of_origin: str, optional
    :param point_of_origin_type: Valid values are : S (for state postal code abbreviation) , F : FTZ Identifier  Applies EEI forms only. Required for EEI form., defaults to None
    :type point_of_origin_type: str, optional
    :param mode_of_transport: Mode of transport by which the goods are exported. Valid values: Air, AirContainerized, Auto, FixedTransportInstallations, Mail, PassengerHandcarried, Pedestrian, Rail, Rail, Containerized, RoadOther, SeaBarge, SeaContainerized, SeaNoncontainerized, Truck, TruckContainerized.  Applies to EEI forms only.  Required for EEI.  Only allowed values can be entered. Only 10 Characters can appear on the form. Anything greater than 10 characters will be truncated on the form., defaults to None
    :type mode_of_transport: str, optional
    :param port_of_export: Should be one of the following-Overland: The U.S. Customs port where the carrier crosses the U.S. border, Vessel and Air: The U.S. Customs port where the goods are loaded on the carrier to be exported from the U.S., Postal: The U.S. Postal Office from where the goods are mailed.  Applies to EEI forms only. No validation is performed., defaults to None
    :type port_of_export: str, optional
    :param port_of_unloading: The country or territory and the port where the goods will be unloaded from the exporting carrier. For vessel and air shipments only.  Applies to EEI forms only. No validation is performed., defaults to None
    :type port_of_unloading: str, optional
    :param loading_pier: Pier where goods are loaded. For vessel shipments only.  Applies to EEI forms only. No validation is performed., defaults to None
    :type loading_pier: str, optional
    :param parties_to_transaction: Information about parties to transaction. Use Related, if the parties to the transaction are related. A related party is an export from a U.S. businessperson or business to a foreign business or from a U.S. business to a foreign person or business where the person has at least 10 percent of the voting shares of the business during the fiscal year. If unincorporated, then an equivalent interest in the business.  Applies to EEI forms only. Valid values: - R - Related - N - Non-related. Parties to transaction is required if EEIFilingOption Code is 3 and if valid UPSFiled POA Code present in request. Default will be set to N - Non-related if invalid code present with length of one. , defaults to None
    :type parties_to_transaction: str, optional
    :param routed_export_transaction_indicator: If Present, indicates that it is a routed export transaction. A routed export transaction is one, where the foreign principal party in interest authorizes a U.S. forwarding (or other) agent to export the merchandise outside the U.S.  Applies to EEI forms only., defaults to None
    :type routed_export_transaction_indicator: str, optional
    :param containerized_indicator: If present indicates that the goods are containerized. This applies to vessel shipments only.  Applies to EEI forms only., defaults to None
    :type containerized_indicator: str, optional
    :param override_paperless_indicator: The application will automatically provide a copy of the invoice or NAFTA/CO with each response regardless of whether the user has enabled Paperless account. The user now has the option to print or ignore the copy provided., defaults to None
    :type override_paperless_indicator: str, optional
    :param shipper_memo: Text for the shipper to add additional information.  Forward shipment only., defaults to None
    :type shipper_memo: str, optional
    :param hazardous_materials_indicator: This is an empty tag. Presence of the indicator for EEI form means shipment contains hazardous material., defaults to None
    :type hazardous_materials_indicator: str, optional
    """

    def __init__(
        self,
        form_type: List[str],
        product: List[InternationalFormsProduct],
        user_created_form: InternationalFormsUserCreatedForm = None,
        ups_premium_care_form: InternationalFormsUpsPremiumCareForm = None,
        cn22_form: InternationalFormsCn22Form = None,
        additional_document_indicator: str = None,
        form_group_id_name: str = None,
        eei_filing_option: InternationalFormsEeiFilingOption = None,
        contacts: InternationalFormsContacts = None,
        invoice_number: str = None,
        invoice_date: str = None,
        purchase_order_number: str = None,
        terms_of_shipment: str = None,
        reason_for_export: str = None,
        comments: str = None,
        declaration_statement: str = None,
        discount: InternationalFormsDiscount = None,
        freight_charges: InternationalFormsFreightCharges = None,
        insurance_charges: InternationalFormsInsuranceCharges = None,
        other_charges: InternationalFormsOtherCharges = None,
        currency_code: str = None,
        blanket_period: InternationalFormsBlanketPeriod = None,
        export_date: str = None,
        exporting_carrier: str = None,
        carrier_id: str = None,
        in_bond_code: str = None,
        entry_number: str = None,
        point_of_origin: str = None,
        point_of_origin_type: str = None,
        mode_of_transport: str = None,
        port_of_export: str = None,
        port_of_unloading: str = None,
        loading_pier: str = None,
        parties_to_transaction: str = None,
        routed_export_transaction_indicator: str = None,
        containerized_indicator: str = None,
        override_paperless_indicator: str = None,
        shipper_memo: str = None,
        hazardous_materials_indicator: str = None,
    ):
        self.form_type = form_type
        if user_created_form is not None:
            self.user_created_form = self._define_object(
                user_created_form, InternationalFormsUserCreatedForm
            )
        if ups_premium_care_form is not None:
            self.ups_premium_care_form = self._define_object(
                ups_premium_care_form, InternationalFormsUpsPremiumCareForm
            )
        if cn22_form is not None:
            self.cn22_form = self._define_object(cn22_form, InternationalFormsCn22Form)
        if additional_document_indicator is not None:
            self.additional_document_indicator = additional_document_indicator
        if form_group_id_name is not None:
            self.form_group_id_name = form_group_id_name
        if eei_filing_option is not None:
            self.eei_filing_option = self._define_object(
                eei_filing_option, InternationalFormsEeiFilingOption
            )
        if contacts is not None:
            self.contacts = self._define_object(contacts, InternationalFormsContacts)
        self.product = self._define_list(product, InternationalFormsProduct)
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if terms_of_shipment is not None:
            self.terms_of_shipment = terms_of_shipment
        if reason_for_export is not None:
            self.reason_for_export = reason_for_export
        if comments is not None:
            self.comments = comments
        if declaration_statement is not None:
            self.declaration_statement = declaration_statement
        if discount is not None:
            self.discount = self._define_object(discount, InternationalFormsDiscount)
        if freight_charges is not None:
            self.freight_charges = self._define_object(
                freight_charges, InternationalFormsFreightCharges
            )
        if insurance_charges is not None:
            self.insurance_charges = self._define_object(
                insurance_charges, InternationalFormsInsuranceCharges
            )
        if other_charges is not None:
            self.other_charges = self._define_object(
                other_charges, InternationalFormsOtherCharges
            )
        if currency_code is not None:
            self.currency_code = currency_code
        if blanket_period is not None:
            self.blanket_period = self._define_object(
                blanket_period, InternationalFormsBlanketPeriod
            )
        if export_date is not None:
            self.export_date = export_date
        if exporting_carrier is not None:
            self.exporting_carrier = exporting_carrier
        if carrier_id is not None:
            self.carrier_id = carrier_id
        if in_bond_code is not None:
            self.in_bond_code = in_bond_code
        if entry_number is not None:
            self.entry_number = entry_number
        if point_of_origin is not None:
            self.point_of_origin = point_of_origin
        if point_of_origin_type is not None:
            self.point_of_origin_type = point_of_origin_type
        if mode_of_transport is not None:
            self.mode_of_transport = mode_of_transport
        if port_of_export is not None:
            self.port_of_export = port_of_export
        if port_of_unloading is not None:
            self.port_of_unloading = port_of_unloading
        if loading_pier is not None:
            self.loading_pier = loading_pier
        if parties_to_transaction is not None:
            self.parties_to_transaction = parties_to_transaction
        if routed_export_transaction_indicator is not None:
            self.routed_export_transaction_indicator = (
                routed_export_transaction_indicator
            )
        if containerized_indicator is not None:
            self.containerized_indicator = containerized_indicator
        if override_paperless_indicator is not None:
            self.override_paperless_indicator = override_paperless_indicator
        if shipper_memo is not None:
            self.shipper_memo = shipper_memo
        if hazardous_materials_indicator is not None:
            self.hazardous_materials_indicator = hazardous_materials_indicator
