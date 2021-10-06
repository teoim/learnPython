#
# XML PARSING
#
# 1. Install xml package (from cmd):
#   pip install xmltodict
#   import xmltodict into the project

import xmltodict

xmlfile = open( "notes.xml", "r" )

content = xmlfile.read()
#print(content)

d = xmltodict.parse( content)
print(d)

print("\n", d["document"]["note"])
print("\n", d["document"]["note"]["from"])  # Jani
print("\n", d["document"]["note"]["to"])    # Tove
print("\n", d["document"]["note"]["body"])  # Don't forget me this weekend!

d["document"]["note"]["from"] = "Tove"
d["document"]["note"]["to"] = "Jani"
d["document"]["note"]["body"] = "Ok coglione!"

print("\n", d["document"]["note"]["from"])  # Tove
print("\n", d["document"]["note"]["to"])    # Javi
print("\n", d["document"]["note"]["body"])  # Ok coglione!

xmlfile.close()

# You changed something and want to save the changes to the file
# xmltodict.unparse() converts from dictionary to xml

xmlfile = open( "notes_output.xml", "w" )

#xmlTxt = xmltodict.unparse(d, xmlfile, encoding="utf-8", pretty=True)  # will print directly to the file
xmlTxt = xmltodict.unparse(d, pretty=True)  # pretty=True : new lines and indents 
print(xmlTxt)

xmlfile.write( xmlTxt)

xmlfile.close()
