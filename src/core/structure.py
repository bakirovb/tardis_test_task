import re
import requests
from datetime import datetime

DEFAULT_URL = 'https://freestylo.ru/'

parse_tag_re = re.compile(r"""
     <([a-zA-Z][-.a-zA-Z0-9:_]*)(?=\s.*>) |            # single tag regexp
     <([a-zA-Z][-.a-zA-Z0-9:_]*)>(?=.*</\2>)           # double tag regexp
     """, flags=re.DOTALL | re.VERBOSE)


def get_html_text(url: str) -> str:
    responce = requests.get(url)
    return responce.text


def get_tags_count(url: str = DEFAULT_URL, needed_tags: list = None) -> dict:
    text = get_html_text(url)
    res = parse_tag_re.findall(text)
    tags = []
    for item in res:
        if item[0] != '':
            tags.append(item[0])
        else:
            tags.append(item[1])
    grouped_tags = {}
    for tag in tags:
        if tag in grouped_tags:
            grouped_tags[tag] += 1
        else:
            grouped_tags[tag] = 1
    if needed_tags is None:
        return grouped_tags
    return weed_out_tags(needed_tags, grouped_tags)


def check_structure(url: str, structure: dict) -> dict:
    tags_count = get_tags_count(url)
    return get_structure_difference(structure, tags_count)


def weed_out_tags(needed_tags: list, tags: dict) -> dict:
    return {key: value for key, value in tags.items() if key in needed_tags}


def get_structure_difference(proposed_structure: dict, structure: dict) -> dict:
    difference_tags = {}
    for key, value in structure.items():
        difference = abs(value - proposed_structure.get(key, 0))
        if difference > 0:
            difference_tags[key] = difference
    return difference_tags
