var last_tags = [];
var tag_mappings = {};
var form_id_complete;
var select_id_complete;
var tip_shown = false;

$(document).ready(function() {
    form_id_complete = "#" + form_id;
    select_id_complete = "#" + select_id;
    $(form_id_complete).keyup(function() {
        var centre_id = $(select_id_complete).val();
        if (centre_id != "") {
            $.ajax({
                url: "/async/get-suggestion/" + centre_id + "/" + $(form_id_complete).val(),
                success: function(data) {
                    last_tags = [];
                    tag_mappings = {};
                    $.each(data, function(index, item) {
                        last_tags.push(item["name"]);
                        tag_mappings[item["name"]] = item["id"];
                    });
                    $(form_id_complete).autocomplete({
                        source: last_tags,
                        response: function (event, ui) {
                            ui.content = $.map(ui.content, function(value, key) {
                                return {
                                    label: value,
                                    value: value
                                }
                            });
                        }
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