# PackingListInfoPackageAssociated

Data Container holding package/product related information that will break up the product into each package on the packing list. Total product amount must equal the product unit value above. Required for packaging list and Air Freight Packing list. Packaging list max allowed : 20
Air Freight Packaging list max allowed: 200

**Properties**

| Name           | Type | Required | Description                                                                                                                      |
| :------------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------- |
| package_number | str  | ✅       | Package number the product should be allocated to ont he packing list. Required for packaging list and Air Freight Packing list. |
| product_amount | str  | ✅       | Amount of Product associated with a package. Required for packaging list and Air Freight Packing list.                           |
| product_note   | str  | ❌       | Product Note.                                                                                                                    |

<!-- This file was generated by liblab | https://liblab.com/ -->