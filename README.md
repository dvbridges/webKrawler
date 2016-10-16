# webKrawler
## A Python webcrawler

This Python webcrawler is in development. The code is mainly inspired by the Introduction to Computer Science course from [Udacity](https://www.udacity.com/), with some additions (such as handling exceptions). The WebKrawler is a depth-first spider which takes a given URL, and searches the html code and creates a list of links which are visited. All URLs are logged and no URL is visited twice. The WebKrawler so far consists of the following functions:

|functions		|Description						   									  			|
|---------------|-----------------------------------------------------------------------------------|
|get_page		|Get webpage and decode bytes to string									  			|
|get_next_target|Find links in html,return url endpoint					                  			|
|get_all_links	|Creates list of all links found html  									  			| 
|union			|Checks newly found urls have not been visite already			   					|
|krawl_web		|Unleashes web crawler on seed URL, with max depth and pages to determine iterations| 