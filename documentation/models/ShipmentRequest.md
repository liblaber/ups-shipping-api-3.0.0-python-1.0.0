# ShipmentRequest

Shipment Request.

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                      |
| :-------------------- | :---------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request               | ShipmentRequestRequest              | ✅       | Request Container                                                                                                                                                                                                                                                                                                                |
| shipment              | ShipmentRequestShipment             | ✅       | Shipment Container                                                                                                                                                                                                                                                                                                               |
| label_specification   | ShipmentRequestLabelSpecification   | ❌       | Container used to define the properties required by the user to print and/or display the UPS shipping label. Required for shipment without return service or shipments with PRL return service. Required for Electronic Return Label or Electronic Import Control Label shipments with SubVersion greater than or equal to 1707. |
| receipt_specification | ShipmentRequestReceiptSpecification | ❌       | Container used to allow the user to choose to print a thermal receipt.                                                                                                                                                                                                                                                           |

<!-- This file was generated by liblab | https://liblab.com/ -->