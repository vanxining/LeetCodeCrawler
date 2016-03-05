
html = open("algo.html").read()
html = html[:html.index("sidebar-module")]

pos = html.index('id="problemList"')
while pos != -1:
    pos = html.find("/problems/", pos)
    end = html.find('"', pos)
    url = html[pos:end]
    print url

    pos = end
