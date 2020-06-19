import random

class Device():

  def __init__(self, strength, defense, attack, signature, *functions):
    self.strength = strength
    self.defense = defense
    self.encryption = 0.0
    self.ecnrypionLevel = Device_EncryptionLevel.NoEncryption
    self.attack = attack
    self.signature = signature
    self.functions = []
    for function in functions:
      self.functions.append(function)
    

  
    

  def CheckSignalStrength(self, distance):
    _strength = self.strength + random.randint(-2,2)
    if _strength >= distance:
      print("Good Signal")
    elif _strength < distance:
      print("Bad Signal")
    else:
      print("Error")


  def HackingAttempt(self, attackerStrength):
    attackerStrength += random.randint(-2,2)
    _defense = self.defense + random.randint(-2,2)
    if _defense > attackerStrength:
      print("Hacking Attempt Prevented")
    elif _defense < attackerStrength:
      print("Hacking Attempted Succeeded")
    else:
      print("hacking Attempt Partially Succeeded")

    def Search():
      return "Search"
    
    def setLevelOfEncrypion(self, level):
      if level == 0 or level > 3:
        return None

      if level == 1:
        self.encryptionLevel = Device_EncryptionLevel.Minimal
      elif level == 2:
        self.encryptionLevel = Device_EncryptionLevel.Medium
      elif level == 3:
        self.encryptionLevel = Device_EncryptionLevel.Maximum
      else:
        self.encryptionLevel = Device_EncryptionLevel.NoEncryption


    def Encryption(self, encryptionLevel):
      if encryptionLevel == Device_EncryptionLevel.NoEncryption:
        return 0.000
      elif encryptionLevel == Device_EncryptionLevel.Minimal:
        return 0.250
      elif encryptionLevel == Device_EncryptionLevel.Medium:
        return 0.500
      elif encryptionLevel == Device_EncryptionLevel.Maximum:
        return 0.750
      else:
        return None

    def Conceal(self):
      if(self.signature < 0.250):
        self.signature -= 0.150
      else:
        self.signature -= 0.250
      

class Device_Type(enumerate):
  Human_Military: 1
  Human_Civilian: 2
  Alien_Military: 3
  Alien_Civilian: 4
  Custom: 5

class Device_EncryptionLevel(enumerate):
  Minimal: 1
  Medium: 2
  Maximum: 3
  NoEncryption: 4