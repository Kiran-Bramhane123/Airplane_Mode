# Copyright (c) 2024, Kiran Vijay Bramhane and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe import _
import random
import string
from frappe.utils.data import cint

class AirplaneTicket(Document):
    def validate(self):
        unique_add_ons = {}
        for add_on in self.add_ons:
            key = add_on.item
            if key not in unique_add_ons:
                unique_add_ons[key] = add_on

        # Update add-ons with unique entries to find unique
        self.set("add_ons", list(unique_add_ons.values()))

        # Calculate total after removing duplicates
        total = 0
        for row in self.add_ons:
            total += cint(row.amount)
        self.total_amount = total + self.flight_price

        # Check capacity before submission
        self.check_capacity()

        # Check status before submission
        if self.status != "Boarded":
            frappe.throw(_("Airplane Ticket cannot be submitted unless the status is 'Boarded'."))

    def check_capacity(self):
        if self.flight:
            # Fetch the count of existing tickets for the flight
            ticket_count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})

            flight = frappe.get_doc("Airplane Flight", self.flight)
            if flight:
                airplane = frappe.get_doc("Airplane", flight.airplane)
                if ticket_count >= airplane.capicity:
                    frappe.throw("Number of tickets exceeds airplane capacity. Cannot create Airplane Ticket.")
