'''from Device import Device
functions = ['stealth','attack', 'defend']
playerDevice = Device(10, 7, 7, functions)
enemyDevice = Device(7,5,5, functions)

'''
import pygame

def switch(arugments):
  if arugments == '':
    return None

  switcher = {
    'attack':Attack(),
    'defend':Defend(),
    'search':Search(),
    'hide':Hide()
  }
  return switcher.get(arugments, "InalidError")



def Attack():
  return "Attack"
def Defend():
  return "Defend"
def Search():
  return "Search"
def Hide():
  return "Hide"

print(switch('hide'))