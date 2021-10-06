#
# JSON PARSING
#
# json objects : similar to dictionaries {"key":"val"}
# numbers : 10, 12.3, ...  int, float
# array : [10, "hello", ...]  list, tuple,

import json

handle = open( "connection.json", "r" )
content = handle.read()
handle.close()
print(content)


d = json.loads(content)
print(d)
print(d['database'])
print(d['database']['port'])

d['database']['port'] = 8080
print(d['database'])

logfname = d['files']['log']
print("Log file name: ", logfname)

logf = open( logfname, "w" )
logf.write("Test log file.")
logf.close()

d['files']['log'] = ("./log/app.log","./log/appRestart.log")

print("=============================================================")

# Write to a new json file

handle = open( "json_output.json", "w" )
print(d)
# j = json.dumps(d)   # json format for the dictionary d - converts ' to " and () to []
j = json.dumps(d,indent=4,sort_keys=True) # 
print(j)
handle.write(j + "\n")
handle.close()
