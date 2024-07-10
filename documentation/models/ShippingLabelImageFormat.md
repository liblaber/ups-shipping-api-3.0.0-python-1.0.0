# ShippingLabelImageFormat

The container image format.

**Properties**

| Name        | Type | Required | Description                                                                                                                                                                                                                                                                                                           |
| :---------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code        | str  | ✅       | Label image code that the labels are generated. Valid values: EPL = EPL2 SPL = SPL ZPL = ZPL GIF = gif images PNG = PNG images. Only EPL, SPL, ZPL and GIF are currently supported. For multi piece COD shipments, the label image format for the first package will always be a GIF for any form of label requested. |
| description | str  | ❌       | Description of the image format.                                                                                                                                                                                                                                                                                      |

<!-- This file was generated by liblab | https://liblab.com/ -->