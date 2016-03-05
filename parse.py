
import os
import re


remove = []

replace = [
    ("<i>", "_"), ("</i>", "_"),
    ("<code>", "`"), ("</code>", "`"),
    ("<br />", "\n"),
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

    return ("## %s\n" % title) + content + '\n'


def main():
    out = "LeetCode Problems\n====\n\n"

    for top, dirs, nondirs in os.walk("raw"):
        for fname in nondirs:
            path = top + "/" + fname
            print(path)

            out += parse(path)

    with open("LeetCode.md", "w") as outf:
        outf.write(out)

    print("DONE!")


def test():
    print parse("raw/largest-rectangle-in-histogram.html")


if __name__ == "__main__":
    main()
