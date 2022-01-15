import base64
from github import Github
from github import InputGitTreeElement
import subprocess

user = "cavernicol4"
token = "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"
commit_message = "prueba"
g = Github(user,token)
repo = g.get_user().get_repo('phishing-feeds-') # repo name
file_list = [
    'phishing-feeds-/prueba2.txt',
    'phishing-feeds-/diarios/prueba3.txt'
            ]
subprocess.call(['git', 'add', '-A'])
subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
#subprocess.call(['git', 'push', 'https://{}@github.com/cavernicola/phishing-feeds-'.format(token)])
subprocess.call("git push --set-upstream https://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@github.com/cavernicola/phishing-feeds- master")