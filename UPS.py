#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import subprocess
import os.path

#ChargeTotalTime=28800        #筿羆计 
ChargeTotalTime=288        #筿羆计
#PowerOnTotalTime=54000		 #筿羆计 
PowerOnTotalTime=540		 #筿羆计 

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
	if os.path.exists('PowerOnTime') == False :	#狦⊿ΤPowerOnTime碞ミ 
	        f = open('PowerOnTime','w+')
	        f.write('0\n')
	else :
			if f1.read() == "" :				# 讽祘Α種い耞(ex:Crtl+C)
				f2 = open('PowerOnTime','a')	# PowerOnTime,PowerOffTime柑穦⊿戈
				f2.write('0\n')					# 祘Α穦Error 
				f2.close
	if os.path.exists('PowerOffTime') == False :	#狦⊿ΤPowerOffTime碞ミ
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
	
	# tail -n 1 PowerOnTime 弄PowerOnTime程︽    秨﹍琌–常 ┮硂妓糶 
	fontail = subprocess.Popen(['tail','-n 1','PowerOnTime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	# tail -n 1 PowerOffTime 弄PowerOffTime程︽
	fofftail = subprocess.Popen(['tail','-n 1','PowerOffTime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		
	Charged=int(fofftail.stdout.readline()) 	           	  #筿计 
	Ontime=int(fontail.stdout.readline())				  #ㄏノ计 
		 
	if Charged == ChargeTotalTime :		#肂ノЧ碞耴箂 Τ快猭碻吏 
		Charged=0
	if Ontime == PowerOnTotalTime :		浂
		Ontime=0
	
	count=0
	print "Starting... "
	GPIO.output(GPI17, True)				
	while Ontime<PowerOnTotalTime:					#筿Time
		print "ㄏノ丁 : %r:%r:%r" % (Ontime/3600, (Ontime/60)%60, Ontime%60)
		#time.sleep(0.1)
		Ontime+=1
		f = open('PowerOnTime','w+')
		f.write("%r\n" % (Ontime))
		f.close()
		count+=1
		if count%60 == 0 :
			ping = os.system("ping -c 1 -w2 192.168.2.1 > /dev/null 2>&1")
			if ping != 0:				#pingぃ隔パ 
				#os.system("sudo init 0")
				TestRun()
				
	GPIO.output(GPI17, False)

	count=0
	while Charged<ChargeTotalTime:					#筿Time
		print "筿丁 : %r:%r:%r" % (Charged/3600, (Charged/60)%60, Charged%60)
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

