travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visited,n,list):
    di={}
    di["country"]=country_visited
    di["visits"]=n
    di["cities"]=list
    travel_log.append(di)
    return travel_log
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
#this program adds a new country to the list of dictionaries!