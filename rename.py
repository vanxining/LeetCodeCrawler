
import os


for entry in open("problems.txt"):
    problem_id, title, url, ac = entry.strip().split('\t')
    print title

    os.rename("raw/%s.html" % url, "raw/%s.%s.html" % (problem_id, url))
