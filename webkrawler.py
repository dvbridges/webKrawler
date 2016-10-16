#!/usr/bin/python3

# Script Name		: webKrawler.py
# Author			: David Bridges
# Email				: david-bridges@hotmail.co.uk
# Created			: 11th October 2016
# Last Modified		: 16th October 2016
# Version			: 1.0
# Description		: Web crawler - in progress

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
	If not in list, append
	"""
	for i in new:
		if i not in old:
			old.append(i)
	
def krawl_web(seed, max_pages, max_depth):
	"""
	Maintains list of urls to crawl. Max_pages determines number of unique pages to search, and max_depth determines depth
	Operations:
	1) Fill tocrawl with all seed links
	2) while tocrawl has urls and depth < max_depth, loop
	3) if page is not in previously crawled and crawled is shorter than max pages
		- fill new_depth with all urls from each url link in tocrawl. Continue until tocrawl is empty
		- add pages visited to crawled
	4) If tocrawl is empty, fill tocrawl with links from next_depth. Depth +=1. This advances crawler to next depth
	"""
	tocrawl=get_all_links(get_page(seed))
	crawled=[]
	next_depth=[]
	depth=0

	while tocrawl and depth <=max_depth:
		page=tocrawl.pop()
		if page not in crawled and len(crawled)<max_pages:
			union(max_depth,get_all_links(get_page(page)))
			crawled.append(page)
		if not tocrawl:
			tocrawl,next_depth=next_depth,[]
			depth+=1
			print("Advancing depth to stage {}".format(depth+1))
	return crawled 

def Main():
	seed='http://www.udacity.com/cs101x/index.html'
	print(krawl_web(seed,10,4))

if __name__=='__main__':
	Main()

