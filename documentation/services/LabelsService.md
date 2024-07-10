# LabelsService

A list of all methods in the `LabelsService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                                             |
| :-------------------------------- | :---------------------------------------------------------------------- |
| [label_recovery](#label_recovery) | The Label Shipping API allows us to retrieve forward and return labels. |

## label_recovery

The Label Shipping API allows us to retrieve forward and return labels.

- HTTP Method: `POST`
- Endpoint: `/labels/{version}/recovery`

**Parameters**

| Name            | Type                                                                    | Required | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| :-------------- | :---------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body    | [LabelrecoveryRequestWrapper](../models/LabelrecoveryRequestWrapper.md) | ✅       | The request body.                                                                                                                                                                                                                                                                                                                                                                                        |
| version         | str                                                                     | ✅       | When UPS introduces new elements in the response that are not associated with new request elements, Subversion is used. This ensures backward compatibility. v1 original features of the application. No support for CODTurn-inPage, HighValueReport or InternationalForms features returned in the response v1701 includes support for CODTurn-inPage features returned in the response. V1903 Length 5 |
| trans_id        | str                                                                     | ❌       | An identifier unique to the request. Length 32                                                                                                                                                                                                                                                                                                                                                           |
| transaction_src | str                                                                     | ❌       | An identifier of the client/source application that is making the request.Length 512                                                                                                                                                                                                                                                                                                                     |

**Return Type**

`LabelrecoveryResponseWrapper`

**Example Usage Code Snippet**

```python
from ups_shipping import UpsShipping, Environment
from ups_shipping.models import LabelrecoveryRequestWrapper

sdk = UpsShipping(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = LabelrecoveryRequestWrapper(
    label_recovery_request={
        "request": {
            "sub_version": "SubVersion",
            "request_option": "RequestOption",
            "transaction_reference": {
                "customer_context": "cupidatat in"
            }
        },
        "label_specification": {
            "http_user_agent": "ex officia",
            "label_image_format": {
                "code": "cons",
                "description": "ut"
            },
            "label_stock_size": {
                "height": "u",
                "width": "d"
            }
        },
        "translate": {
            "language_code": "tem",
            "dialect_code": "co",
            "code": "in"
        },
        "label_delivery": {
            "label_link_indicator": "LabelLinkIndicator",
            "resend_e_mail_indicator": "ResendEMailIndicator"
        },
        "tracking_number": "t",
        "mail_innovations_tracking_number": "Ut anim Excepteur incidi",
        "reference_values": {
            "reference_number": {
                "value": "amet"
            },
            "shipper_number": "doin v"
        },
        "locale": "magna",
        "ups_premium_care_form": {
            "page_size": "no",
            "print_type": "se"
        }
    }
)

result = sdk.labels.label_recovery(
    request_body=request_body,
    version="v1",
    trans_id="transId",
    transaction_src="testing"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
