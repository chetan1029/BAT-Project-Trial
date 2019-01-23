import requests

p_data = []
p_data1 = {}
p_data1["name"] = "Chetan"
p_data1["gender"] = "male"
p_data.append(p_data1)

p_data1 = {}
p_data1["name"] = "Sdd"
p_data1["gender"] = "male"
p_data.append(p_data1)

shipment_data = {
"LabelPrepPreference": "SELLER_LABEL",
"shipment_product": p_data
}

response = requests.post("http://174.138.71.123/amazon/shipments/test.php", json=shipment_data)
data = response.json()
print(data)
