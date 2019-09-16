# coding=gbk
import pyodbc
import time
import re
connect = pyodbc.connect(DRIVER='{SQL Server}',SERVER='1.2.3.4',DATABASE='master',UID='zabbix_read',PWD='******')
#connect = pyodbc.connect(DRIVER='{SQL Server}',SERVER='192.168.0.5',DATABASE='master',UID='pyselect',PWD='******')
cursor = connect.cursor()
cursor.execute("SP_WHOISACTIVE")
mem =cursor.fetchall()

if mem is None:
	print("数据结果为空")
else:
	for i in mem:
		a=i[0]+i[2]
		start_time=str(i[19])
		CPU_INFO=i[5]
		LOGIN_NAME=i[3]
		#b=i[19]
		'''
		str = i[0]
		if len(i[0]) !=0:
			list1 = str.split(' ')
			day = int(list1[0])
			list2 = list1[1].split(':')
			hh = int(list2[0])
			mm = int(list2[1])
			ss = int(list2[2].split('.')[0])

			result = day * 86400 + hh * 3600 + mm * 60 + ss + 1
			if result>1:

				print(i)
				'''


		b=re.sub('\s',' ',a)
		#print (b)
		#print("LOGIN_NAME:%s ;\n CPU_INFO:%s;\n START_TIME:%s;\n sql_text:%s\n" %(LOGIN_NAME,CPU_INFO,start_time,a))
		#print(a[0:7])
		print(a)
		if int(a[4]) or int(a[6]) or int(a[7])!= 0 or int(a[9])>3 :
			f = open("2.txt", 'a', encoding='gbk')
			f.write(b+"start_time:"+start_time+"CPU_INFO:"+CPU_INFO+"LOGIN_NAME:"+LOGIN_NAME+"ERRORS")
			f.close()
		fp = open("log.txt", 'a',encoding="gbk")
		fp.write("start_time:"+start_time+"\n" + "CPU_INFO"+CPU_INFO+"\n"+"LOGIN_NAME:"+LOGIN_NAME+"\n"+a+ "\n")
		fp.close()


connect.commit()
connect.close()

