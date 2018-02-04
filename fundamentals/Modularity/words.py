#!/usr/bin/env python3
"""
Retrieve words from a UTF-8 text document and print it

    Usage:
        python words.py <url>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """
    Fetch a list of words from a URL.
    :param url: The url of a UTF-8 text document.
    :return: A list of strings containing words from a document
    """
    with urlopen(url) as story:
        story_words = []
        print(type(story))
        for line in story:
            print(type(line))
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(items):
    """
    Print items one per line
    :param items: An iterable series of printable items
    """
    for item in items:
        print(item)


def main(arg):
    """
    Print each word from a text document
    :param arg: The URL of a UTF-8 text document
    """
    url = arg
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # the 0 th argument is the module file name.

