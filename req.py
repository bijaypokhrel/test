import requests
import json

url = "https://demoimis.ssf.gov.np/api/api_fhir_r4/CoverageEligibilityRequest/"

payload = json.dumps({
    "resourceType": "CoverageEligibilityRequest",
    "patient": {
        "reference": "Patient/20760000003"
    },
    "extension": [
        {
            "url": "visitDate",
            "valueString": "2022-10-22"
        }
    ]
})
headers = {
    'remote-user': 'patan',
    'Authorization': 'Basic cGF0YW5maGlyOmpyMGE4cXJCNGRWbzhBcXlRcEp5',
    'Content-Type': 'application/json',
    'Cookie': 'csrftoken=fgqxaecrr2eAml1IFxwRLvAm2Rfa6uRlPIrVWXNnKj3bLfCDSfflsipAmBRse2Bw; sessionid=hj3ug3nq0xci5lcq77w6giv60r29kpkp'
}

response = requests.request(
    "POST", url, headers=headers, data=payload, verify=False)



json = json.loads(response.text)
json.pop("patient")


insurance = json["insurance"][0]
insurance_extension_1 = insurance["extension"][0]
name1 = insurance_extension_1['valueString']
balance1 = insurance_extension_1['valueDecimal']


item1 = insurance["item"][0]
benefit1 = item1["benefit"][0]
allowed_money1 = benefit1["allowedMoney"]["value"]
used_money1 = benefit1["usedMoney"]["value"]
category1 = item1["category"]["text"]


a = {
    "schema1": [
        {
            "name": f"{name1}",
            "balance": f"{balance1}",
            "allowedMoney": f"{allowed_money1}",
            "usedMoney": f"{used_money1}",
            "category": f"{category1}"
        }
    ]
}
print(a)

insurance2 = json["insurance"][1]
insurance_extension_2 = insurance2['extension'][0]
name2 = insurance_extension_2["valueString"]
balance2 = insurance_extension_2["valueDecimal"]
insurance_ipd_opd = insurance2['extension']

opd_balance = None
ipd_balance = None
for item in insurance_ipd_opd:
    if item['url'] == 'OPDBalance':
        opd_balance = item['valueString']
    elif item['url'] == 'IPDBalance':
        ipd_balance = item['valueString']


item2 = insurance2["item"][0]
benefit2 = item2["benefit"][0]
allowed_money2 = benefit2["allowedMoney"]["value"]
used_money2 = benefit2["usedMoney"]["value"]
category2 = item2["category"]["text"]

b = {
    "schema2": [
        {
            "name": f"{name2}",
            "balance": f"{balance2}",
            "OPDBalance": f"{opd_balance}",
            "IPDBalance": f"{ipd_balance}",
            "allowedMoney": f"{allowed_money2}",
            "usedMoney": f"{used_money2}",
            "category": f"{category2}"
        }
    ]
}
print(b)
