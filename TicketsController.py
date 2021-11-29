from TicketsModel import TicketsClass
from TicketsViewer import TicketsDisplayClass
from dotenv import load_dotenv
import os
import sys
import math


class Controller:

    def __init__(self, domain, username, password):
        self.model = TicketsClass(domain, username, password)
        self.view = TicketsDisplayClass()
        self.current_input = ""
        self.current_page = 1
        response = self.model.get_ticket_number()
        if response[0]:
            self.ticket_number = response[1]
        else:
            self.view.error_message(response[1])
            sys.exit()
        self.pagesize = self.model.get_page_size()

    def _set_input(self):
        self.current_input = input()

    def _main_listener(self):
        while (True):
            self._set_input()
            if (self.current_input == "display"):
                self.display_page()
            elif (self.current_input == "search"):
                self.search()
            elif (self.current_input == "exit"):
                sys.exit()
            else:
                self.view.invalid_command()
                self.view.start_menu()

    def _check_response_error(self, response):
        if response[0]:
            return response[1]
        else:
            self.view.error_message(response[1])
            sys.exit()       
        
    def _display_page_listener(self, display_current, page_number):
        while (True):
            self._set_input()
            if (self.current_input == "+"):
                if (self.current_page + 1 <= page_number):
                    self.current_page += 1
                    display_current()
                else:
                    continue
            elif (self.current_input == "-"):
                if (self.current_page - 1 >= 1):
                    self.current_page -= 1
                    display_current()
                else:
                    continue
            elif (self.current_input == "exit"):
                sys.exit()
            else:
                self.view.invalid_command()
                display_current()

    def _search_listener(self):
        while (True):
            self._set_input()
            if self.current_input.isdigit():
                ticket = self._check_response_error(self.model.get_ticket(self.current_input))
                self.view.search_ticket(ticket)
            elif (self.current_input == "exit"):
                sys.exit()
            else:
                self.view.invalid_command()
                self.view.search_menu()

    def main(self):
        self.view.start_menu()
        self._main_listener()

    def display_page(self):
        page_number = math.ceil(self.ticket_number/self.pagesize)
        def display_current():
            ticket_list = self._check_response_error(self.model.get_ticket_of_page(self.current_page))
            self.view.display_ticket_list(self.current_page, page_number, self.pagesize, ticket_list)
        display_current()
        self._display_page_listener(display_current, page_number)

    def search(self):
        self.view.search_menu()
        self._search_listener()


if __name__ == "__main__":
    load_dotenv()
    os.system('cls' if os.name == 'nt' else 'clear')
    c = Controller(os.getenv("DOMAIN"), os.getenv("MAILBOX"), os.getenv("PASSWORD"))
    c.main()