a=input("Enter text to write to the file :\n ")
file1=open('output.txt','w')
writing_file=file1.write(a)
print(writing_file)
file1.close()

b=input("Enter Additional text to append : ")
file1=open('output.txt','a')
appending_file=file1.write(b)
print(appending_file)
file1.close()

file1=open('output.txt','r')
reading_file=file1.read()
print(reading_file)
file1.close()

