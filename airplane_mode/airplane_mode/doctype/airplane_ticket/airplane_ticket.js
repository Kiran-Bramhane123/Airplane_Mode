// Copyright (c) 2024, Pragati Dhawale and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        
    },
    // validate: function(frm) {
    //     // Remove duplicate entries from add-ons
    //     let uniqueAddOns = {};
    //     frm.doc.add_ons.forEach(function(add_on) {
    //         let key = add_on.item;
    //         if (!uniqueAddOns[key]) {
    //             uniqueAddOns[key] = add_on;
    //         }
    //     });
    //     // Update add-ons with unique entries
    //     frm.set_value("add_ons", Object.values(uniqueAddOns));
    // }
});

frappe.ui.form.on("Airplane Ticket Add-on Item", {
    amount(frm, cdt, cdn) {
        let total = 0;
        console.log(total);
        frm.doc.add_ons.forEach(function(d) {
            total += parseFloat(d.amount) || 0;
        });
        console.log(total);
        total += frm.doc.flight_price || 0;
        console.log(total);
        frm.set_value("total_amount", total);
    }
});
