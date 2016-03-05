
from bs4 import BeautifulSoup


soup = BeautifulSoup(open("algo.html"), "lxml")
entries = []

for a in soup.select("td > a"):
    title = a.string
    url = a["href"][10:-1]

    siblings = [sibling for sibling in a.parent.previous_siblings]
    problem_id = siblings[1].string
    ac = siblings[3].span["class"][0]
    if ac == "None":
        ac = "n/a"

    entry = '\t'.join((problem_id, title, url, ac))
    entries.append(entry)


with open("problems.txt", "w") as outf:
    outf.write('\n'.join(entries))
