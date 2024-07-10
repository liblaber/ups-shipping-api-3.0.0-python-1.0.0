# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .contacts_forward_agent import ContactsForwardAgent
from .contacts_ultimate_consignee import ContactsUltimateConsignee
from .contacts_intermediate_consignee import ContactsIntermediateConsignee
from .contacts_producer import ContactsProducer
from .contacts_sold_to import ContactsSoldTo


@JsonMap(
    {
        "forward_agent": "ForwardAgent",
        "ultimate_consignee": "UltimateConsignee",
        "intermediate_consignee": "IntermediateConsignee",
        "producer": "Producer",
        "sold_to": "SoldTo",
    }
)
class InternationalFormsContacts(BaseModel):
    """Holds the contact information of various parties.  Applicable for EEI and NAFTA CO only. Required for NAFTA CO and EEI. Ultimate consignee contact information is required for EEI.  Producer contact information is required for NAFTA CO

    :param forward_agent: The forwarding agent is the company or person acting as agent in the trans-shipping of freight to the destination country or territory.  Applicable for EEI form only., defaults to None
    :type forward_agent: ContactsForwardAgent, optional
    :param ultimate_consignee: The ultimate consignee is the person or company who receives the goods for end-use or the person or company listed on the export license. This is the end-user of the goods.  Applicable for EEI form only., defaults to None
    :type ultimate_consignee: ContactsUltimateConsignee, optional
    :param intermediate_consignee: The intermediate consignee is the person or company in the importing country or territory that makes final delivery to the ultimate consignee.  Applicable for EEI form only., defaults to None
    :type intermediate_consignee: ContactsIntermediateConsignee, optional
    :param producer: Information of the producer. The NAFTA Certificate of Origin must be completed, signed, and dated by the exporter.  When the Certificate is completed by the producer for use by the exporter, it must be completed, signed, and dated by the producer. The date must be the date the Certificate was completed and signed.  Applies to NAFTA CO.  Required for NAFTA CO forms., defaults to None
    :type producer: ContactsProducer, optional
    :param sold_to: SoldTo Container. The Sold To party's country code must be the same as the Ship To party's country code with the exception of Canada and satellite countries.  Applies to Invoice and NAFTA CO Forms. Required if Invoice or NAFTA CO (International Form) is requested., defaults to None
    :type sold_to: ContactsSoldTo, optional
    """

    def __init__(
        self,
        forward_agent: ContactsForwardAgent = None,
        ultimate_consignee: ContactsUltimateConsignee = None,
        intermediate_consignee: ContactsIntermediateConsignee = None,
        producer: ContactsProducer = None,
        sold_to: ContactsSoldTo = None,
    ):
        if forward_agent is not None:
            self.forward_agent = self._define_object(
                forward_agent, ContactsForwardAgent
            )
        if ultimate_consignee is not None:
            self.ultimate_consignee = self._define_object(
                ultimate_consignee, ContactsUltimateConsignee
            )
        if intermediate_consignee is not None:
            self.intermediate_consignee = self._define_object(
                intermediate_consignee, ContactsIntermediateConsignee
            )
        if producer is not None:
            self.producer = self._define_object(producer, ContactsProducer)
        if sold_to is not None:
            self.sold_to = self._define_object(sold_to, ContactsSoldTo)