
# open( file_path_and_name , open_parameter )
#
# The open_parameter can be : r, w, a, r+, w+, a+
#
# file.read()
# file.readline()
# file.readlines()


file = open( "plato_the_apology.txt", "r" )

#rd = file.read()    # reads the whole file
#print(type(rd)) # <class 'str'>
#print( file.read(11) ) # THE APOLOGY


res2 = file.readline()  # read a single line
print( type(res2) )
print( res2 )
print( file.readline() )


res = file.readlines()  # reads the whole file
print( type(res))   # <class 'list'>

print( res[:5] )    # Every line in the file is an entry in the list, based on the "\n" character

file.close()
