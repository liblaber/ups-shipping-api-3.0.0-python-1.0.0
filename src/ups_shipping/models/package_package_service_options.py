# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .package_service_options_delivery_confirmation import (
    PackageServiceOptionsDeliveryConfirmation,
)
from .package_service_options_declared_value import PackageServiceOptionsDeclaredValue
from .package_service_options_cod import PackageServiceOptionsCod
from .package_service_options_access_point_cod import (
    PackageServiceOptionsAccessPointCod,
)
from .package_service_options_notification import PackageServiceOptionsNotification
from .package_service_options_haz_mat import PackageServiceOptionsHazMat
from .package_service_options_dry_ice import PackageServiceOptionsDryIce


@JsonMap(
    {
        "delivery_confirmation": "DeliveryConfirmation",
        "declared_value": "DeclaredValue",
        "cod": "COD",
        "access_point_cod": "AccessPointCOD",
        "shipper_release_indicator": "ShipperReleaseIndicator",
        "notification": "Notification",
        "haz_mat": "HazMat",
        "dry_ice": "DryIce",
        "ups_premium_care_indicator": "UPSPremiumCareIndicator",
        "proactive_indicator": "ProactiveIndicator",
        "package_identifier": "PackageIdentifier",
        "clinical_trials_id": "ClinicalTrialsID",
        "refrigeration_indicator": "RefrigerationIndicator",
    }
)
class PackagePackageServiceOptions(BaseModel):
    """Package Service Options container.

    :param delivery_confirmation: Delivery Confirmation container.  Refer to Delivery Confirmation Origin- Destination Pairs in the Appendix for a list of valid values.  Valid only for forward shipment only., defaults to None
    :type delivery_confirmation: PackageServiceOptionsDeliveryConfirmation, optional
    :param declared_value: Container for Declared Value., defaults to None
    :type declared_value: PackageServiceOptionsDeclaredValue, optional
    :param cod: Container for COD.  Indicates COD is requested. Package level COD is available for shipment without return service from US/PR to US/PR, CA to CA, and CA to US. CA to US COD is not allowed for package Letter/ Envelope. COD is not valid for return service movements., defaults to None
    :type cod: PackageServiceOptionsCod, optional
    :param access_point_cod: Access Point COD indicates Package COD is requested for a shipment.  Valid only for "01 - Hold For Pickup At UPS Access Point" Shipment Indication type. Package Access Point COD is valid only for shipment without return service from US/PR to US/PR and CA to CA. Not valid with COD at package level., defaults to None
    :type access_point_cod: PackageServiceOptionsAccessPointCod, optional
    :param shipper_release_indicator: The presence indicates that the package may be released by driver without a signature from the consignee.  Empty Tag. Only available for US50/PR to US50/PR packages without return service., defaults to None
    :type shipper_release_indicator: str, optional
    :param notification: Receiver Return Notification.  Applicable for Shipment with returned service., defaults to None
    :type notification: PackageServiceOptionsNotification, optional
    :param haz_mat: haz_mat, defaults to None
    :type haz_mat: List[PackageServiceOptionsHazMat], optional
    :param dry_ice: Container for Dry Ice.  Maximum 1 Dry Ice is allowed. Lane check will happen based on postal code/ city., defaults to None
    :type dry_ice: PackageServiceOptionsDryIce, optional
    :param ups_premium_care_indicator: An UPSPremiumCareIndicator indicates special handling is required for shipment having controlled substances. Empty Tag means indicator is present. The UPSPremiumCareIndicator cannot be requested for package with Delivery Confirmation - Adult Signature Required and Delivery Confirmation- Signature Required. UPSPremiumCareIndicator is valid for following Return services: - Returns Exchange (available with a contract) - Print Return Label - Print and Mail - Electronic Return Label - Return Service Three Attempt The UPSPremiumCareIndicator can be requested with following UPS services: - UPS ExpressÂ® Early - UPS Express - UPS Express Saver - UPS Standard - Valid only for Canada to Canada movements. , defaults to None
    :type ups_premium_care_indicator: str, optional
    :param proactive_indicator: Presence/Absence Indicator. Any value is ignored. If present, the package is rated for UPS Proactive Response and proactive package tracking. Contractual accessorial for health care companies to allow package monitoring throughout the UPS system.  Shippers account needs to have valid contract for UPS Proactive Reponse., defaults to None
    :type proactive_indicator: str, optional
    :param package_identifier: Identifies the package containing Dangerous Goods.  Required for Hazmat shipment if SubVersion is greater than or equal to 1701., defaults to None
    :type package_identifier: str, optional
    :param clinical_trials_id: Unique identifier for clinical trials, defaults to None
    :type clinical_trials_id: str, optional
    :param refrigeration_indicator: Presence/Absence Indicator. Any value is ignored. If present, indicates that the package contains an item that needs refrigeration.  Shippers account needs to have a valid contract for Refrigeration., defaults to None
    :type refrigeration_indicator: str, optional
    """

    def __init__(
        self,
        delivery_confirmation: PackageServiceOptionsDeliveryConfirmation = None,
        declared_value: PackageServiceOptionsDeclaredValue = None,
        cod: PackageServiceOptionsCod = None,
        access_point_cod: PackageServiceOptionsAccessPointCod = None,
        shipper_release_indicator: str = None,
        notification: PackageServiceOptionsNotification = None,
        haz_mat: List[PackageServiceOptionsHazMat] = None,
        dry_ice: PackageServiceOptionsDryIce = None,
        ups_premium_care_indicator: str = None,
        proactive_indicator: str = None,
        package_identifier: str = None,
        clinical_trials_id: str = None,
        refrigeration_indicator: str = None,
    ):
        if delivery_confirmation is not None:
            self.delivery_confirmation = self._define_object(
                delivery_confirmation, PackageServiceOptionsDeliveryConfirmation
            )
        if declared_value is not None:
            self.declared_value = self._define_object(
                declared_value, PackageServiceOptionsDeclaredValue
            )
        if cod is not None:
            self.cod = self._define_object(cod, PackageServiceOptionsCod)
        if access_point_cod is not None:
            self.access_point_cod = self._define_object(
                access_point_cod, PackageServiceOptionsAccessPointCod
            )
        if shipper_release_indicator is not None:
            self.shipper_release_indicator = shipper_release_indicator
        if notification is not None:
            self.notification = self._define_object(
                notification, PackageServiceOptionsNotification
            )
        if haz_mat is not None:
            self.haz_mat = self._define_list(haz_mat, PackageServiceOptionsHazMat)
        if dry_ice is not None:
            self.dry_ice = self._define_object(dry_ice, PackageServiceOptionsDryIce)
        if ups_premium_care_indicator is not None:
            self.ups_premium_care_indicator = ups_premium_care_indicator
        if proactive_indicator is not None:
            self.proactive_indicator = proactive_indicator
        if package_identifier is not None:
            self.package_identifier = package_identifier
        if clinical_trials_id is not None:
            self.clinical_trials_id = clinical_trials_id
        if refrigeration_indicator is not None:
            self.refrigeration_indicator = refrigeration_indicator
