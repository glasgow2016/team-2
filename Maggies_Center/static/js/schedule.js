$(document).ready(function () {
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15 // Creates a dropdown of 15 years to control year
    });

    var row_count = 1;
    $("#add-row").click(function(){
        var $button = $("#add-row");
        var $original = $("#last-row").attr("id", "whocares");
        var $clone = $original.clone(true);
        $clone.attr("id","last-row");
        $clone.insertBefore($original);
        $button.remove();
        row_count++;
    });
});

function createRow() {

    
}
