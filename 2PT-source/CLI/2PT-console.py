# TODO: Remove double quotes and replace with single
# TODO: Remove File_ext from install instances

# 2PT-Keys CLI Version - 1.0.2.1
try:
  import random
  import string
  import requests
  import os, sys
  import hashlib
  import subprocess
  import time
except:
  raise ImportError('Please install the required packages: hashlib, subprocess, request and random')

debug = False

class vars():
  x32_keylength = 24
  x64_keylength = 32
  user = os.getlogin()
  CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  main_Dir = str(f'C:/Users/{user}/2PT-Keys')
  scoop_Dir = str(f'C:/Users/{user}/scoop')
  scoopApp_Dir = str(f'{scoop_Dir}/apps/2PT-Console')
  scoopShim_File = str(f'{scoop_Dir}/shims/2PT.cmd')
  python_Path = str(f'C:/Users/{user}/AppData/Local/Programs/Python')
  powershell = str('C:/Windows/System32/powershell.exe')
  scoopApp_File = str(f'{scoop_Dir}/apps/2PT-Console/2PT.py')
  console_WebFile = str(f'https://itzcozi.github.io/2PT-Keys/data/2PT-console.py')
  
  
class _2PT():

  def update():
    with open(vars.scoopApp_File, "w") as f:
      f.truncate(0)
      f.write(requests.get(vars.console_WebFile).text)
      f.close()

      if debug:
        print("Program Successfully Updated!")

    return True

  def setup():
    if os.path.exists(vars.scoop_Dir):
      if debug:
        print("Scoop is already installed. ")
      pass
    else:
      subprocess.call(f'{vars.powershell} iwr -useb get.scoop.sh | iex')
                      
    if not os.path.exists(vars.main_Dir):
      os.mkdir(vars.main_Dir)
    else:
      pass
    if not os.path.exists(vars.scoopApp_Dir):
      os.mkdir(vars.scoopApp_Dir)
    else:
      pass

    if not os.path.exists(vars.scoopShim_File):
      with open(vars.scoopShim_File, 'w') as file:
        file.write(f'@"{vars.python_Path + "/Python311/python.exe"}" "{vars.scoopApp_File}" %*')
      if debug:
        print(f'Program file {vars.scoopShim_File} !MISSING!')

    if not os.path.exists(vars.scoopApp_File):
      _2PT.utility.install(vars.console_WebFile, vars.scoopApp_Dir, "2PT", ".py")
      if debug:
        print(f"Program file {vars.scoopApp_File} !MISSING!")

  
  class utility():

    def hashFileURL(url):
      newFile = str(f'{vars.scoopApp_Dir}/newfile.txt')

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

      f.close()
      return sha256.hexdigest()

    def install(URL, destination, name):
      # Download and write to file
      file_content = requests.get(URL)
      open(f'{destination}/{name}', 'wb').write(file_content.content)
      if debug:
        print(f'Downloaded file to: {destination}')

    def secure(key):
      keyList = list(key)
      olprime = random.randint(3, 8)
      buff = random.randint(200, 1000)
      alphabet = string.ascii_letters + string.digits + string.digits
      randomkey = list(random.choice(alphabet) for i in range(buff))

      for z in range(olprime):
        random.shuffle(keyList)
        random.shuffle(keyList)
        bar = keyList + randomkey
        for i in bar:
          random.shuffle(bar)

      newkey = ''.join(random.choice(bar) for i in range(len(key)))
      newList = list(newkey)

      for y in range(olprime):
        random.shuffle(randomkey)
        random.shuffle(randomkey)

      for x in range(olprime):
        random.shuffle(newList)
        random.shuffle(newList)
        foo = randomkey + newList
        for i in foo:
          random.shuffle(foo)

      returnKey = _2PT.split_key(''.join(random.choice(foo) for i in range(len(key))))

      return str(returnKey)

    def save_key(key):
      try:
        with open(f'{vars.main_Dir}/save_file.txt', 'w') as file:
          file.write(key)
          return 'Key saved successfully'
      except PermissionError:
        return 'SAVE_KEY: Permission denied, please run as administrator'

    @staticmethod
    def wipe_keys():
      try:
        with open(f'{vars.main_Dir}/save_file.txt', 'w') as file:
          file.truncate(0)
          return 'All saved keys have been deleted'
      except PermissionError:
        return 'WIPE_KEYS: Permission denied, please run as administrator'

    @staticmethod
    def display_dir():
      print(vars.main_Dir)
      return True

  
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

        key = ''.join(random.choice(foo) for iterable in range(vars.x32_keylength))

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

        key = ''.join(random.choice(foo) for iterable in range(vars.x64_keylength))

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

      key = str(f"0x{''.join(random.choice(foo) for iterable in range(random.choice(lengthlist)))}")

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

      key = f'{"".join(wordlist)}{str(random.randint(175, 9999) - 75)}'

      return str(key)


  def split_key(key):
    if not isinstance(key, str):
      raise TypeError('`key` parameter must be a string object')

    keylist = list(key)
    returnkey = []
    n = 4

    for index in range(0, len(keylist), n):
      returnkey.append(f"{''.join(keylist[index:index + n])}.")
    formattedKey = ''.join(returnkey)

    return str(''.join(formattedKey[0:-1]))

  def createkey(type):
    if not isinstance(type, str):
      raise TypeError('`type` parameter must be a string object and a valid option.')

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


def driver():
  help_menu = ('''
---- 2PT Keys Console Tool ----

COMMANDS
  -new(type) : This command creates a new key of a certain type.
  -secure(key) : This will secure the given key and re-split it.
  -save_key(key) : Will save the given key in a txt file.
  -update : This function checks for an update and if applicable updates.
  -display_dir : This command simply prints the directory 2PT uses.
  -wipe_keys : Wipes the key save file.
  -say(text) : Will output the text passed with it.
  -help : Prints this message to console.
  -clear : Wipes all text from the terminal.
  -Ctrl + C : Exits the program.

USAGE
  To pass a command type in the command and add a space between it and 
  any parameters you might use then press `Enter`, The return should be 
  a key or a desired output if not please create an issue on the Github.
  
  Key types are as follows: x32, x64, hex, wrd
  Github: https://github.com/itzCozi/2PT-Keys/tree/main

  ------ Command  |  Example ------
    new(type) - new x32
    secure(key) - secure 0x3H8I
    save_key(key) - save_key 0xR2D2
  ---------------------------------
  ''')

  # Call to setup() / prep console
  _2PT.setup()
  vars.CC()
  print(help_menu)

  @staticmethod
  def input_loop():
    userinput = input('> ')
    inputlist = userinput.split(' ')

    try:
      if inputlist[0] == 'new':
        print(_2PT.createkey(inputlist[1]))
        time.sleep(0.5)
        input_loop()
      elif inputlist[0] == 'help':
        vars.CC()
        print(help_menu)
        input_loop()
      elif inputlist[0] == 'say':
        print(' '.join(inputlist[1:len(inputlist)]))
        time.sleep(0.5)
        input_loop()
      elif inputlist[0] == 'clear':
        vars.CC()
        input_loop()
      elif inputlist[0] == 'secure':
        print(_2PT.utility.secure(inputlist[1]))
        time.sleep(0.5)
        input_loop()
      elif inputlist[0] == 'save_key':
        print(_2PT.utility.save_key(' '.join(inputlist[1:len(inputlist)])))
        time.sleep(0.5)
        input_loop()
      elif inputlist[0] == 'update':
        _2PT.update()
        time.sleep(0.5)
        input_loop()
      elif inputlist[0] == 'display_dir':
        _2PT.utility.display_dir()
        time.sleep(0.5)
        input_loop()
      elif inputlist[0] == 'wipe_keys':
        print(_2PT.utility.wipe_keys())
        time.sleep(0.5)
        input_loop()
      else:
        print('ERROR: Invalid command.')
        time.sleep(0.5)
        input_loop()

    except:
      vars.CC()
      print('Something went wrong, make sure your add parameters and using valid commands.')
      time.sleep(2)
      sys.exit(0)

  # Initialize loop
  input_loop()


try:
  driver()
except KeyboardInterrupt:
  vars.CC()
  print('Exiting...')
  time.sleep(2)
  sys.exit(0)
except Exception as e:
  print(f'ERROR: An unknown runtime error occurred.')
  sys.exit(2)
  