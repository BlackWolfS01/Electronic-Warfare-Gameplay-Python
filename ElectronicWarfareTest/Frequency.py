import Device
import random

class Frequency():
  def __init__(self):
    self.ConnectedDevices = [Device()]

  def AddDevice(self, device):
    self.ConnectedDevices.append(device)

  def RemoveDeviceAt(self, index):
    self.ConnectedDevices.remove(index)

  def GetDeviceAt(self, index):
    return self.ConnectedDevices.pop(index)
  '''
  def ScanForDevices(self):
    detectedDevices = []
    for device in self.ConnectedDevices:
      if random.uniform(0,2.0) < device.signature
  '''