//$('#myclock').thooClock();
var week = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
var clock = {};

updateTime();
lunar();

// setInterval(lunar, 60000);
// 每分钟更新一次农历
function updateTime() {
    var cd = new Date();
    clock.time = zeroPadding(cd.getHours(), 2) + ':' + zeroPadding(cd.getMinutes(), 2);
    clock.second = zeroPadding(cd.getSeconds(), 2);
    clock.date = zeroPadding(cd.getFullYear(), 4) + '-' + zeroPadding(cd.getMonth() + 1, 2) + '-' + zeroPadding(cd.getDate(), 2) + ' ' + week[cd.getDay()];
    setTimeout(updateTime, 1000);
    //console.log(clock)
    $('.date').text(clock.date)
    $('.datetime .time').html(clock.time + '<sup class="' + 'dimmed">' + clock.second + '</sup>')
    // console.log('---', $('.time').val())

    //$('#clock .dimmed').text(clock.second)
    if (clock.second == 0) {
        lunar();
    }
}

function zeroPadding(num, digit) {
    var zero = '';
    for (var i = 0; i < digit; i++) {
        zero += '0';
    }
    return (zero + num).slice(-digit);
}

function lunar() {
    $.ajax({
        type: 'get',
        async: true,
        dataType: 'json',
        url: 'http://192.168.1.147:8000/lunar/',
        success: function (res) {
            //console.log(res)
            $('.ganzhi').text(res.ganzhi + " " + res.shengxiao + '年')
            var yueri = res.lunarMonth + '月' + res.lunarDay
            $('.yueri').text(yueri)
            $('.jieri').text(res.remark)
        },
        error: function () {

        }
    })
}

