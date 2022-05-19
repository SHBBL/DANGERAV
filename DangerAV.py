import glob,shutil,winreg,os,signal

def DEL_RUN_USER():
    del_registry_user = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
    del_key_user = winreg.OpenKey(del_registry_user,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_ALL_ACCESS)
    for i in range(100):
        try:
            z = winreg.EnumValue(del_key_user,i)
            print(f'Name:{z[0]} \nkey:{z[1]}')
            print('\n')
        except:
            pass
    con = input("name: ")
    try:
        winreg.DeleteValue(del_key_user,con)
        print(f"{con} successfully removed")
    except FileNotFoundError:
        print("CANT FIND SPECIFIED VALUE!!!") 
        pass

def DEL_RUN_MACHINE():
    del_registry_machine = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    del_key_machine = winreg.OpenKey(del_registry_machine,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_ALL_ACCESS)
    for i in range(100):
        try:
            z = winreg.EnumValue(del_key_machine,i)
            print(f'Name:{z[0]} \nkey:{z[1]}')
            print('\n')
        except:
            pass
    con = input("name: ")
    try:
        winreg.DeleteValue(del_key_machine,con)
        print(f"{con} successfully removed")
    except FileNotFoundError:
        print("CANT FIND SPECIFIED VALUE!!!") 
        pass

def SHELL_MACHINE():
    registry_machine = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    try:
        key_machine = winreg.OpenKey(registry_machine,r"SOFTWARE\MICROSOFT\WINDOWS NT\CURRENTVERSION\WINLOGON\\SHELL")
    except:
        raise SystemExit
    z = []
    for i in range(100):
        try:
            a = winreg.EnumValue(key_machine,i)
            print(a)
            z.append('k')
        except FileNotFoundError:
            print("NO SHELL HERE")
        if len(z) > 0:
            con2 = input("Name: ")
            try:
                winreg.DeleteValue(key_machine,con2)
                print(f"{con2} successfully removed")
            except FileNotFoundError:
                print("CANT FIND SPECIFIED KEY!!!") 
                pass
        else:
            pass

def HELL_MACHINE():
    reg_machine = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    key1_machine = winreg.OpenKey(reg_machine,r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree",0,winreg.KEY_ALL_ACCESS)
    for i in range(100):
        try:
            a = winreg.EnumKey(key1_machine,i)
            print(a)
        except:
            pass
    con1 = input("Name: ")
    try:
        winreg.DeleteKey(key1_machine,con1)
        print(f"{con1} successfully removed")
    except FileNotFoundError:
        print("CANT FIND SPECIFIED KEY!!!") 
        pass

def SYSTEM32():
    os.chdir('C:\Windows\System32\Tasks')
    for i in glob.glob('*'):
        a = i.split('.')
        if len(a) > 1:
            print(f'{a[0]}.{a[1]}')
        else:
            print(a[0])
    while True:
        con3 = input('name: ')
        try:
            if '.' in con3:
                os.remove(con3)
                print(f'{con3} is removed successfully!!!')
                continue
            else:
                if os.path.exists(con3):
                    shutil.rmtree(con3)
                    print(f'{con3} is removed successfully!!!')
                    continue
                else:
                    print('Folder not found')
                    continue
        except:
            print(f"no such file named {con3}")
            continue

def LOC_FILES():
    con4 = input('File name + extention: ')
    for a,b,c in os.walk('\\'):
        if con4 in c:
            print(f'C:{a}\{con4}')
            continue
        else:
            pass

def DEL_FILES():
    while True:
        con5 = input("path/name: ")
        try:
            os.remove(con5)
            print("Done")
            continue
        except FileNotFoundError:
            print("File doesnt exist!!!")
            continue
        
def PROCESS_KILL():
    con6 = input("Enter process Name + extension: ")
    try:
        for line in os.popen("TASKKILL /IM " + con6):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)
            print("Process Successfully terminated")
    except:
        pass
    print("Done!!")
