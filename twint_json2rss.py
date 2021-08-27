import twint
import argparse
from feedgen.feed import FeedGenerator
from dateparser import parse
from pathlib import Path
import json


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert twitter feed to RSS')
    parser.add_argument('--input',
                        help='input json file')
    parser.add_argument('--output',
                        help='Output RSS file')
    args = parser.parse_args()
    inputJson = Path(args.input).read_text("utf8")

    inputLines = inputJson.split("\n")

    fg = FeedGenerator()
    fg = FeedGenerator()
    fg.id('http://www.twitter.com/' + args.input)
    fg.title(args.input)
    fg.description("Rss Feed for twitter account " + args.input)
    fg.author({'name': 'John Doe', 'email': 'john@example.de'})
    fg.logo('http://ex.com/logo.jpg')
    fg.subtitle('This is a cool feed!')
    fg.link(href='http://www.twitter.com/' + args.input, rel='alternate')
    fg.language('en')

    for i in inputLines:
        if len(i.strip()) == 0:
            continue
        else:
            print(i)
            e = json.loads(i)
            dt = parse(e["created_at"])
            entry = fg.add_entry()
            entry.id(e["link"])
            entry.title(e["tweet"])
            entry.description(e["tweet"])
            entry.link(href=e["link"])
            entry.pubdate(dt)
            entry.updated(dt)

    fg.rss_file(args.output)
