# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .freight_shipment_information_freight_density_info import (
    FreightShipmentInformationFreightDensityInfo,
)


@JsonMap(
    {
        "freight_density_info": "FreightDensityInfo",
        "density_eligible_indicator": "DensityEligibleIndicator",
    }
)
class ShipmentFreightShipmentInformation(BaseModel):
    """Container to hold Freight Shipment information.

    :param freight_density_info: Freight Density Info container.  Required if DensityEligibleIndicator is present., defaults to None
    :type freight_density_info: FreightShipmentInformationFreightDensityInfo, optional
    :param density_eligible_indicator: The presence of the tag indicates that the rate request is density based. For Density Based Rating (DBR), the customer must have DBR Contract Service., defaults to None
    :type density_eligible_indicator: str, optional
    """

    def __init__(
        self,
        freight_density_info: FreightShipmentInformationFreightDensityInfo = None,
        density_eligible_indicator: str = None,
    ):
        if freight_density_info is not None:
            self.freight_density_info = self._define_object(
                freight_density_info, FreightShipmentInformationFreightDensityInfo
            )
        if density_eligible_indicator is not None:
            self.density_eligible_indicator = density_eligible_indicator
