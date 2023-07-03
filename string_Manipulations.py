#split string in half
str = str[:(len(str))//2] #even
str = str[:(len(str)-1)//2] #odd

#remove duplicates from string
str ="heellloooh"
print("".join(dict.fromkeys(str)))  #outputs "helo"
