# AC App Template by Hunter Vaners
# ------------------------------
#
# Don't forget to rename assettocorsa\apps\python\Template_Assetto_Corsa_App
#           by assettocorsa\apps\python\[Your_App_Name_Without_Spaces]
#  and
# the file Template_Assetto_Corsa_App.py
#           by Your_App_Name_Without_Spaces.py
#
# ------------------------------

import ac
import acsys
from third_party.sim_info import *
import sys
import json
import time



appName = "ednoUI"



active_driver = 0
def writeToFile(speed, rpm, gear):
 
    # Data to be written
    dictionary = {
        "rpm": rpm,
        "speed": speed,
        "gear":gear
    }
 
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    try:
        outfile = open( "path_to_folder_from_root" +"AssettoSpeedo/car_data.json", "w")
        try:
            outfile.write(json_object)
            ac.console("wrote w success")
        except:
            ac.console("oopsie")
        finally:
            outfile.close()
    except:
        ac.console("oopsie")

def acMain(ac_version):#----------------------------- App window Init

    # Don't forget to put anything you'll need to update later as a global variables
    global appWindow, car_name, speed, gear, previous_lap_time, counter # <- you'll need to update your window in other functions.
    counter = 0
    speed = ac.getCarState(0, acsys.CS.SpeedMPH)
    speed = round(speed*1.60934)

    rpm = ac.getCarState(0,acsys.CS.RPM)
    rpm = round(rpm)

    gear = ac.getCarState(0, acsys.CS.Gear)

    appWindow = ac.newApp(appName, 1)
    ac.setTitle(appWindow)
    ac.setSize(appWindow, 960, 720)
    ac.drawBorder(appWindow, 0)
    ac.setIconPosition(appWindow, 0, -9001)
    ac.setBackgroundOpacity(appWindow, 0)

    ac.addRenderCallback(appWindow, appGL) # -> links this app's window to an OpenGL render function

    active_driver = ac.getDriverName(ac.getFocusedCar())
    ac.setFontColor(active_driver, 1, 1, 0, 1)
    ac.setText(active_driver)
    car_name = ac.getCarName(ac.getFocusedCar())
    ac.setFontColor(active_driver, 1, 1, 0, 1)
    ac.setText(car_name)

    return "All good... ?"





def appGL(deltaT):#-------------------------------- OpenGL UPDATE
    """
    This is where you redraw your openGL graphics
    if you need to use them .
    """
    pass # -> Delete this line if you do something here !




def acUpdate(deltaT):#-------------------------------- AC UPDATE
    global counter
    speed = ac.getCarState(0, acsys.CS.SpeedMPH)
    speed = round(speed*1.60934)
    
    rpm = ac.getCarState(0,acsys.CS.RPM)
    rpm = round(rpm)

    gear = ac.getCarState(0, acsys.CS.Gear)

    if counter == 1:
        writeToFile(speed, rpm, gear-1)
        counter = 0
    else:
        counter = counter +1