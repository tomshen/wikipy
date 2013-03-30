# wikipy

Easy access to the MediaWiki API in Python 2 or 3.
Uses [Requests](http://www.python-requests.org).

## Usage
```python
from wiki import Wiki
page_html = Wiki().getPage('Monty Python').getHTMLContent()
```
