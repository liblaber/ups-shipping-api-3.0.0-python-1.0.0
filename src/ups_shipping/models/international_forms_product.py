# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .product_unit import ProductUnit
from .product_net_cost_date_range import ProductNetCostDateRange
from .product_product_weight import ProductProductWeight
from .product_schedule_b import ProductScheduleB
from .product_exclude_from_form import ProductExcludeFromForm
from .product_packing_list_info import ProductPackingListInfo
from .product_eei_information import ProductEeiInformation


@JsonMap(
    {
        "description": "Description",
        "unit": "Unit",
        "commodity_code": "CommodityCode",
        "part_number": "PartNumber",
        "origin_country_code": "OriginCountryCode",
        "joint_production_indicator": "JointProductionIndicator",
        "net_cost_code": "NetCostCode",
        "net_cost_date_range": "NetCostDateRange",
        "preference_criteria": "PreferenceCriteria",
        "producer_info": "ProducerInfo",
        "marks_and_numbers": "MarksAndNumbers",
        "number_of_packages_per_commodity": "NumberOfPackagesPerCommodity",
        "product_weight": "ProductWeight",
        "vehicle_id": "VehicleID",
        "schedule_b": "ScheduleB",
        "export_type": "ExportType",
        "sed_total_value": "SEDTotalValue",
        "exclude_from_form": "ExcludeFromForm",
        "packing_list_info": "PackingListInfo",
        "eei_information": "EEIInformation",
    }
)
class InternationalFormsProduct(BaseModel):
    """Contains the commodity/product information.  Applies to EEI, Invoice, Partial Invoice, CO and NAFTA CO. When any International form is requested, at least one Product must be present.

    Maximum number of products allowed for different forms are:

    50: Package Packing List

    100: Commercial Invoice, NAFTA, CO, EEI

    1000: Air Freight packing list

    Note: For Partial Invoice this container is optional.

    :param description: Description of the product.  Applies to all International Forms. Optional for Partial Invoice. Must be present at least once and can occur for a maximum of 3 times.
    :type description: List[str]
    :param unit: Container tag for the Unit information of each product. (also called as commodity)  Required for Invoice forms and optional for Partial Invoice., defaults to None
    :type unit: ProductUnit, optional
    :param commodity_code: 6-to-15-alphanumeric commodity code. Customs uses this code to determine what duties should be assessed on the commodity.  Applies to Invoice, Partial Invoice and NAFTA CO. Required for NAFTA CO and optional for Partial Invoice. Should be at least 6 alphanumeric. For NAFTA CO: For each good described in Description of Goods field, identify the H.S. tariff classification to six digits. If the good is subject to a specific rule of origin in Annex 401 that requires eight digits, identify to eight digits, using the H.S. tariff classification of the country or territory into whose territory the good is imported., defaults to None
    :type commodity_code: str, optional
    :param part_number: The part number or reference number for the product contained in the invoice line, as indicated on the customs invoice.  Applies to Invoice and Partial Invoice. Required for Invoice forms and optional for Partial Invoice., defaults to None
    :type part_number: str, optional
    :param origin_country_code: The country or territory in which the good was manufactured, produced or grown. For detailed information on country or territory of origin, certificate of origin, rules of origin, and any related matters, please refer to the U.S. Customs and Border Protection Web site at www.customs.gov or contact your country or territory's Customs authority., defaults to None
    :type origin_country_code: str, optional
    :param joint_production_indicator: If present, JNT will be used as the origin of country or territory code on the NAFTA form and the Product/Origincountry or territoryCode tag will be ignored.  Applies to NAFTA CO only., defaults to None
    :type joint_production_indicator: str, optional
    :param net_cost_code: For each good described in the Description of Goods field, where the good is subject to a regional value content (RVC) requirement, indicate NC if the RVC is calculated according to the net cost method; otherwise, indicate NO. If the RVC is calculated over a period of time then indicate "NC with begin/end date" by passing code "ND"  Applies to NAFTA CO only. Required for NAFTA CO.  Valid values: - NC - ND - NO , defaults to None
    :type net_cost_code: str, optional
    :param net_cost_date_range: Date Range for regional value content (RVC).  Applies to NAFTA CO only., defaults to None
    :type net_cost_date_range: ProductNetCostDateRange, optional
    :param preference_criteria: Indicates the criterion (A through F) for each good described in the Description of Goods field if applicable.  The rules of origin are contained in Chapter Four and Annex 401.  Additional rules are described in Annex 703.2 (certain agricultural goods), Annex 300-B, Appendix 6 (certain textile goods) and Annex 308.1 (certain automatic data processing goods and their parts).  Applies to NAFTA CO only., defaults to None
    :type preference_criteria: str, optional
    :param producer_info: Indicate the following:  Yes - If shipper is the producer of the good. If not, state 02, 03, and 04 depending on whether this certificate was based upon:   No [1] - Knowledge of whether the good qualifies as an originating good.  No [2] - Reliance on the producers written representation (other than a Certificate of Origin) that the good qualifies as an originating good.  No [3] - A completed and signed Certificate for the good voluntarily provided to the exporter by the producer.  Applicable for NAFTA CO and is required. Valid values: Yes, No [1], No [2], and No [3]., defaults to None
    :type producer_info: str, optional
    :param marks_and_numbers: Any special marks, codes, and numbers that may appear on package.  Applies to CO Only., defaults to None
    :type marks_and_numbers: str, optional
    :param number_of_packages_per_commodity: The total number of packages, cartons, or containers for the commodity.  Applicable for CO and is required. Should be numeric. Valid characters are 0 -9., defaults to None
    :type number_of_packages_per_commodity: str, optional
    :param product_weight: The shipping weight, including containers, for each commodity with a separate Harmonized Tariff Code / Schedule B Number. This weight does not include carrier equipment.  Applies to CO and EEI forms only. Required for CO and EEI forms., defaults to None
    :type product_weight: ProductProductWeight, optional
    :param vehicle_id: Includes the following information for used self-propelled vehicles as defined in Customs regulations 19 CFR 192.1: The unique Vehicle Identification Number (VIN) in the proper format. Or The Product Identification Number (PIN) for those used self-propelled vehicles for which there are no VINs.  Or the Vehicle Title Number.  Applies to EEI forms only., defaults to None
    :type vehicle_id: str, optional
    :param schedule_b: Container tag for the schedule B information of a commodity.  Applies to EEI forms only. Required for EEI form, defaults to None
    :type schedule_b: ProductScheduleB, optional
    :param export_type: Code indicating Domestic: Exports that have been produced, manufactured, or grown in the United States or Puerto Rico. This includes imported merchandise which has been enhanced in value or changed from the form in which imported by further manufacture or processing in the United States or Puerto Rico. Foreign: Merchandise that has entered the United States and is being exported again in the same condition as when imported.   Applies to EEI forms only. Required for EEI form.  Valid values:  D: Domestic; F: Foreign., defaults to None
    :type export_type: str, optional
    :param sed_total_value: This amount will always be USD.  Applies to EEI forms only. Required for EEI form. Valid characters are 0-9 and \'.\' (Decimal point). Limit to 2 digit after the decimal. The maximum length of the field is 15 including \'.\' and can hold up to 2 decimal places. Note: This value is calculated based on the Product/Unit/Value and /Product/Unit/Number (Number of Units * Price per Unit). If the total value is incorrect it will be replaced by the actual calculated total value. , defaults to None
    :type sed_total_value: str, optional
    :param exclude_from_form: Container tag for determining whether or not to exclude product information from a particular form.  If this container is not present we assume that the DEFAULT is selected which is "none" and all products will appear on all forms., defaults to None
    :type exclude_from_form: ProductExcludeFromForm, optional
    :param packing_list_info: Data Container holding package related information.  Required for packaging list and Air Freight Packing list., defaults to None
    :type packing_list_info: ProductPackingListInfo, optional
    :param eei_information: Required for EEI form.  Applies to EEI form only., defaults to None
    :type eei_information: ProductEeiInformation, optional
    """

    def __init__(
        self,
        description: List[str],
        unit: ProductUnit = None,
        commodity_code: str = None,
        part_number: str = None,
        origin_country_code: str = None,
        joint_production_indicator: str = None,
        net_cost_code: str = None,
        net_cost_date_range: ProductNetCostDateRange = None,
        preference_criteria: str = None,
        producer_info: str = None,
        marks_and_numbers: str = None,
        number_of_packages_per_commodity: str = None,
        product_weight: ProductProductWeight = None,
        vehicle_id: str = None,
        schedule_b: ProductScheduleB = None,
        export_type: str = None,
        sed_total_value: str = None,
        exclude_from_form: ProductExcludeFromForm = None,
        packing_list_info: ProductPackingListInfo = None,
        eei_information: ProductEeiInformation = None,
    ):
        self.description = description
        if unit is not None:
            self.unit = self._define_object(unit, ProductUnit)
        if commodity_code is not None:
            self.commodity_code = commodity_code
        if part_number is not None:
            self.part_number = part_number
        if origin_country_code is not None:
            self.origin_country_code = origin_country_code
        if joint_production_indicator is not None:
            self.joint_production_indicator = joint_production_indicator
        if net_cost_code is not None:
            self.net_cost_code = net_cost_code
        if net_cost_date_range is not None:
            self.net_cost_date_range = self._define_object(
                net_cost_date_range, ProductNetCostDateRange
            )
        if preference_criteria is not None:
            self.preference_criteria = preference_criteria
        if producer_info is not None:
            self.producer_info = producer_info
        if marks_and_numbers is not None:
            self.marks_and_numbers = marks_and_numbers
        if number_of_packages_per_commodity is not None:
            self.number_of_packages_per_commodity = number_of_packages_per_commodity
        if product_weight is not None:
            self.product_weight = self._define_object(
                product_weight, ProductProductWeight
            )
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id
        if schedule_b is not None:
            self.schedule_b = self._define_object(schedule_b, ProductScheduleB)
        if export_type is not None:
            self.export_type = export_type
        if sed_total_value is not None:
            self.sed_total_value = sed_total_value
        if exclude_from_form is not None:
            self.exclude_from_form = self._define_object(
                exclude_from_form, ProductExcludeFromForm
            )
        if packing_list_info is not None:
            self.packing_list_info = self._define_object(
                packing_list_info, ProductPackingListInfo
            )
        if eei_information is not None:
            self.eei_information = self._define_object(
                eei_information, ProductEeiInformation
            )