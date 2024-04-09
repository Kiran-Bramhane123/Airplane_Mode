// Copyright (c) 2024, Pragati Dhawale and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {   
    }
});

frappe.ui.form.on("Airplane Ticket Add-on Item",{
    amount(frm,cdt,cdn){
        let total=0;
        frm.doc.add_ons.forEach(function(d){
            total=total+=d.amount;
        });
        total+=frm.doc.flight_price || 0;
        frm.set_value("total_amount",total);
    }
});