var compliments = ['帅爆了', '你是世界上最帅的', '看看这美丽的面庞'];

function init() {
    //updateCompliment();
    // setInterval(function () {
    //     updateCompliment();
    // }, 1000 * 60 * 5) //5分钟更新一次数据
    var i = 0;
    setInterval(function () {
        currentCompliment = compliments[i];
        $('.compliment').updateWithText(currentCompliment, 4000);
        i++;
        if (i > 4) {
            i = 0
        }
    }, 1000 * 60)
}

function updateCompliment() {
    $.ajax({
        type: 'get',
        async: true,
        dataType: 'json',
        url: '/interactive/',
        success: function (res) {
            if (res.length !== 0) {
                compliments = res;
                console.log(compliments)
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
var _randomIndex = Math.floor(Math.random() * compliments.length);
currentCompliment = compliments[_randomIndex];
$('.compliment').updateWithText(currentCompliment, 3000);

init();
