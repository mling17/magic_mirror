var pi_info = [];

function init() {
    getPiInfo();
    setInterval(function () {
        getPiInfo();
    }, 1000 * 60 * 50) //5min更新一次数据
    var i = 0;
    setInterval(function () {
        currentPiInfo = pi_info[i];
        $('.pi_info').updateWithText(currentPiInfo, 1000);
        i++;
        if (i > 4) {
            i = 0
        }
    }, 1000 * 10)
}

function getPiInfo() {
    $.ajax({
        type: 'get',
        async: true,
        dataType: 'json',
        url: '/pi_info/',
        success: function (res) {
            if (res.length !== 0) {
                var ip = res['ip']
                var cpu_used = res['cpu_used']
                var cpu_temp = res['cpu_temp']
                var ram_state = JSON.parse(res['ram_state'])
                var ram_total = ram_state['ram_total']
                var ram_used = ram_state['ram_used']
                var ram_free = ram_state['ram_free']
                var disk_state = JSON.parse(res['disk_state'])
                var disk_total = disk_state['disk_total']
                var disk_used = disk_state['disk_used']
                var disk_percent = disk_state['disk_percent']
                pi_info = []
                pi_info.push('ip:' + ip)
                pi_info.push('cpu温度:' + cpu_temp + '℃' +'cpu使用率:' + cpu_used +"%")
                pi_info.push('内存信息:' + ram_used + '/' + ram_total + '\t剩余:' + ram_free+"MB")
                pi_info.push('存储信息:' + disk_used + '/' + disk_total + '\t使用率:' + disk_percent)
            }
        },
        error: function (err) {
            console.log(err)
        }
    })
}


jQuery.fn.updateWithText = function (text, speed) {
    var dummy = $('<div/>').html(text);
    if ($(this).html() != dummy.html()) {
        $(this).fadeOut(speed / 2, function () {
            $(this).html(text);
            $(this).fadeIn(speed / 2, function () {
                //done
            });
        });
    }
};

setTimeout(function () {
    $('.pi_info').updateWithText(pi_info[0], 1000);
    init()
}, 1000)
init()