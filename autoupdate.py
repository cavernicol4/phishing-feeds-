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
#subprocess.call(['git', 'push', 'https://{}@github.com/cavernicol4/phishing-feeds-'.format(token)])
subprocess.call(['git', 'push', '--set-upstream', 'https://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@github.com/cavernicola/phishing-feeds- master'])