# ShipmentShipmentIndicationType

Container for Shipment Indication Type. Required to indicate whether shipment is "Hold For Pickup At UPS Access Point" for use by approved shippers to identify a UPS Access Point location as an alternate delivery option during shipment preparation or "UPS Access Pointâ„¢ Delivery", ship parcels directly to a UPS Access Point location for collection by the receiver.

**Properties**

| Name        | Type | Required | Description                                                                                                                                                                                                                                                               |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| code        | str  | ✅       | Valid values: - '01' - Hold for Pickup at UPS Access Point aka Direct to Retail (D2R) - '02' - UPS Access Pointâ„¢ Delivery aka Retail to Retail (R2R) If '01' code is present indicates shipment will be send to Retail location where it is held to consignee to claim. |
| description | str  | ❌       | Description for the code.                                                                                                                                                                                                                                                 |

<!-- This file was generated by liblab | https://liblab.com/ -->
