import requests

version = '0.1'
user_agent = 'wikipy/' + version + '(https://github.com/tomshen/wikipy)'
headers = {'User-Agent': user_agent}

class Wiki():
    def __init__(self, endpoint='http://en.wikipedia.org/w/api.php'):
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
            i = content[:content.index("'''")].rindex('}}')+ len('}}')
            content = content[i:]
            article_endings = ['== See also ==', '==See also==',
                               '== References ==', '==References==',
                               '== Further reading ==', '==Further reading==',
                               '== External links ==', '==External links==']
            for ending in article_endings:
                if ending in content:
                    return content[:content.index(ending)].strip()

        def getReferences(self):
            content = self.getContent()
            if '== References ==' in content:
                content = content[content.index('== References =='):]
                return content[:content.index('==', len('== References =='))].strip()
            else:
                return 'No references found.'

    def getPage(self, title):
        return self.Page(self.endpoint, title)