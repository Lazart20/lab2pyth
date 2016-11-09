from itertools import groupby
import re
f1 = open('access.log', 'r')
s = set()
q=[]
for line in f1.readlines():
	
        pattern1 = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        pattern2 = '(\d{1,3}\.\d{1,3}\.\d{1,3}\.)\d{1,3}'
        ip = re.findall(pattern1, line)
        for i in range(len(ip)):
             
                        network= re.findall(pattern2,ip[i])
                        q.append((ip[i],network))



for key, group in groupby(q, lambda x: x[0]):
        for q in group:
                if key in group:
                        pass
                else:
                        
                        print("A %s IP имеет  a %s" % (key, q[1]))
                      
