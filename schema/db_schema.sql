DROP TABLE IF EXISTS PurchaseOrder;
DROP TABLE IF EXISTS OrderLines;
DROP TABLE IF EXISTS OrderLine;
DROP TABLE IF EXISTS PersonInfo;
DROP TABLE IF EXISTS LineItem;
DROP TABLE IF EXISTS LinePriceInfo;

create TABLE PurchaseOrder (
    poid INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    createdby text
);


create table OrderLines(
poid int,    
OrderLinesId INTEGER PRIMARY KEY AUTOINCREMENT,
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
VendorId text,
DocumentType text,
OrderNo text,
Purpose text,
CustomerEMailID text,
CustomerPONo text,
OrderDate text,
EntryType text,
OrderType text,
Division text,
EnteredBy text,
EnterpriseCode text
);


create table OrderLine(
poid int,      
OrderLinesId int,
OrderLineId  INTEGER PRIMARY KEY AUTOINCREMENT,
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
CarrierServiceCode text,
ManufacturerName text,
DeliveryMethod text,
RecevingNode text,
DeliveryCode text,
ReqDeliveryDate text,
PrimeLineNo text,
CarrierAccountNo text,
CustomerLinePONo text,
SubLineNo text,
FillQuantity text,
SCAC text,
ShipmentConsolidationGroupId text,
ItemGroupCode text,
ReqShipDate text,
ShipNode text,
FreightTerms text,
OrderedQty text,
LineType text,
FulfillmentType text);




create table PersonInfo(
poid int,  
OrderLinesId int,
PersonInfoId INTEGER PRIMARY KEY AUTOINCREMENT,
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
OtherPhone text,
Company text,
FirstName text,
ZipCode text,
Title text,
City text,
MiddleName text,
EmailId text,
DayPhone text,
MobilePhone text,
AddressLine3 text,
AddressLine2 text,
AddressLine1 text,
PersonID text,
AddressLine6 text,
State text,
Country text,
LastName text
);

create table LineItem(
poid int,  
OrderLineId int, 
LineItemId INTEGER PRIMARY KEY AUTOINCREMENT,
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
CustomerItem text,
ItemDesc text,
ItemId text,
ManufacturerItem text,
ProductClass text,
UnitOfMeasure text 
);


create table LinePriceInfo(
poid int,  
OrderLineId int,
LinePriceInfoId INTEGER PRIMARY KEY AUTOINCREMENT,
created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
IsPriceLocked text,
UnitPrice text 
);