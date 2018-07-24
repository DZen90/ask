$(function() {
    checkFields();
})

$('#id_username').on("input", checkFields);

function checkFields() {
    $('.fields-valid').attr('disabled', $.trim(this.value).length === 0);
}

