

def delete_duplicates(s):
  li = []
  [li.append(x) for x in s.split() if x not in li]
  print (' '.join(li))

delete_duplicates('yellow grey white yellow black grey grey red')
