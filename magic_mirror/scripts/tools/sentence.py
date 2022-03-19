import requests


def onePhrase():
    url = 'https://v1.hitokoto.cn/?encode=json&charset=utf-8'
    try:
        res = requests.get(url).json()
    except:
        return None
    hitokoto = res['hitokoto']
    source = res['from']
    content = "{}\n--《{}》".format(hitokoto, source)
    return content


if __name__ == '__main__':
    juzi = onePhrase()
    print(juzi)
