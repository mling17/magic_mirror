updateToDo();
setInterval(function () {
    updateToDo();
}, 1000 * 60)

function updateToDo() {
    $.ajax({
        type: 'get',
        async: true,
        dataType: 'json',
        url: '/todo/',
        success: function (res) {
            console.log(res);
            if (res.length == 0) {
                $('.table').text('');
                $('#module_3_calendar').addClass('hide');
            } else {
                $('#module_3_calendar').removeClass('hide');
                $('.todo-total').text('(' + res.length + ')');
                var opacity_value = 1;
                $('.table').text('')
                for (var i = 0; i < res.length; i++) {
                    $('.table').append(`<tr class="normal event" style="opacity: ${opacity_value}">
                        <td class="symbol align-right "><span class="fa fa-fw fa-calendar-check-o"></span></td>
                        <td class="title bright ">${res[i]}</td>
                    </tr>`)
                    opacity_value -= 0.2;
                }
            }
        },
        error: function (err) {
            console.log(err)
        }
    })
}
