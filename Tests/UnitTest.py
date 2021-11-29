from TicketsModel import TicketsClass
from TicketsViewer import TicketsDisplayClass
from dotenv import load_dotenv
import unittest
import os


class TestView(unittest.TestCase):
    def test_viewer(self):
        TDC = TicketsDisplayClass()
        self.assertEqual(TDC.start_menu(),0)
        self.assertEqual(TDC.display_menu(), 0)
        self.assertEqual(TDC.invalid_command(), 0)
        self.assertEqual(TDC.error_message(401), 0)


class TestModel(unittest.TestCase):
    def test_get_ticket_number(self):
        load_dotenv()
        TC = TicketsClass(os.getenv("DOMAIN"), os.getenv("MAILBOX"), os.getenv("PASSWORD"))        
        ticket_number = TC.get_ticket_number()
        self.assertEqual(ticket_number, 100)

    def test_get_ticket(self):
        load_dotenv()
        TC = TicketsClass(os.getenv("DOMAIN"), os.getenv("MAILBOX"), os.getenv("PASSWORD"))        
        ticket = TC.get_ticket(250)
        self.assertEqual(len(ticket), 1)
        self.assertEqual(ticket['ticket']['id'], 250)

    def test_get_all_tickets(self):
        load_dotenv()
        TC = TicketsClass(os.getenv("DOMAIN"), os.getenv("MAILBOX"), os.getenv("PASSWORD"))        
        page_tickets = TC.get_ticket_of_page(1)
        self.assertEqual(len(page_tickets), 25)


if __name__ == '__main__':
    unittest.main()
