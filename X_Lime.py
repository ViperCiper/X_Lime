#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import shutil
import sys
from termcolor import colored
from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format
init(strip=not sys.stdout.isatty())



x1 = '\033[1;32m1\033[1;m'
x2 = '\033[1;32m2\033[1;m'
x3 = '\033[1;32m3\033[1;m'
x4 = '\033[1;32m4\033[1;m'
x5 = '\033[1;32m5\033[1;m'
x6 = '\033[1;32m6\033[1;m'
a1_sign = '\033[1;37m[\033[1;m'
a2_sign = '\033[1;37m]\033[1;m'
d_sign = '\033[1;37m[\033[1;m''\033[1;32m--\033[1;m''\033[1;37m]\033[1;m'
d_sign1 = '\033[1;37m: \033[1;m'
d_sign2 = '\033[1;37m[\033[1;m''\033[1;31mXX\033[1;m''\033[1;37m]\033[1;m'

dir_path = os.path.dirname(os.path.realpath(__file__))

c_dir_path = colored(dir_path, 'red', attrs=['bold'])
apk_directory = colored('Move the apk file to this dircetory ', 'green', attrs=['bold']) 
apk_enter = colored('Enter the name of the apk ⬎', 'green', attrs=['bold'])


def cls():
	os.system('cls' if os.name=='nt' else 'clear')
pass

def c_print(s):
	os_size = int(subprocess.check_output(['stty', 'size']).split()[1])
pass

def derp():
    print("          ─────────▄▄───────────────────▄▄──")
    print("          ──────────▀█───────────────────▀█─")
    print("          ──────────▄█───────────────────▄█─")
    print("          ──█████████▀───────────█████████▀─")
    print("          ───▄██████▄─────────────▄██████▄──")
    print("          ─▄██▀────▀██▄─────────▄██▀────▀██▄")
    print("          ─██────────██─────────██────────██")
    print("          ─██───██───██─────────██───██───██")
    print("          ─██────────██─────────██────────██")
    print("          ──██▄────▄██───────────██▄────▄██─")
    print("          ───▀██████▀─────────────▀██████▀──")
    print("          ──────────────────────────────────")
    print("          ──────────────────────────────────")
    print("          ──────────────────────────────────")
    print("          ───────────█████████████──────────")
    print("          ──────────────────────────────────")
    print("          ──────────────────────────────────")
pass

def space():
	print("")
pass

clear = lambda: os.system('cls')
print colored('================================================', 'red', attrs=['bold'])
print colored(' ##:::: ##: ##::::::: ####: ##:::: ##: ########:', 'green', attrs=['bold'])
print colored('. ##:: ##:: ##:::::::. ##:: ###:: ###: ##.....::', 'green', attrs=['bold'])
print colored(':. ## ##::: ##:::::::: ##:: #### ####: ##:::::::', 'green', attrs=['bold'])
print colored('::. ###:::: ##:::::::: ##:: ## ### ##: ######:::', 'green', attrs=['bold'])
print colored(':: ## ##::: ##:::::::: ##:: ##. #: ##: ##...::::', 'green', attrs=['bold'])
print colored(': ##:. ##:: ##:::::::: ##:: ##:.:: ##: ##:::::::', 'green', attrs=['bold'])
print colored(' ##:::. ##: ########: ####: ##:::: ##: ########:', 'green', attrs=['bold'])
print colored('..:::::..::........::....::..:::::..::........::', 'green', attrs=['bold'])
print colored('====================', 'red', attrs=['bold']), colored('X_LIME', 'blue', attrs=['bold']), colored('====================', 'red', attrs=['bold'])
print (d_sign + '\033[1;33mSELECT AN OPTION TO BEGIN: \033[1;m')
print (a1_sign + x1 + a2_sign + '\033[1;32m Decomplie apk\033[1;m')
print (a1_sign + x2 + a2_sign + '\033[1;32m Inject Apk\033[1;m')
print (a1_sign + x3 + a2_sign + '\033[1;32m Help\033[1;m')
print (a1_sign + x4 + a2_sign + '\033[1;32m Help\033[1;m')
print (a1_sign + x5 + a2_sign + '\033[1;32m Help\033[1;m')
print (a1_sign + x6 + a2_sign + '\033[1;32m Help\033[1;m')


choice_1 = raw_input(d_sign1)

if choice_1 == '1':
	cls()
	print colored('▂▂▃▃▄▄▅▅▆▆▇▇██▓▓▒▒░░APK DECOMPILE░░▒▒▓▓██▇▇▆▆▅▅▄▄▃▃▂▂', 'red', attrs=['bold'])
	space()
	derp()
	print(d_sign + apk_directory + c_dir_path)
	print(d_sign + apk_enter)
	apk_file = raw_input(d_sign1)
	if apk_file.endswith('.apk'):
		print("yes")
	else:
		print (d_sign2), colored('Wrong file format!!!!', 'red', attrs=['reverse', 'bold'])

elif choice_1 == '2':
	cls()
	print '2'
elif choice_1 == '3':
	cls()
	print '3'
elif choice_1 == '4':
	cls()
	print '4'
elif choice_1 == '5':
	cls()
	print '5'
elif choice_1 == '6':
	cls()
	print '6'
	pass
