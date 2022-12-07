

def reformat_string(s):
  half1 = s[:int((len(s))/2)]
  half2 = s[int((len(s))/2):]
  s = half1[::-1].lower() + half2[::-1].lower()
  print (s)

reformat_string('Hello')
reformat_string('Data')
