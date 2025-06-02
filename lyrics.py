
import json, re
from urllib.parse import quote
from urllib.request import urlopen

def _request_lyrics(artist, name) -> str:
    template = 'https://api.lyrics.ovh/{}/{}/{}/'
    tmpltvdn = 'v1'
    term = template.format(tmpltvdn, quote(artist), quote(name))

    try:
        with urlopen(term) as url:
            requested = json.load(url)
            return requested['lyrics']
    except:
        'Music Not Found/Website Not Found/Any Other Exceptions'
    return str()

def get_lyrics(artist: str, name: str) -> str:
    """
    :param `artist` - artist of the music you want to find lyrics for\n
    :param `name` - name of the music you want to find lyrics for\n

    returns the lyrics of the music (artist - name)
    """
    requested = _request_lyrics(artist, name)
    if len(requested):
        return re.sub(r'\n{2,}', '\n', requested)
    raise Exception('Lyrics not found')

def get_lyrics_list(artist: str, name: str) -> list[str]:
    """
    :param `artist` - artist of the music you want to find lyrics for\n
    :param `name` - name of the music you want to find lyrics for\n

    returns list of all lines of the lyrics for the music (artist - name)
    """
    return get_lyrics(artist, name).split('\n')
