import requests

version = '0.1'
user_agent = 'wikipy/' + version + '(https://github.com/tomshen/wikipy)'
headers = {'User-Agent': user_agent}

class Wiki():
    def __init__(self, endpoint='http://en.wikipedia.org/w/api.php'):
        self.endpoint = endpoint

    class Page():
        def __init__(self, endpoint, title='', random=False):
            if random:
                payload = {'format': 'json',
                           'action': 'query',
                           'generator': 'random',
                           'prop': 'revisions',
                           'rvprop': 'content'}
            else:
                payload = {'format': 'json',
                           'action': 'query',
                           'titles': title,
                           'prop': 'revisions',
                           'rvprop': 'content'}
            r = requests.get(endpoint, params=payload, headers=headers)
            self.json = r.json()

        def getContent(self):
            for page in self.json['query']['pages'].values():
                return page['revisions'][0]['*']

        def getArticle(self):
            content = self.getContent()
            if "'''" in content:
                content_head = content[:content.index("'''")]
                if '}}' in content_head:
                    article_start = content_head.rindex('}}')+ len('}}')
                    content = content[article_start:]
            article_endings = ['== See also ==', '==See also==',
                               '== References ==', '==References==',
                               '== Further reading ==', '==Further reading==',
                               '== External links ==', '==External links==']
            for ending in article_endings:
                if ending in content:
                    return content[:content.index(ending)].strip()
            return content.strip()

        def getReferences(self):
            content = self.getContent()
            if '== References ==' in content:
                content = content[content.index('== References =='):]
                return content[:content.index('==', len('== References =='))].strip()
            else:
                return 'No references found.'

    def getPage(self, title):
        return self.Page(self.endpoint, title)

    def getRandomPage(self):
        return self.Page(self.endpoint, random=True)