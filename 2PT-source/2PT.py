# 2PT is a framework for very secure cryptographic keys people can use this program by draging the file into there
# project or using the installer to install a modified version of this program for easy to use console app
import random
import string
import hashlib

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
  else:
    return 'ERROR: Invalid key type'

