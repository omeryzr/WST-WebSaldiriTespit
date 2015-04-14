#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import *
from monitoring.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *

import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

data = open(os.path.join(BASE, "serverCommandExec.txt"))

# Create your views here.
def kayit_ekle(request):
    if request.method=='POST':
        logip=request.POST.get('logip')

        log1=log(logip=logip)
        log1.save()
        return HttpResponse('sadsad')
    else:
        return render_to_response('deneme.html', context_instance=RequestContext(request))

class serverCommandExec():

    def __init__(self):
        id = 0
        self.id = id
    def uzunlukKontrol(self,url):
        if len(url)> 150:
            self.id = self.id + 1
            return "ID: %s Dikkat Çok Uzun Satır: %s" %(self.id, len(url))
        else:
            self.id = self.id + 1
            return "%s Normal" %(id)

    #Windows için uzaktan kod çalıştırma
    def codeExecAttack(self,url,payload):
        urlParse = url.split(payload)
        command=['exe','sh','msi']
        if(command[0] in urlParse):
            self.id = self.id + 1
            return 'ID: %s Bulundu %s - %s' %(self.id, command[0].strip(), url.strip())
        elif(command[1] in urlParse):
            self.id = self.id + 1
            return 'ID: %s Bulundu %s - %s' %(self.id, command[1].strip(), url.strip())
        elif(command[2] in urlParse):
            self.id = self.id + 1
            return 'ID: %s Bulundu %s - %s' %(self.id, command[2].strip(), url.strip())
        else:
            return

    #XSS SALDIRI TESPİTİ

    def xssTespit(self,url,payload):
        try:
            a = re.search(payload, url)
            b = a.group()
            if (b == 'script')| (b == 'SCRIPT'):
                self.id = self.id + 1
                return "ID: %s Bulundu %s - %s" %(self.id, b, url)
            elif b == '<STYLE TYPE' | '<LINK REL':
                self.id = self.id + 1
                return "ID: %s Bulundu %s - %s" %(self.id, b, url)

        except:
            pass
    #SQL İnj SALDIIR TESPİTİ
    def sqliTespit(self,url,payload):
        id = 0
        try:
            a = re.search(payload,url)
            b = a.group()
            if (b== "or 1=1")|(b == 'select'):
                id = id + 1
                return "ID: %s Bulundu %s - %s" %(id, b, url)
            elif (b== "%20and%20")|(b == 'union'):
                id = id + 1
                return "ID: %s Bulundu %s - %s" %(id, b, url)
            pass
        except:
            pass


def anasayfa(request):

        return render_to_response('index.html', locals())

def saldiri(request):
    xss = log.objects.all()
    yeni = open(os.path.join(BASE, u"serverCommandExec.txt"))
    url = yeni.read()
    for i in range(0,len(url.split('\n'))):
        payload = ['.']
        satir = url.split('\n')[i]
        if serverCommandExec().codeExecAttack(satir,payload[0]) == None:
            pass
        else:
            print serverCommandExec().codeExecAttack(satir,payload[0])
    yeni.close()
    return render_to_response('saldirilar.html', locals())

def sqlsaldiri(request):
    xss = log.objects.all()
    yeni = open(os.path.join(BASE, u"serverCommandExec.txt"))
    url = yeni.read()
    for i in range(0,3):
        for j in range(0,len(url.split('\n'))):
            sqller = ["or 1=1","select","%20and%20","union"]
            if serverCommandExec().sqliTespit((url.split('\n')[j]),sqller[i]) == None:
                pass
            else:
                print serverCommandExec().sqliTespit((url.split('\n')[j]),sqller[i])
    yeni.close()
    return render_to_response('sqlinjection.html', locals())

def xsssaldiri(request):
    xss = log.objects.all()
    yeni = open(os.path.join(BASE, u"serverCommandExec.txt"))
    url = yeni.read()
    log1 = log.objects.all()
    for i in range(0,3):
        for j in range(0,len(url.split('\n'))):
            xssler = ['script\n','SCRIPT','<STYLE TYPE','<LINK REL']
            if serverCommandExec().xssTespit((url.split('\n')[j]),xssler[i]) == None:
                pass
            else:
                print serverCommandExec().xssTespit((url.split('\n')[j]),xssler[i])
    yeni.close()
    return render_to_response('xss.html', locals())


import re
"""
            Bu uygulama
        1-URL Taraması yapıp, sunucuda komut çalıştıran kodun tespiti
        2-URL Karakter sayısına göre Buffer Overflow atak tespiti
        3-SQL İnjection Saldırı tespiti
        4-XSS Atak Tespiti

"""


def profilsayfasi(request):
	return render_to_response('profil.html', locals())

def iletisimsayfasi(request):
	return render_to_response('iletisim.html', locals())



def xss(request):
        ## Daha önce kullandığımız Doktor.objects.all() fonksiyonu ile verileri doktorlar değişkenine atıyoruz.

        return render_to_response('xss.html',locals())

def urlgiris(request):
        ## Daha önce kullandığımız Doktor.objects.all() fonksiyonu ile verileri doktorlar değişkenine atıyoruz.

        return render_to_response('xss.html',locals())


def urlgiris(request):
    if request.method=='POST':
        logip=request.POST.get('logip')

        logkyt= log(logip=logip)
        logkyt.save()
        return render_to_response('urlgiris.html')
    else:
        return render_to_response('urlgiris.html', context_instance=RequestContext(request))


def giris(request):
    if request.GET.get('cikis'):
        logout(request)
        return HttpResponseRedirect('/index/')

    if request.POST.get('giris'):
          giris_formu = AuthenticationForm(data=request.POST)
    if giris_formu.is_valid():
        kullaniciadi = request.POST['username']
        sifre = request.POST['password']
        kullanici = authenticate(username=kullaniciadi,password=sifre)
    if kullanici is not None:
      if kullanici.is_active:
        login(request,kullanici)
    else:
        giris_formu = AuthenticationForm()

    return render_to_response('login.html',locals(),context_instance = RequestContext(request))


def kayit_ekle(request):
    if request.method=='POST':
        adi=request.POST.get('adi')
        soyadi=request.POST.get('soyadi')
        bolumu=request.POST.get('bolumu')
        eposta=request.POST.get('eposta')
        parola=request.POST.get('parola')

        kyt= uye(adi=adi, soyadi=soyadi, bolumu=bolumu, eposta=eposta, parola=parola)
        kyt.save()
        return HttpResponseRedirect('/login/')
    else:
        return render_to_response('uyeol.html', context_instance=RequestContext(request))
















