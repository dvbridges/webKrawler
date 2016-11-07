#!/usr/bin/python3

# Define a function which finds a start location of a target in a string
string="There once was a man named Dave man"

def get_target(search, target):
	return search.find(target)
print (get_target(string, 'man'))

# Define a function which finds second incidence of a target in a string
string="There once was a man named Dave man"

def get_target(search, target):
	first = search.find(target)
	return search.find(target, first+1)
print (get_target(string, 'man'))

