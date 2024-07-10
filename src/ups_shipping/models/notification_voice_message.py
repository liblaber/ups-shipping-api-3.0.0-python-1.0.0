# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"phone_number": "PhoneNumber"})
class NotificationVoiceMessage(BaseModel):
    """VoiceMessage container is used for specifying phone number for receiving voice Alternate Delivery Location notification and UAP Shipper notification.  Valid only for Alternate Delivery Location notification and UAP Shipper notification. VoiceMessage phone number or TextMessage phone number or email address is required for ADL notification and UAP Shipper notification.

    :param phone_number: Phone number for receiving Voice Alternate Delivery Location notification and UAP Shipper notification.
    :type phone_number: str
    """

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
