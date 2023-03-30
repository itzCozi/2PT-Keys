# 2PT is a framework for very secure cryptographic keys people can use this program by draging the file into there
# project or using the installer to install a modified version of this program for easy to use console app
import random
import string
import requests
import time

# Variables
x32_keylength = 24
x64_keylength = 32


class x32key:

  @staticmethod
  def rawkey():
    threshold = random.randint(7, 16)
    buff = random.randint(500, 1000)
    length = random.randint(8, 20)
    iterable = 0
    alphabet = string.digits + string.ascii_letters + string.digits
    baseList = '.'.join(random.choice(alphabet) for i in range(buff)).split('.')

    while iterable != threshold:
      foo = baseList + list(random.choice(alphabet) for i in range(buff))
      for item in range(length):
        random.shuffle(foo)
      iterable += 1

      key = ''.join(random.choice(foo) for iterable in range(x32_keylength))

    return key


class x64key:

  @staticmethod
  def rawkey():
    threshold = random.randint(7, 16)
    buff = random.randint(1000, 5000)
    length = random.randint(16, 20)
    iterable = 0
    alphabet = string.ascii_letters + string.digits
    baseList = '.'.join(random.choice(alphabet) for i in range(buff)).split('.')

    while iterable != threshold:
      foo = baseList + list(random.choice(alphabet) for i in range(buff))
      for item in range(length):
        random.shuffle(foo)
      iterable += 1

      key = ''.join(random.choice(foo) for iterable in range(x64_keylength))

    return key


class hexkey():

  def rawkey():
    threshold = random.randint(7, 16)
    buff = random.randint(1000, 5000)
    length = random.randint(16, 20)
    lengthlist = [3, 4, 6]
    if random.choice([True, False]):
      for item in lengthlist:
        int(random.choice(lengthlist) - 1)
    else:
      pass
    iterable = 0
    alphabet = string.digits + string.ascii_uppercase + string.digits
    baseList = '.'.join(random.choice(alphabet) for i in range(buff)).split('.')

    while iterable != threshold:
      foo = baseList + list(random.choice(alphabet) for i in range(buff))
      for item in range(length):
        random.shuffle(foo)
      iterable += 1

      key = str('0' + 'x' + ''.join(
        random.choice(foo) for iterable in range(random.choice(lengthlist))))

    return key


class wordkey():

  def rawkey():
    buff = random.randint(1000, 5000)
    wordamount = random.randint(1, 3)
    foo = []
    wordlist = []
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    baseList = response.content.splitlines()

    for i in range(wordamount):
      foo.append(random.choice(baseList).decode('utf-8'))
    for item in foo:
      item = item.capitalize()
      wordlist.append(item)

    key = ''.join(wordlist) + str(random.randint(150, 999) - 75)

    return key


def split_key(key):
  keylist = list(key)
  returnkey = []
  n = 4

  for index in range(0, len(keylist), n):
    returnkey.append(''.join(keylist[index:index + n]) + '.')
  formattedKey = ''.join(returnkey)
  return ''.join(formattedKey[0:-1])


def createkey(type):
  if type == 'x32':
    return split_key(x32key.rawkey())
  elif type == 'x64':
    return split_key(x64key.rawkey())
  elif type == 'hex':
    return hexkey.rawkey()
  elif type == 'word':
    return wordkey.rawkey()
  else:
    return 'ERROR: Invalid key type'


while True:
  time.sleep(0.7)
  print(wordkey.rawkey())