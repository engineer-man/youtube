from Tkinter import *
from threading import Timer
import random
master=Tk()
c=Canvas(master,width=600,height=480)
c.pack()
for x in range(0,24):
	c.create_rectangle(0,20*x,20,20*(x+1),fill="green")
	c.create_rectangle(580,20*x,600,20*(x+1),fill="green")
for x in range(0,30):
	c.create_rectangle(20*x,0,20*(x+1),20,fill="green")
	c.create_rectangle(20*x,460,20*(x+1),480,fill="green")
cobra=[[1,10]]
c.r=[c.create_rectangle(0,0,20,20,fill="blue")]
c.maca=[1+random.randint(0,27),1+random.randint(0,21)]
c.m=c.create_rectangle(20*(c.maca[0]),20*(c.maca[1]),20*(c.maca[0]+1),20*(c.maca[1]+1),fill="red")
c.direcao=2
def anda():
	for x in range(len(cobra)-1,0,-1):
		cobra[x][0]=cobra[x-1][0]
		cobra[x][1]=cobra[x-1][1]
	if c.direcao==0:cobra[0][0]-=1;
	if c.direcao==1:cobra[0][1]-=1;
	if c.direcao==2:cobra[0][0]+=1;
	if c.direcao==3:cobra[0][1]+=1;
	if cobra[0]==c.maca:
		cobra.append([50,50])
		c.maca=[1+random.randint(0,27),1+random.randint(0,21)]
		c.delete(c.m)
		c.m=c.create_rectangle(20*(c.maca[0]),20*(c.maca[1]),20*(c.maca[0]+1),20*(c.maca[1]+1),fill="red")
	for gomo in c.r:
		c.delete(gomo)
	for gomo in cobra:
		c.r.append(c.create_rectangle(20*(gomo[0]),20*(gomo[1]),20*(gomo[0]+1),20*(gomo[1]+1),fill="blue"))
	vivo=True
	for x in range(1,len(cobra)):
		if (cobra[0][0]==cobra[x][0])and(cobra[0][1]==cobra[x][1]):vivo=False
	if(cobra[0][0]>0)and(cobra[0][1]>0)and(cobra[0][0]<29)and(cobra[0][1]<23)and(vivo):
		t=Timer(.3,anda)
		t.start()
def key(event):
	if str(event.keycode)=="113":c.direcao=0
	if str(event.keycode)=="111":c.direcao=1
	if str(event.keycode)=="114":c.direcao=2
	if str(event.keycode)=="116":c.direcao=3
master.bind("<Key>",key)
t=Timer(.3,anda)
t.start()
mainloop()
