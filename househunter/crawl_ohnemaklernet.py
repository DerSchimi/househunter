import logging
import requests
import re
from bs4 import BeautifulSoup
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


class CrawlOhneMaklerNet:
    __log__ = logging.getLogger(__name__)
    URL_PATTERN = re.compile(r'https://www\.ohne-makler\.net')

    def __init__(self):
        logging.getLogger("requests").setLevel(logging.WARNING)

    def get_results(self, search_url):
        self.__log__.debug("Got search URL %s" % search_url)

        soup = self.get_page(search_url)

        # get data from first page
        entries = self.extract_data(soup)
        self.__log__.debug('Number of found entries: ' + str(len(entries)))

        return entries

    def get_page(self, search_url):
        headers = {
            "User-Agent": self.getRandomUserAgent()}
        resp = requests.get(search_url, headers=headers)  # TODO add page_no in url
        if resp.status_code != 200:
            self.__log__.error("Got response (%i): %s" % (resp.status_code, resp.content))
        return BeautifulSoup(resp.content, 'html.parser')

    def extract_data(self, soup):
        entries = []
        soup = soup.find("table",class_="table table-striped immoresults")
        try:
            title_elements = soup.find_all(lambda e: e.has_attr('class') and e.name == 'a' and 'red' in e['class'])
        except AttributeError:
            return entries
        expose_ids = soup.find_all("tr")


        # filter results
        for a in expose_ids:
            result = a.find('a', href=re.compile("^\\/immobilie\\/"))
            if result == None:
                expose_ids.remove(a);
        # remove first
        for a in expose_ids:
            expose_ids.remove(a);
            break;



        # print(expose_ids)
        for idx, title_el in enumerate(title_elements):
            price = expose_ids[idx].find("span",class_="red").text.replace("\n","").replace("\t","").strip()
            address = "https://www.ohne-makler.net/" + title_el.get("href")
           # tags = expose_ids[idx].find_all(class_="simpletag tag-small")

            try:
                # (tags[0].text)
                rooms =  expose_ids[idx].find("strong",text="Zimmer:").next_element.next_element
            except AttributeError:
                # print("Keine Zimmeranzahl gegeben")
                rooms = "Nicht gegeben"
            try:
                size =  expose_ids[idx].find("strong",text="Wohnfläche:").next_element.next_element
            except AttributeError:
                size = "Nicht gegeben"

            try:
                wsize = expose_ids[idx].find("strong", text="Grundstücksfläche:").next_element.next_element.strip()
            except AttributeError:
                wsize = "Nicht gegeben"

            details = {
                'id': int(expose_ids[idx].find("strong", text="Objekt-Nr.:").next_element.next_element[4:].strip()),
                'url': address,
                'title': title_el.text.strip(),
                'price': price,
                'wsize': size,
                'hsize': wsize,
                'rooms': rooms,
                'address': address
            }
            entries.append(details)

        self.__log__.debug('extracted: ' + str(entries))

        return entries

    def load_address(self, url):
        # extract address from expose itself
        exposeHTML = requests.get(url).content
        exposeSoup = BeautifulSoup(exposeHTML, 'html.parser')
        try:
            street_raw = exposeSoup.find(id="street-address").text
        except AttributeError:
            street_raw = ""
        try:
            address_raw = exposeSoup.find(id="viewad-locality").text
        except AttributeError:
            address_raw = ""
        address = address_raw.strip().replace("\n", "") + " " + street_raw.strip()

        return address

    def getRandomUserAgent(self):
        software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.EDGE.value,
                          SoftwareName.INTERNET_EXPLORER.value, SoftwareName.ANDROID.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        user_agents = user_agent_rotator.get_user_agents()
        user_agent = user_agent_rotator.get_random_user_agent()
        self.__log__.debug('using user agent: ' + str(user_agent))

        return user_agent
