var form_id_complete;
var select_id_complete;
var tip_shown = false;

$(document).ready(function() {
    $("#suggestions").hide();
    form_id_complete = "#" + form_id;
    select_id_complete = "#" + select_id;
    $(form_id_complete).keyup(function() {
        var centre_id = $(select_id_complete).val();
        if (centre_id != "") {
            $.ajax({
                url: "/async/get-suggestion/" + centre_id + "/" + $(form_id_complete).val(),
                success: function(data) {
                    $("#suggestions_in").html("");
                    if (data.length == 0) {
                        $("#suggestions").hide();
                    } else {
                        $("#suggestions").show();
                    }
                    $.each(data, function(index, item) {
                        // In the future, replace with proper jQuery node instantiation, instead
                        // of html strings. Time doesn't allow otherwise
                        $("#suggestions_in").append("<div class='card horizontal'>" +
		                    "<div class='card-image'>" +
		                        "<img src='http://lorempixel.com/100/190/nature/6'>" +
		                    "</div>" +
		                    "<div class='card-stacked'>" +
		                        "<div class='card-content'>" +
			                        "<h5>" + item['name'] + "</h5>" +
		                            item["gender"] + "<br/>" + item["cancer_type"] +
		                        "</div>" +
		                        "<div class='card-action'>" +
			                        "<a href='/add-visitor/?id=" + item["id"] +
			                        "'>View visitor</a>" +
		                        "</div>" +
                            "</div>" +
	                        "</div>");
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