# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "e_mail_address": "EMailAddress",
        "undeliverable_e_mail_address": "UndeliverableEMailAddress",
    }
)
class PreAlertNotificationEMailMessage(BaseModel):
    """This container is used for Populating EMailMessage details for PreAlertNotification.

    :param e_mail_address: EMailAddress where PreAlertNotification is sent.
    :type e_mail_address: str
    :param undeliverable_e_mail_address: This is used for notification when EMailAddress for PreAlertNotification is undeliverable., defaults to None
    :type undeliverable_e_mail_address: str, optional
    """

    def __init__(self, e_mail_address: str, undeliverable_e_mail_address: str = None):
        self.e_mail_address = e_mail_address
        if undeliverable_e_mail_address is not None:
            self.undeliverable_e_mail_address = undeliverable_e_mail_address
