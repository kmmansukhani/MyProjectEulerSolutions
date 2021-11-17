'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

numletters = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
              10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen", 18: "eighteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def getLettersGivenNum(n):
    if n == 1000:
      return "one thousand"
    if n in numletters:
        return numletters[n]
    str_n = str(n)
    result = ""
    for i in range(len(str_n)):
      if len(str_n) - i == 3: #hundred
        result += numletters[int(str_n[i])] + " hundred" + " and"
      if len(str_n) - i == 4: #thousand
        result += numletters[int(str_n[i])] + " thousand " + "and"
      if len(str_n) - i == 2: #tens
        if str_n[i] == "0": #if no tens
          continue
        else:
          if str_n[i] == "1": #if between 10 - 19
            if int(str_n[i:i+2]) in numletters:
              result += numletters[int(str_n[i:i+2])]
            else:
              result += numletters[int(str_n[i+1])] + "teen"
            return result
          else: #if between 20 - 99
            result += numletters[int(str_n[i:i + 1] + "0")]

      if len(str_n) - i == 1:
        if str_n[i] != "0":
          result += numletters[int(str_n[i])]
    if result.rfind("and") == len(result) - 3:
      return result[:i-5]
    return result

count = 0
for i in range(1, 1001):
  l = getLettersGivenNum(i)
  for c in l:
    if c.isalpha():
        count += 1
print(count)
