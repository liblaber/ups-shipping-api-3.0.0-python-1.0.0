# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dry_ice_dry_ice_weight import DryIceDryIceWeight


@JsonMap(
    {
        "regulation_set": "RegulationSet",
        "dry_ice_weight": "DryIceWeight",
        "medical_use_indicator": "MedicalUseIndicator",
    }
)
class PackageServiceOptionsDryIce(BaseModel):
    """Container for Dry Ice.  Maximum 1 Dry Ice is allowed. Lane check will happen based on postal code/ city.

    :param regulation_set: Regulation set for dryIce Shipment. Valid values: CFR = HazMat regulated by US Dept. of Transportation within the U.S. or ground shipments to Canada, IATA= Worldwide Air movement.  The following values are valid: IATA, CFR.
    :type regulation_set: str
    :param dry_ice_weight: Container for Dry Ice weight.
    :type dry_ice_weight: DryIceDryIceWeight
    :param medical_use_indicator: Presence/Absence Indicator. Any value inside is ignored. Relevant only in CFR regulation set. If present it is used to designate the dry Ice is for any medical use and rates are adjusted for DryIce weight more than 2.5 Kgs or 5.7 Lbs., defaults to None
    :type medical_use_indicator: str, optional
    """

    def __init__(
        self,
        regulation_set: str,
        dry_ice_weight: DryIceDryIceWeight,
        medical_use_indicator: str = None,
    ):
        self.regulation_set = regulation_set
        self.dry_ice_weight = self._define_object(dry_ice_weight, DryIceDryIceWeight)
        if medical_use_indicator is not None:
            self.medical_use_indicator = medical_use_indicator
