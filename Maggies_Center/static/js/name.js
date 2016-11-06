var last_tags = [];
var form_id_complete = "#" + form_id;
var select_id_complete = "#" + select_id;
var tip_shown = false;

$(document).ready(function() {
    $(form_id_complete).change(function() {
        var centre_id = $(select_id_complete).val();
        if (centre_id != "") {
            last_tags = $.ajax({
                url: "/async/suggest/" + centre_id + "/" + $(form_id_complete).val();
                success: function(data) {
                    $(form_id_complete).autocomplete({
                        source: last_tags
                    });
                }
            });
        } else {
            if (!tip_shown) {
                tip_shown = true;
                Materialize.toast("Please select a centre first to get suggestions as you type in the name", 6000);
            }
        }
    });
});