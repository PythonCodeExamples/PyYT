from os import system
from urllib.parse import urlparse

from db_manager import DBManager
from utils import show_channel_video, check_url
from config import YT_MIRROR_URL, START_MESSAGE, HELP_MESSAGE


class Shell:
    def __init__(self):
        self.__command_invite = "PyYT $ "
        self.db = DBManager()
        self.quit_flag = False

        # Some buffering for reduce
        # number of requests
        self.buffered_channel_name = ""
        self.buffered_video_list = {}


    def run(self) -> None:
        """ Runs interactive shell. """
        print(START_MESSAGE)
        while not self.quit_flag:
            command = input(self.__command_invite).split(" ")
            self._handle_command(command)
            print()


    def _handle_command(self, command: list) -> None:
        """ Processes commands from user. """
        if command[0] == "show":
            if len(command) == 1:
                self._show_handler(None)
            elif len(command) == 2:
                self._show_handler(command[1])
            else:
                print("Usage: show [OPTIONAL: <channel name>]")
           
        elif command[0] == "add": 
            if len(command) == 3:
                self._add_handler(command[1], command[2])
            else:
                print("Usage: add <channel name> <channel URL>")
            
        elif command[0] == "remove":
            try:
                if (command[1],) in self.db.show_channels():
                    self.db.remove_channel(command[1])
                else:
                    print("Name doesn't exist.")
            except IndexError as _ex:
                print("Usage: remove <channel name>")
        
        elif command[0] == "watch":
            if len(command) == 2:
                if not self.buffered_channel_name == "":
                    self._watch_handler(self.buffered_channel_name, int(command[1]))
                else:
                    print('Buffer is empty for now.\nUse: "show <channel name>"')
            elif len(command) == 3:
                self._watch_handler(command[1], int(command[2]))
            else:
                print("Usage: watch <channel name> <video's index>")

        elif command[0] == "help":
            print(HELP_MESSAGE)

        elif command[0] == "exit":
            self.quit_flag = True

        else:
            print("error: Unknown command")
    

    def _show_handler(self, channel: str) -> None:
        """
        Prints list of channels if arguments is None,
        otherwise prints list of videos from channel.
        """
        try:
            if not channel:
                for chan_info in self.db.show_channels():
                    print(f"{chan_info[0]}")
            else:
                # If video list is not in the buffer, parse it
                if not self.buffered_channel_name == channel:
                    self.buffered_video_list = show_channel_video(
                        self.db.get_channel_link(channel)
                    )
                self.buffered_channel_name = channel
                self._print_video_list()
        except TypeError:
            print("Invalid channel name. Try again.")

    
    def _add_handler(self, name: str, url: str) -> None:
        """ Adds new channel and link into follows. """
        if (name,) in self.db.show_channels():
            print("Name already exists.")
            return

        if not check_url(url):
            print("Invalid link.")
            return

        self.db.add_channel(name, url)

    def _watch_handler(self, channel: str, index: int) -> None:
        """ Starts MPV player with video <index> from <channel>. """

        # If buffer doesn't contains videos from channel
        # refresh buffer with videos from channel
        if not self.buffered_channel_name == channel:
            try:
                self.buffered_video_list = show_channel_video(
                    self.db.get_channel_link(channel)
                )
            except TypeError:
                print("Invalid channel name.")
                return

        videos_list = [name for name in self.buffered_video_list.keys()]
        videos_list.reverse()

        try:
            link = YT_MIRROR_URL + self.buffered_video_list[videos_list[index-1]]
        except IndexError:
            print("Invalid video index.")
            return

        system(f'mpv --ytdl-format="bestvideo[height<=720]+bestaudio/best" {link}')
    

    def _print_video_list(self) -> None:
        """ Prints list of videos titles from dictioanary of videos. """
        counter = len(self.buffered_video_list.keys())
        for name in self.buffered_video_list.keys():
            print(f"{counter}. {name}")
            counter -= 1
            