import os
import yaml
import githubapimock as api

config_path = os.path.expanduser("~/repo.yml")
settings = yaml.load(open(config_path))


org = settings["org"]
repo = settings["repo"]
user = settings["user"]
token = settings["token"]

all_issues = api.get_issues(org, repo, user, token)
issue = all_issues[0]
number = issue["number"]

print(number)
