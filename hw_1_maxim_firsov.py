import requests
from pprint import pprint
import json

main_link = 'https://api.github.com/users/'
user = 'postmanlabs'
link = f'{main_link}{user}/repos'

repos = requests.get(link)

if repos.ok:
    data = json.loads(repos.text)

for repo in repos.json():
    if not repo['private']:
        print(f"У пользователя {user} есть такой публичный репозиторий {repo['html_url']}")


