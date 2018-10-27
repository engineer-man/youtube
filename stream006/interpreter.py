#!/usr/bin/env python3
import re
import os
import sys

if len(sys.argv) < 2:
	print('you must specify a file to run')
	quit()

input_file = sys.argv[1]

with open(input_file) as file:
	chr = 0
	source = file.read()

variables = {}

def squeeze():
	global chr

	while chr < len(source) and source[chr] in [' ', '\t', '\n']:
		chr += 1

def handle_assignment():
	global chr

	var_name = re.findall(r'^([a-zA-Z0-9]+)\s+?=', source[chr:])[0]

	chr += len(var_name)
	squeeze()
	chr += 1
	squeeze()

	var_content = ''

	if source[chr] == '\'':
		chr += 1
		while source[chr] != '\'':
			var_content += source[chr]
			chr += 1

	variables[var_name] = var_content

	chr += 1
	squeeze()

def handle_print():
	global chr

	chr += 5
	squeeze()
	chr += 1

	var_name = ''

	while source[chr] != ')':
		var_name += source[chr]
		chr += 1

	chr += 1
	squeeze()

	try:
		print(variables[var_name])
	except:
		print('unknown variable name: %s' % var_name)
		quit()


while chr < len(source):
	# assignment test
	if re.match(r'^([a-zA-Z0-9]+)\s+?=', source[chr:]):
		handle_assignment()
		continue

	# print test
	if re.match(r'^print\s*\(', source[chr:]):
		handle_print()
		continue

	chr += 1
