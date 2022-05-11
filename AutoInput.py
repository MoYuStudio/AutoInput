
# = COPYRIGHT © 2020 MOYU STUDIO. ALL RIGHTS RESERVED. = #

import os
import time
import win32api
import win32con
import win32gui
import keyboard
import shutil # shutilwhich
import pyautogui

RUN = True

sleep_timer = 1

def WriteAutoStartCmd():
    path = os.getcwd()
    bat = open('autoinput_autostart.bat','w')
    cmd_data = path[0]+path[1]+'\n'
    cmd_data += 'cd '+path+'\n'
    cmd_data += 'start AutoInput.exe\n'
    bat.write(cmd_data)
    bat.close()

def ReadData():
    global config_data,setting_data
    path = os.getcwd()
    config = open(path+'\data\config.moyustudio','r')
    setting = open(path+'\data\setting.moyustudio','r')
    config_data = config.read()
    setting_data = setting.read()
    config.close()
    setting.close()

    config_data = eval(config_data)
    setting_data = eval(setting_data)

    return config_data,setting_data

def MainLoop():
    for code in range(len(config_data)):
        name_length = len(config_data[code]['name'])

        window_hwnd = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(window_hwnd)

        if window_title[-name_length:] == config_data[code]['name']:
            if config_data[code]['key_type'] == 'key':
                pyautogui.key(config_data[code]['key'])
            if config_data[code]['key_type'] == 'hotkey':
                pyautogui.hotkey(config_data[code]['hotkey'][0],config_data[code]['hotkey'][1])

if __name__ == '__main__':
    
    ReadData()

    if setting_data['set_autostartcmd'] == 'True':
        WriteAutoStartCmd()
        try:
            os.remove('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/autoinput_autostart.bat')
        except:
            # win32api.MessageBox(0, 'AutoStart Fail to Close\n 开机自启 关闭失败', 'AutoInput', win32con.MB_OK)
            pass
        try:
            shutil.move(os.getcwd()+'/autoinput_autostart.bat','C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup')
        except:
            # win32api.MessageBox(0, 'AutoStart Fail to Open\n 开机自启 启动失败', 'AutoInput', win32con.MB_OK)
            pass

    if setting_data['set_autostartcmd'] == 'False':
        try:
            os.remove('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/autoinput_autostart.bat')
        except:
            # win32api.MessageBox(0, 'AutoStart Fail to Close\n 开机自启 关闭失败', 'AutoInput', win32con.MB_OK)
            pass

    while RUN:
        if keyboard.is_pressed(setting_data['close_key']):
            RUN = False

        sleep_timer -= 1
        if sleep_timer <= 0:
            MainLoop()
            sleep_timer = int(setting_data['sleep_time'])*10
        
        time.sleep(0.1)

    input()

# = COPYRIGHT © 2020 MOYU STUDIO. ALL RIGHTS RESERVED. = #
