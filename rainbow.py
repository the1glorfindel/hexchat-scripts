import xchat, re
import string
 
__module_name__ = "Rainbow"
__module_version__ = "1.0.0"
__module_description__ = "Generates rainbow colored versions of the text you enter. Post it for the specified line-count"
 
def Rainbow(text,offset):
		colorlist = ["\x034","\x037","\x038","\x039","\x0311","\x0312","\x0313","\x036","\x034"]
		rainbowed = ""
 
		for i in xrange(len(text)):
			rainbowed += (colorlist[(i+offset)%len(colorlist)] + text[i])
		return rainbowed
def rainbowcmd(word,word_eol,userdata):
	count = 6
	text = ""
	if len(word) > 1:
		try:
			text = word[1]
		except ValueError:
			text = ""
	if len(word) > 2:
		try:
			count = int(word[2])
		except ValueError:
			count = 6
	for i in xrange(0,count):
		(xchat.get_context()).command("say "+Rainbow(text,i))
 
 
 
xchat.hook_command("r",rainbowcmd,help="/r (text) (line count)")
print "Rainbow script by DEElekgolo loaded. use \\r (text) (count) to generate rainbow-ed text"
