import re

text = "In LPA2-reconstituted MEF cells lacking LPA1    '3 the levels of gamma-H2AX decreased rapidly, whereas in Vector MEF were high and remained sustained."

print(re.sub(r'\s+', ' ', text))
print(text)
