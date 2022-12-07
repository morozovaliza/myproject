

def replace_characters(s):
  a = s[:s.find('g') + 1] 
  b = s[s.find('g') + 1:]
  s = a + b.replace('g', 'G')
  print (s)

replace_characters('In the hole in the ground there lived a grey ghost')
