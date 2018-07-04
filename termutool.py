#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import sys
from instalacoes import *
def principal():
    os.system("clear")
    termutoolMsg()
    
    print("[1]- Scanners de portas")
    print("[2]- Conexão reversa (AriCon)")
    print("[3]- Backdoor (AriTrojan)")
    print("[0]- Sair do programa")     
    op = int(input("\nopção >>> "))    
    
    if op > 3:
        os.system("clear")
        print("\033[31m A opção {} não existe, por favor escolha uma opção VÁLIDA!".format(op))
        time.sleep(3)
        principal()
    elif op == 1:
        os.system("clear")
        portscanMsg()
        print("[1]- AriPort")
        print("[0]- Voltar")
        print("[99]- Sair do programa")
        portScan = int(input("\nopção >>> "))
        
        if portScan > 1 and portScan < 99:
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