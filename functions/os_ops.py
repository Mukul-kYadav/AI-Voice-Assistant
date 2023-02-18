import os
import subprocess as sp


paths = {
    'notepad': "C:\\Program Files (x86)\\Notepad++\\notepad++.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_camera():
    sp.run('start microsoft.widows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_calculator():
    sp.Popen(paths["calculator"])

def open_cmd():
    os.system('start-cmd')