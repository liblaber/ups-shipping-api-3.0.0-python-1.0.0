# PackageCommodity

Container to hold the Commodity information. It is required if the Ground Freight Pricing Shipment indicator is present in the request.

**Properties**

| Name          | Type          | Required | Description                                                                                                                                      |
| :------------ | :------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| freight_class | str           | ✅       | Freight Classification. Freight class partially determines the freight rate for the article. Required for Ground Freight Pricing Shipments only. |
| nmfc          | CommodityNmfc | ❌       | Container to hold the NMFC codes.                                                                                                                |

<!-- This file was generated by liblab | https://liblab.com/ -->