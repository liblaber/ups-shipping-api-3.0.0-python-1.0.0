# LabelRecoveryRequestReferenceValues

Container that holds reference number and shipper number If tracking number is not present use reference Number

**Properties**

| Name             | Type                           | Required | Description                                                                                                                                                                          |
| :--------------- | :----------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| reference_number | ReferenceValuesReferenceNumber | ✅       | Container for reference number                                                                                                                                                       |
| shipper_number   | str                            | ✅       | Required if ReferenceNumber/Value is populated. Shipper's six digit account number. Must be six alphanumeric characters. Must be associated with the Internet account used to login. |

<!-- This file was generated by liblab | https://liblab.com/ -->