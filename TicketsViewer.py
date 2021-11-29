
import os


class TicketsDisplayClass:
    def _clean(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_menu(self):
        self._clean()
        print("Type 'display' to view tickets by pages. \n" )
        print("Type 'search' to view a ticket by id. \n")
        print("Type 'exit' to exit. \n")

    def display_menu(self, current, total, pagesize):
        self._clean()
        self.display_header(current, total, pagesize)
        print("Type '-' to display the previous page.\n")
        print("Type '+' to dispaly the next page.\n" )
        print("Type 'exit' to exit.\n")

    def display_header(self, current, total, pagesize):
        print("---------- Page "+ str(current) + "/" + str(total) + "  " + str(pagesize) + "tickets pre page ----------\n")
    
    def _print_ticket(self, ticket_dict):
        print(str(ticket_dict['id']) +"\t" )
        print(ticket_dict['subject'] +"\t" )
        print(ticket_dict['status'] +"\t" )
        print(str(ticket_dict['assignee_id']) +"\t" )
        print(ticket_dict['subject'] +"\t" )
        print(str(ticket_dict['requester_id']) +"\t" )
        print(ticket_dict['created_at']+"\t" )
        print(ticket_dict['description'] +"\t\n" )

    def display_ticket_list(self,  current, total, pagesize,  paginated_ticket_list):
        self.display_menu(current, total, pagesize)
        print("ID \t Subject \t Status \t Assignee \t Subject \t Requester \t Date \t Description")
        for ticket in paginated_ticket_list:
            self._print_ticket(ticket)

    def invalid_command(self):
        print("[Error] Invalid command. \n")

    def error_message(self, error_code):
        print("[Error] Error Code: "+ str(error_code) +" \n")

    def search_menu(self):
        self._clean()
        print("Type a ticket id")

    def search_ticket(self, ticket):
        self.search_menu()       
        self._print_ticket(ticket['ticket'])
