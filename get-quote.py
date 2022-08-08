import random
def primary():
   print("Keep it logically awesome.")
     last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)

if __name__== "__main__":
  primary()
