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
#Length - The length of a string is the number of characters it contains.
len("kulvir")           #IT STARTS COUNTING FROM 1 BECAUSE k,u,l,v,i,r ARE 6 CHARACTERS
print("The length of the string is: ", len("kulvir")) #OUTPUT IS 6
#--------------------------------------------------------------------------------
#------------------------FIND LENGTH OF A STRING---------------------------------
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
#---------------------------------------------------------------------------------
#-------------------------SO LET'S MOVE ON FURTHER--------------------------------
#---------------------------------------------------------------------------------
