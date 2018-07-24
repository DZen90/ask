$(function() {
    confirmPassword();
})

$('#like').click(function() {
    $.ajax({
        type: "POST",
        url: "/like/",
        data: {'question_id': $(this).attr('question_id'), 'csrfmiddlewaretoken': getCookie("csrftoken")},
        dataType: "json",
        success: function(response) {
            //alert(response.message);
            $('#like').toggleClass("fa-thumbs-down fa-thumbs-up");
            $('#like').text(response.likes_count);
        },
        error: function(rs, e) {
            alert(rs.responseText);
        }    
    });
});

$(':password').on("input", confirmPassword);

function confirmPassword() {
    var confirmPassword = $('#id_confirm_password').val();
    var password = $('#id_password').val();
    $('.password-confirm').attr('disabled', confirmPassword != password);
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
