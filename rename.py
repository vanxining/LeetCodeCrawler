
import os


for entry in open("problems.txt"):
    problem_id, title, url, ac = entry.strip().split('\t')
    problem_id = int(problem_id)
    print title

    os.rename("raw/%d.%s.html" % (problem_id, url), "raw/%03d.%s.html" % (problem_id, url))
