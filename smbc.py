import wiki
import datetime

# implementation of http://www.smbc-comics.com/index.php?db=comics&id=2922
class ConceptionConnection:
    def __init__(self, birthday=[1982, 9, 5], delta=5):
        self.birthday = birthday
        self.conception_dates = self.findConceptionRange(delta)

    def findConceptionDate(self):
        [y, m, d] = self.birthday
        conception_date = datetime.date(y, m, d) - datetime.timedelta(days=266)
        return tuple(conception_date.strftime('%Y-%B-%d').split('-'))

    def findConceptionRange(self, delta):
        [y, m, d] = self.birthday
        conception_dates = []
        for diff in range(-1 * delta, delta + 1):
            conception_date = datetime.date(y, m, d) - datetime.timedelta(days=(266 - diff))
            conception_dates.append(tuple(conception_date.strftime('%Y %B %d').split(' ')))
        return conception_dates

    def getWikipediaEvents(self, year):
        page = wiki.Wiki().getPage(year).getHTMLContent()
        events = page[page.index('<span class="mw-headline" id="Events">Events</span>')
                     :page.index('<span class="mw-headline" id="Births">Births</span>')]
        return events

    def extractDateEvents(self, events, month, day):
        cs1 = '<li><a href="http://en.wikipedia.org/wiki/'
        cs1 += month + '_' + day
        cs1 += '" title="' + month + ' ' + day + '">' + month + ' ' + day + '</a>'
        if cs1 in events:
            evd = events[events.index(cs1) + len(cs1):].strip()
            if '<ul>' in evd[:len('<ul>')]:
                evd = evd[evd.index('<ul>'):evd.index('</ul>')] + '</ul>'
            else:
                evd = '<ul><li>' + evd[:evd.index('</li>')] + '</li></ul>'
            return evd.replace('<li>– ', '<li>').replace('<li>–', '<li>')
        else:
            return ''

    def extractEvents(self):
        curr_year = self.conception_dates[0][0]
        year_events = self.getWikipediaEvents(curr_year)
        events = ''
        for y, m, d in self.conception_dates:
            if y > curr_year:
                curr_year = y
                year_events = self.getWikipediaEvents(curr_year)
            date_events = self.extractDateEvents(year_events, m, d)
            if date_events:
                events += '<h2>' + m + ' ' + d + '</h2>\n' + date_events + '\n'
        return events

def main():
    with open('events.html', encoding='utf-8', mode='w+') as f:
        f.write(ConceptionConnection().extractEvents())

if __name__ == "__main__":
    main()