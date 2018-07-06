#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time

def fbrute():
    print("Baixando Face-Brute...")
    time.sleep(3)
    os.system("git clone https://github.com/mahasiahreaperdaemon/face-brute.git")
    os.system("clear")
    
    print("====================================")
    print("Instalando arquivos dependentes...")
    time.sleep(3)
    os.system("apt-get update")
    os.system("apt-get install python-pip") #instalação do pip caso não tiver
    os.system("pip install --upgrade pip") #atualização do pip 
    os.system("pip install mechanize") #instalação do módulo machanize
    os.system("pip2 install mechanize")
    print("=========================")
    print("CONCLUIDO!!!")
    print("Digite 'cd face-brute' para entrar na pasta do programa")
    print("Em seguida digite 'python2 face-brute.py' para executar o programa")


def aribanner():
    print("Baixando AriBanner...")
    time.sleep(3)
    os.system("git clone https://github.com/mahasiahreaperdaemon/captura_banner.git")
    print("=========================")
    print("CONCLUIDO!!!")
    print("Digite 'cd captura_banner' para entrar na pasta do programa")
    print("Em seguida digite 'python3 ariBanner.py [alvo.com.br] [porta]' para executar o programa")
    

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
                
                
                
def bannerCapMsg():
    print("\033[32m#=#=#=#=#=#=#=#=#=#")
    print("     TERMUTOOL     ")
    print("-------------------")
    print("  \033[36mCaptura de Banner\033[m")
    print("\033[32m#=#=#=#=#=#=#=#=#=#\033[m")
    
    
def bruteMsg():
    print("\033[32m#=#=#=#=#=#=#=#=#=#")
    print("     TERMUTOOL     ")
    print("-------------------")
    print("  \033[36mForça bruta\033[m")
    print("\033[32m#=#=#=#=#=#=#=#=#=#\033[m")
