#!usr/bin/env python
# -*- coding:utf-8 -*-
# _*_ coding:cp1254 _*_
from Tkinter import *
import RPi.GPIO as gpio
import time
from PCA9685 import PWM
from smbus import SMBus

#gpio ayarları
gpio.setmode(gpio.BCM)
#PCA9685 setup
i2c_adres=0x40
bus=SMBus(1)
pwm_s=PWM(bus,i2c_adres)
pwm_s.setFreq(50)
#step
gpio.setup(4,gpio.OUT)
gpio.setup(17,gpio.OUT)
gpio.setup(23,gpio.OUT)
gpio.setup(24,gpio.OUT)
#dc
gpio.setup(26,gpio.OUT)
gpio.setup(19,gpio.OUT)

gpio.output(26,gpio.HIGH)
gpio.output(19,gpio.HIGH)


class AdminPanel:
    def __init__(self, pencere):
        self.kontrol_birimi = 0

        frame = Frame(pencere)
        frame.pack()

        self.l1 = Label(frame, text="Kullanıcı Adı")
        self.l1.grid(row=0, column=0)

        self.e1 = Entry(frame)
        self.e1.grid(row=0, column=1)

        self.l2 = Label(frame, text="Şifre")
        self.l2.grid(row=1, column=0)

        self.e2 = Entry(frame)
        self.e2.grid(row=1, column=1)

        self.b1 = Button(frame, text="Giriş",command=self.kontrol,padx=5, pady=5, relief=RIDGE, bg="grey")
        self.b1.grid(row=2, column=0)
        

    def kontrol(self):
        if (self.e1.get() == "" and self.e2.get() == ""):  
            print "\nGiris Basarili"
            self.kontrol_birimi = 1
            pencere.destroy()
        else:
            print "\nKullanici Adi veya Sifre Hatali !!!"


class KontrolPanel:
    def __init__(self, denetim):
        self.deger = 0
        self.kontrol_birimi = 0

        frame2 = Frame(denetim,bg="white",padx=5,pady=5,relief=RIDGE)
        frame2.pack(side=TOP)

        frame3 = Frame(denetim, padx=5)
        frame3.pack(side=LEFT)
        
        frame4 = Frame(denetim, padx=5)
        frame4.pack(side=RIGHT)

        frame5 = Frame(denetim, padx=5)
        frame5.pack(side=BOTTOM)

        self.baslik = Label(frame2, text="H. Avni İncekara Fen Lisesi Denizaltı Projesi",bg="grey")
        self.baslik.grid(row=0)

        self.l2=Label(frame2,bg="aqua",text="""Denizaltı Durumu="Su Üstünde" """)
        self.l2.grid(row=1,column=0,pady=2,padx=1)

        self.l3=Label(frame2,bg="aqua",text="Motor Gücü %")
        self.l3.grid(row=2,column=0)
        
	self.s1 = Scale(frame4, from_=100, to=0, orient=VERTICAL)
        self.s1.grid(row=0, column=1)
	#arka panel
	self.s2 = Scale(frame3, from_=25, to=160, orient=HORIZONTAL,command=self.servo_arka_panel)
        self.s2.grid(row=0, column=2)
	#kanatlar
        self.s3 = Scale(frame3, from_=2, to=-2, orient=VERTICAL,command=self.servo_kanat)
        self.s3.grid(row=0, column=1)

        self.b5 = Button(frame4, text="Ana Motor \n--->", command=self.s1_deger, padx=5, pady=5, relief=RIDGE,bg="grey")
        self.b5.grid(row=0, column=0)

        self.d_e = Entry(frame5)
        self.d_e.grid(row=1)

        self.b6 = Button(frame5, text="Uygula", command=self.dal_cik,padx=5, pady=5, relief=RIDGE, bg="grey")
        self.b6.grid(row=2, pady=10)

        

        

    def s1_deger(self):
        print "\nMotor %",self.s1.get(), "Gucte Calisiyor"
        if(self.s1.get()==0):
            print "***********Motor stabil.\n"
        if(self.s1.get()==100):
            print "***********Motor tam gucte.\n"    
        self.l3["text"]="Motor Gücü %",self.s1.get()
	pwm_s.setDuty(2,self.s1.get()/2)
	gpio.output(26,gpio.LOW)
	gpio.output(19,gpio.HIGH)
        
    def dal_cik(self):
        if (self.d_e.get() == "dal"):
            print "\nDalis Komutu Uygulaniyor"
	    self.l2["text"]="Lütfen Bekleyiniz"
	    print "3"
	    time.sleep(1)
	    print "2"
	    time.sleep(1)
	    print "1"
	    time.sleep(1)
	    self.step_ileri()
            self.l2["text"]="""Denizalti durumu="Su Altında" """
            self.d_e.delete(0, END)
        elif (self.d_e.get() == "cik"):
            print "\nCik Komutu Uygulaniyor"
	    self.l2["text"]="Lütfen Bekleyiniz"
	    print "3"
	    time.sleep(1)
	    print "2"
	    time.sleep(1)
	    print "1"
	    time.sleep(1)
	    self.step_geri()
            self.l2["text"]="""Denizalti durumu="Su Üstünde" """
            self.d_e.delete(0, END)
        else:
            print "\nHatali Deger Girdiniz"
            self.d_e.delete(0, END)       

    def step_ileri(self):
	for i in range(0, 1000):
            self.setStep(1, 0, 0, 1)
            time.sleep(1.5/1000.0)
            self.setStep(1, 1, 0, 0)
            time.sleep(1.5/1000.0)
            self.setStep(0, 1, 1, 0)
            time.sleep(1.5/1000.0)
            self.setStep(0, 0, 1, 1)
            time.sleep(1.5/1000.0)
    
    def step_geri(self):	  
        for i in range(0, 1000):
            self.setStep(1, 0, 0, 1)
            time.sleep(1.5/1000.0)
            self.setStep(0, 0, 1, 1)
            time.sleep(1.5/1000.0)
            self.setStep(0, 1, 1, 0)
            time.sleep(1.5/1000.0)
            self.setStep(1, 1, 0, 0)
            time.sleep(1.5/1000.0)

    def setStep(self,w1,w2,w3,w4):
	gpio.output(4,w1)
	gpio.output(17,w2)
	gpio.output(23,w3)
	gpio.output(24,w4)
    def servo_arka_panel(self,angle):
	print "Arka Levha Pozisyon=",float(angle)
	duty=8.5/180*float(angle)+2
	pwm_s.setDuty(0,duty)
    def servo_kanat(self,angle):
	print "Kanat Pozisyon=",float(angle)
	if(self.s3.get()==0):
	    duty=8.5/180*90+2
            pwm_s.setDuty(3,duty)
	elif(self.s3.get()==1):
	    duty=8.5/180*100+2
            pwm_s.setDuty(3,duty)
	elif(self.s3.get()==2):
	    duty=8.5/180*135+2
            pwm_s.setDuty(3,duty)
	elif(self.s3.get()==-1):
	    duty=8.5/180*67.5+2
            pwm_s.setDuty(3,duty)
	elif(self.s3.get()==-2):
	    duty=8.5/180*45+2
            pwm_s.setDuty(3,duty)

pencere = Tk()
pencere.title("Giris Paneli")
c = AdminPanel(pencere)
pencere.mainloop()

denetim = Tk()
denetim.geometry("600x250")
denetim.title("Kontrol Paneli")

if (c.kontrol_birimi == 1):
    g = KontrolPanel(denetim)
else:
    denetim.destroy()

denetim.mainloop()
gpio.cleanup()



