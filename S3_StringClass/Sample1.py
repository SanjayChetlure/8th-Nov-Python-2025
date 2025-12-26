
s1="velocity"
s2="ABCD"
s3="abcd"
s4="my name is abc"
s5="abcaba"
s6=" hi "
s7="1234"
s8="abc123"
s9="  "
s10="my name is abc is abc"


print(s3.capitalize())        #Velocity  -> capitalize 1st char of string
print(s4.title())            #converts first char of each word to uppercase

print(s1.isalpha())        #true
print(s7.isdigit())        #true
print(s8.isalnum())        #true
print(s9.isspace())        #true
print(s10.count("i"))     #2
print("----------------")

print(s2+s3)      #ABCDabcd        #combine multiple strings

print(s6)
print(s6.strip())      #remove spaces from left & right side
print(s6.lstrip())     #remove spaces from only left side
print(s6.rstrip())     #remove spaces from only right side

print(s4.replace("abc","xyz"))

print("---------------------")

print(s1[1])              #get single character
print(s1[3:6])            #[startIndex:endIndex+1]   get multiple chars

print(s5.find("b"))       #1  get index of 1st occurrence char from left side
print(s5.index("b"))      #Alternate method for find
print(s5.rfind("b"))       #4  get index of 1st occurrence char from right side


print("------------")
print(len(s1))             #8

# s1=s1.upper()     #VELOCITY   -> re initialization
print(s1.upper())      #VELOCITY
print(s1)

# s2=s2.lower()
print(s2.lower())      #abcd
print(s2)

print("----------")

print(s2==s3)                        #compare data & case
print(s2.__eq__(s3))                 #compare data & case
print(s2.lower()==s3.lower())        #compare only data
print("------------")

print("ci" in s1)                   #true
print(s1.__contains__("ci"))        #true
print("is" in s4)
print(s4.__contains__("is"))
print("--")

print(s4.startswith("my"))        #true
print(s4.endswith("abc"))        #true
print("------------")





