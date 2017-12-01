#Author-Roger Cheng
#Description-Hello World Fusion 360 script

import adsk.core, adsk.fusion, adsk.cam, traceback

import sys

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        version = sys.version_info
        ui.messageBox("We're running on Python " + str(version.major), "Version detection")

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
