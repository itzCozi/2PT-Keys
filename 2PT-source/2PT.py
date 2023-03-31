# 2PT is a framework for very secure cryptographic keys people can use this program by draging the file into there
# project or using the installer to install a modified version of this program for easy to use console app
import random
import string
import requests

# Variables
x32_keylength = 24
x64_keylength = 32


class x32key:

  @staticmethod
  def x32_rawkey():
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

    return str(key)


class x64key:

  @staticmethod
  def x64_rawkey():
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

    return str(key)


class hexkey():

  @staticmethod
  def hex_rawkey():
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

      key = str('0' + 'x' + ''.join(random.choice(foo) for iterable in range(random.choice(lengthlist))))

    return str(key)


class wordkey():

  @staticmethod
  def word_rawkey():
    wordamount = random.randint(1, 3)
    foo = []
    shortlist = []
    wordlist = []
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    baselist = response.content.splitlines()

    for word in baselist:
      if len(word) <= random.randint(6, 12):
        shortlist.append(word)
      else:
        pass
    for i in range(wordamount):
      foo.append(random.choice(shortlist).decode('utf-8'))
    for item in foo:
      item = item.capitalize()
      wordlist.append(item)

    key = ''.join(wordlist) + str(random.randint(175, 9999) - 75)

    return str(key)


def split_key(key):
  if not isinstance(key, str):
    raise TypeError('`key` parameter must be a string object')

  keylist = list(key)
  returnkey = []
  n = 4

  for index in range(0, len(keylist), n):
    returnkey.append(''.join(keylist[index:index + n]) + '.')
  formattedKey = ''.join(returnkey)
  return ''.join(formattedKey[0:-1])


def createkey(type):
  if not isinstance(type, str):
    raise TypeError('`type` parameter must be a string object and a valid option.')

  if type == 'x32':
    return split_key(x32key.x32_rawkey())
  if type == 'x64':
    return split_key(x64key.x64_rawkey())
  if type == 'hex':
    return hexkey.hex_rawkey()
  if type == 'wrd':
    return wordkey.word_rawkey()
  else:
    return 'ERROR: Invalid key type'

