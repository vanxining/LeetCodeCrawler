
import os
import re
import StringIO
import HTMLParser


html_parser = HTMLParser.HTMLParser()

remove = []

replace = [
    ('"/static/images', '"https://leetcode.com/static/images'),
]


def parse(path):
    html = open(path).read()

    beg = html.index("<title>") + 7
    end = html.index('<', beg)
    if beg == end:
        return ""

    title = html[beg:html.index(" | ", beg)]

    beg = html.find("question-content")
    if beg == -1:
        return ""

    beg += 18
    end = html.index("<div>", beg)

    content = html[beg:end]

    for pattern in remove:
        content = content.replace(pattern, ' ')

    for pattern in replace:
        content = content.replace(*pattern)

    return ("<h2>%s</h2>\n" % title) + content + "<br />\n"


def main():
    out = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <title>LeetCode Problems</title>
  <link rel="stylesheet" href="pandoc.css" type="text/css" />
</head>
<body>

<h1>LeetCode Problems</h1>
'''
    count = 0

    for top, dirs, nondirs in os.walk("raw"):
        for fname in nondirs:
            if fname.endswith(".html"):
                path = top + "/" + fname
                print(path)

                out += parse(path)

                count += 1
                if count == 2000:
                    break

    out += "</body></html>"

    with open("LeetCode.html", "w") as outf:
        outf.write(out)

    print("DONE!")


def test():
    out = ""
    out += parse("raw/084.largest-rectangle-in-histogram.html")
    out += parse("raw/031.next-permutation.html")
    print out


if __name__ == "__main__":
    main()
