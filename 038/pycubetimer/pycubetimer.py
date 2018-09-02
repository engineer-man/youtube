# author: shreyas

import time
import os
from tkinter import *
from tkinter import messagebox
from pyTwistyScrambler import scrambler333

b = 0
timed = '0.00'


def change_scramble():
	scramble.config(text=scrambler333.get_WCA_scramble())


def watch(args=0):
	global b, timed
	# Sets focus on stop button so it can be run through space-bar
	stop.focus_set()
	b = 0
	timed = '0.00'
	now = time.time()
	# Enable Stop button and Disable Start button
	start.config(state=DISABLED)
	stop.config(state=NORMAL)
	while b == 0:
		time.sleep(0.01)
		timer.config(text="%.2f" % (time.time() - now))
		timed = "%.2f" % (time.time() - now)
		root.update()


def freeze(args=0):
	global b, timed, count, times_list, p, avg5, avg5_flo, times_list_5_flo, times_list_5, min_5, max_5, min_c, max_c, avg12, avg12_flo, times_list_12_flo, times_list_12, min_12, max_12, min_c12, max_c12, k ,mean
	# To stop the timer
	b=b+1
	if(float(timed) < 14.96) :
		messagebox.showinfo("Congratulations!", "You just beat the Developer's Best Time of 14.96 seconds!")
	# Re-Enable Start button and Disable Stop button
	start.config(state = NORMAL)
	stop.config(state = DISABLED)
	# To get new scramble
	scramble.config(text = scrambler333.get_WCA_scramble())
	# Save new time to file
	times_file = open('times.txt', 'a+')
	times_file.write(timed + '\n')
	times_file.close()
	# Re-read the file to update stats
	times_file = open('times.txt', 'r+')
	times_list = times_file.readlines()
	count = len(times_list)
	times_file.close()
	# Updates No. of Solves and Last 12 Solves after new solve
	i = 1
	saved_times_str = ''
	if (count < 12):
		while (i <= count):
			if (i == count):
				saved_times_str = saved_times_str + times_list[count - i].strip()
				break
			saved_times_str = saved_times_str + times_list[count - i].strip() + ', '
			i = i + 1
	else:
		while (i < 13):
			if (i == 12):
				saved_times_str = saved_times_str + times_list[count - i].strip()
				break
			saved_times_str = saved_times_str + times_list[count - i].strip() + ', '
			i = i + 1
	times_count.config(text='No. of Solves: ' + str(count))
	saved_times.config(text='Last 12 Solves: ' + saved_times_str)
	# Updates Average of 5 after new solve
	avg5 = ''
	avg5_flo = 0
	min_c = 0
	max_c = 0
	if (count >= 5):
		times_list_5 = times_list[count - 5:count]
		times_list_5_flo = [0, 1, 2, 3, 4]
		p = 0
		while (p < 5):
			times_list_5_flo[p] = float(times_list_5[p].strip())
			p = p + 1
		min_5 = min(times_list_5_flo)
		max_5 = max(times_list_5_flo)
		p = 0
		while (p < 5):
			if (times_list_5_flo[p] == max_5 and max_c == 0):
				p = p + 1
				max_c = 1
				continue
			if (times_list_5_flo[p] == min_5 and min_c == 0):
				p = p + 1
				min_c = 1
				continue
			avg5_flo = avg5_flo + (times_list_5_flo[p] / 3)
			p = p + 1
		avg5 = '%.2f' % (avg5_flo)
	ao5.config(text = 'Average of 5: ' + avg5)
	# Updates Average of 12 after new solve
	avg12 = ''
	avg12_flo = 0
	max_c12 = 0
	min_c12 = 0
	if (count >= 12):
		times_list_12 = times_list[count - 12:count]
		times_list_12_flo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
		p = 0
		while (p < 12):
			times_list_12_flo[p] = float(times_list_12[p].strip())
			p = p + 1
		min_12 = min(times_list_12_flo)
		max_12 = max(times_list_12_flo)
		p = 0
		while (p < 12):
			if (times_list_12_flo[p] == max_12 and max_c12 == 0):
				p = p + 1
				max_c12 = 1
				continue
			if (times_list_12_flo[p] == min_12 and min_c12 == 0):
				p = p + 1
				min_c12 = 1
				continue
			avg12_flo = avg12_flo + (times_list_12_flo[p] / 10)
			p = p + 1
		avg12 = '%.2f' % (avg12_flo)
	ao12.config(text='Average of 12: ' + avg12)
	# Updates Total Mean after new solve
	k = 0
	mean = 0
	while (k < count):
		mean = mean + (float(times_list[k].strip()) / count)
		k = k + 1
	mean = '%.2f' % (mean)
	meantotal.config(text='Total Mean: ' + mean)
	root.update()
	# Sets focus on start button so it can be run through space-bar
	start.focus_set()


root = Tk()
root.config(background='#f6e58d')
# Check if times.txt exists, create if not.
if(not os.path.exists('times.txt')):
	times_file = open('times.txt', 'a+')
	times_file.close()
# Read the file to get existing times and generate stats
times_file = open('times.txt', 'r+')
times_list = times_file.readlines()
count = len(times_list)
times_file.close()
# Main GUI Elements
timer = Label(root, text = '0.00', font=('Helvetica', 120), background='#f6e58d', fg = 'black')
img1 = PhotoImage(file="img/start.png")
img2 = PhotoImage(file="img/stop.png")
chng_image = PhotoImage(file="img/refresh.png")
start = Button(root, command = watch, background='#f6e58d', image=img1, font=('Verdana', 20), relief = FLAT)
start.focus_set()
stop = Button(root, background='#f6e58d', command = freeze, image=img2, font=('Verdana',20), relief = FLAT, state = DISABLED)
times_count = Label(root, text = 'No. of Solves: ' + str(count), font=20, background='#f6e58d', fg = 'black')
# Get last 12 solves
i=1
saved_times_str = ''
if(count<12):
	while (i <= count):
		if (i == count):
			saved_times_str = saved_times_str + times_list[count - i].strip()
			break
		saved_times_str = saved_times_str + times_list[count - i].strip() + ', '
		i = i + 1
else:
	while(i<13):
		if(i==12):
			 saved_times_str = saved_times_str + times_list[count - i].strip()
			 break
		saved_times_str = saved_times_str + times_list[count-i].strip() + ', '
		i = i+1

saved_times = Label(root, text = 'Last 12 Solves: ' + saved_times_str, font=20, background='#f6e58d', fg = 'black')
scramble = Label(root, text = scrambler333.get_WCA_scramble(), font=20, background = '#f6e58d', fg='black')
chng_scramble = Button(root, image=chng_image, relief=FLAT, background = "#f6e58d", command = change_scramble)
# Pack the elements
timer.grid(row=1, columnspan=4, padx = 20, pady = 20)
start.grid(row=2, pady=15, padx=10)
stop.grid(row=2, column=3, pady=15, padx=10)
times_count.grid(row=3, columnspan=4, pady =10, padx = 5)
saved_times.grid(row=4, columnspan=4, pady=10, padx = 10)
scramble.grid(row=0, columnspan=4, pady=15, padx = 5)
chng_scramble.grid(row=0, column=3)
# Initial Average of 5
avg5 = ''
avg5_flo = 0
max_c=0
min_c=0
if(count>=5):
	times_list_5 = times_list[count-5:count]
	times_list_5_flo = [0,1,2,3,4]
	p=0
	while(p<5):
		times_list_5_flo[p] = float(times_list_5[p].strip())
		p=p+1
	min_5 = min(times_list_5_flo)
	max_5 = max(times_list_5_flo)
	p=0
	while(p<5):
		if(times_list_5_flo[p] == max_5 and max_c == 0):
			p=p+1
			max_c = 1
			continue
		if(times_list_5_flo[p] == min_5 and min_c == 0):
			p = p + 1
			min_c = 1
			continue
		avg5_flo = avg5_flo + (times_list_5_flo[p]/3)
		p = p+1
	avg5 = '%.2f' % (avg5_flo)
ao5 = Label(root, text = 'Average of 5: ' + avg5, font=20, background='#f6e58d', fg = 'black')
ao5.grid(row=5, column=0, pady=5, padx=10)
# Initial Average of 12
avg12 = ''
avg12_flo = 0
max_c12=0
min_c12=0
if(count>=12):
	times_list_12 = times_list[count-12:count]
	times_list_12_flo = [0,1,2,3,4,5,6,7,8,9,10,11]
	p=0
	while(p<12):
		times_list_12_flo[p] = float(times_list_12[p].strip())
		p=p+1
	min_12 = min(times_list_12_flo)
	max_12 = max(times_list_12_flo)
	p=0
	while(p<12):
		if(times_list_12_flo[p] == max_12 and max_c12 == 0):
			p=p+1
			max_c12 = 1
			continue
		if(times_list_12_flo[p] == min_12 and min_c12 == 0):
			p = p + 1
			min_c12 = 1
			continue
		avg12_flo = avg12_flo + (times_list_12_flo[p]/10)
		p = p+1
	avg12 = '%.2f' % (avg12_flo)
ao12 = Label(root, text = 'Average of 12: ' + avg12, font=20, background='#f6e58d', fg = 'black')
ao12.grid(row=5, column =1, pady=5, padx=10)
# Initial Total Mean
k = 0
mean = 0
while(k<count) :
	mean = mean + (float(times_list[k].strip()) / count)
	k = k+1
mean = '%.2f' % (mean)
meantotal = Label(root, text = 'Total Mean: ' + mean, font=20, background='#f6e58d', fg = 'black')
meantotal.grid(row=5, column =2, pady=5, padx=10)
devbest = Label(root, text = "Developer's Best: 14.96", font=20, background='#f6e58d', fg = 'black')
devbest.grid(row=5, column =3, pady=5, padx=10)
root.title('pyCubeTimer v1.1')
#root.wm_iconbitmap('img/icon.ico')
root.mainloop()
