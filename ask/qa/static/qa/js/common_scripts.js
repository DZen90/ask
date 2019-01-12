$(function() {
    // configure typeahead
    $("#q").typeahead({
        highlight: false,
        minLength: 1
    },
    {
        display: function(suggestion) { return null; },
        source: search,
        limit: 10,
        templates: {
            suggestion: Handlebars.compile(
                "<div>" + 
                "<a href='/question/{{ pk }}'>{{ fields.title }}</a>" +
                "</div>"
            )
        }
    })
});

function search(query, syncResults, asyncResults) {
    //var parameters = { 'q': query, 'csrfmiddlewaretoken': getCookie("csrftoken") };
    var parameters = { 'q': query, 'ajax': "true" };
    $.ajax({
        type: "GET",
        url: "/search/",
        data: parameters,
        dataType: "json",
        success: function(response) {
            //alert(response);
            asyncResults(response);
        },
        error: function(rs, e) {
            asyncResults([]);
        }    
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};
