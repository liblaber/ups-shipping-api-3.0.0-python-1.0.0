# ShipmentServiceOptionsCod

COD container Indicates COD is requested. Shipment COD is only available for EU origin countries or territories and for shippers account type Daily Pickup and Drop Shipping. Not available to shipment with return service.

**Properties**

| Name           | Type         | Required | Description                                                                                            |
| :------------- | :----------- | :------- | :----------------------------------------------------------------------------------------------------- |
| cod_funds_code | str          | ✅       | For valid values refer to: Rating and Shipping COD Supported Countries or Territories in the Appendix. |
| cod_amount     | CodCodAmount | ✅       | COD Amount container.                                                                                  |

<!-- This file was generated by liblab | https://liblab.com/ -->