from wiki import Wiki
import json

def printJSON(ugly_json):
    print(json.dumps(ugly_json, sort_keys=True, 
                     indent=4, separators=(',', ': ')))

def writeToFile(filename, content):
    with open(filename, encoding='utf-8', mode='w+') as f:
        f.write(content)

def main():
    writeToFile('temp.html', Wiki().getPage('Monty Python').getHTMLContent())

if __name__ == '__main__':
    main()