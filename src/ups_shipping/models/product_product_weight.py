# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .product_weight_unit_of_measurement import ProductWeightUnitOfMeasurement


@JsonMap({"unit_of_measurement": "UnitOfMeasurement", "weight": "Weight"})
class ProductProductWeight(BaseModel):
    """The shipping weight, including containers, for each commodity with a separate Harmonized Tariff Code / Schedule B Number. This weight does not include carrier equipment.  Applies to CO and EEI forms only. Required for CO and EEI forms.

    :param unit_of_measurement: Container tag for the Unit of Measurement of weight.  Applies to CO and EEI forms only.
    :type unit_of_measurement: ProductWeightUnitOfMeasurement
    :param weight: Weight of Product.  Applies to CO and EEI forms only. Valid characters are 0-9 and '.' (Decimal point). Limit to 1 digit after the decimal. The maximum length of the field is 5 including '.' and can hold up to 1 decimal place.
    :type weight: str
    """

    def __init__(
        self, unit_of_measurement: ProductWeightUnitOfMeasurement, weight: str
    ):
        self.unit_of_measurement = self._define_object(
            unit_of_measurement, ProductWeightUnitOfMeasurement
        )
        self.weight = weight
