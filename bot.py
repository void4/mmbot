from github import Github

accesstoken = open("accesstoken.txt").read().strip()

g = Github(accesstoken)

repo = g.get_repo("void4/mmbot")

"""
pulls = repo.get_pulls(state="open", sort="created", base="main")

for pr in pulls:
    print(pr.number)
"""

issues = repo.get_issues(state="open", labels=["proof"])

for issue in issues:
    print(issue)
    print(dir(issue))
    print(issue.body)
    for comment in issue.get_comments():
        print(comment)
