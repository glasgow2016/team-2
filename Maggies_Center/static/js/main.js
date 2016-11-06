$(document).ready(function() {
    $('select').material_select();
	$(".button-collapse").sideNav();
	Materialize.updateTextFields();
	$("#centre_select").change(function() {
	    window.location.href=window.location.href.split("?")[0] + "?centre=" + $(this).val();
	});
	$("visitorIn").click
});