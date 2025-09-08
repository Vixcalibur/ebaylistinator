from fastapi import FastAPI, Form, Request, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
import csv, re, io
from pathlib import Path
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("ebaylive.html", {"request": request})


@app.post("/generate")
def generate_csv(
    request: Request,
    photoURL: str = Form(...),
    shortTitle: str = Form(...),
    fullTitle: str = Form(...),
    listingType: str = Form(...),
    SHIPPING: str = Form(...),
    itemSKU: List[str] = Form(...),
    customLabelSKU: List[str] = Form(...),
    startingSKU: List[int] = Form(...),
    numberOfListings: List[int] = Form(...),
    prices: List[int] = Form(...)
):

    numberOfListings = [int(x) for x in numberOfListings]
    numberOfListings = [int(x) for x in numberOfListings]

    if not (len(itemSKU) == len(customLabelSKU) == len(startingSKU) == len(numberOfListings)):
        raise Exception("All input lists must be of equal length.")

    def clean_filename(filename: str) -> str:
        return re.sub(r'[\\/:*?"<>|\s]', '_', filename)

    if SHIPPING == "0":
        shipping = "FREE SHIPPING - (ID: 231299707026)"
    elif SHIPPING == "1":
        shipping = "$2.49 Shipping Each item , All items - (ID: 241841053026)"
    else:
        raise Exception("Invalid Shipping Option")

    


    rows = []

    # COINS

    if listingType == "0":
        headers = ["*Action(SiteID=US|Country=US|Currency=USD|Version=1193)",
            "Custom Label (SKU)","Category ID","Category Name","Title","Relationship",
            "Relationship details","Schedule Time","P:EPID","Start price","Quantity",
            "Item photo URL","VideoID","Condition ID","Description","Format","Duration",
            "Buy It Now price","Best Offer Enabled","Best Offer Auto Accept Price",
            "Minimum Best Offer Price","Immediate pay required","Location","Shipping service 1 option",
            "Shipping service 1 cost","Shipping service 1 priority","Shipping service 2 option",
            "Shipping service 2 cost","Shipping service 2 priority","Max dispatch time",
            "Returns accepted option","Returns within option","Refund option","Return shipping cost paid by",
            "Shipping profile name","Return profile name","Payment profile name","C:Certification",
            "C:Denomination","C:Strike Type","C:Mint Location","C:Fineness","C:Year","C:KM Number"]
        for i in range(len(customLabelSKU)):
            i_customLabelSKU = customLabelSKU[i]
            i_itemSKU = itemSKU[i]
            for j in range(numberOfListings[i]):
                num = startingSKU[i] + j
                suffix = f"{num:03}"
                j_customLabelSKU = i_customLabelSKU + " " + suffix + " " + i_itemSKU
                title=f"{shortTitle}"
                price=f"{prices[i]}"
                listingName = j_customLabelSKU + " C: LIVE " + title + " RTTV"
                desc = f"Item Shown on Screen During {fullTitle}"
                row = ["Add", j_customLabelSKU, "525", "/Coins & Paper Money/Coins: US/Collections, Lots",
                       listingName, "", "", "", "", price, "1", photoURL, "", "3000-Used", desc, "Auction", "7", "", "", "", "",
                       "", "Marietta, GA", "", "", "", "", "", "", "", "", "", "", "", shipping,
                       "No Return Accepted (234360674026) - (ID: 234360674026)",
                       "Auction - (ID: 231040727026)", "Uncertified", "", "", "", "", "", ""]
                rows.append(row)
    # COINS
    # BULLION
    elif listingType == "1":
        headers = ["*Action(SiteID=US|Country=US|Currency=USD|Version=1193)",
            "Custom Label (SKU)","Category ID","Category Name","Title","Relationship",
            "Relationship details","Schedule Time","P:EPID","Start price","Quantity",
            "Item photo URL","VideoID","Condition ID","Description","Format","Duration",
            "Buy It Now price","Best Offer Enabled","Best Offer Auto Accept Price",
            "Minimum Best Offer Price","Immediate pay required","Location","Shipping service 1 option",
            "Shipping service 1 cost","Shipping service 1 priority","Shipping service 2 option",
            "Shipping service 2 cost","Shipping service 2 priority","Max dispatch time",
            "Returns accepted option","Returns within option","Refund option","Return shipping cost paid by",
            "Shipping profile name","Return profile name","Payment profile name","C:Shape",
            "C:Precious Metal Content per Unit","C:Brand/Mint","C:Fineness"]
        for i in range(len(customLabelSKU)):
            i_customLabelSKU = customLabelSKU[i]
            i_itemSKU = itemSKU[i]
            for j in range(numberOfListings[i]):
                num = startingSKU[i] + j
                suffix = f"{num:03}"
                j_customLabelSKU = i_customLabelSKU + " " + suffix + " " + i_itemSKU
                title=f"{shortTitle}"
                price=f"{prices[i]}"
                listingName = j_customLabelSKU + " C: LIVE " + title + " RTTV"
                desc = f"Item Shown on Screen During {fullTitle}"
                row = ["Add", j_customLabelSKU, "39489", "/Coins & Paper Money/Bullion/Silver/Bars & Rounds",
                       listingName, "", "", "", "", price, "1", photoURL, "", "3000-Used", desc, "Auction", "7", "", "", "", "",
                       "", "Marietta, GA", "", "", "", "", "", "", "", "", "", "", "", shipping,
                       "No Return Accepted (234360674026) - (ID: 234360674026)",
                       "Auction - (ID: 231040727026)","","","",0.999]
                rows.append(row)    
    # BULLION
    # Jewelry
    elif listingType == "2":
        headers = ["*Action(SiteID=US|Country=US|Currency=USD|Version=1193)",
            "Custom Label (SKU)","Category ID","Category Name","Title","Relationship",
            "Relationship details","Schedule Time","P:EPID","Start price","Quantity",
            "Item photo URL","VideoID","Condition ID","Description","Format","Duration",
            "Buy It Now price","Best Offer Enabled","Best Offer Auto Accept Price",
            "Minimum Best Offer Price","Immediate pay required","Location","Shipping service 1 option",
            "Shipping service 1 cost","Shipping service 1 priority","Shipping service 2 option",
            "Shipping service 2 cost","Shipping service 2 priority","Max dispatch time",
            "Returns accepted option","Returns within option","Refund option","Return shipping cost paid by",
            "Shipping profile name","Return profile name","Payment profile name","C:Brand","C:Department",
            "C:Type","C:Dial Color","C:Movement","C:Case Color","C:Case Material","C:Features",
            "C:Year Manufactured","C:Display","C:Model","C:Indices","C:Style","C:With Original Box/Packaging",
            "C:With Papers","C:Water Resistance","C:Customized","C:MPN","Product Safety Pictograms",
            "Product Safety Statements","Product Safety Component","Regulatory Document Ids","Manufacturer Name",
            "Manufacturer AddressLine1","Manufacturer AddressLine2","Manufacturer City","Manufacturer Country",
            "Manufacturer PostalCode","Manufacturer StateOrProvince","Manufacturer Phone","Manufacturer Email",
            "Manufacturer ContactURL","Responsible Person 1","Responsible Person 1 Type",
            "Responsible Person 1 AddressLine1","Responsible Person 1 AddressLine2","Responsible Person 1 City",
            "Responsible Person 1 Country","Responsible Person 1 PostalCode","Responsible Person 1 StateOrProvince"
            ",Responsible Person 1 Phone","Responsible Person 1 Email","Responsible Person 1 ContactURL"]
        for i in range(len(customLabelSKU)):
            i_customLabelSKU = customLabelSKU[i]
            i_itemSKU = itemSKU[i]
            for j in range(numberOfListings[i]):
                num = startingSKU[i] + j
                suffix = f"{num:03}"
                j_customLabelSKU = i_customLabelSKU + " " + suffix + " " + i_itemSKU
                title=f"{shortTitle}"
                price=f"{prices[i]}"
                listingName = j_customLabelSKU + " C: LIVE " + title + " RTTV"
                desc = f"Item Shown on Screen During {fullTitle}"
                row = ["Add", j_customLabelSKU, "260326", "/Jewelry & Watches/Watches, Parts & Accessories/Watches/Other Watches",
                       listingName, "", "", "", "", price, "1", photoURL, "", "3000-Used", desc, "Auction", "7", "", "", "", "",
                       "", "Marietta, GA", "", "", "", "", "", "", "", "", "", "", "", shipping,
                       "No Return Accepted (234360674026) - (ID: 234360674026)",
                       "Auction - (ID: 231040727026)","Unbranded","Unisex Adults","Key Ring Watch","","","","","","","","",
                       "","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
                rows.append(row)   
    else:
        raise Exception("Only Listing Types '0' (Coins), '1' (Bullion), and '2' (Jewelry) are supported.")
    # JEWELRY

    filename = clean_filename(fullTitle) + ".csv"
    import io
    from fastapi.responses import StreamingResponse

    output = io.StringIO()
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(headers)
    writer.writerows(rows)
    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}

    )


@app.post("/extract-column", response_class=HTMLResponse)
async def extract_column(file: UploadFile = File(...)):
    contents = await file.read()
    decoded = contents.decode("utf-8")
    reader = csv.reader(io.StringIO(decoded))

    # Extract column K (index 10) from each row, skipping header
    column_j = []
    for i, row in enumerate(reader):
        if len(row) > 9:  # index 10 = column K
            column_j.append(row[9])
        else:
            column_j.append("")

    # Format as a copy-paste list
    joined = "\n".join(column_j)

    return f"""
    <h2>Extracted Column K</h2>
    <textarea style='width:100%; height:300px'>{joined}</textarea>
    <br><a href="/">Back</a>
    """

@app.post("/generate-sku-list")
def generate_sku_list(first_sku: str = Form(...), last_sku: str = Form(...)):
    first_sku = first_sku.upper()
    last_sku = last_sku.upper()

    codes = []
    for first in range(ord(first_sku[2]), ord(last_sku[2]) + 1):
        for second in range(ord(first_sku[1]), ord(last_sku[1]) + 1):
            for third in range(ord(first_sku[0]), ord(last_sku[0]) + 1):
                prefix = chr(third) + chr(second) + chr(first) + " "
                for number in range(1, 281):
                    codes.append(f"{prefix}{number:03}")

    title = codes[0] + " - " + codes[-1]
    file_content = title + "\n" + "\n".join(codes)

    # Return the result as downloadable .txt
    return PlainTextResponse(file_content, headers={
        "Content-Disposition": f"attachment; filename={title}.txt"
    })


