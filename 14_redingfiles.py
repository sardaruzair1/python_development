lang_File = open('document/1_test.txt' , 'r')

# print(lang_File.readable())
# print(lang_File.readline())
# print(lang_File.readlines()[3])
# print(lang_File.readlines())

# read files through loopin on it

for file in lang_File.readlines():
    print(file)

lang_File.close()




# importtant note
# .readable() is return true or false
# .readline() is return the first line of the file and if we used it gain it print another line 
# .readlines() is return all the lines which is in the file and it can print it in the list formate we can also apply indexing on it

# for is a loop used to print the readed files by using loop we can priont files in proper files order

