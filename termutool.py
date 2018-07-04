#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import sys
from instalacoes import *
def principal():
    os.system("clear")
    termutoolMsg()
    
    print("\033[32m[1]- Scanners de portas")
    print("[2]- Conexão reversa (AriCon)")
    print("[3]- Backdoor (AriTrojan)\033[m")
    print("\033[31m[0]- Sair do programa\033[m")     
    op = int(input("\033[32m\nopção >>> \033[m"))    
    
    if op > 3:
        os.system("clear")
        print("\033[31m A opção {} não existe, por favor escolha uma opção VÁLIDA!\033[m".format(op))
        time.sleep(3)
        principal()
    elif op == 1:
        os.system("clear")
        portscanMsg()
        print("\033[32m[1]- AriPort")
        print("[0]- Voltar\033[m")
        print("\033[31m[99]- Sair do programa\033[m")
        portScan = int(input("\nopção >>> "))
        
        if portScan > 1 and portScan < 99 or portScan > 99:
            os.system("clear")
            print("A opção {} não existe, por favor escolha uma opção VÁLIDA!".format(portScan))
            time.sleep(3)
            principal()
        
        elif portScan == 1:
            os.system("clear")
            ariport()
            
        elif portScan == 0:
            principal()
        
        elif portScan == 99:
            os.system("clear")
            exibirMensagem()
            sys.exit()
            

principal()