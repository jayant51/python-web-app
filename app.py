from flask import (
    Flask,
    Blueprint,
    render_template,
    jsonify,
    request,
    url_for,
    flash,
    redirect,
)
import sqlite3
from sqlite3 import Error
import json
import os


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("pages/home.html")


@app.route("/about")
def about():
    return render_template("pages/about.html")


@app.route("/po")
def po():
    return render_template("pages/po_entry.html")


def createOrderLines(poLns):

    # connection = sqlite3.connect("supplychain.db")
    connection = create_connection()

    try:
        cursor = connection.cursor()
        records = cursor.execute("select poid from PurchaseOrder")
        poid_val = 1
        for row in records:
            poid_val = row[0]

        print("insert into OrderLines 1")
        # poLns = orderlines()
        cursor.execute(
            "insert into OrderLines (poid, VendorId, DocumentType, OrderNo, Purpose, CustomerEmailId, CustomerPONo, OrderDate, EntryType, \
                OrderType, Division, EnteredBy, EnterpriseCode) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                poid_val,
                poLns.VendorID,
                poLns.DocumentType,
                poLns.OrderNo,
                poLns.Purpose,
                poLns.CustomerEmailId,
                poLns.CustomerPONo,
                poLns.OrderDate,
                poLns.EntryType,
                poLns.OrderType,
                poLns.Division,
                poLns.EnteredBy,
                poLns.EnterpriseCode,
            ),
        )
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to perform operations with sqlite ", error)
    finally:
        if connection:
            connection.close()
    return


def createOrderLine(poLn):

    # connection = sqlite3.connect("supplychain.db")
    connection = create_connection()

    try:
        cursor = connection.cursor()
        records = cursor.execute("select poid, OrderLinesId from OrderLines")
        poid_val = 1
        OrderLinesId_val = 1
        for row in records:
            poid_val = row[0]
            OrderLinesId_val = row[1]

        print("insert into OrderLine")
        # poLn = orderline_obj()
        print(repr(poLn))
        cursor.execute(
            "insert into OrderLine ( poid, OrderLinesId, CarrierServiceCode, ManufacturerName, DeliveryMethod, RecevingNode, \
                DeliveryCode, ReqDeliveryDate, PrimeLineNo, CarrierAccountNo, CustomerLinePONo,  SubLineNo, FillQuantity, SCAC, ShipmentConsolidationGroupId,\
                ItemGroupCode, ReqShipDate, ShipNode, FreightTerms, OrderedQty, LineType, FulfillmentType) \
                values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )",
            (
                poid_val,
                OrderLinesId_val,
                poLn.CarrierServiceCode,
                poLn.ManufacturerName,
                poLn.DeliveryMethod,
                poLn.RecevingNode,
                poLn.DeliveryCode,
                poLn.ReqDeliveryDate,
                poLn.PrimeLineNo,
                poLn.CarrierAccountNo,
                poLn.CustomerLinePONo,
                poLn.SubLineNo,
                poLn.FillQuantity,
                poLn.SCAC,
                poLn.ShipmentConsolidationGroupId,
                poLn.ItemGroupCode,
                poLn.ReqShipDate,
                poLn.ShipNode,
                poLn.FreightTerms,
                poLn.OrderedQty,
                poLn.LineType,
                poLn.FulfillmentType,
            ),
        )
        connection.commit()

        cursor.close()
    except sqlite3.Error as error:
        print("Failed to perform operations with sqlite ", error)
    finally:
        if connection:
            connection.close()
    return


def createPersonInfo(info):

    # connection = sqlite3.connect("supplychain.db")
    connection = create_connection()

    try:
        cursor = connection.cursor()
        records = cursor.execute("select poid, OrderLinesId from OrderLines")
        poid_val = 1
        OrderLinesId_val = 1
        for row in records:
            poid_val = row[0]
            OrderLinesId_val = row[1]

        print("insert into PersonInfo")
        # info = personInfo_obj()
        cursor.execute(
            "insert into PersonInfo ( poid, OrderLinesId, OtherPhone, Company, FirstName, ZipCode, Title, City, MiddleName, EmailId, DayPhone, \
            MobilePhone, AddressLine3, AddressLine2, AddressLine1, PersonID, AddressLine6, State, Country, LastName ) \
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                poid_val,
                OrderLinesId_val,
                info.otherPhone,
                info.company,
                info.FirstName,
                info.ZipCode,
                info.Title,
                info.City,
                info.MiddleName,
                info.EmailId,
                info.DayPhone,
                info.MobilePhone,
                info.AddressLine3,
                info.AddressLine2,
                info.AddressLine1,
                info.PersonID,
                info.AddressLine6,
                info.State,
                info.Country,
                info.LastName,
            ),
        )
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to perform operations with sqlite ", error)
    finally:
        if connection:
            connection.close()
    return


def createLineItem(lineItem):

    # connection = sqlite3.connect("supplychain.db")
    connection = create_connection()

    try:
        cursor = connection.cursor()
        records = cursor.execute("select poid, OrderLineId from OrderLine")
        poid_val = 1
        OrderLineId_val = 1
        for row in records:
            poid_val = row[0]
            OrderLineId_val = row[1]

        print("insert into LineItem")
        # lineItem = lineitem_obj()
        cursor.execute(
            "insert into LineItem ( poid, OrderLineId, CustomerItem, ItemDesc, ItemId, ManufacturerItem, ProductClass, UnitOfMeasure) \
            values (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                poid_val,
                OrderLineId_val,
                lineItem.CustomerItem,
                lineItem.ItemDesc,
                lineItem.ItemId,
                lineItem.ManufacturerItem,
                lineItem.ProductClass,
                lineItem.UnitOfMeasure,
            ),
        )
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to perform operations with sqlite ", error)
    finally:
        if connection:
            connection.close()
    return


def createLinePriceInfo(priceInfo):

    # connection = sqlite3.connect("supplychain.db")
    connection = create_connection()

    try:
        cursor = connection.cursor()
        records = cursor.execute("select poid, OrderLineId from OrderLine")
        poid_val = 1
        OrderLineId_val = 1
        for row in records:
            poid_val = row[0]
            OrderLineId_val = row[1]

        print("insert into LinePriceInfo")
        cursor.execute(
            "insert into LinePriceInfo ( poid, OrderLineId, IsPriceLocked, UnitPrice) values (?, ?, ?, ?)",
            (
                poid_val,
                OrderLineId_val,
                priceInfo.IsPriceLocked,
                priceInfo.UnitPrice,
            ),
        )
        connection.commit()

        cursor.close()
    except sqlite3.Error as error:
        print("Failed to perform operations with sqlite ", error)
    finally:
        if connection:
            connection.close()
    return


@app.route("/init")
def init():

    # connection = sqlite3.connect("supplychain.db")
    connection = create_connection()
    cursor = connection.cursor()
    try:

        with open("./schema/db_schema.sql") as schema:
            cursor.executescript(schema.read())

        print(cursor._last_executed)
        # cursor = connection.cursor()
        print("insert into PurchaseOrder")
        cursor.execute("insert into PurchaseOrder (createdby) values ('System')")
        connection.commit()

        """ 
        poLns = orderlines_obj()
        createOrderLines(poLns)

        poLn = orderline_obj()
        createOrderLine(poLn)

        info = personInfo_obj()
        createPersonInfo(info)

        line = lineitem_obj()
        createLineItem(line)

        priceInfo = linepriceinfo_obj()
        createLinePriceInfo(priceInfo)
        """

    except sqlite3.Error as error:
        print("Failed to perform operations with sqlite ", error)
    finally:
        if connection:
            connection.close()
    return render_template("pages/po_entry.html")


@app.route("/getPO")
def getpo():

    # conn = sqlite3.connect("supplychain.db")
    connection = create_connection()
    try:
        cur = connection.cursor()
        cur.execute(
            # " select * from PurchaseOrder po, OrderLines ols, OrderLines ol, personInfo pf where po.poid = ols.poid and po.poid = ol.poid and ols.OrderLinesId = ol.OrderLinesId and pf.OrderLinesId=ol.OrderLinesId"
            # "select * from OrderLines ols, OrderLine ol where  ols.OrderLinesId = ol.OrderLinesId"
            # "select * from OrderLines ols, OrderLine ol, LineItem li where  ols.OrderLinesId = ol.OrderLinesId and li.OrderLineId = ol.OrderLineId;"
            # " select * from OrderLines ols, OrderLine ol, LineItem li, LinePriceInfo lipf where  ols.OrderLinesId = ol.OrderLinesId and li.OrderLineId = ol.OrderLineId and li.OrderLineId = lipf.OrderLineId"
            " select * from OrderLines ols, OrderLine ol, LineItem li, LinePriceInfo lipf, PersonInfo pif where  ols.OrderLinesId = ol.OrderLinesId and li.OrderLineId = ol.OrderLineId and li.OrderLineId = lipf.OrderLineId and  ols.OrderLinesId = pif.OrderLinesId"
        )
        std_po = []
        db_po = []
        rows = cur.fetchall()
        print(rows)

        for row in rows:
            print(row)

        for row in rows:
            d = {}
        for i, col in enumerate(cur.description):
            d[col[0]] = row[i]
        db_po.append(d)

        # Convert the list of dictionaries to JSON and print it
        json_db_po = json.dumps(db_po)
        print("--------------------------------------")
        print(json_db_po)

        with open(
            "/Users/jayantkulkarni/Desktop/atos/python_code_examples/board/schema/createOrder.json"
        ) as podata:
            std_po = json.loads(podata.read())
        keylist = std_po.keys()

        # print(std_po["OrderLines"]['OrderLine']["EnteredBy"])
        # print("KeyList = ")
        # print(keylist)   # gives top level keys only

        # get file jason #
        C = []
        with open(
            "/Users/jayantkulkarni/Desktop/atos/python_code_examples/board/schema/createOrder.json"
        ) as podata:
            std_po = json.loads(podata.read())
        print(std_po)
        keys(
            std_po,
            C,
        )

        # workes from here #
        std_json_keys = list(map(".".join, keys(std_po)))
        print("===>")
        print(std_json_keys)
        """
        for i in result:
            print(i)
            if i in parsed_po:
                # print(i)
                cur_key = parsed_po[i]
                json_keys = cur_key.split(".")
                last_key = json_keys[len(json_keys) - 1]
                print(last_key)
        """
        db_json = db_po[0]
        for i in std_json_keys:
            # print(i)
            json_key = i.split(".")
            last_key = json_key[len(json_key) - 1]
            # print(last_key)
            if last_key in db_json:
                print(last_key + " " + db_json[last_key])
                if len(json_key) == 1:
                    std_po[last_key] = db_json[last_key]
                if len(json_key) == 2:
                    std_po[json_key[0]][json_key[1]] = db_json[last_key]
                if len(json_key) == 3:
                    std_po[json_key[0]][json_key[1]][json_key[2]] = db_json[last_key]
            else:
                print("-->" + last_key)

        print("=============++++============")
        # print(std_po["OrderLines"]["OrderLine"]["CarrierAccountNo"])
        # print(std_po["PersonInfoBillTo"])
        print(str(std_po))
        # print(std_po["OrderLines"])

        # print(std_json_keys)
        cur.close()
    except sqlite3.Error as error:
        print("Failed to perform operations with sqlite ", error)
    finally:
        if connection:
            connection.close()
    return std_po


""" 
# return render_template("pages/po_entry.html", podata=rows)
"""


def keys(d, c=[]):
    return [
        i
        for a, b in d.items()
        for i in ([c + [a]] if not isinstance(b, dict) else keys(b, c + [a]))
    ]

    # result = list(map(".".join, keys(d)))


@app.route("/create/", methods=("GET", "POST"))
def create():
    # connection = sqlite3.connect("supplychain.db")
    connection = create_connection()
    try:

        # with open("./schema/db_schema.sql") as f:
        #    connection.executescript(f.read())

        cursor = connection.cursor()
        if request.method == "POST":

            records = cursor.execute("select poid, OrderLineId from OrderLine")
            poid_val = 1
            for row in records:
                poid_val = row[0]
                OrderLineId_val = row[1]

            orderlines = orderlines_obj
            orderline = orderline_obj
            lineitem = lineitem_obj
            personInfoSoldTo = personInfo_obj
            priceinfo = linepriceinfo_obj

            orderlines.OrderNo = request.form["orderNum"]
            orderlines.CustomerPONo = request.form["custPONum"]
            createOrderLines(orderlines)

            orderline.DeliveryCode = request.form["dcode"]
            orderline.DeliveryMethod = request.form["dmethod"]

            orderline.CarrierAccountNo = request.form["CarrierAccountNo"]
            orderline.CarrierServiceCode = request.form["CarrierServiceCode"]
            # orderline.CustomerLinePONo = request.form["CustomerPOLineNo"]
            createOrderLine(orderline)

            lineitem.CustomerItem = request.form["CustomerItem"]
            lineitem.ItemDesc = request.form["ItemDesc"]  ##Laptop 14
            createLineItem(lineitem)

            priceinfo.UnitPrice = request.form["uPrice"]
            priceinfo.IsPriceLocked = request.form["lockedPrice"]
            createLinePriceInfo(priceinfo)

            personInfoSoldTo.FirstName = request.form["firstn"]
            personInfoSoldTo.MiddleName = request.form["middlen"]
            personInfoSoldTo.LastName = request.form["lastn"]
            personInfoSoldTo.EmailId = request.form["Email"]
            personInfoSoldTo.AddressLine1 = request.form["sAddress"]
            personInfoSoldTo.City = request.form["state"]  # city
            personInfoSoldTo.State = request.form["state"]  # state
            personInfoSoldTo.Country = request.form["state"]  # country
            createPersonInfo(personInfoSoldTo)

            # nameoncard = request.form["nameoncard"]

            # expiresyear = request.form["ExpiresYear"]

            # async with cursor.execute("insert into PurchaseOrder values (2)") as cursor:
            #    print("Total changes: {}".format(cursor.rowcount))

            cursor.execute(" insert into PurchaseOrder (createdby) values ('System')")
            connection.commit()

            records = cursor.execute("select poid from PurchaseOrder")
            for row in records:
                poid_val = row[0]

            cursor.close()

    except sqlite3.Error as error:
        print("Failed to perform operations with sqlite ", error)
    finally:
        if connection:
            connection.close()
    return render_template("pages/create.html")


def create_connection():
    print("create a database connection to a database that resides in the memory")

    try:
        # conn = sqlite3.connect(":memory:")
        conn = sqlite3.connect(r"./schema/supplychain.db")
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


class orderlines_obj:
    VendorID = ""
    DocumentType = "0005"
    OrderNo = "PO_2024020903"
    Purpose = "Purchase Order"
    CustomerEmailId = "person@vendor1.com"
    CustomerPONo = "C123456-4"
    OrderDate = ""
    EntryType = "WEB"
    OrderType = "B2B"
    Division = "ATOS"
    EnteredBy = "989898"
    EnterpriseCode = "ATOS"


class personInfo_obj:  # PersonInfoSoldlTo, PersonInfoBillTo, PersonInfoShipTo
    otherPhone = "+1-111222333"
    otherPhone = "+1-111222333"
    company = "Vendor-1"
    FirstName = "Allan"
    ZipCode = "75093"
    Title = ""
    City = "Virginia"
    MiddleName = ""
    EmailId = "person@vendor1.com"
    DayPhone = "+1-999888777"
    MobilePhone = "+1-999888777"
    AddressLine3 = ""
    AddressLine2 = "Plano"
    AddressLine1 = "5920 Windhaven Pkwy #120"
    PersonID = "AC0000-5694"
    AddressLine6 = ""
    State = "NH"
    Country = "US"
    LastName = "Fava.dummy"


class orderline_obj:
    CarrierServiceCode = "UPS"
    ManufacturerName = "ABC"
    DeliveryMethod = "SHP"
    RecevingNode = ""
    DeliveryCode = "Collect"
    ReqDeliveryDate = "2024-02-09"
    PrimeLineNo = "1"
    CarrierAccountNo = "123"
    CustomerLinePONo = "1"
    SubLineNo = "1"
    FillQuantity = ""
    SCAC = "UPS"
    ShipmentConsolidationGroupId = ""
    ItemGroupCode = ""
    ReqShipDate = "2024-02-20"
    ShipNode = "ATOS_Store"
    FreightTerms = ""
    OrderedQty = "1"
    LineType = "DS"
    FulfillmentType = "SHP"


class lineitem_obj:
    CustomerItem = ""
    ItemDesc = "Laptop 14"
    ItemId = "Laptop 14"
    ManufacturerItem = ""
    ProductClass = ""
    UnitOfMeasure = "EACH"


class linepriceinfo_obj:
    IsPriceLocked = "Y"
    UnitPrice = "0"


if __name__ == "__main__":
    app.debug = os.environ.get("FLASK_DEBUG", True)

    port = os.environ.get("FLASK_PORT") or 8080
    port = int(port)

    app.run(port=port, host="0.0.0.0")


# python3 -m flask --app board run --port 8000 --debug
