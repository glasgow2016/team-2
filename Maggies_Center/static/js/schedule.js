$(document).ready(function () {
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15 // Creates a dropdown of 15 years to control year
    });
    $('select').material_select();
    var row_count = 1;
    $("#add-row").click(function(){
        $original = $('#last-row').attr("id","who-cares");
        $clone = $original.clone(true,true).insertBefore($original);
        $clone.attr("id","last-row");
        row_count++;
    });
});

