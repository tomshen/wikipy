import wiki
import json

def printJSON(ugly_json):
    print(json.dumps(ugly_json, sort_keys=True, 
                     indent=4, separators=(',', ': ')))

def main():
    w = wiki.Wiki()
    page = w.getPage('Wikipedia')
    print(page.getReferences().decode('ascii', 'ignore'))

if __name__ == "__main__":
    main()