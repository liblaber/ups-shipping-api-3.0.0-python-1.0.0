# VoidShipmentResponse

Void Response Container.

**Properties**

| Name                 | Type                                         | Required | Description                                                                                                                                                                                                                                                                    |
| :------------------- | :------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| response             | VoidShipmentResponseResponse                 | ✅       | Response Container.                                                                                                                                                                                                                                                            |
| summary_result       | VoidShipmentResponseSummaryResult            | ✅       | Container for the Summary Result                                                                                                                                                                                                                                               |
| package_level_result | List[VoidShipmentResponsePackageLevelResult] | ❌       | Contains the Package Level Results. **NOTE:** For versions >= v2403, this element will always be returned as an array. For requests using versions < v2403, this element will be returned as an array if there is more than one object and a single object if there is only 1. |

<!-- This file was generated by liblab | https://liblab.com/ -->
