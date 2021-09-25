from platform import system as platform
import random

if __name__ == "__main__":
  os = platform()
  print(os)
  type = ["good", "not bad", "bad OS", "I don't know"]
  print("type:" + random.choice(type))
  exit()
