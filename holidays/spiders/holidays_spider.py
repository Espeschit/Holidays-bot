import scrapy
import unidecode

class QuotesSpider(scrapy.Spider):
    name = 'holidays'

    def start_requests(self):
        allowed_domains = ['feriados.com.br']
        domain = 'https://www.feriados.com.br/feriados-estado-'
        states = ['ac.php', 'al.php', 'ap.php', 'am.php', 'ba.php',
            'ce.php', 'df.php', 'es.php', 'go.php', 'ma.php',
            'mt.php', 'ms.php', 'mg.php', 'pa.php', 'pb.php',
            'pr.php', 'pe.php', 'pi.php', 'rj.php', 'rn.php',
            'rs.php', 'ro.php', 'rr.php', 'sc.php', 'sp.php',
            'se.php', 'to.php']
        for i in states:
            yield scrapy.Request(url=domain+i, callback=self.parseCities, meta={'state': i}) 

    def parseCities(self, response):
        stateName = response.meta['state']
        cityName = []
        domain = 'https://www.feriados.com.br/feriados-'

        # Get city names
        for selector in response.css("span.style_estados"):
            cityName.append(selector.css("::text").extract())

        # Remove states from list
        del cityName[:27]

        # Replace spaces
        cityName = [[item.replace(" ", "_").lower() for item in sublist] for sublist in  cityName]
       
       # Remove accents
        cityName = [[unidecode.unidecode(item) for item in sublist] for sublist in cityName]

        for i in cityName:
            yield scrapy.Request(url=domain+i[0]+'-'+stateName, callback=self.parseHolidays, meta={'name': i[0], 'stateName': stateName[:2]})

    def parseHolidays(self, response):
        cityName = response.meta['name']
        stateName = response.meta['stateName']
        feriado = []
        facult = []

        # Get holidays
        for selector in response.css("span.style_lista_feriados"):
            feriado.append(selector.css("::text").extract())
        
        # Get optional holiday (facultativo)
        for selector in response.css("span.style_lista_facultativos"):
            facult.append(selector.css("::text").extract())
        
        # Join holiday date and name in the same string
        feriado = [''.join(item) for item in feriado]
        facult = [''.join(item) for item in facult]
    
        cities = {
                'city': {
                    'uf': stateName,
                    'cityName': cityName,
                    'holidays': {
                        'facult': facult,
                        'feriado': feriado
                        }
                    }
        }

        yield(cities)
