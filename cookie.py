import hexchat
import random

__module_name__ = "cookies"
__module_author__ = "Glorfindel"
__module_version__ = "0.1"

cookieflavor = ['chocolate chip', 'M&M', 'peanut butter', 'gingersnap', 'plain', 'shortbread']

def cookie(word, word_eol, userdata):
    if len(word) < 1:
        hexchat.command("me passes out %s cookies" %(random.choice(cookieflavor)))
    elif len(word) > 1:
        hexchat.command("me hands %s a %s cookie" %(word[1], random.choice(cookieflavor)))
    return hexchat.EAT_ALL

hexchat.hook_command("cookies",cookie)
hexchat.prnt("Cookies V0.1 loaded and ready to be eaten!")
