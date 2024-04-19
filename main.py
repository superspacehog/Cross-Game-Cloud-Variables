import os
import scratchattach
import time
import json

game1 = 1002254974
game2 = 1004691810

session = scratchattach.Session(".eJxVkM1OwzAQhN8lZwj1XxL3VkBCvYAE4kAv0dreJCaNHcUORSDeHVvKpdKeZkbfzu5vsQZcHExY7IuwzriEGTQOvi9uiuhHdElnBhqgktZCMN6ZqtlxjXWFkmihOOF7PH69vD9OSql-8E9keYj4FuI3OZ2OCXP2vXW3dk6kWpScl0SmYclpYY1Dmxu01iSbECl3UlKRPPMJrvdttBP-eJfrHSZcrIa7Z7y0H34ZrwEDhCGFuDRGA6s4k8C0RNWprtNAQTS86SRFquuKNnU-D0PU3o82wy8JiOYaqUCnB-RiWUMX0_ZovSs3I5SvOJ838X4L__0DiaxvIg:1rxuuY:1yS5rH0jHeQHZc3ZdfFlel9WY1g", username='superspacehog')
connection1 = session.connect_cloud(game1)
connection2 = session.connect_cloud(game2)

print('Connection established')

def getVar1():
  return scratchattach.get_var(game1, 'Cloud Variable')

def getVar2():
  return scratchattach.get_var(game2, 'Cloud Variable')
  
def setVar1(value):
  connection1.set_var('Cloud Variable', value)

def setVar2(value):
  connection2.set_var('Cloud Variable', value)

jsonData = None
with open('data.json', 'r') as jsonFile:
  jsonData = json.load(jsonFile)

lastValue = None
totalUpdates = jsonData['totalUpdates']
serverStatus = 0

setVar1(getVar2())

while True:
  try:
    while True:
      game1Value = getVar1()
      game2Value = getVar2()
      if game1Value != game2Value:
        if lastValue == game1Value:
          setVar1(game2Value)

          timeout = 5
          while game1Value == getVar1() and timeout > 0:
            time.sleep(1)
            timeout -= 1

          if timeout == 0:
            print("Failed to set game 1's cloud variable")

          print("Recieved update from game 2. Updated game 1's cloud variable to " + game2Value)
        else:
          setVar2(game1Value)

          timeout = 5
          while game2Value == getVar2() and timeout > 0:
            time.sleep(1)
            timeout -= 1

          if timeout == 0:
            print("Failed to set game 2's cloud variable")
          
          print("Recieved update from game 1. Updated game 2's cloud variable to " + game1Value)

        totalUpdates += 1

        jsonData['totalUpdates'] = totalUpdates
        with open('data.json', 'w') as jsonFile:
          json.dump(jsonData, jsonFile, indent=4)

        connection1.set_var('Total Updates', totalUpdates)
        connection2.set_var('Total Updates', totalUpdates)
        print('Total updates: ' + str(totalUpdates))

        lastValue = game1Value
      else:
        time.sleep(1)
  except:
    print('Error occured. Restarting...')
  
  connection1.set_var('Server Status', serverStatus)
  connection2.set_var('Server Status', serverStatus)
  serverStatus = 1-serverStatus
