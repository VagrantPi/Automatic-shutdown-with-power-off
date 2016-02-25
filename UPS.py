#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import subprocess
import os.path

ChargeTotalTime=28800        #充電總時數 
PowerOnTotalTime=54000		 #放電總時數 
# test 測試
GPIO.setmode(GPIO.BOARD)
GPI17 = 11
GPIO.setup(GPI17, GPIO.OUT)

def TestRun() :
	GPIO.output(GPI17, True)
	time.sleep(0.5)
	GPIO.output(GPI17, False)
	time.sleep(0.5)
	GPIO.output(GPI17, True)
	time.sleep(0.5)
	GPIO.output(GPI17, False)
	time.sleep(0.5)



while True:
	if os.path.exists('PowerOnTime') == False :	#如果沒有PowerOnTime就建立 
	        f = open('PowerOnTime','w+')
	        f.write('0\n')
	else :
			if f1.read() == "" :				# 當程式意外中斷時(ex:Crtl+C)
				f2 = open('PowerOnTime','a')	# PowerOnTime,PowerOffTime裡會沒資料
				f2.write('0\n')					# 程式因此會Error 
				f2.close
	if os.path.exists('PowerOffTime') == False :	#如果沒有PowerOffTime就建立
	        f = open('PowerOffTime','w+')
	        f.write('0\n')
	else :
			if f1.read() == "" :
				f2 = open('PowerOffTime','a')
				f2.write('0\n')
				f2.close
				
	# ============================================= 
	# f1 = open('PowerOnTime','r')  
	# if f1.read() == "" :
	#         f2 = open('PowerOnTime','a')
	#         f2.write('0\n')	
	# 	f2.close
	# f1.close
	# f1 = open('PowerOffTime','r')
	# if f1.read() == "" :
	#         f2 = open('PowerOffTime','a')
	#         f2.write('0\n')
	#         f2.close
	# f1.close
	# ============================================= 
	
	# tail -n 1 PowerOnTime 讀PowerOnTime最後一行    一開始是每秒都存入 所以才這樣寫 
	fontail = subprocess.Popen(['tail','-n 1','PowerOnTime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	# tail -n 1 PowerOffTime 讀PowerOffTime最後一行
	fofftail = subprocess.Popen(['tail','-n 1','PowerOffTime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		
	Charged=int(fofftail.stdout.readline()) 	           	  #已充電時數 
	Ontime=int(fontail.stdout.readline())				  #已使用時數 
		 
	if Charged == ChargeTotalTime :		#額度用完就歸零 才有辦法下個循環 
		Charged=0
	if Ontime == PowerOnTotalTime :		
		Ontime=0
	
	count=0
	print "Starting... "
	GPIO.output(GPI17, True)				
	while Ontime<PowerOnTotalTime:					#放電Time
		print "已使用時間 : %r:%r:%r" % (Ontime/3600, (Ontime/60)%60, Ontime%60)
		#time.sleep(0.1)
		Ontime+=1
		f = open('PowerOnTime','w+')
		f.write("%r\n" % (Ontime))
		f.close()
		count+=1
		if count%60 == 0 :
			ping = os.system("ping -c 1 -w2 192.168.2.1 > /dev/null 2>&1")
			if ping != 0:				#ping不到路由時 
				#os.system("sudo init 0")
				TestRun()
				
	GPIO.output(GPI17, False)

	count=0
	while Charged<ChargeTotalTime:					#充電Time
		print "已充電時間 : %r:%r:%r" % (Charged/3600, (Charged/60)%60, Charged%60)
		#time.sleep(0.1)
		Charged+=1
		f = open('PowerOffTime','w+')
		f.write("%r\n" % (Charged))
		f.close()
		count+=1
        if count%60 == 0 :
        	ping = os.system("ping -c 1 -w2 192.168.2.1 > /dev/null 2>&1")
        	if ping != 0: 
				TestRun()

	GPIO.output(GPI17, True)

