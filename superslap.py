# Type /slap <nick> to slap some one.
import hexchat
import random
__module_name__ = "Super Slap"
__module_version__ = "1.0"
__module_description__ = "Slap script with random items and sizes"
__author__ = "Glorfindel"

full_name = "{} v{} by {}".format(__module_name__,__module_version__,__author__)
help_hook = "\"/slap [nick]\" will slap a [nick]."


items = ["bass", "trout", "salmon", "bluegill", "goldfish", "catfish", "dogfish", "shark", "piranha", "stingray", "jellyfish", "sink", "showerhead", "table", "television", "laptop", "chair", "lamp", "lead pipe", "copy of DOS", "copy of OSX", "copy of OS/2", "an octothorpe", "a copy of Hexchat", "a copy of ubottu"]
size = ["big", "ginormous", "small", "massively small", "nonexistant"]

def cmd_slap(word, word_eol, userdata):
    slapstring = "with a %s %s" %(random.choice(size), random.choice(items))
    if len(word) < 2:
        hexchat.prnt("Choose a nick please")
        return hexchat.EAT_ALL
    if len(word) == 2:
        hexchat.command("me slaps %s around a bit %s " %(word[1], slapstring))
        return hexchat.EAT_ALL
    
hexchat.hook_command("slap", cmd_slap)
print "Super Slap 1.0 By Glorfindel Loaded"
