# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def str_time(time):
	time = str(time)
	if len(time) == 1:
		time = '0' + time
	return (time)

people = int(input())
possible_start_hour = 0
possible_start_minute = 0
possible_end_hour = 24
possible_end_minute = 0
is_possible = True
for i in range(people):
	is_possible_start = True
	is_possible_end = True
	time = input().split(' ~ ')
	start = time[0].split(':')
	start_hour = int(start[0])
	start_minute = int(start[1])
	end = time[1]
	end = time[1].split(':')
	end_hour = int(end[0])
	end_minute = int(end[1])
	if start_hour >= possible_start_hour:
			if start_hour > possible_start_hour:
				possible_start_minute = start_minute
			elif start_minute >= possible_start_minute:
				possible_start_minute = start_minute
			possible_start_hour = start_hour
	if end_hour <= possible_end_hour:
			if end_hour < possible_end_hour:
				possible_end_minute = end_minute
			elif end_minute <= possible_end_minute:
				possible_end_minute = end_minute
			possible_end_hour = end_hour
	if start_hour <= possible_start_hour:
		if start_hour < possible_start_hour:
			is_possible_start = False
		elif start_hour == possible_start_hour:
			if start_minute < possible_start_minute:
				is_possible_start = False
	if end_hour >= possible_end_hour:
		if end_hour > possible_end_hour:
			is_possible_end = False
		elif end_hour == possible_end_hour:
			if end_minute > possible_end_minute:
				is_possible_end = False
	if (not is_possible_start) and (not is_possible_end):
		is_possible = False
		break
possible_start_hour = str_time(possible_start_hour)
possible_start_minute = str_time(possible_start_minute)
possible_end_hour = str_time(possible_end_hour)
possible_end_minute = str_time(possible_end_minute)

if possible_start_hour >= possible_end_hour:
	if possible_start_hour > possible_end_hour:
		is_possible = False
	elif possible_start_minute >= possible_end_minute:
		is_possible = False
if is_possible:
	print("{}:{} ~ {}:{}".format(possible_start_hour, possible_start_minute, possible_end_hour, possible_end_minute))
else:
	print(-1)