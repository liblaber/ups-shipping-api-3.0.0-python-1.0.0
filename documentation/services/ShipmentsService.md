# ShipmentsService

A list of all methods in the `ShipmentsService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description                                                                                                                |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------- |
| [shipment](#shipment)           | The Shipping API makes UPS shipping services available to client applications that communicate with UPS using the Internet |
| [void_shipment](#void_shipment) | The Void Shipping API is used to cancel the previously scheduled shipment                                                  |

## shipment

The Shipping API makes UPS shipping services available to client applications that communicate with UPS using the Internet

- HTTP Method: `POST`
- Endpoint: `/shipments/{version}/ship`

**Parameters**

| Name                        | Type                                                  | Required | Description                                                                                                              |
| :-------------------------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------- |
| request_body                | [ShipRequestWrapper](../models/ShipRequestWrapper.md) | ✅       | The request body.                                                                                                        |
| version                     | str                                                   | ✅       | Indicates Ship API to display the new release features in Ship API response based on Ship release. Valid values: - v2403 |
| additionaladdressvalidation | str                                                   | ❌       | Valid Values: city = validation will include city.Length 15                                                              |
| trans_id                    | str                                                   | ❌       | An identifier unique to the request. Length 32                                                                           |
| transaction_src             | str                                                   | ❌       | An identifier of the client/source application that is making the request.Length 512                                     |

**Return Type**

`ShipResponseWrapper`

**Example Usage Code Snippet**

```python
from ups_shipping import UpsShipping, Environment
from ups_shipping.models import ShipRequestWrapper

sdk = UpsShipping(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = ShipRequestWrapper(
    shipment_request={
        "request": {
            "request_option": "laborum culpa",
            "sub_version": "qui ",
            "transaction_reference": {
                "customer_context": "consequat cillum adipisicing proident"
            }
        },
        "shipment": {
            "description": "voluptate dolore ipsum culpa",
            "return_service": {
                "code": "c",
                "description": "amet deserunt occ"
            },
            "documents_only_indicator": "DocumentsOnlyIndicator",
            "shipper": {
                "name": "minim mollit eiusmod",
                "attention_name": "cupidatat mol",
                "company_displayable_name": "sunt anim cupida",
                "tax_identification_number": "ipsum",
                "phone": {
                    "number": "mo",
                    "extension": "comm"
                },
                "shipper_number": "incidi",
                "fax_number": "tem",
                "e_mail_address": "in",
                "address": {
                    "address_line": [
                        "AddressLine"
                    ],
                    "city": "dolore nisi voluptate la",
                    "state_province_code": "ul",
                    "postal_code": "reprehen",
                    "country_code": "qu"
                }
            },
            "ship_to": {
                "name": "dolor do offi",
                "attention_name": "veniam sunt dolore do",
                "company_displayable_name": "sit",
                "tax_identification_number": "eiusmod la",
                "phone": {
                    "number": "do E",
                    "extension": "s"
                },
                "fax_number": "enim repr",
                "e_mail_address": "exercitation Ut proident ea con",
                "address": {
                    "address_line": [
                        "AddressLine"
                    ],
                    "city": "magn",
                    "state_province_code": "mo",
                    "postal_code": "proiden",
                    "country_code": "es",
                    "residential_address_indicator": "ResidentialAddressIndicator"
                },
                "location_id": "cul"
            },
            "alternate_delivery_address": {
                "name": "dolor dolore in ipsum do",
                "attention_name": "et dolor quis mollit in",
                "ups_access_point_id": "officiasu",
                "address": {
                    "address_line": [
                        "AddressLine"
                    ],
                    "city": "est esse pariatur",
                    "state_province_code": "qu",
                    "postal_code": "quis ea ",
                    "country_code": "ip"
                }
            },
            "ship_from": {
                "name": "laboris voluptate exercitation anim",
                "attention_name": "amet dolore anim",
                "company_displayable_name": "qui c",
                "tax_identification_number": "veli",
                "tax_id_type": {
                    "code": "Code",
                    "description": "Description"
                },
                "phone": {
                    "number": "ull",
                    "extension": "Du"
                },
                "fax_number": "aliquip ex ea ",
                "address": {
                    "address_line": [
                        "AddressLine"
                    ],
                    "city": "u",
                    "state_province_code": "i",
                    "postal_code": "i",
                    "country_code": "ut"
                },
                "vendor_info": {
                    "vendor_collect_id_type_code": "am",
                    "vendor_collect_id_number": "commo",
                    "consignee_type": "ci"
                }
            },
            "payment_information": {
                "shipment_charge": [
                    {
                        "type_": "se",
                        "bill_shipper": {
                            "account_number": "nisiin",
                            "credit_card": {
                                "type_": "se",
                                "number": "id laboru",
                                "expiration_date": "ipsum ",
                                "security_code": "Exce",
                                "address": {
                                    "address_line": [
                                        "AddressLine"
                                    ],
                                    "city": "consectetur id",
                                    "state_province_code": "al",
                                    "postal_code": "ex fu",
                                    "country_code": "es"
                                }
                            },
                            "alternate_payment_method": "in"
                        },
                        "bill_receiver": {
                            "account_number": "proide",
                            "address": {
                                "postal_code": "vo"
                            }
                        },
                        "bill_third_party": {
                            "account_number": "velit ",
                            "certified_electronic_mail": "exercitation",
                            "interchange_system_code": "sit",
                            "address": {
                                "postal_code": "sunt eiu",
                                "country_code": "am"
                            }
                        },
                        "consignee_billed_indicator": "ConsigneeBilledIndicator"
                    }
                ],
                "split_duty_vat_indicator": "SplitDutyVATIndicator"
            },
            "frs_payment_information": {
                "type_": {
                    "code": "ci",
                    "description": "eiusmod laboris"
                },
                "account_number": "nulla ",
                "address": {
                    "postal_code": "o",
                    "country_code": "ex"
                }
            },
            "freight_shipment_information": {
                "freight_density_info": {
                    "adjusted_height_indicator": "AdjustedHeightIndicator",
                    "adjusted_height": {
                        "value": "elit",
                        "unit_of_measurement": {
                            "code": "ex",
                            "description": "fugiat"
                        }
                    },
                    "handling_units": [
                        {
                            "quantity": "pariatur",
                            "type_": {
                                "code": "inv",
                                "description": "nisi"
                            },
                            "dimensions": {
                                "unit_of_measurement": {
                                    "code": "al",
                                    "description": "sit commodo mollit ad"
                                },
                                "length": "e",
                                "width": "exercitation ",
                                "height": "ullamco "
                            }
                        }
                    ]
                },
                "density_eligible_indicator": "DensityEligibleIndicator"
            },
            "goods_not_in_free_circulation_indicator": "GoodsNotInFreeCirculationIndicator",
            "promotional_discount_information": {
                "promo_code": "do adipis",
                "promo_alias_code": "ut culpa mollitin ad"
            },
            "dg_signatory_info": {
                "name": "non estauteamet sedadipisicingad la",
                "title": "Duis ut eiusmod magna enimlaboris d",
                "place": "suntvoluptate nulla dolor exconsect",
                "date_": "id sint ",
                "shipper_declaration": "es",
                "upload_only_indicator": "UploadOnlyIndicator"
            },
            "shipment_rating_options": {
                "negotiated_rates_indicator": "NegotiatedRatesIndicator",
                "frs_shipment_indicator": "FRSShipmentIndicator",
                "rate_chart_indicator": "RateChartIndicator",
                "tpfc_negotiated_rates_indicator": "TPFCNegotiatedRatesIndicator",
                "user_level_discount_indicator": "UserLevelDiscountIndicator"
            },
            "movement_reference_number": "consectetur repreh",
            "reference_number": [
                {
                    "bar_code_indicator": "BarCodeIndicator",
                    "code": "cu",
                    "value": "eiusmod commodo exercitation"
                }
            ],
            "service": {
                "code": "la",
                "description": "nostrud ut"
            },
            "invoice_line_total": {
                "currency_code": "con",
                "monetary_value": "aute in min"
            },
            "num_of_pieces_in_shipment": "sint",
            "usps_endorsement": "u",
            "mi_label_cn22_indicator": "MILabelCN22Indicator",
            "sub_classification": "co",
            "cost_center": "laboris aliqua Duis deserunt u",
            "cost_center_barcode_indicator": "CostCenterBarcodeIndicator",
            "package_id": "ex officia non labor",
            "package_id_barcode_indicator": "PackageIDBarcodeIndicator",
            "irregular_indicator": "i",
            "shipment_indication_type": [
                {
                    "code": "Du",
                    "description": "e"
                }
            ],
            "mi_dual_return_shipment_key": "Lorem nostrud occaecat sunt magna",
            "mi_dual_return_shipment_indicator": "MIDualReturnShipmentIndicator",
            "rating_method_requested_indicator": "RatingMethodRequestedIndicator",
            "tax_information_indicator": "TaxInformationIndicator",
            "shipment_service_options": {
                "saturday_delivery_indicator": "SaturdayDeliveryIndicator",
                "saturday_pickup_indicator": "SaturdayPickupIndicator",
                "cod": {
                    "cod_funds_code": "p",
                    "cod_amount": {
                        "currency_code": "et ",
                        "monetary_value": "cupid"
                    }
                },
                "access_point_cod": {
                    "currency_code": "est",
                    "monetary_value": "nostru"
                },
                "deliver_to_addressee_only_indicator": "DeliverToAddresseeOnlyIndicator",
                "direct_delivery_only_indicator": "DirectDeliveryOnlyIndicator",
                "notification": [
                    {
                        "notification_code": "n",
                        "e_mail": {
                            "e_mail_address": [
                                "sit consequat"
                            ],
                            "undeliverable_e_mail_address": "nisi ",
                            "from_e_mail_address": "dolore do",
                            "from_name": "magna nostrud id cons",
                            "memo": "et voluptate cillum ut"
                        },
                        "voice_message": {
                            "phone_number": "incid"
                        },
                        "text_message": {
                            "phone_number": "consect"
                        },
                        "locale": {
                            "language": "ani",
                            "dialect": "cu"
                        }
                    }
                ],
                "label_delivery": {
                    "e_mail": {
                        "e_mail_address": "aliqua aute irure ipsum",
                        "undeliverable_e_mail_address": "qui culpa",
                        "from_e_mail_address": "deserunt incididunt qui magna si",
                        "from_name": "ut consequat qui in repr",
                        "memo": "ut in ex",
                        "subject": "voluptate",
                        "subject_code": "do"
                    },
                    "label_links_indicator": "LabelLinksIndicator"
                },
                "international_forms": {
                    "form_type": [
                        "FormType"
                    ],
                    "user_created_form": {
                        "document_id": [
                            "DocumentID"
                        ]
                    },
                    "ups_premium_care_form": {
                        "shipment_date": "ShipmentDate",
                        "page_size": "al",
                        "print_type": "Ex",
                        "num_of_copies": "no",
                        "language_for_ups_premium_care": {
                            "language": [
                                "Language"
                            ]
                        }
                    },
                    "cn22_form": {
                        "label_size": "do",
                        "prints_per_page": "d",
                        "label_print_type": "co",
                        "cn22_type": "l",
                        "cn22_other_description": "cillum esse eiusmod ",
                        "fold_here_text": "adipisicing in magna ipsumminim inc",
                        "cn22_content": [
                            {
                                "cn22_content_quantity": "CN22ContentQuantity",
                                "cn22_content_description": "occaecat",
                                "cn22_content_weight": {
                                    "unit_of_measurement": {
                                        "code": "min",
                                        "description": "laborum deserunt ut i"
                                    },
                                    "weight": "ad dolo"
                                },
                                "cn22_content_total_value": "ad Duisnu",
                                "cn22_content_currency_code": "rep",
                                "cn22_content_country_of_origin": "in",
                                "cn22_content_tariff_number": "irure fugiatindolore exercitation pariat"
                            }
                        ]
                    },
                    "additional_document_indicator": "AdditionalDocumentIndicator",
                    "form_group_id_name": "occaecat velit ut",
                    "eei_filing_option": {
                        "code": "c",
                        "e_mail_address": "adipisicing u",
                        "description": "tempor dolor Duis ",
                        "ups_filed": {
                            "poa": {
                                "code": "e",
                                "description": "aliqua voluptate"
                            }
                        },
                        "shipper_filed": {
                            "code": "o",
                            "description": "sunt aliqua",
                            "pre_departure_itn_number": "ullamco aute mini",
                            "exemption_legend": "dolore ut aliquipqui",
                            "eei_shipment_reference_number": "Lorem ve"
                        }
                    },
                    "contacts": {
                        "forward_agent": {
                            "company_name": "eu est",
                            "tax_identification_number": "laboris aute s",
                            "address": {
                                "address_line": [
                                    "AddressLine"
                                ],
                                "city": "elit consequat",
                                "state_province_code": "conse",
                                "town": "velit do",
                                "postal_code": "proident",
                                "country_code": "nu"
                            }
                        },
                        "ultimate_consignee": {
                            "company_name": "veniam enim ea",
                            "address": {
                                "address_line": [
                                    "AddressLine"
                                ],
                                "city": "ut in",
                                "state_province_code": "sin",
                                "town": "exercit",
                                "postal_code": "cu",
                                "country_code": "in"
                            },
                            "ultimate_consignee_type": {
                                "code": "i",
                                "description": "dolor aliquip "
                            }
                        },
                        "intermediate_consignee": {
                            "company_name": "quis aliqua officia",
                            "address": {
                                "address_line": [
                                    "AddressLine"
                                ],
                                "city": "sint ut laborum elit",
                                "state_province_code": "esse",
                                "town": "aute offic",
                                "postal_code": "veniam ",
                                "country_code": "ni"
                            }
                        },
                        "producer": {
                            "option": "al",
                            "company_name": "dolor ",
                            "tax_identification_number": "pari",
                            "address": {
                                "address_line": [
                                    "AddressLine"
                                ],
                                "city": "ex irure in",
                                "state_province_code": "lab",
                                "town": "amet ci",
                                "postal_code": "eiusm",
                                "country_code": "no"
                            },
                            "attention_name": "in aliqua quis proident ",
                            "phone": {
                                "number": "minim",
                                "extension": "co"
                            },
                            "e_mail_address": "Lorem et quis"
                        },
                        "sold_to": {
                            "name": "id dolore voluptate et",
                            "attention_name": "et irure culpa ",
                            "tax_identification_number": "sunt",
                            "phone": {
                                "number": "adip",
                                "extension": "c"
                            },
                            "option": "al",
                            "address": {
                                "address_line": [
                                    "AddressLine"
                                ],
                                "city": "Ut dol",
                                "state_province_code": "do",
                                "town": "d",
                                "postal_code": "ut",
                                "country_code": "ma"
                            },
                            "e_mail_address": "ullamco sunt do culpa esse",
                            "account_number": "fugi"
                        }
                    },
                    "product": [
                        {
                            "description": [
                                "Description"
                            ],
                            "unit": {
                                "number": "do occ",
                                "unit_of_measurement": {
                                    "code": "e",
                                    "description": "dol"
                                },
                                "value": "labore"
                            },
                            "commodity_code": "do cillum",
                            "part_number": "la",
                            "origin_country_code": "nu",
                            "joint_production_indicator": "JointProductionIndicator",
                            "net_cost_code": "nu",
                            "net_cost_date_range": {
                                "begin_date": "nostrud ",
                                "end_date": "velit am"
                            },
                            "preference_criteria": "t",
                            "producer_info": "sit",
                            "marks_and_numbers": "dolore Except",
                            "number_of_packages_per_commodity": "al",
                            "product_weight": {
                                "unit_of_measurement": {
                                    "code": "E",
                                    "description": "in id occaecat"
                                },
                                "weight": "u"
                            },
                            "vehicle_id": "ad",
                            "schedule_b": {
                                "number": "dolore tem",
                                "quantity": [
                                    "Quantity"
                                ],
                                "unit_of_measurement": [
                                    {
                                        "code": "ve",
                                        "description": "eiusmod"
                                    }
                                ]
                            },
                            "export_type": "e",
                            "sed_total_value": "tempor",
                            "exclude_from_form": {
                                "form_type": [
                                    "FormType"
                                ]
                            },
                            "packing_list_info": {
                                "package_associated": [
                                    {
                                        "package_number": "PackageNumber",
                                        "product_amount": "ProductAmount",
                                        "product_note": "ProductNote"
                                    }
                                ]
                            },
                            "eei_information": {
                                "export_information": "ip",
                                "license": {
                                    "number": "suntsunt",
                                    "code": "eiu",
                                    "license_line_value": "consec",
                                    "eccn_number": "culpa"
                                },
                                "ddtc_information": {
                                    "itar_exemption_number": "enim",
                                    "usml_category_code": "ad",
                                    "eligible_party_indicator": "EligiblePartyIndicator",
                                    "registration_number": "et inc",
                                    "quantity": "non mol",
                                    "unit_of_measurement": {
                                        "code": "Code",
                                        "description": "Description"
                                    },
                                    "significant_military_equipment_indicator": "SignificantMilitaryEquipmentIndicator",
                                    "acm_number": "aliqua repr"
                                }
                            }
                        }
                    ],
                    "invoice_number": "non in nostrud qui",
                    "invoice_date": "in dolor",
                    "purchase_order_number": "ad",
                    "terms_of_shipment": "est",
                    "reason_for_export": "in nisi sunt volupt",
                    "comments": "elit",
                    "declaration_statement": "dolore ex",
                    "discount": {
                        "monetary_value": "laborum irure"
                    },
                    "freight_charges": {
                        "monetary_value": "ut culpa e"
                    },
                    "insurance_charges": {
                        "monetary_value": "tempor est"
                    },
                    "other_charges": {
                        "monetary_value": "ea cupidatat",
                        "description": "in"
                    },
                    "currency_code": "cup",
                    "blanket_period": {
                        "begin_date": "culpa te",
                        "end_date": "dolor ma"
                    },
                    "export_date": "non qui amet sint",
                    "exporting_carrier": "Excepteur",
                    "carrier_id": "eu",
                    "in_bond_code": "in",
                    "entry_number": "culpa enim ut",
                    "point_of_origin": "d",
                    "point_of_origin_type": "e",
                    "mode_of_transport": "adipisicing",
                    "port_of_export": "Ut sunt",
                    "port_of_unloading": "exercitat",
                    "loading_pier": "anim exercitation",
                    "parties_to_transaction": "v",
                    "routed_export_transaction_indicator": "RoutedExportTransactionIndicator",
                    "containerized_indicator": "ContainerizedIndicator",
                    "override_paperless_indicator": "OverridePaperlessIndicator",
                    "shipper_memo": "ut eu",
                    "hazardous_materials_indicator": "HazardousMaterialsIndicator"
                },
                "delivery_confirmation": {
                    "dcis_type": "v",
                    "dcis_number": "au"
                },
                "return_of_document_indicator": "ReturnOfDocumentIndicator",
                "import_control_indicator": "ImportControlIndicator",
                "label_method": {
                    "code": "co",
                    "description": "sint ullamco consectetur no"
                },
                "commercial_invoice_removal_indicator": "CommercialInvoiceRemovalIndicator",
                "up_scarbonneutral_indicator": "UPScarbonneutralIndicator",
                "pre_alert_notification": [
                    {
                        "e_mail_message": {
                            "e_mail_address": "in ",
                            "undeliverable_e_mail_address": "adipisi"
                        },
                        "voice_message": {
                            "phone_number": "reprehenderit l"
                        },
                        "text_message": {
                            "phone_number": "pariatur "
                        },
                        "locale": {
                            "language": "do",
                            "dialect": "co"
                        }
                    }
                ],
                "exchange_forward_indicator": "ExchangeForwardIndicator",
                "hold_for_pickup_indicator": "HoldForPickupIndicator",
                "dropoff_at_ups_facility_indicator": "DropoffAtUPSFacilityIndicator",
                "lift_gate_for_pick_up_indicator": "LiftGateForPickUpIndicator",
                "lift_gate_for_delivery_indicator": "LiftGateForDeliveryIndicator",
                "sdl_shipment_indicator": "SDLShipmentIndicator",
                "epra_release_code": "magna",
                "restricted_articles": {
                    "diagnostic_specimens_indicator": "DiagnosticSpecimensIndicator",
                    "alcoholic_beverages_indicator": "AlcoholicBeveragesIndicator",
                    "perishables_indicator": "PerishablesIndicator",
                    "plants_indicator": "PlantsIndicator",
                    "seeds_indicator": "SeedsIndicator",
                    "special_exceptions_indicator": "SpecialExceptionsIndicator",
                    "tobacco_indicator": "TobaccoIndicator"
                },
                "inside_delivery": "et",
                "item_disposal": "ItemDisposal"
            },
            "locale": "amet ",
            "shipment_value_threshold_code": "en",
            "master_carton_id": "id",
            "master_carton_indicator": "MasterCartonIndicator",
            "shipment_date": "mollit s",
            "package": [
                {
                    "description": "voluptate reprehenderit",
                    "pallet_description": "dolore Lorem cillum officia dolore",
                    "num_of_pieces": "d",
                    "unit_price": "nul",
                    "packaging": {
                        "code": "al",
                        "description": "sit magna"
                    },
                    "dimensions": {
                        "unit_of_measurement": {
                            "code": "su",
                            "description": "fugiat dolore o"
                        },
                        "length": "nis",
                        "width": "n",
                        "height": "in "
                    },
                    "dim_weight": {
                        "unit_of_measurement": {
                            "code": "Exc",
                            "description": "id ex dolor pariatur eiusmod"
                        },
                        "weight": "dolor "
                    },
                    "package_weight": {
                        "unit_of_measurement": {
                            "code": "e",
                            "description": "laboris sint ali"
                        },
                        "weight": "i"
                    },
                    "large_package_indicator": "LargePackageIndicator",
                    "oversize_indicator": "OversizeIndicator",
                    "minimum_billable_weight_indicator": "MinimumBillableWeightIndicator",
                    "reference_number": [
                        {
                            "bar_code_indicator": "BarCodeIndicator",
                            "code": "in",
                            "value": "de"
                        }
                    ],
                    "additional_handling_indicator": "AdditionalHandlingIndicator",
                    "simple_rate": {
                        "code": "ci",
                        "description": "in Ut est"
                    },
                    "ups_premier": {
                        "category": "nu",
                        "sensor_id": "tempor",
                        "handling_instructions": {
                            "instruction": "nul"
                        }
                    },
                    "package_service_options": {
                        "delivery_confirmation": {
                            "dcis_type": "l",
                            "dcis_number": "dolore pa"
                        },
                        "declared_value": {
                            "type_": {
                                "code": "Du",
                                "description": "Duis"
                            },
                            "currency_code": "cup",
                            "monetary_value": "in pariat"
                        },
                        "cod": {
                            "cod_funds_code": "a",
                            "cod_amount": {
                                "currency_code": "dol",
                                "monetary_value": "amet "
                            }
                        },
                        "access_point_cod": {
                            "currency_code": "vel",
                            "monetary_value": "ad"
                        },
                        "shipper_release_indicator": "ShipperReleaseIndicator",
                        "notification": {
                            "notification_code": "l",
                            "e_mail": {
                                "subject": "sed aliquip",
                                "subject_code": "n",
                                "e_mail_address": [
                                    "exercitation culpa cillum "
                                ],
                                "undeliverable_e_mail_address": "ea off",
                                "from_e_mail_address": "adipisicing anim D",
                                "from_name": "in",
                                "memo": "adipisicing ullamco eiusmod"
                            }
                        },
                        "haz_mat": [
                            {
                                "packaging_type_quantity": "aut",
                                "record_identifier1": "RecordIdentifier1",
                                "record_identifier2": "RecordIdentifier2",
                                "record_identifier3": "RecordIdentifier3",
                                "sub_risk_class": "deserun",
                                "a_dr_item_number": "ea minim s",
                                "a_dr_packing_group_letter": "r",
                                "technical_name": "exercitation sintanim nostrud ex est reprehenderitExcepteur nonexercitation proident qui occaecat nonnulla eu qui culpa magnaculpaest ullamco velit eiusmodLorem ut exquis dolore sint et fugiatnon sint",
                                "hazard_label_required": "eiusmod et officianulla dolor amet irurevoluptateq",
                                "class_division_number": "null",
                                "reference_number": "deserunt e",
                                "quantity": "est",
                                "uom": "id",
                                "packaging_type": "nulla amet do",
                                "id_number": "cill",
                                "proper_shipping_name": "adipisicing cupidatat aliqua",
                                "additional_description": "exercitation",
                                "packaging_group_type": "no",
                                "packaging_instruction_code": "el",
                                "emergency_phone": "dolor velit",
                                "emergency_contact": "ad irure",
                                "reportable_quantity": "L",
                                "regulation_set": "qui ",
                                "transportation_mode": "enim",
                                "commodity_regulated_level_code": "do",
                                "transport_category": "m",
                                "tunnel_restriction_code": "commo",
                                "chemical_record_identifier": "con",
                                "local_technical_name": "commodo ad labore ullamco Lorem",
                                "local_proper_shipping_name": "anim consequat"
                            }
                        ],
                        "dry_ice": {
                            "regulation_set": "Ut ",
                            "dry_ice_weight": {
                                "unit_of_measurement": {
                                    "code": "Code",
                                    "description": "Description"
                                },
                                "weight": "Weight"
                            },
                            "medical_use_indicator": "MedicalUseIndicator"
                        },
                        "ups_premium_care_indicator": "UPSPremiumCareIndicator",
                        "proactive_indicator": "ProactiveIndicator",
                        "package_identifier": "se",
                        "clinical_trials_id": "irureDuis in dolored",
                        "refrigeration_indicator": "RefrigerationIndicator"
                    },
                    "commodity": {
                        "freight_class": "enim offic",
                        "nmfc": {
                            "prime_code": "et e",
                            "sub_code": "mi"
                        }
                    },
                    "haz_mat_package_information": {
                        "all_packed_in_one_indicator": "AllPackedInOneIndicator",
                        "over_packed_indicator": "OverPackedIndicator",
                        "q_value": "qui",
                        "outer_packaging_type": "ex"
                    }
                }
            ]
        },
        "label_specification": {
            "label_image_format": {
                "code": "ulla",
                "description": "ullamco voluptate in"
            },
            "http_user_agent": "proident nisi et exercitation",
            "label_stock_size": {
                "height": "e",
                "width": "o"
            },
            "instruction": [
                {
                    "code": "Ex",
                    "description": "en"
                }
            ],
            "character_set": "con"
        },
        "receipt_specification": {
            "image_format": {
                "code": "cup",
                "description": "veniam ea nulla"
            }
        }
    }
)

result = sdk.shipments.shipment(
    request_body=request_body,
    version="v2403",
    additionaladdressvalidation="additionaladdressvalidation",
    trans_id="transId",
    transaction_src="testing"
)

print(result)
```

## void_shipment

The Void Shipping API is used to cancel the previously scheduled shipment

- HTTP Method: `DELETE`
- Endpoint: `/shipments/{version}/void/cancel/{shipmentidentificationnumber}`

**Parameters**

| Name                         | Type | Required | Description                                                                                                                                                                                                                                                                                                     |
| :--------------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| version                      | str  | ✅       | API Version Valid values: - v2403                                                                                                                                                                                                                                                                               |
| shipmentidentificationnumber | str  | ✅       | The shipment's identification number Alpha-numeric. Must pass 1Z rules. Must be upper case. Length 18                                                                                                                                                                                                           |
| trackingnumber               | str  | ❌       | The package's tracking number. You may have up to 20 different tracking numbers listed. If more than one tracking number, pass this value as: trackingnumber= ["1ZISUS010330563105","1ZISUS01033056310 8"] with a coma separating each number. Alpha-numeric. Must pass 1Z rules. Must be upper case. Length 18 |
| trans_id                     | str  | ❌       | An identifier unique to the request. Length 32                                                                                                                                                                                                                                                                  |
| transaction_src              | str  | ❌       | An identifier of the client/source application that is making the request.Length 512                                                                                                                                                                                                                            |

**Return Type**

`VoidshipmentResponseWrapper`

**Example Usage Code Snippet**

```python
from ups_shipping import UpsShipping, Environment

sdk = UpsShipping(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.shipments.void_shipment(
    version="v2403",
    shipmentidentificationnumber="shipmentidentificationnumber",
    trackingnumber="trackingnumber",
    trans_id="transId",
    transaction_src="testing"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
