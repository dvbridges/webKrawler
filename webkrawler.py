#!/usr/bin/python3

# Script Name		: webKrawler.py
# Author			: David Bridges
# Email				: david-bridges@hotmail.co.uk
# Created			: 11th October 2016
# Last Modified		: 11th October 2016
# Version			: 1.0

import urllib.request

def get_page(url_req):
	"""
	Get webpage and decode bytes to string
	"""

	with urllib.request.urlopen(url_req) as response:
		return response.read().decode('utf-8')

def get_next_target(s):
	"""
	Find all links in a html file and return url and last known endpoint
	"""

	start_link=s.find("<a href=")

	# If no links, return None, position 0
	if start_link==-1:
		return None, 0

	# Parse URL from HTML
	start_quote=s.find('"', start_link)
	end_quote=s.find('"',start_quote+1)
	url=s[start_quote+1:end_quote]
	
	#Return URL and last known end position
	return url, end_quote


def print_all_links(page):
	"""
	Print all links in a html file
	"""

	while True:
		# If URL exists, get the URL from get_next_target
		url, end_pos=get_next_target(page)
		if url:
			print (url)
			page=page[end_pos:]
		else: break

def Main():
	page=get_page('http://xkcd.com/353')
	print_all_links(page)


if __name__=='__main__':
	Main()