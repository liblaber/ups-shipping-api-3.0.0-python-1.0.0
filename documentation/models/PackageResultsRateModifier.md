# PackageResultsRateModifier

Container for returned Rate Modifier information. Applies only if SubVersion is 2205 or greater.

**Properties**

| Name          | Type | Required | Description                                                                                                              |
| :------------ | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------- |
| modifier_type | str  | ✅       | Rate Modifier Type. Example: "ORM". Applies only if SubVersion is 2205 or greater.                                       |
| modifier_desc | str  | ✅       | Rate Modifier Description. Example: "Origin Modifier". Applies only if SubVersion is 2205 or greater.                    |
| amount        | str  | ✅       | Amount. Example: "-1.00","0.25". It contains positive or negative values. Applies only if SubVersion is 2205 or greater. |

<!-- This file was generated by liblab | https://liblab.com/ -->