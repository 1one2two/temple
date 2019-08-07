function send() {
    $("#bb")[0].innerHTML = "Hello";
}

$(function () {
    $('button').click(function () {
        $('#sel')[0].selectedIndex = 1
        alert('Success!!!');
    })

    $('#sel').change(function () {
        alert($('#sel').selectedIndex())
    })

    $("#test1").change(function () {
        /*
        * $(this).val() : #test1 的 value 值
        * $('#test1 :selected').text() : #test1 的 text 值     
        */
        $("#test2").append($(`<option value="0">` + $('#test1 :selected').text() + `</option>`));
    });
})
