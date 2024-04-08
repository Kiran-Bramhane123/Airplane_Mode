# Copyright (c) 2024, Kiran Vijay Bramhane and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class AirplaneTicket(Document):
    def before_submit(self):
        # Check if the status is "Boarded"
        if self.status != "Boarded":
            frappe.throw("Cannot submit the ticket. Status must be 'Boarded'.")

        # Set the status to "Completed"
        self.status = "Completed"

class AirplaneTicket(Document):
    def before_insert(self):
        # Generate a random integer (between 1 and 99)
        random_integer = random.randint(1, 99)

        # Generate a random capital letter (A to E)
        random_letter = random.choice(string.ascii_uppercase[:5])

        # Combine the integer and letter to form the seat string
        seat = f"{random_integer}{random_letter}"
        self.seat = seat
