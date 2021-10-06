#
# write to files
#
# file.tell()  -> current cursor position in the file
# file.seek(offset,position)  -> change cursor position in the file
#   offset  -> number of chars
#   position -> 0 - start of the file
#               1 - current position    ( offset should always be 0 with this option )
#               2 - end of the file     ( offset should always be 0 with this option )
# seek(5,0) -> go to 5 characters from the start of the file
# seek(0,2) -> go to 0 characters from the end of the file
#
# open modes: r, w, a, r+, w+, a+
#
# r => pointer at begining of file, file should exist, read
# r+ => pointer at begining of file, file should exist, read + write
#
# w => pointer at begining of file, creates a new file if it doesn't find it, write
# w+ => pointer at begining of file, creates a new file if it doesn't find it, write + read
#
# a => pointer at the end of file, creates a new file if it doesn't find it, write at the end
# a+ => pointer at the end of file, creates a new file if it doesn't find it, write + read
#


file = open( "write1.txt", "w" )    # !!! use "w" for new files. "w" will delete the contents of the file, if this already exists !!!

file.write("Hello world of files.\n")
print( file.tell() )  # 23

# file.read()   # io.UnsupportedOperation: not readable

file.close()


# w+
# write and read
file = open( "write1.txt", "w+" )    # !!! use "w" for new files. "w" will delete the contents of the file, if this already exists !!!

file.write("Hello world of files.\n")
print( file.tell() )  # 23

print( file.read())   # ""

file.seek(0)    # start of file ``

print( file.read())    # Hello world of files.

file.close()




# r+
# read + write
# unlike w and w+ , r+ will maintain the content of the file and you can also write to the file

file = open( "write1.txt", "r+" )
content = file.read()
print("\n\nr+ :\n", content)

file.write( "\n\nText added using \"r+\" mode.\n" )

file.seek(0,0)

content = file.read()
print("New content: \n", content)
file.close()


#
# a, a+   ->  by default, the pointer is at the end fo the file
# r, r+, w, w+   ->  by default, the pointer is at the begining of the file
#
file = open( "write1.txt", "a+" )
print( file.tell() ) # 56
file.close()
