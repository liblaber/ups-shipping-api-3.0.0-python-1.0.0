# PackageResultsShippingLabel

The container for UPS shipping label. Returned for following shipments -
Forward shipments,
Shipments with PRL returns service,
Electronic Return Label or Electronic Import Control Label shipments with SubVersion greater than or equal to 1707. Shipping label wont be returned if BarCodeImageIndicator is present.

**Properties**

| Name                                  | Type                     | Required | Description                                                                                                                                                                                                                                                                                                                                                                 |
| :------------------------------------ | :----------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| image_format                          | ShippingLabelImageFormat | ✅       | The container image format.                                                                                                                                                                                                                                                                                                                                                 |
| graphic_image                         | str                      | ✅       | Base 64 encoded graphic image.                                                                                                                                                                                                                                                                                                                                              |
| graphic_image_part                    | List[str]                | ❌       | Base 64 encoded graphic image. Applicable only for Mail Innovations CN22 Combination Forward Label with more than 3 commodities. **NOTE:** For versions >= v2403, this element will always be returned as an array. For requests using versions < v2403, this element will be returned as an array if there is more than one object and a single object if there is only 1. |
| international_signature_graphic_image | str                      | ❌       | Base 64 encoded graphic image of the Warsaw text and signature box. EPL2, ZPL and SPL labels. The image will be returned for non-US based shipments. One image will be given per shipment and it will be in the first PackageResults container.                                                                                                                             |
| html_image                            | str                      | ❌       | Base 64 encoded html browser image rendering software. This is only returned for gif and png image formats.                                                                                                                                                                                                                                                                 |
| pdf417                                | str                      | ❌       | PDF-417 is a two-dimensional barcode, which can store up to about 1,800 printable ASCII characters or 1,100 binary characters per symbol. The symbol is rectangular. The image is Base 64 encoded and returned if the LabelImageFormat code is GIF. Shipment with PRL return service only.                                                                                  |

<!-- This file was generated by liblab | https://liblab.com/ -->