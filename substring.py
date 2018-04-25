string1 = 'abcd'
string2 = 'cdabcdab'


def finder(string1, string2):
  temp = string1
  count = 1
  while (temp.find(string2) < 0):
    temp = temp + string1
    count += 1
  return count, temp  

print(finder(string1, string2))
