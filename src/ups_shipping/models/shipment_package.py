# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .package_packaging import PackagePackaging
from .package_dimensions import PackageDimensions
from .package_dim_weight import PackageDimWeight
from .package_package_weight import PackagePackageWeight
from .package_reference_number import PackageReferenceNumber
from .package_simple_rate import PackageSimpleRate
from .package_ups_premier import PackageUpsPremier
from .package_package_service_options import PackagePackageServiceOptions
from .package_commodity import PackageCommodity
from .package_haz_mat_package_information import PackageHazMatPackageInformation


@JsonMap(
    {
        "description": "Description",
        "pallet_description": "PalletDescription",
        "num_of_pieces": "NumOfPieces",
        "unit_price": "UnitPrice",
        "packaging": "Packaging",
        "dimensions": "Dimensions",
        "dim_weight": "DimWeight",
        "package_weight": "PackageWeight",
        "large_package_indicator": "LargePackageIndicator",
        "oversize_indicator": "OversizeIndicator",
        "minimum_billable_weight_indicator": "MinimumBillableWeightIndicator",
        "reference_number": "ReferenceNumber",
        "additional_handling_indicator": "AdditionalHandlingIndicator",
        "simple_rate": "SimpleRate",
        "ups_premier": "UPSPremier",
        "package_service_options": "PackageServiceOptions",
        "commodity": "Commodity",
        "haz_mat_package_information": "HazMatPackageInformation",
    }
)
class ShipmentPackage(BaseModel):
    """Package Information container.  For Return Shipments up to and including 20 packages are allowed. US/PR origin return movements are limited to only one package. For Mail Innovations and Simple Rate shipments only one package is allowed.

    :param description: Merchandise description of package.  Required for shipment with return service., defaults to None
    :type description: str, optional
    :param pallet_description: Description of articles & special marks. Applicable for Air Freight only, defaults to None
    :type pallet_description: str, optional
    :param num_of_pieces: Number of Pieces. Applicable for Air Freight only, defaults to None
    :type num_of_pieces: str, optional
    :param unit_price: Unit price of the commodity. Applicable for Air Freight only  Limit to 2 digit after the decimal. The maximum length of the field is 12 including '.' and can hold up to 2 decimal place. (e.g. 999999999.99), defaults to None
    :type unit_price: str, optional
    :param packaging: Packaging container.  Container for Packaging Type.
    :type packaging: PackagePackaging
    :param dimensions: Dimensions information container. Note: Currently dimensions are not applicable to Ground Freight Pricing.  Length + 2*(Width + Height) must be less than or equal to 165 IN or 330 CM. Required for Heavy Goods service. Package Dimension will be ignored for Simple Rate, defaults to None
    :type dimensions: PackageDimensions, optional
    :param dim_weight: Dimensional weight of shipment. Please visit ups.com for rules on calculating. There is one implied decimal place (e.g. 115 = 11.5).  If dimensions are provided, dimensional weight is ignored. For US/PR/CA shipments, dimensional weight is ignored, defaults to None
    :type dim_weight: PackageDimWeight, optional
    :param package_weight: Container to hold package weight information.  Package weight is a required for Ground Freight Pricing shipments and Heavy Goods service. Package Weight will be ignored for Simple Rate., defaults to None
    :type package_weight: PackagePackageWeight, optional
    :param large_package_indicator: Presence of the indicator mentions that the package is Large Package. This is an empty tag, any value inside is ignored., defaults to None
    :type large_package_indicator: str, optional
    :param oversize_indicator: Presence/Absence Indicator. Any value is ignored. If present, indicates that the package is over size.   Applicable for UPS Worldwide Economy DDU service., defaults to None
    :type oversize_indicator: str, optional
    :param minimum_billable_weight_indicator: Presence/Absence Indicator. Any value is ignored. If present, indicates that the package is qualified for minimum billable weight.   Applicable for UPS Worldwide Economy DDU service., defaults to None
    :type minimum_billable_weight_indicator: str, optional
    :param reference_number: reference_number, defaults to None
    :type reference_number: List[PackageReferenceNumber], optional
    :param additional_handling_indicator: Additional Handling Required. The presence indicates additional handling is required, the absence indicates no additional handling is required. Additional Handling indicator indicates it's a non-corrugated package., defaults to None
    :type additional_handling_indicator: str, optional
    :param simple_rate: SimpleRate Container, defaults to None
    :type simple_rate: PackageSimpleRate, optional
    :param ups_premier: UPS Premier Container., defaults to None
    :type ups_premier: PackageUpsPremier, optional
    :param package_service_options: Package Service Options container., defaults to None
    :type package_service_options: PackagePackageServiceOptions, optional
    :param commodity: Container to hold the Commodity information.  It is required if the Ground Freight Pricing Shipment indicator is present in the request., defaults to None
    :type commodity: PackageCommodity, optional
    :param haz_mat_package_information: Required when number of hazmat containers in a package is greater than 1. It indicates whether all the hazmat materials are kept in a single box or multiple boxes.  Required when number of hazmat container in a package is greater than 1., defaults to None
    :type haz_mat_package_information: PackageHazMatPackageInformation, optional
    """

    def __init__(
        self,
        packaging: PackagePackaging,
        description: str = None,
        pallet_description: str = None,
        num_of_pieces: str = None,
        unit_price: str = None,
        dimensions: PackageDimensions = None,
        dim_weight: PackageDimWeight = None,
        package_weight: PackagePackageWeight = None,
        large_package_indicator: str = None,
        oversize_indicator: str = None,
        minimum_billable_weight_indicator: str = None,
        reference_number: List[PackageReferenceNumber] = None,
        additional_handling_indicator: str = None,
        simple_rate: PackageSimpleRate = None,
        ups_premier: PackageUpsPremier = None,
        package_service_options: PackagePackageServiceOptions = None,
        commodity: PackageCommodity = None,
        haz_mat_package_information: PackageHazMatPackageInformation = None,
    ):
        if description is not None:
            self.description = description
        if pallet_description is not None:
            self.pallet_description = pallet_description
        if num_of_pieces is not None:
            self.num_of_pieces = num_of_pieces
        if unit_price is not None:
            self.unit_price = unit_price
        self.packaging = self._define_object(packaging, PackagePackaging)
        if dimensions is not None:
            self.dimensions = self._define_object(dimensions, PackageDimensions)
        if dim_weight is not None:
            self.dim_weight = self._define_object(dim_weight, PackageDimWeight)
        if package_weight is not None:
            self.package_weight = self._define_object(
                package_weight, PackagePackageWeight
            )
        if large_package_indicator is not None:
            self.large_package_indicator = large_package_indicator
        if oversize_indicator is not None:
            self.oversize_indicator = oversize_indicator
        if minimum_billable_weight_indicator is not None:
            self.minimum_billable_weight_indicator = minimum_billable_weight_indicator
        if reference_number is not None:
            self.reference_number = self._define_list(
                reference_number, PackageReferenceNumber
            )
        if additional_handling_indicator is not None:
            self.additional_handling_indicator = additional_handling_indicator
        if simple_rate is not None:
            self.simple_rate = self._define_object(simple_rate, PackageSimpleRate)
        if ups_premier is not None:
            self.ups_premier = self._define_object(ups_premier, PackageUpsPremier)
        if package_service_options is not None:
            self.package_service_options = self._define_object(
                package_service_options, PackagePackageServiceOptions
            )
        if commodity is not None:
            self.commodity = self._define_object(commodity, PackageCommodity)
        if haz_mat_package_information is not None:
            self.haz_mat_package_information = self._define_object(
                haz_mat_package_information, PackageHazMatPackageInformation
            )
