#split string in half
s = s[:(len(str))//2] #even
s = s[:(len(str)-1)//2] #odd

#remove duplicates from string
s ="heellloooh"
print("".join(dict.fromkeys(s)))  #outputs "helo"
