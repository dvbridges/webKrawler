#!/usr/bin/python3

# Script Name		: webKrawler.py
# Author			: David Bridges
# Email				: david-bridges@hotmail.co.uk
# Created			: 11th October 2016
# Last Modified		: 16th October 2016
# Version			: 1.0
# Description		: A depth-first web crawler

import urllib.request

def get_page(url_req):
	"""
	Get webpage and decode bytes to string
	"""

	try:
		response=urllib.request.Request(url_req, headers={'User-Agent': 'Mozilla/5.0'})
		with urllib.request.urlopen(response) as f: 
			return f.read().decode('utf-8')
	except UnicodeDecodeError: 
		print("File not utf-8 encoded, switching to cp1252 decoding")
	try:
		response=urllib.request.Request(url_req, headers={'User-Agent': 'Mozilla/5.0'})
		with urllib.request.urlopen(response) as f: 
			return f.read().decode('cp1252')
	except UnicodeDecodeError: 
		print("File not cp1252 encoded, switching to Latin1 decoding")
		response=urllib.request.Request(url_req, headers={'User-Agent': 'Mozilla/5.0'})
		with urllib.request.urlopen(response) as f: 
			return f.read().decode('Latin-1')
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


def get_all_links(page):
	"""
	Print all links in a html file
	"""
	links=[]
	while True:
		# If URL exists, get the URL from get_next_target
		url, end_pos=get_next_target(page)

		if url:
			links.append(url)
			page=page[end_pos:]
		else: break
	return links

def union(old,new):
	"""
	Union function checks whether page is in tocrawl list.
	If not in list, append and visit that webpage
	"""
	for i in new:
		if i not in old:
			old.append(i)
	
def krawl_web(seed):
	"""
	Maintains list of urls to crawl. Visited URLs are removed and sent to "krawled" procedure.
	"""
	tocrawl=get_all_links(get_page(seed))
	crawled=[]
	while tocrawl:
		page=tocrawl.pop()
		if page not in crawled:
			union(tocrawl,get_all_links(get_page(page)))
			crawled.append(page)
	return crawled 

def Main():
	seed='http://www.udacity.com/cs101x/index.html'
	print(krawl_web(seed))

if __name__=='__main__':
	Main()