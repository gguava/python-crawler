#_*_encoding:utf-8_*_

import  urllib

class GetOnePageFlow:
	url=""
	content=""
	def openNewthread(self):
		print "ok"
		
	def setUrl(self, url):
		self.url=url
		print self.url
		
	def getpage(self):
		f = urllib.urlopen(self.url)
		print f.getcode()
		#print f.info()
		buf=f.read()
		#print buf.encode( 'utf-8' )
		
		f = open('spath.html', "w" ) 
		f.write( buf)
		
		x2=buf.decode('gbk','ignore').encode( 'utf-8' )
		f = open('spath2.html', "w" ) 
		f.write( x2)
		
	
	def save2db(self):
		print "ok"
	def getCode(self):
		print 'ok'	
	
x=GetOnePageFlow()
x.setUrl("http://www.biquge.com/0_200/469850.html")

x.getpage()
x.getCode()