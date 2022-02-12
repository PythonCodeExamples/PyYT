import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup as BS

from config import YT_MIRROR_URL


def show_channel_video(url: str) -> dict:
    """
    Parses videos from url and returns
    dictionary like this <video name>: <url>
    """
    path = _get_path_from_url(url)
    to_parse = YT_MIRROR_URL + path
    return parse_channel(to_parse)


def parse_channel(url: str) -> dict:
    """ Does main parsing job. """
    html = requests.get(url)
    html.encoding = "utf-8"
    soup = BS(html.text, "html.parser")
    divs = soup.find_all("div", class_="thumbnail")
    video_a_tags = [div.parent for div in divs]
    video_a_tags.reverse()
    videos = {}
    for tag in video_a_tags:
        videos[tag.find("p", recursive=False).text] = tag["href"]
    return videos


def _get_path_from_url(url: str) -> str:
    """
    Returns path from URL.
    before: https://youtube.com/channel/somehashofchannel
    after:  /channel/somehashofchannel
    """
    return urlparse(url).path


def check_url(url: str) -> bool:
    res = urlparse(url)
    return res.path.startswith("/c") and res.netloc == "www.youtube.com"