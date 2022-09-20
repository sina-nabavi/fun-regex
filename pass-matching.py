import re

txt = "HardpassL2@@"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$", txt)

print(x)

if x:
  print("Pass Changed.")
else:
  print("Password must include lower, upper chars and digit and between 6,12!")
