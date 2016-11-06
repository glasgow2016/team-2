$(document).ready(function() {
    $('select').material_select();
	$(".button-collapse").sideNav();
	Materialize.updateTextFields();
	$("#centre_select").change(function() {
	    window.location.href=window.location.href.split("?")[0] + "?centre=" + $(this).val();
	});
	$("#visitorIn").firstChild.firstChild.click(function(e) {
		this.html = "<a href=\"#\" id=\"visitorOut\"><i class=\"material-icons grey-text text-lighten-1\">home</i>"
	})
});