# LabelResultsReceipt

Container for the HTML receipt and the receipt link.

**Properties**

| Name       | Type         | Required | Description                                                                                                                    |
| :--------- | :----------- | :------- | :----------------------------------------------------------------------------------------------------------------------------- |
| html_image | str          | ❌       | Base 64 encoded html browser image.                                                                                            |
| image      | ReceiptImage | ❌       | Container for the receipt in the format other than HTML.                                                                       |
| url        | str          | ❌       | Receipt's url Applicable for following types of shipments: Print/Electronic Return Label Print/Electronic Import Control Label |

<!-- This file was generated by liblab | https://liblab.com/ -->