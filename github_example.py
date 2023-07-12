import github

gh = github.Github()

repo = gh.get_repo("PyGithub/PyGithub")
print(repo.get_topics())  # Ctrl-click `get_topics`
