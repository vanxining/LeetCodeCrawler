
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
    end = html.index('<a href="/subscribe/">Subscribe</a>', beg)
    end = html.rindex("<div>", beg, end)

    content = html[beg:end]

    for pattern in remove:
        content = content.replace(pattern, ' ')

    for pattern in replace:
        content = content.replace(*pattern)

    content = remove_tree_serialization_hints(content)
    content = add_hints_alert(content)
    content = remove_credits(content)

    return ("<h2>%s</h2>\n" % title) + content + "\n<br />\n"


def add_hints_alert(content):
    pos = content.find('<ol id="hints">')
    if pos == -1:
        return content

    return content[:pos] + "<p><b>Hints:</b></p>\n" + content[pos:]


def remove_credits(content):
    pos = content.find("<p><b>Credits:</b>")
    if pos == -1:
        return content

    end = content.index("</p>", pos) + 4
    return content[:pos] + content[end:]


def remove_tree_serialization_hints(content):
    beg = content.find("OJ's Binary Tree Serialization")
    if beg == -1:
        return content

    beg = content[:beg].rindex('<p class="showspoilers">confused what')
    end = content.index('</div></p>', beg) + 6

    return content[:beg] + content[end:]


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
    out += parse("raw/229.majority-element-ii.html")
    out += parse("raw/216.combination-sum-iii.html")
    out += parse("raw/084.largest-rectangle-in-histogram.html")
    out += parse("raw/031.next-permutation.html")
    out += parse("raw/094.binary-tree-inorder-traversal.html")
    print out
    quit()


if __name__ == "__main__":
    main()
