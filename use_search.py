#!/usr/bin/python

from apiclient.discovery import build
from optparse import OptionParser
import get_videos


if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("--q", dest="q", help="Search term",
	default="Google")
	parser.add_option("--max-results", dest="maxResults",
	help="Max results", default=25)
	(options, args) = parser.parse_args()


results= get_videos.youtube_ earch(options)
print results, type(results)  # unicode results 
list_results= list(results)  # listify results  
print type(list_results), list_results

video_ids= [] 
for i in list_results: 
	#a= \(.*?\)
	video_ids.append(a)
print a
# for i in results: 
# 	# print i 
# 	if ord(i) == 40: 
# 		start = results.index(i) 
# 		# print start