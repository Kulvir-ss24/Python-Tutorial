#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#String is a data type that stores a sequence of characters.
#It is a collection of characters that can be letters, numbers, or special characters.
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
"BASIC OPERATIONS"
#CONCATENATION - Concatenation is the process of combining two or more strings into a single string.
c="kulvir" + "singh"    #make sure identifiers must be defined before the string values[example - 'c' is an identifier described before the string value]
print("The string we get after concatenation: ", c)
print("what is the datatype: ", type(c))  #for checking datatype of the output
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------FIND LENGTH OF A STRING-------------------------------------
#--------------------------------------------------------------------------------
#------------IN PYTHON WE COUNT THE VALUE OF STRING THROUGH '1'------------------
#------------IN PYTHON WE COUNT THE VALUE OF STRING THROUGH '1'------------------
#Length - The length of a string is the number of characters it contains.
len("kulvir")           #IT STARTS COUNTING FROM 1 BECAUSE k,u,l,v,i,r ARE 6 CHARACTERS
print("The length of the string is: ", len("kulvir")) #OUTPUT IS 6
#--------------------------------------------------------------------------------
#------------------------FIND LENGTH OF A STRING?---------------------------------
#------------IN PYTHON WE COUNT THE VALUE OF STRING THROUGH '1'------------------
#------------IN PYTHON WE COUNT THE VALUE OF STRING THROUGH '1'------------------
str1="My name is kulvir"
length=len(str1)
print("The length of the string is: ", length) #OUTPUT IS 17
#Because spaces will also be counted as you can seen in 'str1'
str2="My name is Alex"
length=len(str2)
print("The total length is: ", length) #OUTPUT IS 15
#--------------------------------------------------------------------------------
#LET'S HAVE SOME TWIST
final_str=str1 + " " + str2   #SPACING IS ADDED BETWEEN THE TWO STRINGS 
#SPACE WILL ALSO BE COUNT AS LENGTH SO MAKE SURE IF YOU WANT TO CALCULATE FULL LENGTH THEN DON'T ADD ANY SPACE BETWEEN THE STRINGS.
print(final_str)      #My name is kulvir My name is Alex
print(len(final_str))  #33
#-----HERE'S WE HAVE SEEN HOW TO CONCATENATE & FIND LENGTH OF A STRING-----------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#----------------------WAYS OF ACCESSING STRING CHARACTERS-----------------------
#--------------------------------------------------------------------------------
str="My name is kulvir" #widely these kind of double quotes were used mostly
str1='My age is 21'
str3="""Teaching Python"""
print(str+" "+str1+" "+str3)  #it will print all str,str1,str3 together [called as string concatenation]
print(str+"\n"+str2+"\n"+str3)  #SEE HOW WE USED \n FOR NEW LINE THAT IS ESCAPE SEQUENCE CHARACTER
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------WHAT IS USE OF STRING?--------------------------------
#---------------------------------------------------------------------------------
"Today's is my second day"
'Somebody doesn"t know me'
"""Somebody doesn"t know me"""  #whenever use double quotes in between the string make sure to put the sntence in triple quotes [Recommended By Me]
#I HOPE YOU UNDERSTOOD THE CONCEPT PROPERLY
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#--------------SUPPOSE WE HAVE TO WRITE ALL SENTENCES IN ONE STRING!!!!-----------
#---------------------------------------------------------------------------------
"BUT WE WANT TO PRINT THE SENTENCE IN NEXT LINE"
#TO DO THIS WE WILL USE ESCAPE SEQUENCE CHARACTERS THAT IS WIDELY USED IN PYTHON
"SUCH AS \n"  #\n - backslash n
#----------------------EXAMPLE FOR YOU--------------------------------------------
print("Hello, world!\nThis is my first Python program.\nI am learning Python.")
#Hello, world!
#This is my first Python program.
#I am learning Python.
"IT WILL PRINT ALL SENTENCES IN NEXT LINE AFTER \n"
#CAN BE USED WHEN WRITING LARGE PARAGRAPHS THEN THIS \n WOULD BE VERY USEFUL
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---ONE PROGRAM IS HERE FOR SWAPPING TWO VALUES [IMPORTANT INTERVIEW QUESTION]----
#---------------------------------------------------------------------------------
a=int(input("Before Swapping a:"))
b=int(input("Before Swapping b: "))
temp=a
a=b
b=temp
print("After Swapping a:",a)
print("After Swapping b:",b)
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#------------ONE MORE PROGRAM TO PRINT LENGTH OF AN ARRAY [imp question]----------
#---------------------------------------------------------------------------------
"taking array as an variable"
array=["car","bike","boat","plane"]
x=len(array) #x is a random variable
print(x)       #output is 4 because there are 4 elements in array each separated by comma
#-------------MAKE SURE WE COUNT FROM '1' TO FIND THE LENGTH----------------------
arr=[1,2,3,4,5,6]
x=len(arr)
print(x)  #output is 6 because we have to be counted from 1 and in this 'arr' has 6 elements
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#-------------------------SO LET'S MOVE ON FURTHER--------------------------------
#---------------------------------------------------------------------------------
#------------------WHAT IS INDEXING?-----INDEXING---------------------------------
#----------------------STARTS FROM 0----------------------------------------------
#----------------------STARTS FROM 0----------------------------------------------
#----------------------STARTS FROM 0----------------------------------------------
#----------------------STARTS FROM 0----------------------------------------------
#------------------------------INDEXING--WE FIND ONLY POSITIONS-------------------
#INDEXING IS USED TO ACCESS THE STRING CHARACTERS
#IT CAN ALSO ACCESS SPECIAL CHARACTERS '_' AND '.' OR THE SPACES IN BETWEEN
"IN PYTHON INDEXING STARTS FROM 0" #python mei strings ki numbering 0 se shuru hoti hai instead of '1'
#---------------------------------------------------------------------------------
"LET'S SEE HOW INDEXING HELPS US?"  #YANI KONSA INDEX PE VALUE LIE KRTI HAI USKI POSITON KA PTA LGATE HAI YAHA
#IT HELPS US TO ACCESS CHARACTER POSITION
str="pythontutorial"
index_value=str[3]    #count starts from 0
print(index_value) #output is 'h' because at 3rd position there is 'h'
#let's find character repeated here
print(str.count('t'))  #Always use quotes if finding count for a string/letter
#output is 3 because letter 't' is repeated 3 times in the string
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#----PROGRAM OF ARRAY - IT EVENTUALLY COMES IN MY MIND SO I AM WRITING IT HERE----
"HOW TO FIND THE REPETATION OF A CHARACTER OR NUMBER"
arr[3]=[1,2,3,4]
print(arr.count(3)) #Repeated no of '3' in array it is '1' times repeated
#output 1
#---------------------------------------------------------------------------------
string=[1,2,3,4,5,6,7,8]
#count starts from 0
number=string[3]   #here we are accessing position number '3' in the index of an array
print(number) #output is 4 because at position '3' there is 4
#---------------------------------------------------------------------------------
"LET'S DO IT WITH ARRAY"
arrlen=['list','orange','juice','drink']
trick=arrlen[3]  #it will take 'drink' as an index value
print(trick) #output is 'drink' 
#because at position '3' there is 'drink'
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#-------------------------LET'S MOVE ON FURTHER-----------------------------------
#---------------------------------------------------------------------------------
#------------------WHAT IS SLICING?-----SLICING-----------------------------------
#---------------------------------------------------------------------------------
#-----------SLICING IS WIDELY USED IN MACHINE LEARNING ALGORITHMS TO DEAL WITH COMPLEX INFORMATION------------------------------------
#---------------------------------------------------------------------------------------
#-------------------------SLICING IS USED TO ACCESSING PARTS OF A STRING----------------
#---------------------------------------------------------------------------------------
str="kulvir tutorial"
print(str[7:len(str)])   #we used len(str) because we want to access till the last character length so it will be easier as per my view
#or it can be written as
print(str[7:14]) #it will print 'tutorial' because it will access from 7th index to 13
# print(len(str)) #just for checking total length of the string that is '15' including spaces
#one for example to reach the last index------------------------------------------------
example="python batch"
print(example[7: ]) #[7:12] --- here the last index number doesn't count keep in mind while doing indexing [7:len(example)]
print(example[:6])  #[0:6] --- here the first index number is by default '0' while not listing & last index number doesn't count.
print(example[0:12]) #it will print 'python batch' because it will access from 0th index to 11
print(example[0:len(example)]) #it will print the same as 'python batch'
#make sure last index number doesn't count ever in python
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#-------------------------NEGATIVE INDEXING IN SLICING----------------------------------
#-----------------------------THESE ARE USED WHEN WE DON'T KNOW THE ACTUAL LENGTH OF THE STRING OR AN IDEA------------------------
"NEGATIVE INDEXING CAN BE USED FOR BACKWARD COUNTING AS WE ARE DOING FORWARD INDEXING IN POSITIVE INDEXING CHECK ABOVE--------"
#example [Apple] but index count will be [-5,-4,-3,-2,-1]
apple="Apple"
print(apple[-5:]) #it will print 'Apple' because it will access from -5
#as per the rule last index '-1' doesn't be counted [-5:-2]#example
print(apple[-5:-3]) #it will print 'ap' because last -3 index doesn't count
print(apple[ ::-3]) #it will print 'ppA' because it can count last digit 'p' as -3 index because of [::]
#reverse indexing is used to access the string from right to left
"IF you want help to learn concept of negative indexing in reverse order conact me - kulvirsingh.s2411@gmail.com"
"example [ :: -2] this works actually all you can ask there"
#--------------------------------------------------------------------------------------
"AND TO PRINT PRINT THE REVERSE STRING IN A SEQUENCE"
print(apple[ ::-1]) #it will print 'elppa' because it will access from -1 to -6 
"it is compulsory to put :: before -1 or last value to get the reverse string"
#---------------------------------------------------------------------------------------
app="valorant"
xyz=app[-9:len(app)]  
print(xyz)   #it will print 'valorant'
abcd=len(xyz)  
print(abcd)  #the output is 8 
#for reverse of str
print(app[len(xyz)::-1]) #it will print 'tnarolav' either it can be written as 'print(app[ ::-1])', the value is same as 'tnarolav'
#str="apple"
#str[-5:-1] is "appl". Here 'e' will not count because of the last element in the indexing
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-------STRINGSSSSSSSSSSSSSSSSSSSS OFFFFFFFFFFFF FUNCTIONSSSSSSSSSSSSSSSSSSSSS------------
#-------STRINGSSSSSSSSSSSSSSSSSSSS OFFFFFFFFFFFF FUNCTIONSSSSSSSSSSSSSSSSSSSSS------------
#-------STRINGSSSSSSSSSSSSSSSSSSSS OFFFFFFFFFFFF FUNCTIONSSSSSSSSSSSSSSSSSSSSS------------
#-------STRINGSSSSSSSSSSSSSSSSSSSS OFFFFFFFFFFFF FUNCTIONSSSSSSSSSSSSSSSSSSSSS------------
#-------STRINGSSSSSSSSSSSSSSSSSSSS OFFFFFFFFFFFF FUNCTIONSSSSSSSSSSSSSSSSSSSSS------------
#-------STRINGSSSSSSSSSSSSSSSSSSSS OFFFFFFFFFFFF FUNCTIONSSSSSSSSSSSSSSSSSSSSS------------
# ------------------SERIES CONTINUES------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-------------------------STRINGS WITH FUCTIONS-------------------------------------------
#-----------------------------------------------------------------------------------------
