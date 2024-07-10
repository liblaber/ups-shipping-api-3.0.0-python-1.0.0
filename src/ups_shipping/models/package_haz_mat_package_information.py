# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "all_packed_in_one_indicator": "AllPackedInOneIndicator",
        "over_packed_indicator": "OverPackedIndicator",
        "q_value": "QValue",
        "outer_packaging_type": "OuterPackagingType",
    }
)
class PackageHazMatPackageInformation(BaseModel):
    """Required when number of hazmat containers in a package is greater than 1. It indicates whether all the hazmat materials are kept in a single box or multiple boxes.  Required when number of hazmat container in a package is greater than 1.

    :param all_packed_in_one_indicator: Presence/Absence Indicator. Any value is ignored. Presence indicates if multiple, different hazmat/chemicals are contained within one box in a package  When number of Hazmat containers in a package is more than one, either AllPackedInOneIndicator or OverPackedIndicator is needed, defaults to None
    :type all_packed_in_one_indicator: str, optional
    :param over_packed_indicator: Presence/Absence Indicator. Any value is ignored. Presence indicates that one or more hazmat/chemicals are in separate boxes in a package.  When number of Hazmat containers in a package is more than one, either AllPackedInOneIndicator or OverPackedIndicator is needed, defaults to None
    :type over_packed_indicator: str, optional
    :param q_value: When a HazMat shipment specifies AllPackedInOneIndicator and the regulation set for that shipment is IATA, Ship API must require the shipment to specify a Q-Value with exactly one of the following values: 0.1; 0.2; 0.3; 0.4; 0.5; 0.6; 0.7; 0.8; 0.9; 1.0, defaults to None
    :type q_value: str, optional
    :param outer_packaging_type: This field is used for the Outer Hazmat packaging type.  Ex. FIBERBOARD BOX, WOOD(EN) BOX, PLASTIC JERRICAN, METAL BOX, STEEL DRUM, OTHER, PLASTIC BOX, PLASTIC DRUM, STYROFOAM BOX, CYLINDERS, ENVIROTAINER, PLYWOOD BOX, ALUMINUM DRUM, ALUMINUM CYLINDERS, PLASTIC PAIL, PLYWOOD DRUM, FIBER DRUM, STEEL JERRICAN, ALUMINUM JERRICAN, STEEL BOX, CARTON, ALUMINUM BOX, defaults to None
    :type outer_packaging_type: str, optional
    """

    def __init__(
        self,
        all_packed_in_one_indicator: str = None,
        over_packed_indicator: str = None,
        q_value: str = None,
        outer_packaging_type: str = None,
    ):
        if all_packed_in_one_indicator is not None:
            self.all_packed_in_one_indicator = all_packed_in_one_indicator
        if over_packed_indicator is not None:
            self.over_packed_indicator = over_packed_indicator
        if q_value is not None:
            self.q_value = q_value
        if outer_packaging_type is not None:
            self.outer_packaging_type = outer_packaging_type
