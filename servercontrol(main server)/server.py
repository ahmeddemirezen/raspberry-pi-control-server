#!usr/bin/env python
# -*- coding:utf-8 -*-
# _*_ coding:cp1254 _*_
#Ahmed Demirezen Feezx1
import socket
from Tkinter import *

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

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

        self.l3=Label(frame2,bg="aqua",text="DC Guc Kademesi::0")
        self.l3.grid(row=2,column=0)
        #dc 
        self.s1 = Scale(frame4, from_=10, to=0, orient=VERTICAL)
        self.s1.grid(row=0, column=1)
        #arka panel
        self.s2 = Scale(frame3, from_=-2, to=2, orient=HORIZONTAL,command=self.servo_a)
        self.s2.grid(row=0, column=2)
	
	#kanatlar
        self.s3 = Scale(frame3, from_=2, to=-2, orient=VERTICAL,command=self.servo_y)
        self.s3.grid(row=0, column=1)

        self.b5 = Button(frame4, text="Ana Motor \n--->", padx=5, pady=5, relief=RIDGE,bg="grey",command=self.dc)
        self.b5.grid(row=0, column=0)

        self.d_e = Entry(frame5)
        self.d_e.grid(row=1)

        self.b6 = Button(frame5, text="Uygula",padx=5, pady=5, relief=RIDGE, bg="grey",command=self.dal_cik)
        self.b6.grid(row=2, pady=10)

    def dal_cik(self):
        if (self.d_e.get()=="dal"):
            self.l2["text"]="""Denizaltı Durumu="Su Altinda" """
            addr.send("dal")
        elif(self.d_e.get()=="cik"):
            self.l2["text"]="""Denizaltı Durumu="Su Ustunde" """
            addr.send("cik")
        
    def servo_a(self,angle):
        if (float(angle)==0.0):
            addr.send("servo_a_0")
            print "Arka Panel Pozisyon::0"
            
        elif (float(angle)==1.0):
            addr.send("servo_a_1")
            print "Arka Panel Pozisyon::1"
            
        elif (float(angle)==2.0):
            addr.send("servo_a_2")
            print "Arka Panel Pozisyon::2"
            
        elif (float(angle)==-1.0):
            addr.send("servo_a_-1")
            print "Arka Panel Pozisyon::-1"
            
        elif (float(angle)==-2.0):
            addr.send("servo_a_-2")
            print "Arka Panel Pozisyon::-2"
            
    def servo_y(self,angle):
        if (float(angle)==0.0):
            addr.send("servo_y_0")
            print "Kanat Pozisyon::0"
            
        elif (float(angle)==1.0):
            addr.send("servo_y_1")
            print "Kanat Pozisyon::1"
            
        elif (float(angle)==2.0):
            addr.send("servo_y_2")
            print "Kanat Pozisyon::2"
            
        elif (float(angle)==-1.0):
            addr.send("servo_y_-1")
            print "Kanat Pozisyon::-1"
            
        elif (float(angle)==-2.0):
            addr.send("servo_y_-2")
            print "Kanat Pozisyon::-2"
            
    def dc(self):
        print "DC Guc Kademesi::",self.s1.get()
        
        if self.s1.get()==0:
            addr.send("dc_0")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==1:
            addr.send("dc_1")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==2:
            addr.send("dc_2")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==3:
            addr.send("dc_3")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==4:
            addr.send("dc_4")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==5:
            addr.send("dc_5")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==6:
            addr.send("dc_6")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==7:
            addr.send("dc_7")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==8:
            addr.send("dc_8")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==9:
            addr.send("dc_9")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
        elif self.s1.get()==10:
            addr.send("dc_10")
            self.l3["text"]="DC Guc Kademesi:: ",self.s1.get()
            
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
        if (self.e1.get() == "admin" and self.e2.get() == "123"):  
            print "\nGiris Basarili"
            self.kontrol_birimi = 1
            pencere.destroy()
        else:
            print "\nKullanici Adi veya Sifre Hatali !!!"
    

class baglanti:
    def __init__(self,pencere2):
        self.ana_panel_kontrol=0
        
        frame=Frame(pencere2)
        frame.pack()
        
        self.bilgi_l=Label(frame,text="Ip|Port::")
        self.bilgi_l.grid(row=0)
        
        #server ayarlari
        self.l1=Label(frame,text="host::")
        self.l1.grid(row=1,column=0)
        self.e1=Entry(frame)
        self.e1.grid(row=1,column=1)
        

        self.l2=Label(frame,text="port::")
        self.l2.grid(row=2,column=0)
        self.e2=Entry(frame)
        self.e2.grid(row=2,column=1)
        self.b2=Button(frame,text="Kontrol Et",command=self.ip_port)
        self.b2.grid(row=2,column=2,padx=5,pady=5)

        self.b3=Button(frame,text="Baslat",command=self.server_b)
        self.b3.grid(row=3,column=1)
    def ip_port(self):
        self.host=self.e1.get()
        self.port=int(self.e2.get())
        print type(self.host),self.host,type(self.port),self.port
        self.bilgi_l["text"]="Ip|Port::",self.host,"|",self.port

    def server_b(self):
        self.host=self.e1.get()
        self.port=int(self.e2.get())
        
        server.bind((self.host,self.port))
        
        pencere2.destroy()




##pencereler

pencere = Tk()
pencere.title("Giris Paneli")
c = AdminPanel(pencere)
pencere.mainloop()

pencere2=Tk()
if (c.kontrol_birimi == 1):
    g = baglanti(pencere2)
    g.ana_panel_kontrol=1
else:
    g = baglanti(pencere2)
    pencere2.destroy()
pencere2.mainloop()

server.listen(1)
print "Baglanti Bekleniyor"
addr,ip=server.accept()
print "Baglanti basarili\nBaglanan adres::",ip
addr.send("komut")

denetim = Tk()
denetim.geometry("600x250")
denetim.title("Kontrol Paneli")
if (g.ana_panel_kontrol==1):
    h=KontrolPanel(denetim)
else:
    denetim.destroy()
denetim.mainloop()
