// Copyright (c) 2024, Pragati Dhawale and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh(frm) {
        frm.add_custom_button(('Assign Seat'), ()=> {
            frappe.prompt([
                {
                    label:('Seat Number'),
                    fieldname: 'seat_number',
                    fieldtype: 'Data',
                    reqd: true
                }
            ], (values)=> {
                frm.set_value('seat', values.seat_number);
            });
        }, ('Action'));
    }
});

