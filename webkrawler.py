#!/usr/bin/python3

# Script Name		: webKrawler.py
# Author			: David Bridges
# Email				: david-bridges@hotmail.co.uk
# Created			: 11th October 2016
# Last Modified		: 16th October 2016
# Version			: 1.0
# Description		: Web crawler and search engine


import urllib.request
def get_page(url):
	"""
	Get webpage and decode bytes to string
	"""
	try:
		if url == "http://www.udacity.com/cs101x/index.html":
			 return ('<html> <body> This is a test page for learning to crawl! '
			 '<p> It is a good idea to '
			 '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
			 'crawl</a> before you try to  '
			 '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
			 'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
			 '</p> </body> </html> ')
		elif url == "http://www.udacity.com/cs101x/crawling.html":
			 return ('<html> <body> I have not learned to crawl yet, but I '
			 'am quite good at '
			 '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
			 '</body> </html>')
		elif url == "http://www.udacity.com/cs101x/walking.html":
			 return ('<html> <body> I cant get enough '
			 '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
			 '</body> </html>')
		elif url == "http://www.udacity.com/cs101x/flying.html":
			 return ('<html> <body> The magic words are Squeamish Ossifrage! '
			 '</body> </html>')
		elif url == "http://top.contributors/velak.html":
			 return ('<a href="http://top.contributors/jesyspa.html">'
		'<a href="http://top.contributors/forbiddenvoid.html">')
		elif url == "http://top.contributors/jesyspa.html":
			 return  ('<a href="http://top.contributors/elssar.html">'
		'<a href="http://top.contributors/kilaws.html">')
		elif url == "http://top.contributors/forbiddenvoid.html":
			 return ('<a href="http://top.contributors/charlzz.html">'
		'<a href="http://top.contributors/johang.html">'
		'<a href="http://top.contributors/graemeblake.html">')
		elif url == "http://top.contributors/kilaws.html":
			 return ('<a href="http://top.contributors/tomvandenbosch.html">'
		'<a href="http://top.contributors/mathprof.html">')
		elif url == "http://top.contributors/graemeblake.html":
			 return ('<a href="http://top.contributors/dreyescat.html">'
		'<a href="http://top.contributors/angel.html">')
		elif url == "A1":
			 return  '<a href="B1"> <a href="C1">  '
		elif url == "B1":
			 return  '<a href="E1">'
		elif url == "C1":
			 return '<a href="D1">'
		elif url == "D1":
			 return '<a href="E1"> '
		elif url == "E1":
			 return '<a href="F1"> '
	except:
			return ""
	return ""

	# try:
	# 	response=urllib.request.Request(url_req, headers={'User-Agent': 'Mozilla/5.0'})
	# 	with urllib.request.urlopen(response) as f: 
	# 		return f.read().decode('utf-8')
	# except UnicodeDecodeError: 
	# 	print("File not utf-8 encoded, switching to cp1252 decoding")
	# try:
	# 	response=urllib.request.Request(url_req, headers={'User-Agent': 'Mozilla/5.0'})
	# 	with urllib.request.urlopen(response) as f: 
	# 		return f.read().decode('cp1252')
	# except UnicodeDecodeError: 
	# 	print("File not cp1252 encoded, switching to Latin1 decoding")
	# 	response=urllib.request.Request(url_req, headers={'User-Agent': 'Mozilla/5.0'})
	# 	with urllib.request.urlopen(response) as f: 
	# 		return f.read().decode('Latin-1')

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
	index={}
	depth=0
	graph={}

	while tocrawl and max_depth >=1:
		page=tocrawl.pop()
		if page not in crawled and len(crawled)<=max_pages:
			content=get_page(page)
			add_page_to_index(index, page, content)
			outlinks=get_all_links(content)
			graph[page]=outlinks
			union(next_depth,outlinks)
			crawled.append(page)
		if not tocrawl:
			tocrawl,next_depth=next_depth,[]
			max_depth-=1
	return index,graph

def add_page_to_index(index, url, content):
	"""
	Takes all words from webpage, and adds to index linking URL to keyword
	"""
	words = content.split()
	for word in words:
		add_to_index(index, word, url)

def add_to_index(index, keyword, url):
	"""
	Takes all words from webpage, and adds to index linking URL to keyword
	"""
	if keyword in index:
		index[keyword].append(url)
	else:
		index[keyword]=[url]

def lookup(index, keyword):
	"""
	Looks up keyword in index, returns URL if found, None if not found
	"""
	if keyword in index:
		return index[keyword]
	return None

def compute_ranks(graph):
	"""
	Function for computing ranked web pages
	"""
	d = 0.8 # damping factor
	numloops=10

	ranks={}
	npages=len(graph)
	
	for page in graph:
		ranks[page]=1.0/npages

	for i in range(0,numloops):
		newranks={}
		for page in graph:
			newrank=(1-d)/npages
			for node in graph:
				if page in graph[node]:
					newrank=newrank+d*(ranks[node]/len(graph[node]))
			newranks[page]=newrank
		ranks=newranks
	return ranks	
def get_topRank(rank):
	"""
	Function for sorting and returns highest ranked pages, and ranking
	"""
	maxRank=[]
	best=[]

	for page in rank:
		maxRank.append(rank[page])
	maxRank.sort(reverse=True)
	
	for page in rank:
		if rank[page]==maxRank[0]:
			best.append(page)
	return best, maxRank[0] 		

def Main():
	seed='http://www.udacity.com/cs101x/index.html'
	index,graph = krawl_web(seed,10,6)

	# Look up page
	print ("The word {} can be found at {}\n".format('good',lookup(index,'good')))

	# Get page ranks
	ranks = compute_ranks(graph)
	print ("The page ranks are:\n {}\n".format((ranks)))

	# Get highest ranking page
	highest = get_topRank(ranks)
	print("The highest ranking pages from the search are: \n{}\n".format(highest))

if __name__=='__main__':
	Main()