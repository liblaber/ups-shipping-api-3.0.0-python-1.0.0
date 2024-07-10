# PackageServiceOptionsDeclaredValue

Container for Declared Value.

**Properties**

| Name           | Type              | Required | Description                                                                                                                                                                                        |
| :------------- | :---------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| currency_code  | str               | ✅       | Declared value amount currency type. Defaults to the non-Euro currency used in the shippers country or territory. Code must represent a currency that is a valid for Shipper country or territory. |
| monetary_value | str               | ✅       | Declared value amount.                                                                                                                                                                             |
| type\_         | DeclaredValueType | ❌       | Container for Declared Value Type.                                                                                                                                                                 |

<!-- This file was generated by liblab | https://liblab.com/ -->