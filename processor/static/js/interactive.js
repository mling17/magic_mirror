var compliments = ['看看这美丽的面庞',];

function init() {
    updateCompliment();
    setInterval(function () {
        updateCompliment();
    }, 1000 * 60 * 1) //5分钟更新一次数据
    var i = 0;
    setInterval(function () {
        currentCompliment = compliments[i];
        fun(currentCompliment);
        $('.compliment').updateWithText(currentCompliment, 3000);
        fun(currentCompliment);
        // $('.hd-text').updateWithText(currentCompliment, 1000);
        i++;
        if (i > compliments.length) {
            i = 0
        }
    }, 1000 * 15)
}

function updateCompliment() {
    $.ajax({
        type: 'get',
        async: true,
        dataType: 'json',
        url: '/interactive/',
        success: function (res) {
            if (res.length !== 0) {
                compliments = res.data;
                console.log(compliments);
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

function fun(string) {//动态调整font-size
    let box = document.getElementById('box')

    function getFontSize(str, targetSize = 50) {
        let boxWith = box.offsetWidth;
        let fontSize = targetSize;
        let theCanvas = null;
        let practicalWidth = getWidth(str, fontSize)

        function getWidth(text, size) { // 使用canvas计算字符串展示所需宽度
            let font = `normal ${size}px Microsoft YaHei`
            const canvas = theCanvas || (theCanvas = document.createElement('canvas'));
            const context = canvas.getContext('2d');
            context.font = font;
            return Math.floor(context.measureText(text).width)
        }

        while ((10 <= fontSize) && (practicalWidth > boxWith)) { // 所需宽度小于实际宽度，或者计算字体大于最小字体10
            fontSize -= 2
            practicalWidth = getWidth(str, fontSize); // 重新计算目标字符串所需宽度
            boxWith = box.offsetWidth - getWidth('...', fontSize); // 文本溢出剔除...所占距离
            if (practicalWidth < boxWith) {
                break
            }
        }
        return fontSize; // 输出fontSize
    }

    var str = $('.compliment').text()
    var size = getFontSize(str).toString()
    box.style.fontSize = size + 'px'
}

init();
