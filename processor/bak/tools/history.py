import requests


def history():
    url = 'https://www.ipip5.com/today/api.php?type=json'
    try:
        history_list = []
        res = requests.get(url).json()
        result = res.get('result')[:-1]
        today = res.get('today')
        for item in result:
            year = item['year']
            title = item['title']
            content = '%s年%s,%s' % (year, today, title)
            history_list.append(content)
        return history_list
    except Exception as e:
        print('---', e)


if __name__ == '__main__':
    history()
