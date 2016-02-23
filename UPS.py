#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import subprocess
import os.path

#ChargeTotalTime=28800        #�R�q�`�ɼ� 
ChargeTotalTime=288        #�R�q�`�ɼ�
#PowerOnTotalTime=54000		 #��q�`�ɼ� 
PowerOnTotalTime=540		 #��q�`�ɼ� 

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
	if os.path.exists('PowerOnTime') == False :	#�p�G�S��PowerOnTime�N�إ� 
	        f = open('PowerOnTime','w+')
	        f.write('0\n')
	else :
			if f1.read() == "" :				# ��{���N�~���_��(ex:Crtl+C)
				f2 = open('PowerOnTime','a')	# PowerOnTime,PowerOffTime�̷|�S���
				f2.write('0\n')					# �{���]���|Error 
				f2.close
	if os.path.exists('PowerOffTime') == False :	#�p�G�S��PowerOffTime�N�إ�
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
	
	# tail -n 1 PowerOnTime ŪPowerOnTime�̫�@��    �@�}�l�O�C���s�J �ҥH�~�o�˼g 
	fontail = subprocess.Popen(['tail','-n 1','PowerOnTime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	# tail -n 1 PowerOffTime ŪPowerOffTime�̫�@��
	fofftail = subprocess.Popen(['tail','-n 1','PowerOffTime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		
	Charged=int(fofftail.stdout.readline()) 	           	  #�w�R�q�ɼ� 
	Ontime=int(fontail.stdout.readline())				  #�w�ϥήɼ� 
		 
	if Charged == ChargeTotalTime :		#�B�ץΧ��N�k�s �~����k�U�Ӵ`�� 
		Charged=0
	if Ontime == PowerOnTotalTime :		��
		Ontime=0
	
	count=0
	print "Starting... "
	GPIO.output(GPI17, True)				
	while Ontime<PowerOnTotalTime:					#��qTime
		print "�w�ϥήɶ� : %r:%r:%r" % (Ontime/3600, (Ontime/60)%60, Ontime%60)
		#time.sleep(0.1)
		Ontime+=1
		f = open('PowerOnTime','w+')
		f.write("%r\n" % (Ontime))
		f.close()
		count+=1
		if count%60 == 0 :
			ping = os.system("ping -c 1 -w2 192.168.2.1 > /dev/null 2>&1")
			if ping != 0:				#ping������Ѯ� 
				#os.system("sudo init 0")
				TestRun()
				
	GPIO.output(GPI17, False)

	count=0
	while Charged<ChargeTotalTime:					#�R�qTime
		print "�w�R�q�ɶ� : %r:%r:%r" % (Charged/3600, (Charged/60)%60, Charged%60)
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

