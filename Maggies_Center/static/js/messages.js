$(document).ready(function() {
    $.each(messages, function(index, val) {
        Materialize.toast(val, 6000);
    });
});