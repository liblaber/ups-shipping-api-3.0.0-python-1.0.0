# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .frs_shipment_data_transportation_charges import (
    FrsShipmentDataTransportationCharges,
)
from .frs_shipment_data_freight_density_rate import FrsShipmentDataFreightDensityRate
from .frs_shipment_data_handling_units import FrsShipmentDataHandlingUnits


@JsonMap(
    {
        "transportation_charges": "TransportationCharges",
        "freight_density_rate": "FreightDensityRate",
        "handling_units": "HandlingUnits",
    }
)
class ShipmentResultsFrsShipmentData(BaseModel):
    """Ground Freight Pricing Shipment data container. Ground Freight Pricing shipment data is only guaranteed to be returned for Ground Freight Pricing shipments only.

    :param transportation_charges: Transportation charges container. Ground Freight Pricing transportation charges. These are only returned for Ground Freight Pricing enabled shipper account number when the user includes the FRSShipmentIndicator in the request.
    :type transportation_charges: FrsShipmentDataTransportationCharges
    :param freight_density_rate: FreightDensityRate container for Density based rating., defaults to None
    :type freight_density_rate: FrsShipmentDataFreightDensityRate, optional
    :param handling_units: Handling Unit for Density based rating container. **NOTE:** For versions >= v2403, this element will always be returned as an array. For requests using versions < v2403, this element will be returned as an array if there is more than one object and a single object if there is only 1. , defaults to None
    :type handling_units: List[FrsShipmentDataHandlingUnits], optional
    """

    def __init__(
        self,
        transportation_charges: FrsShipmentDataTransportationCharges,
        freight_density_rate: FrsShipmentDataFreightDensityRate = None,
        handling_units: List[FrsShipmentDataHandlingUnits] = None,
    ):
        self.transportation_charges = self._define_object(
            transportation_charges, FrsShipmentDataTransportationCharges
        )
        if freight_density_rate is not None:
            self.freight_density_rate = self._define_object(
                freight_density_rate, FrsShipmentDataFreightDensityRate
            )
        if handling_units is not None:
            self.handling_units = self._define_list(
                handling_units, FrsShipmentDataHandlingUnits
            )