import wiki
import json

def printJSON(ugly_json):
    print(json.dumps(ugly_json, sort_keys=True, 
                     indent=4, separators=(',', ': ')))

def main():
    w = wiki.Wiki() # defaults to English Wikipedia
    page = w.getPage('Python (programming language)')
    with open('temp.txt', encoding='utf-8', mode='w+') as f:
        f.write(page.getArticle())
        f.close()

if __name__ == "__main__":
    main()