# ShipmentReferenceNumber

Reference Number information container.

**Properties**

| Name               | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| :----------------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| value              | str  | ✅       | Customer supplied reference number. Valid if the origin/destination pair is not US/US or PR/PR                                                                                                                                                                                                                                                                                                    |
| bar_code_indicator | str  | ❌       | If the indicator is present then the reference number's value will be bar coded on the label. This is an empty tag, any value inside is ignored. Only one shipment-level or package-level reference number can be bar coded per shipment. In order to barcode a reference number, its value must be no longer than 14 alphanumeric characters or 24 numeric characters and cannot contain spaces. |
| code               | str  | ❌       | Shipment Reference number type code. The code specifies the Reference name. Refer to the Reference Number Code table. Valid if the origin/destination pair is not US/US or PR/PR and character should be alpha-numeric.                                                                                                                                                                           |

<!-- This file was generated by liblab | https://liblab.com/ -->