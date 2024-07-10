# ContactsSoldTo

SoldTo Container. The Sold To party's country code must be the same as the Ship To party's country code with the exception of Canada and satellite countries. Applies to Invoice and NAFTA CO Forms. Required if Invoice or NAFTA CO (International Form) is requested.

**Properties**

| Name                      | Type          | Required | Description                                                                                                                                                                                                |
| :------------------------ | :------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                      | str           | ✅       | Company Name.                                                                                                                                                                                              |
| attention_name            | str           | ✅       | Sold to contact name.                                                                                                                                                                                      |
| address                   | SoldToAddress | ✅       | Sold To Address Container. Applies to NAFTA CO.                                                                                                                                                            |
| tax_identification_number | str           | ❌       | SoldTo Tax Identification Number.                                                                                                                                                                          |
| phone                     | SoldToPhone   | ❌       | Phone Container.                                                                                                                                                                                           |
| option                    | str           | ❌       | The text associated with the code will be printed in the sold to section of the NAFTA CO form. The values indicate the following: 01 â€“ Unknown. Applies to NAFTA CO form. Possible Values are 01 and 02. |
| e_mail_address            | str           | ❌       | SoldTo email address.                                                                                                                                                                                      |
| account_number            | str           | ❌       | SoldTo AccountNumber                                                                                                                                                                                       |

<!-- This file was generated by liblab | https://liblab.com/ -->