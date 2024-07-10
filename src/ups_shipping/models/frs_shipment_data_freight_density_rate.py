# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"density": "Density", "total_cubic_feet": "TotalCubicFeet"})
class FrsShipmentDataFreightDensityRate(BaseModel):
    """FreightDensityRate container for Density based rating.

    :param density: Density is returned if the Shipper is eligible for Density based rate.   Valid values are 0 to 999.9
    :type density: str
    :param total_cubic_feet: Total Cubic feet is returned if the Shipper is eligible for Density based rate.   Valid values are 0 to 99999.999
    :type total_cubic_feet: str
    """

    def __init__(self, density: str, total_cubic_feet: str):
        self.density = density
        self.total_cubic_feet = total_cubic_feet
