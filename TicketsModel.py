import requests
from urllib.parse import urlparse, parse_qs


class TicketsClass:
    def __init__(self, domain, username, password, page_size='25'):
        self.domain = domain
        self.username = username
        self.password = password
        self.page_size = page_size

    def _get_response(self, url):
        try:
            response = requests.get(url, auth=(self.username, self.password))
            status_code = response.status_code
            if (status_code != 200):
                return [False, status_code]
            else:
                return [True, response.json()]
        except requests.exceptions.RequestException:
            return [False, 'RequestException']

    def get_page_size(self):
        return int(self.page_size)

    def get_ticket(self, ticket_id):
        ticket_url = "https://" + self.domain + ".zendesk.com/api/v2/tickets/" + ticket_id + ".json"
        return self._get_response(ticket_url)

    def get_ticket_number(self):
        count_url = "https://" + self.domain + ".zendesk.com/api/v2/tickets/count.json"
        r = self._get_response(count_url)
        if r[0]:
            return [r[0], r[1]['count']['value']]
        else:
            return r

    def get_ticket_of_page(self, page):
        tickets_page_url = "https://" + self.domain + ".zendesk.com/api/v2/tickets.json?page=" + str(page) + "&per_page=" + self.page_size
        r = self._get_response(tickets_page_url)
        if r[0]:
            return [r[0], r[1]['tickets']]
        else:
            return r