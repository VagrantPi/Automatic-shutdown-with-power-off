#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import subprocess
import os.path

<<<<<<< HEAD
ChargeTotalTime=28800        #�R�q�`�ɼ� 
PowerOnTotalTime=54000		 #��q�`�ɼ� 



=======
ChargeTotalTime=28800        #充電總時數 
PowerOnTotalTime=54000		 #放電總時數 
# test 測試
>>>>>>> df4af07dfa536ef8c640844d90077ad1ecd05df2
GPIO.setmode(GPIO.BOARD)
GPI17 = 11			# relay 1 
GPI18 = 12			# relay 2
GPIO.setup(GPI17, GPIO.OUT)
GPIO.setup(GPI18, GPIO.OUT)

#def TestRun1() :
#	GPIO.output(GPI17, True)
#	time.sleep(0.5)
#	GPIO.output(GPI17, False)
#	time.sleep(0.5)
#	GPIO.output(GPI17, True)
#	time.sleep(0.5)
#	GPIO.output(GPI17, False)
#	time.sleep(0.5)

#def TestRun2() :
#	GPIO.output(GPI18, True)
#	time.sleep(0.5)
#	GPIO.output(GPI18, False)
#	time.sleep(0.5)
#	GPIO.output(GPI18, True)
#	time.sleep(0.5)
#	GPIO.output(GPI18, False)
#	time.sleep(0.5)




while True:
<<<<<<< HEAD
	f = open('PowerOnTime','w+')
	if os.path.exists('PowerOnTime') == False :	#�p�G�S��PowerOnTime�N�إ� 
	        f.write('0\n')
	else :
			if f.read() == "" :				# ��{���N�~���_��(ex:Crtl+C)
				f2 = open('PowerOnTime','a')	# PowerOnTime,PowerOffTime�̷|�S���
				f2.write('0\n')					# �{���]���|Error 
				f2.close
	f.close
	f = open('PowerOnTime2','w+')
	if os.path.exists('PowerOnTime2') == False :	#�p�G�S��PowerOnTime�N�إ� 
	        f.write('0\n')
	else :
			if f.read() == "" :				# ��{���N�~���_��(ex:Crtl+C)
				f2 = open('PowerOnTime2','a')	# PowerOnTime,PowerOffTime�̷|�S���
				f2.write('0\n')					# �{���]���|Error 
				f2.close
	f.close
	f = open('PowerOffTime','w+')
	if os.path.exists('PowerOffTime') == False :	#�p�G�S��PowerOffTime�N�إ�
=======
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
>>>>>>> df4af07dfa536ef8c640844d90077ad1ecd05df2
	        f.write('0\n')
	else :
			if f.read() == "" :
				f2 = open('PowerOffTime','a')
				f2.write('0\n')
				f2.close
	f.close
	f = open('PowerOffTime2','w+')
	if os.path.exists('PowerOffTime2') == False :	#�p�G�S��PowerOffTime�N�إ�
	        f.write('0\n')
	else :
			if f.read() == "" :
				f2 = open('PowerOffTime2','a')
				f2.write('0\n')
				f2.close
	f.close
	
<<<<<<< HEAD
	f = open("PowerOffTime","r")
	f2 = open("PowerOffTime2","r")
	f3 = open("PowerOnTime","r")
	f4 = open("PowerOnTime2","r")
		
	Charged=int(f.readline()) 	           	  #�w�R�q�ɼ� 
	Charged2=int(f2.readline()) 
	Ontime=int(f3.readline())				  #�w�ϥήɼ� 
	Ontime2=int(f4.readline())				  #�w�ϥήɼ� 

	 
	if Charged == ChargeTotalTime :		#�B�ץΧ��N�k�s �~����k�U�Ӵ`�� 
		Charged=0
	if Ontime == PowerOnTotalTime :
=======
	# tail -n 1 PowerOnTime 讀PowerOnTime最後一行    一開始是每秒都存入 所以才這樣寫 
	fontail = subprocess.Popen(['tail','-n 1','PowerOnTime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	# tail -n 1 PowerOffTime 讀PowerOffTime最後一行
	fofftail = subprocess.Popen(['tail','-n 1','PowerOffTime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		
	Charged=int(fofftail.stdout.readline()) 	           	  #已充電時數 
	Ontime=int(fontail.stdout.readline())				  #已使用時數 
		 
	if Charged == ChargeTotalTime :		#額度用完就歸零 才有辦法下個循環 
		Charged=0
	if Ontime == PowerOnTotalTime :		
>>>>>>> df4af07dfa536ef8c640844d90077ad1ecd05df2
		Ontime=0
	if Charged2 == ChargeTotalTime :		#�B�ץΧ��N�k�s �~����k�U�Ӵ`�� 
		Charged2=0
	if Ontime2 == PowerOnTotalTime :
		Ontime2=0

	count=0
	print "Cycle... "
	GPIO.output(GPI17, True)				
<<<<<<< HEAD
	GPIO.output(GPI18, True)				

	if Ontime!=0
		while Ontime<PowerOnTotalTime:					#��qTime
			#print "�w�ϥήɶ� : %r:%r:%r" % (Ontime/3600, (Ontime/60)%60, Ontime%60)
			if Charged2 < ChargeTotalTime :
				print "A use : %r:%r:%r   " % (Ontime/3600, (Ontime/60)%60, Ontime%60),
			else :
				print "A use : %r:%r:%r   " % (Ontime/3600, (Ontime/60)%60, Ontime%60)
			time.sleep(1)
			Ontime+=1
			f = open('PowerOnTime','w+')
			f.write("%r\n" % (Ontime))
			f.close()
			if Charged2 < ChargeTotalTime :
				print "B Charged : %r:%r:%r" % (Charged2/3600, (Charged2/60)%60, Charged2%60)
				Charged2+=1
				f = open('PowerOffTime2','w+')
				f.write("%r\n" % (Charged2))
				f.close()
			count+=1
			if count%60 == 0 :
				ping = os.system("ping -c 1 -w2 192.168.2.1 > /dev/null 2>&1")
				if ping != 0:				#ping������Ѯ� 
					os.system("sudo init 0")
			

=======
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
				
>>>>>>> df4af07dfa536ef8c640844d90077ad1ecd05df2
	GPIO.output(GPI17, False)
	GPIO.output(GPI18, False)

	count=0
<<<<<<< HEAD

	if Ontime!=0
		while Ontime2<PowerOnTotalTime:					#�R�qTime
			if Charged < ChargeTotalTime :
				print "B use : %r:%r:%r   " % (Ontime2/3600, (Ontime2/60)%60, Ontime2%60),
			else :
				print "B use : %r:%r:%r   " % (Ontime2/3600, (Ontime2/60)%60, Ontime2%60)
			time.sleep(1)
			Ontime2+=1
			f = open('PowerOnTime','w+')
			f.write("%r\n" % (Ontime2))
			f.close()
			if Charged < ChargeTotalTime :
				print "A Charged : %r:%r:%r" % (Charged/3600, (Charged/60)%60, Charged%60)
				Charged+=1
				f = open('PowerOffTime2','w+')
				f.write("%r\n" % (Charged))
				f.close()
			count+=1
			if count%60 == 0 :
				ping = os.system("ping -c 1 -w2 192.168.2.1 > /dev/null 2>&1")
				if ping != 0:				#ping������Ѯ� 
					os.system("sudo init 0")

=======
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
>>>>>>> df4af07dfa536ef8c640844d90077ad1ecd05df2

	GPIO.output(GPI17, True)
	GPIO.output(GPI18, True)

