import requests

url = "https://diagnosis.p.rapidapi.com/api/DDxItems/GetSymptoms"

querystring = {"AuthenticationID":"DEMO_AuthenticationID"}

headers = {
	"X-RapidAPI-Key": "59ac7d2cadmsh664b50412aa531bp133fd0jsn1da9685dbdb5",
	"X-RapidAPI-Host": "diagnosis.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.json())
def symptoms():
    for symptom in response.json():
        #print(symptom)
        stext = symptom.get("symptom")
        if ("[" not in stext):
            print(stext.strip() + ": " + symptom.get("category"))