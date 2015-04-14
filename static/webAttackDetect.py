#!/usr/bin/python
#-*- coding:utf-8 -*-
import re
"""
            Bu uygulama
        1-URL Taraması yapıp, sunucuda komut çalıştıran kodun tespiti
        2-URL Karakter sayısına göre Buffer Overflow atak tespiti
        3-SQL İnjection Saldırı tespiti
        4-XSS Atak Tespiti

"""
yeni = open(u"serverCommandExec.txt")
url = yeni.read()
global id
id = 0

class serverCommandExec():

    def __init__(self):
        pass
    def uzunlukKontrol(self,url):
        if len(url)> 150:
            return "ID: %s Dikkat Çok Uzun Satır: %s" %(id, len(url))
        else:
            return "%s Normal" %(id)

    #Windows için uzaktan kod çalıştırma
    def codeExecAttack(self,url,payload):
        urlParse = url.split(payload)
        command=['exe','sh','msi']
        if(command[0] in urlParse):
            return 'ID: %s Bulundu %s - %s' %(id, command[0].strip(), url.strip())
        elif(command[1] in urlParse):
            return 'ID: %s Bulundu %s - %s' %(id, command[1].strip(), url.strip())
        elif(command[2] in urlParse):
            return 'ID: %s Bulundu %s - %s' %(id, command[2].strip(), url.strip())
        else:
            return

    #XSS SALDIRI TESPİTİ
    def xssTespit(self,url,payload):
        try:
            a = re.search(payload, url)
            b = a.group()
            if (b == 'script')| (b == 'SCRIPT'):
                return "ID: %s Bulundu %s - %s" %(id, b, url)
            elif b == '<STYLE TYPE' | '<LINK REL':
                return "ID: %s Bulundu %s - %s" %(id, b, url)
        except:
            pass

    #SQL İnj SALDIIR TESPİTİ
    def sqliTespit(self,url,payload):
        try:
            a = re.search(payload,url)
            b = a.group()
            if (b== "or 1=1")|(b == 'select'):
                return "ID: %s Bulundu %s - %s" %(id, b, url)
            elif (b== "%20and%20")|(b == 'union'):
                return "ID: %s Bulundu %s - %s" %(id, b, url)
            pass
        except:
            pass



for i in range(0,3):
    for j in range(0,len(url.split('\n'))):
        sqller = ["or 1=1","select","%20and%20","union"]
        id = id + 1
        if serverCommandExec().sqliTespit((url.split('\n')[j]),sqller[i]) == None:
            pass
        else:
            print serverCommandExec().sqliTespit((url.split('\n')[j]),sqller[i])




for i in range(0,3):
    for j in range(0,len(url.split('\n'))):
        xssler = ['script','SCRIPT','<STYLE TYPE','<LINK REL']
        id = id + 1
        if serverCommandExec().xssTespit((url.split('\n')[j]),xssler[i]) == None:
            pass
        else:
            print serverCommandExec().xssTespit((url.split('\n')[j]),xssler[i])



for i in range(0,len(url.split('\n'))):
    payload = ['.']
    satir = url.split('\n')[i]
    if serverCommandExec().codeExecAttack(satir,payload[0]) == None:
        pass
    else:
        id = id + 1
        print serverCommandExec().codeExecAttack(satir,payload[0])
        yeni.close()



