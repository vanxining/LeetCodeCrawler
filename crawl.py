
import common
common.prepare(use_proxy=True)


for problem in open("problems.txt"):
    problem = problem.strip()
    url = "https://leetcode.com/problems/%s/" % problem
    html = common.simple_read(url)

    with open("raw/%s.html" % problem, "w") as outf:
        outf.write(html)

    print "Done crawling", url
    common.random_sleep(10)
