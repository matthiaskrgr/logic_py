#!/usr/bin/python3

#    attempt to put out information on logical formulas
#    Copyright (C) 2015  Matthias Krüger

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 1, or (at your option)
#    any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA  02110-1301 USA


import sys

__author__ = 'Matthias "matthiaskrgr" Krüger'

_input=[]

# split args
for arg in sys.argv:
	for i in arg.split():
		_input.append(i)

_input.pop(0) # remove the first element which is the script name

print("Input :" + str(_input))

tokenized_input = []


for i in _input:
	# and
	if ((i == "AND") or (i == "&&" ) or (i == "and") or (i == "∧")):
		tokenized_input.append("∧")
		continue
	# or
	if ((i == "OR") or (i == "||" ) or (i == "or") or (i == "∨")):
		tokenized_input.append("∨")
		continue
	# not
	if ((i == "NOT") or (i == "not") or (i == "!" ) or (i == "¬")):
		tokenized_input.append("¬")
		continue
	tokenized_input.append(i)

print("Tokenized: "+  str(tokenized_input))
