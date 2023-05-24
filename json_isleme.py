import json

file = open("personel.json", "r")

data = json.load(file)

# print(data["personel"][2])

# for p in data["personel"]:
#     print(p["ad"])
#     print(p["maas"])

data["personel"].append({"ad" : "Betul", "soyad" : "Bayram", "yas" : "21", "pozisyon": "engineer", "maas": 0})

print(data["personel"])

json_object = json.dumps(data)

output_file = open("yeni-kayit.json", "w")

json.dump(data, output_file)
