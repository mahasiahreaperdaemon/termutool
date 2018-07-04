#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time

def ariport():
    print("Baixando AriPort...")
    time.sleep(3)
    os.system("git clone https://github.com/mahasiahreaperdaemon/ariport.git")
    print("=========================")
    print("CONCLUIDO!!!")
    print("Digite 'cd ariport' para entrar na pasta do programa")
    print("Em seguida digite 'python ariport.py' para executar o programa")
    
    
def exibirMensagem():
    print("Obrigado por usar o TermuTool... Tchau! :D")
    
    
    
def termutoolMsg():
    print("\033[32m#=#=#=#=#=#=#=#=#=#")
    print("     TERMUTOOL     ")
    print("#=#=#=#=#=#=#=#=#=#")
    print("Criado por: \033[35mAstaroth Ariel\033[m")
    print("--------------------------\033[m")
    
    
    
def portscanMsg():
    print("\033[32m#=#=#=#=#=#=#=#=#=#")
    print("     TERMUTOOL     ")
    print("-------------------")
    print("  \033[36mScanner de portas\033[m")
    print("\033[32m#=#=#=#=#=#=#=#=#=#\033[m")