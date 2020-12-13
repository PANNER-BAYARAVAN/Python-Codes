dict = {'Name': 'John', 'Age': 19, 'Passport': 'A5645455'}

print (dict)

released = {
"iphone" : 2010,
"iphone 3G" : 2011,
"iphone 3GS" : 2012,
"iphone 4" : 2013,
"iphone 4S" : 2014,
"iphone 5" : 2016
}
print (released)

released["iphone 5S"] = 2017
print (released)


del released["iphone"]
print (released)

for key,val in released.items():
    print (key, "=>", val)
