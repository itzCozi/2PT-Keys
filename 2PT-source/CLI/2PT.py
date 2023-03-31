# Gotta make 2PT console app. Links: https://github.com/itzCozi/Terminal-Bypass-Game (Also check if scoop is installed and if not, install it)
try:
  import random
  import string
  import requests
  import os, sys
  import hashlib
  import subprocess
except:
  raise ImportError('Please install the required packages: hashlib, subprocess, request and random')

# Variables
x32_keylength = 24
x64_keylength = 32
debug = True


class _2PT():
  main_Dir = str('C:/Users/' + os.getlogin() + '/2PT-Keys')
  scoop_Dir = str('C:/Users/' + os.getlogin() + '/scoop')
  scoopApp_Dir = str(scoop_Dir + '/apps/2PT-Console')
  scoopShim_File = str(scoop_Dir + '/shims/2PT.cmd')
  powershell = str('C:\Windows\System32\powershell.exe')
  scoopApp_File = str(scoop_Dir + 'apps/2PT-Console/2PT-console.py')

  def autoUpdate():
    # Compares the hashes of the main file and the file on the website. And if they are not the same replace them
    webFile = _2PT.utility.hashFileURL('https://itzcozi.github.io/2PT-Keys/data/2PT-console.py')
    scoop_Dir = str('C:/Users/' + os.getlogin() + '/scoop')
    localFile = _2PT.utility.hashFileLOCAL(_2PT.scoopApp_File)

    if webFile != localFile:
      if debug:
        print("Program files !OUTDATED!")
        print("Updating Program Files...")

      # Update file
      with open(scoop_Dir + 'apps/2PT-Console/2PT-console.py', "w") as f:
        f.truncate(0)
        f.write(
          requests.get('https://itzcozi.github.io/2PT-Keys/data/2PT-console.py').text)
        f.close()

      if debug:
        print("Program Successfully Updated!")

  def setup():
    if os.path.exists(_2PT.scoop_Dir):
      print("Scoop is already installed. ")
      pass
    else:
      # NEEDS TESTING ON PC : https://www.makeuseof.com/windows-install-scoop/?newsletter_popup=1
      subprocess.call(_2PT.powershell + 'iwr -useb get.scoop.sh | iex, shell=False')

    os.mkdir(_2PT.main_Dir)
    os.mkdir(_2PT.scoopApp_Dir)

    if not os.path.exists(_2PT.scoopShim_File):
      with open(_2PT.scoopShim_File, 'w') as file:
        file.write('@' + _2PT.scoopApp_File + ' %*')
      if debug:
        print("Program file [" + _2PT.scoopShim_File + "] !MISSING!")

    if not os.path.exists(_2PT.scoopApp_File):
      _2PT.utility.install(
        "https://itzcozi.github.io/2PT-Keys/data/2PT-console.py",_2PT.scoopApp_File, "2PT", ".cmd")
      if debug:
        print("Program file [" + _2PT.scoopApp_File + "] !MISSING!")

  
  class utility():

    def hashFileURL(url):
      newFile = str('C:/Users/' + os.getlogin() + '/2PT-Keys/newfile')

      with open(newFile, "w") as f:
        f.write(requests.get(url).text)
        f.close()

      BUF_SIZE = os.path.getsize(newFile)
      sha256 = hashlib.sha256()
      with open(newFile, 'rb') as f:
        while True:
          data = f.read(BUF_SIZE)
          if not data:
            break

      sha256.update(data)

      f.close()
      os.remove(newFile)

      return sha256.hexdigest()

    def hashFileLOCAL(file):
      BUF_SIZE = os.path.getsize(file)
      sha256 = hashlib.sha256()
      with open(file, 'rb') as f:
        while True:
          data = f.read(BUF_SIZE)

          if not data:
            break

      sha256.update(data)

      return sha256.hexdigest()

    def install(URL, Destination, NewName, FileExt=""):
      # Download and write to file
      file_content = requests.get(URL)
      open(Destination + '/' + NewName + FileExt,
           "wb").write(file_content.content)
      if debug:
        print("Downloaded file to: " + Destination)
  
  
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

        key = str('0' + 'x' + ''.join(
          random.choice(foo) for iterable in range(random.choice(lengthlist))))

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
    return str(''.join(formattedKey[0:-1]))

  def createkey(type):
    if not isinstance(type, str):
      raise TypeError(
        '`type` parameter must be a string object and a valid option.')

    if type == 'x32':
      return _2PT.split_key(_2PT.x32key.x32_rawkey())
    if type == 'x64':
      return _2PT.split_key(_2PT.x64key.x64_rawkey())
    if type == 'hex':
      return _2PT.hexkey.hex_rawkey()
    if type == 'wrd':
      return _2PT.wordkey.word_rawkey()
    else:
      return 'ERROR: Invalid key type'


if __name__ == '__main__':
  print('''
---- 2PT Keys Console Tool ----

COMMANDS

-new(type) : This command creates a new key of a certain type.
-secure(key) : This will secure the given key and re-split it.
-save_key(key) : Will save the given key in a txt file.
-update : This function checks for an update and if applicable updates.
-display_dir : This command simply prints the directory 2PT uses.
-wipe_keys : Wipes the key save file.

USAGE
To pass a command type the desired command into the `> ` text field and press 'Enter'. (Examples shown below)

Command  |  Example
new(type) : new x32
secure(key) : secure 0x3H8I
save_key(key) : save_key 0xR2D2

-------------------------------
''')

  userinput = input('> ')
  inputlist = userinput.split(' ')
  
  if inputlist[0] == 'new':
    print(_2PT.createkey(inputlist[1]))
