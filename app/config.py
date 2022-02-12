YT_MIRROR_URL = "https://yewtu.be"

START_MESSAGE = """
Hello, you are using PyYT. Terminal YouTube client for linux.
You are able to read the documentation by typing "help"

"""

HELP_MESSAGE = """
Usage: 
add <channel name> <channel URL>     - Adds new channel to channel-list.
remove <channel name>                - Removes channel from channel-list.
show                                 - Shows channel-list.
show <channel name>                  - Shows video from channel.
watch <video's index>                - Run video. (Works only after "show <channel name>")
watch <channel name> <video's index> - Run video in MPV player.
exit                                 - Closes the shell.
help                                 - Prints this message.
"""