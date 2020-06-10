print ( "Введите строку:" )
s = input()
s1 = ""
for c in s:
  if c == "а":
      c = "б"
  s1 = s1 + c
print ( s1 )