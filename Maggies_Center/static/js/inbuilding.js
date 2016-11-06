/**
 * Created by sbeanie on 11/6/16.
 */


function visitor_in(mapping_id) {
    $.ajax({
        url: "/async/set-left/" + mapping_id,
        context: document.body,
        success: function () {
            $(this).addClass("done");
        }
    });
}