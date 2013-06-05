#!/usr/bin/env python
#
# googl.py
# a url shortener using goo.gl service
# return short url
# ./googl.py --url http://mweldan.com
####################################

import argparse
import sys
import requests
import json

"""
URl objects
"""
class target:
	pass

"""
Overwrite error message handling, show help
"""
class MyParser(argparse.ArgumentParser):
	def error(self, message):
		sys.stderr.write("Error: %s\n" % message)
		sys.stderr.write("============================\n")
		self.print_help()
		sys.exit(2)
		
"""
Run script
"""			
def run():
	url = 'https://www.googleapis.com/urlshortener/v1/url'
	payload = { "longUrl": target.url }
	headers = { "content-type": "application/json" }
	
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	
	if r.ok == True:
		result = r.json()
		print "====================================="
		print "Short URL: "+result.values()[1]
		print "====================================="	

"""
Show help text
"""
def main():
	parser = MyParser(
		prog="googl.py",
		description="A goo.gl url shortener script \
		[ Weldan Jamili <mweldan@gmail.com ]"
	)
	parser.add_argument(
		'--url', 
		help='URL', 
		required=True, 
		metavar='http://mweldan.com'
	)
	
	arguments = parser.parse_args(namespace=target)	

	if target.url.find("//") != -1:
		run()
	else:
		parser.print_help()
	
if __name__ == "__main__":
	main()
