# Copyright (c) 2024, Kiran Vijay Bramhane and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document
from frappe import _

class AirplaneTicket(Document):
    def validate(self):
        self.calculate_total_amount()

    def calculate_total_amount(self):
        total = 0
        for row in self.add_ons:
            total += row.amount
        frappe.msgprint(f"Total amount calculated: {total}")

        # Assuming you have a field named 'total_amount' in your DocType
        self.total_amount = total + self.flight_price

    def before_submit(self):
        print(self.status)
        if self.status != "Boarded":
            frappe.throw(_("Airplane ticket cannot be submitted unless the status is 'Boarded'."))

    class AirplaneTicket(Document):
        def before_insert(self):
            # Generate random seat number
            seat_number = str(random.randint(10, 99)) + random.choice(['A', 'B', 'C', 'D', 'E'])
            self.seat = seat_number

    class AirplaneFlight(Document):
        def on_submit(self):
            # Set status to Completed after document submission
            self.status = "Completed"
