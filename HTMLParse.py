#_*_encoding:utf-8_*_

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr
    def handle_endtag(self, tag):
        print "End tag  :", tag
    def handle_data(self, data):
        print "Data     :", data
    def handle_comment(self, data):
        print "Comment  :", data
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c
    def handle_decl(self, data):
        print "Decl     :", data


class GP(HTMLParser):
	encoding=''
	def handle_starttag(self, tag, attrs):
		if tag=="meta":
			#print tag
			if attrs[0][0]=="http-equiv":
				#print attrs[0][1]
				#print attrs[1][1]
				s=attrs[1][1].split(';')
				for s1 in s:
					if s1.find("charset=")!=-1:
						#print s1.split('charset=')[-1]+"gg"
						self.encoding=s1.split('charset=')[-1]+"gg"
			#for attr in attrs:
				#print "-attr",attr
				'''
				if attr[0]=="content":
					print attr[1]
					'''
	


xconten=""
f2 = open("spath2.html", "r" )
for  line  in  f2:
	#print (line.decode("utf-8"))
	xconten+=line.decode("utf-8")
f2.close()
#print xconten

parser = GP()
parser.feed(xconten)
print parser.encoding