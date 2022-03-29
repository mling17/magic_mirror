updateWeather();
updateForecast();
updateHouseTempHum();
setInterval(function () {
    updateWeather();
    updateForecast();
    updateHouseTempHum();
}, 1000 * 60 * 5);

function updateWeather() {
    $.ajax({
        type: 'get',
        async: true,
        dataType: 'json',
        url: '/weather/',
        success: function (res) {
            if (res.length !== 0) {
                console.log(res)
                $('.city').text(res.city);
                $('.windpower').text(res.winddirection + res.windpower).addClass(res.winddirection_icon);
                $('.humidity-padding').text(res.humidity + "%");
                $('.temp .icon').removeClass(function (index, className) {
                    return (className.match(/(^|\s)wi-\S+/g) || []).join(' ');
                }).addClass(res.weather_icon);
                $('.temp .weather-text').text(res.weather);
                $('.temp .temperature').text(res.temperature);
                if (res.temperature) {
                    $('.temp sup').show();
                }
            }
        },
        error: function (err) {
            console.log(err)
        }
    })
}

function updateHouseTempHum() {
    $.ajax({
        type: 'get',
        async: true,
        dataType: 'json',
        url: '/temp_hum/',
        success: function (res) {
            if (res.status == 0) {
                console.log('asjlkdfjlaksdglkahs')
                $('.inside').addClass('hide')
                return
            } else {
                $('.inside').removeClass('hide')
                $('.house_temperature').text(res.temp + '℃');
                $('.house_humidity').text(res.hum + '%');
            }

        },
        error: function (err) {
            console.log(err)
        }
    })
}

function updateForecast() {
    $.ajax({
        type: 'get',
        async: true,
        dataType: 'json',
        url: '/forecast/',
        success: function (res) {
            console.log(res);
            console.log(res[0])
            $('.forecast-table').text('');
            for (var i = 0; i < res.length; i++) {
                $('.forecast-table').append(`<tr>
                    <td style="opacity:1" class="day">${res[i].week}</td>
                    <td style="opacity:1" style="width:60px">${res[i].weather_am}</td>
                    <td style="opacity:1" class="temp-max">${res[i].temperature_am}</td>
                    <td style="opacity:1" class="temp-min">${res[i].temperature_pm}</td>
                </tr>`)
            }
        },
        error: function (err) {
            console.log(err)
        }
    })
}

function removeClass(index, css) {
    return (css.match(/(^|\s)star\S+/g) || []).join(' ');//移除以“star”开头的类
}

