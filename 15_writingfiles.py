intro_file = open('document/2_test.txt','w')
intro_file.write('hello world from sardar uzair')
intro_file.close()

new_file = open('document/3_test.txt','w')
new_file.write('hello world this is created from pyton by sardar uzair')
new_file.close()

append_file = open('document/4_test.txt','a')
append_file.write('\ni am a python programmer')
append_file.close()

python_file = open('document/5_test.py','w')
python_file.write('print(\'hello this is python file created by programe\')')
python_file.close()

# important note for this lesson
# .wirte() canm write the file but replace the content and write new content
# we can create new file with content by usi9ng write function
# a flag is used to appened the files
#  \n is used to go in the new line
#  \\ is used to wrinte the code in strings