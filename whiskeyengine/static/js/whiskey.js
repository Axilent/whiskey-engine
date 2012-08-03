/* ===================== */
/* = Whiskey Engine JS = */
/* ===================== */

function review(whiskey_id) {
    $('#review_dialog').load('/review/'+whiskey_id+'/').dialog({width:530,height:450,title:'Add Your Review'});
}

function cancel_review() {
    $('#review_dialog').dialog('close');
}