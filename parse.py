
import os
import re
import StringIO
import HTMLParser


html_parser = HTMLParser.HTMLParser()

remove = []

replace = [
    ("<i>", "_"), ("</i>", "_"),
    ("<code>", "`"), ("</code>", "`"),
    ("<pre>", "```txt\n"), ("</pre>", "\n```"),
    ("<br />", "\n"),
    ("<li>", "* "),
    ("<sup>", " "),
]


def replace_images(content):
    beg = 0

    while True:
        beg = content.find('<img src="', beg)
        if beg == -1:
            break

        beg += 10
        end = content.index('"', beg)

        md = '" />' + "![](%s) <br" % content[beg:end]
        content = content[:beg] + md + content[(end + 1):]

        beg += len(md) + 5

    return content


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

    content = replace_images(content)
    content = re.sub("<[^<]+?>", "", content)

    content = content.decode("utf-8")
    content = html_parser.unescape(content).encode("utf-8")

    sio = StringIO.StringIO(content)
    out = ""
    pre = False

    for line in sio:
        line = line.rstrip()

        if "```" in line:
            pre = not pre

        if not pre:
            line = line.lstrip()

        if not line:
            continue

        out += line + "\n\n"

    return ("## %s\n" % title) + out + '\n'


def main():
    out = "LeetCode Problems\n====\n\n"
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

    with open("LeetCode.md", "w") as outf:
        outf.write(out)

    print("DONE!")


def test():
    out = ""
    out += parse("raw/084.largest-rectangle-in-histogram.html")
    out += parse("raw/031.next-permutation.html")
    print out


if __name__ == "__main__":
    main()
