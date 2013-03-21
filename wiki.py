import requests
import json

version = '0.1'
ua = 'wikipy/' + version + '(https://github.com/tomshen/wikipy)'
headers = {'user-agent': ua}

class Wiki():
    def __init__(self, endpoint='http://en.wikipedia.org/w/api.php'):
        if endpoint:
            self.endpoint = endpoint

    class Page():
        def __init__(self, endpoint, title):
            payload = {'format': 'json',
                   'action': 'query',
                   'titles': title,
                   'prop': 'revisions',
                   'rvprop': 'content'}
            r = requests.get(endpoint, params=payload, headers=headers)
            self.json = r.json()

        def getContent(self):
            for page in self.json['query']['pages'].values():
                return page['revisions'][0]['*'].encode('utf-8')

        def getArticle(self):
            content = self.getContent()
            return content[content.index("'''"):content.index('== See also ==')].strip()

        def getReferences(self):
            content = self.getContent()
            if '== References ==' in content:
                content = content[content.index('== References =='):]
                return content[:content.index('== ', len('== References =='))].strip()
            else:
                return 'No references found.'

    def getPage(self, title):
        return self.Page(self.endpoint, title)