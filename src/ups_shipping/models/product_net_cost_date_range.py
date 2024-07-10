# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"begin_date": "BeginDate", "end_date": "EndDate"})
class ProductNetCostDateRange(BaseModel):
    """Date Range for regional value content (RVC).  Applies to NAFTA CO only.

    :param begin_date: If the RVC is calculated over a period of time, it should be identified by the begin date (yyyyMMdd) of that period. (Reference: Articles 402.1, 402.5).  Applies to NAFTA CO only. Format is yyyyMMdd.
    :type begin_date: str
    :param end_date: If the RVC is calculated over a period of time, it should be identified by the End date (yyyyMMdd) of that period. (Reference: Articles 402.1, 402.5).  Applies to NAFTA CO only. Format is yyyyMMdd.
    :type end_date: str
    """

    def __init__(self, begin_date: str, end_date: str):
        self.begin_date = begin_date
        self.end_date = end_date
