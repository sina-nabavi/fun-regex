import re

txt = "<a> hello </a>"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall("<([\w]+).*>(.*?)<\/(\1)>", txt)

print(x)

if x:
  print("Valid URL.")
else:
  print("Invalid URL!")

## TURNS OUT WE CAN'T PASS CAPTURING GROUP NUMBERS IN FINALL AND WE 
## HAVE TO ITER OVER THEM LATER
