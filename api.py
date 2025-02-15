import requests
import zipcodes

secret_key = "KD3HKABEPM6SMYXU3YHLFVE4Z"

zipcode = input("Enter a zipcode: ")

extracted_zip = zipcodes.matching(zipcode)[0]

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{zipcode}?unitGroup=us&key=KD3HKABEPM6SMYXU3YHLFVE4Z&contentType=json"

r = requests.get(url)
#print(r)

resp = r.json() 

#print(resp["days"])

days = resp["days"]

print("Current Zipcode: " + zipcode)

print("City: " + extracted_zip["city"])
print("County: " + extracted_zip["county"])

for day in days: 
    #print(day["tempmax"])
    #print(day["tempmin"])
    #print(day["temp"])
    print(
        "Date: " + day["datetime"] + " " + "High: " + str(day["tempmax"]) + " " + "Low: " + str(day["tempmin"]) + " " + "Average: " + str(day["temp"])
          )

# TODO: Modify API Call to take in user input of zip-code