

def encode_str(s):
  i = 0
  sum = ''
  a = list(s)
  c = len(list(s))

  if c % 2 == 1:
    c +=1

  while i < int(c/2):
    sum += a[i]
    i += 1
    if len(list(s)) % 2 == 0 or i <= (int(c/2) - 1):
      sum += a[-i]
  print (sum)


def decode_str(s):
  sum1 = ''
  sum2 = ''
  count = 0

  for text in s:
      count += 1
      if (count % 2 == 1):
        sum1 += text
      else:
        sum2 = text + sum2
  print(sum1 + sum2)

encode_str("sandwich")
encode_str("12345678")
encode_str("123456789")
print("")
decode_str("shacnidw")
decode_str("18273645")
decode_str("192837465")
