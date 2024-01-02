string = (""
          
          ""
          "")
sstring = ""
s = "aaaaa"
num = 0
for i in string:
    if i != '$' and num % 2 == 0:
        sstring += i
    elif i == '$':
        num += 1
        if num % 2 == 0:
            sstring += s

print(sstring)
