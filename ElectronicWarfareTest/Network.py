class Network():

  def __init__(self):
    self.networkMap = {}
  
  def addDevice(self, key, device):
    self.networkMap[key] = device