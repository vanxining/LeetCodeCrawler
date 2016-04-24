LeetCodeCrawler
=====

A crawler that generates a single HTML page containing all open (free) problems on LeetCode site.

### Usage

A hard way to finish the job:

* Save <https://leetcode.com/problemset/algorithms/> to a single HTML page named algo.html
* Run `extract_problems.py` to extract all problem titles. This step will
create the `problems.txt` file in the current directory
* Run `crawl.py` to download all problems listed in `problems.txt`. The raw HTML files
will be placed in the `raw` sub directory
* Run `parse2.py` to generate a single HTML page with the name `LeetCode.html`
* Print the HTML page in a browser
* DONE!