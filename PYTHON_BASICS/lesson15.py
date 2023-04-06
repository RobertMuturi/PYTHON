#JSON (JavaScript Object Notation) Python Library
import json

#JSON format data
data = '{"Name":"Paul", "Age": 42, "Work": "NGO"}'

#Make JSON data accessible as Python data type json.loads(data_varible)
converted_json_data = json.loads(data)
print("Converted data: ",converted_json_data)
print("Person name: ", converted_json_data['Name'])
print("Person age: ", converted_json_data['Age'])
print("Person work: ", converted_json_data['Work'])

#Convert to JSON from Python json.dumps(data_varible)
data_python = {"UserID": 24343, "Username": "elizath", "Location":"Nairobi"}
json_data = json.dumps(data_python)
print("Data converted to JSON from Python Dictionary: \n ", json_data)
print(type(json_data))

#Converting different Python objects (data types) to JSON format
print(json.dumps(['Jack', 34, 'JKUAT']))
print(json.dumps(('Eliza', 20, 'Juja')))
print(json.dumps('We are learning JSON conversion'))
print(json.dumps(100))
print(json.dumps(23.457))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

python_data = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#print("Convert to JSON: ", json.dumps(python_data))
#print(json.dumps(python_data, indent=4, separators=(" . ", "=")))
#Sort data in JSON format
print(json.dumps(python_data, indent=4, separators=(" . ", "="), sort_keys =True))


###RegEX Library - to check search pattern - eg. email format (string@company.com)
import re
text = "We are learning Regular Expression"
search_pattern = re.search("^We.*Expression$", text)

if search_pattern:
    print("Correct match")
else:
    print("No correct match")
#Finding a specific word/keyword (number of occurences)
some_text ="""
Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")
"""

search_keyword = re.findall("the", some_text)
print("'The' Keywords: ", search_keyword)
print("'The' Appears {} Times".format(len(search_keyword)))
                          

