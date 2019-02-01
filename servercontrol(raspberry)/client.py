#!usr/bin/env python
# -*- coding:utf-8 -*-
# _*_ coding:cp1254 _*_
#Ahmed Demirezen Feezx1
import socket
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

gpio.output(26,gpio.LOW)
gpio.output(19,gpio.HIGH)
pwm_s.setDuty(2,0)

#Server bilgileri(Çalıştırmadan önce bilgileri güncelleyin)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.1.198"
port=8585
buf=1024

s.connect((host,port))

while True:
    data=s.recv(buf)
    if data=="komut":
        print "Baglanti Basarili"
#step motor
    elif data=="dal":
        print "daliyor"
    elif data=="cik":
        print "cikiyor"    
#servo arka panel
    elif data=="servo_a_0":
        print data
        duty=8.5/180*90+2
        pwm_s.setDuty(3,duty)
    elif data=="servo_a_1":
        print data
        duty=8.5/180*111.5+2
        pwm_s.setDuty(3,duty)
    elif data=="servo_a_2":
        print data
        duty=8.5/180*135+2
        pwm_s.setDuty(3,duty)
    elif data=="servo_a_-1":
        print data
        duty=8.5/180*67.5+2
        pwm_s.setDuty(3,duty)
    elif data=="servo_a_-2":
        print data
        duty=8.5/180*45+2
        pwm_s.setDuty(3,duty)
#servo kanatlar
    elif data=="servo_y_0":
        print data
        duty=8.5/180*90+2
        pwm_s.setDuty(0,duty)
    elif data=="servo_y_1":
        print data
        duty=8.5/180*111.5+2
        pwm_s.setDuty(0,duty)
    elif data=="servo_y_2":
        print data
        duty=8.5/180*135+2
        pwm_s.setDuty(0,duty)
    elif data=="servo_y_-1":
        print data
        duty=8.5/180*67.5+2
        pwm_s.setDuty(0,duty)
    elif data=="servo_y_-2":
        print data
        duty=8.5/180*45+2
        pwm_s.setDuty(0,duty)
#dc     
    elif data=="dc_0":
        print data
        pwm_s.setDuty(2,0)
    elif data=="dc_1":
        print data
        pwm_s.setDuty(2,5)
    elif data=="dc_2":
        print data
        pwm_s.setDuty(2,10)
    elif data=="dc_3":
        print data
        pwm_s.setDuty(2,15)
    elif data=="dc_4":
        print data
        pwm_s.setDuty(2,20)
    elif data=="dc_5":
        print data
        pwm_s.setDuty(2,25)
    elif data=="dc_6":
        print data
        pwm_s.setDuty(2,30)
    elif data=="dc_7":
        print data
        pwm_s.setDuty(2,35)
    elif data=="dc_8":
        print data
        pwm_s.setDuty(2,40)
    elif data=="dc_9":
        print data
        pwm_s.setDuty(2,45)
    elif data=="dc_10":
        print data
        pwm_s.setDuty(2,50)

        
s.close()
