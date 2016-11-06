$(document).ready(function() {
    $('select').material_select();
	$(".button-collapse").sideNav();
	Materialize.updateTextFields();
	$("#centre_select").change(function() {
	    window.location.href=window.location.href.split("?")[0] + "?centre=" + $(this).val();
	});
	$(".card-house-button a").click(function(e) {
		visitor_in($(this).attr("data-uid"));
	});
});

function visitor_in(mapping_id) {
    $.ajax({
        url: "/async/set-left/" + mapping_id + "/",
        context: document.body,
        success: function () {
            $(this).addClass("done");
			// Use some more complicated DOM manipulation when time is nicer with us
			window.reload();
        }
    });
}