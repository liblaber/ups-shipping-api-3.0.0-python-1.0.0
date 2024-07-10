# UltimateConsigneeAddress

Address information of the Ultimate consignee. Applicable for EEI form only.

**Properties**

| Name                | Type      | Required | Description                                                                                                                                                                                 |
| :------------------ | :-------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| address_line        | List[str] | ✅       | Address line of the Ultimate consignee. Applicable for EEI form only.                                                                                                                       |
| city                | str       | ✅       | City of the Ultimate consignee. Applicable for EEI form only.                                                                                                                               |
| country_code        | str       | ✅       | Country or Territory code of the Ultimate consignee. Applicable for EEI form only.                                                                                                          |
| state_province_code | str       | ❌       | State of the Ultimate consignee. Applicable for EEI form only. Required for certain countries or territories. The length of the postal code depends on the country or territory code        |
| town                | str       | ❌       | Town of the Ultimate consignee. Applicable for EEI form only.                                                                                                                               |
| postal_code         | str       | ❌       | Postal code of the Ultimate consignee. Applicable for EEI form only. Required for certain countries or territories. The length of the postal code depends on the country or territory code. |

<!-- This file was generated by liblab | https://liblab.com/ -->