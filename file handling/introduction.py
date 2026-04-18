#file handling is the process of handing the file or storing the data into the permanent storage
#files-files stores the data like audio,vedio,text
#files are of two types-
#1.Text files and human redable file
#2.binary files and machine readable file(human non-readable)

#file read
#here we are opening the file into the resd mode
#it means the file or script has only access to read the file
#mode-access
#open("filepath","mode")
#file=open('file.txt',"r")
#with the . read function or method we basically read all the contenst of the file
#content=file.read()
#readline is basically used for reading the content line by line
#content1=file.readline()
#print(content1)

#print(content)
#after performing all the opwration on the file we have to clase the file by using the file.close()
#file.close()

#read lines this function returns the list of all the lines which is stored into the file \
#read function return all the text and content of the file in text form
#readline this function returns one by one line(one line at a time)
file=open("file.txt","r")
content=file.readlines()
print(content) 
#whenever we read or write a flie then the sciprt users the pointer to iterate over thr file to read or write the content of the file 

#whever we want to read or check the position of the pointer then we have to user file.tell()method.
print(file.tell())
# whenever we want to  move the poinyer at some position ,we use file.seek(position)
file.seek(25)

#read about all the modes of the file handling
#write,append,update,delete

#write mode -writing content into the file using the script of the python
#write mode is used to write the content into the file
#if the file dosent exist then it creates the file and then write the content to the file
#.write() method is used to write the content into the filr which takes the argument as an string
#file.write("this is the content i have to write in the file")
file=open("write.txt","w")
file.write("this is the content from the write function")
#file.close()

#writelines
#.writelines method is used to write multiple lines which are stored into the list.
#in write method every thig is over written by the new content
file.writelines(["this is the 1st line\n","this is the second line"])

#append mode
#into the append mode we basically add new lines or write new into the files without over writting the content
file=open("write.txt","a")
file.write("\n this is new line\n")
file.close()

#"r+" mode=this mode enables the system to read and write
#in the r+ mode if the file dosent exist then it will throw an exception or error will raise.
file=open("write.txt","r+")
file.write("this is the new content\n")
file.seek(0)
content=file.read()
print(content)
file.close()

#"w+"mode-in this mode if the file dosent exist then it creates a file and then read it rather than throeing an error

#append =in this mode we can add the data into the file in the end and through this we can only add the content we can not read it
#append "a+"=in this method we can also add the content in file at the end and we can read it also



#context manager-"with " statement is used in file handling which opens the file and what ever the task has done in to with  block then after the file is automatically closed
with open ("write.txt","r") as file:
    content=file.read()
print(content)
content=file.read() #it will give the error because file is closed now

print(content)