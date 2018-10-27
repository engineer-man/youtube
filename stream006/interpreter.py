#!/usr/bin/env python3
import os
import sys
import re

if len(sys.argv) < 2:
	print('you must supply an input file')
	quit()

variables = {}
chr = 0
source = ''

with open(sys.argv[1]) as file:
	source = file.read()

def squeeze():
	global chr

	while chr < len(source) and source[chr] in [' ', '\t', '\n']:
		chr += 1

def handle_comment():
	global chr

	while chr < len(source) and source[chr] != '\n':
		chr += 1

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
		chr += 1
		variables[var_name] = var_content

	if source[chr] in ['0','1','2','3','4','5','6','7','8','9']:
		while source[chr] != '\n':
			var_content += source[chr]
			chr += 1
		variables[var_name] = int(var_content)

	squeeze()

def handle_yell():
	global chr

	chr += 4
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
		print('unknown variable: %s' % var_name)
		quit()


while chr < len(source):
	if source[chr:].startswith('#'):
		handle_comment()
		continue

	if re.match(r'^([a-zA-Z0-9]+)\s+?=', source[chr:]):
		handle_assignment()
		continue

	if re.match(r'^yell\s*\(', source[chr:]):
		handle_yell()
		continue

	chr += 1
