import frappe

def get_context(context):
    context.no_cache = 1
    context.flights = frappe.get_all("Airplane Flight", fields=["airplane","source_airport","source_airport_code","destination_airport_code","date_of_departure","time_of_departure","duration"])
    context.flights = frappe.get_all("Airplane Ticket", fields=["airplane","source_airport_code","destination_airport_code","date_of_departure","time_of_departure","duration"])
    return context
