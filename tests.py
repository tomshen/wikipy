import wiki
import json

def printJSON(ugly_json):
    print(json.dumps(ugly_json, sort_keys=True, 
                     indent=4, separators=(',', ': ')))

def main():
    w = wiki.Wiki() # defaults to English Wikipedia
    page = w.getPage('Wikipedia')
    with open('temp.txt', 'w') as f:
        f.write(page.getArticle().decode('ascii', 'ignore'))
        f.close()

if __name__ == "__main__":
    main()