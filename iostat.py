# Francisco Londono
# May 7 2017
# 
# Input file:
#  iostat.log
#  
# This script calculates min,max, avg, and standard deviation of %user, %nice, %system,
# %iowait %steal, and %idle, and plots the CPU utilization per second
# 
import re
import pdb
import statistics
import matplotlib.pyplot as plt

userlst = []
nicelst = []
systemlst = []
iowaitlst = []
steallst = []
idlelst = []

try:
  file = open("iostat.log","rU")
except:
  print ("Cannot open input file:")
  exit()

## Read the first line
line = file.readline()

while line:
			
	if "avg-cpu" in line:
	   line = file.readline()
	   line.strip()
	   words = line.split()
	   a,b,c,d,e,f = words[0],words[1],words[2],words[3],words[4],words[5]
	   	   
	   userlst.append(a)
	   nicelst.append(b)
	   systemlst.append(c)
	   iowaitlst.append(d)
	   steallst.append(e)
	   idlelst.append(f)
	   
	   		   
	line = file.readline()


file.close()

# plot %system, %user, %idle 
fig = plt.figure()

fig.subplots_adjust(bottom=0.2)

ax1 = fig.add_subplot(111)

line1 = ax1.plot(systemlst,'bo-',label='system')
line2 = ax1.plot(userlst,'go-',label='user')
line3 = ax1.plot(idlelst,'ro-',label='idle')

ax1.set_ylim(0,100)

plt.xlabel("time in seconds")
plt.ylabel("%")
plt.title("CPU Utilization")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),ncol=2)
plt.grid()
plt.show()

# calculate min,max, avg, and standard deviation of %user, %nice, %system,
# %iowait %steal, and %idle
# Lists gets sorted

userlst = [float(i) for i in userlst]
max = len(userlst)
userlst.sort(key=float)

print ("user Min:", userlst[0])
print ("user Max:", userlst[max-1])
print ("user average: %.2f" % (sum(userlst)/max))
print ("user average with lib %.2f" % statistics.mean(userlst))
print ("user std: %.2f" % (statistics.stdev(userlst)))
print ("")

nicelst = [float(i) for i in nicelst]
sorted(nicelst)

print ("nice Min:", nicelst[0])
print ("nice Max:", nicelst[max-1])
print ("nice average: %.2f" % (sum(nicelst)/max))
print ("nice std: %.2f" % (statistics.stdev(nicelst)))
print ("")

systemlst = [float(i) for i in systemlst]
systemlst.sort(key=float)
print ("system Min:", systemlst[0])
print ("system Max:", systemlst[max-1])
print ("system average: %.2f" % (sum(systemlst)/max))
print ("system stddev: %.2f" % statistics.stdev(systemlst))
print ("")

iowaitlst = [float(i) for i in iowaitlst]
iowaitlst.sort(key = float)
print ("iowait Min:", iowaitlst[0])
print ("iowait Max:", iowaitlst[max-1])
print ("iowait average: %.2f" % (sum(iowaitlst)/max))
print ("iowait stddev: %.2f" % statistics.stdev(iowaitlst))
print ("")

steallst = [float(i) for i in steallst]
sorted(steallst)
print ("steal Min:", steallst[0])
print ("steal Max:", steallst[max-1])
print ("steal average: %.2f" % (sum(steallst)/max))
print ("steal stddev: %.2f" % statistics.stdev(steallst))
print ("")

idlelst = [float(i) for i in idlelst]
idlelst.sort(key=float)
print ("idle Min:", idlelst[0])
print ("idle Max:", idlelst[max-1])
print ("idle average: %.2f" % (sum(idlelst)/max))
print ("idle stddev: %.2f" % statistics.stdev(idlelst))
print ("")