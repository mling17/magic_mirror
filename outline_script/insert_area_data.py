"""
导入省市县的id
"""
import pymysql

db = pymysql.connect(host='localhost', user='chen', password='mling17!163.com', database='magic_mirror')

# 使用cursor()方法获取操作游标
cursor = db.cursor()
area = [
    {
        "province": "北京",
        "cityList": [
            {
                "city": "北京",
                "disList": [
                    {
                        "district": "北京",
                        "stationid": "101010100"
                    },
                    {
                        "district": "海淀",
                        "stationid": "101010200"
                    },
                    {
                        "district": "朝阳",
                        "stationid": "101010300"
                    },
                    {
                        "district": "顺义",
                        "stationid": "101010400"
                    },
                    {
                        "district": "怀柔",
                        "stationid": "101010500"
                    },
                    {
                        "district": "通州",
                        "stationid": "101010600"
                    },
                    {
                        "district": "昌平",
                        "stationid": "101010700"
                    },
                    {
                        "district": "延庆",
                        "stationid": "101010800"
                    },
                    {
                        "district": "丰台",
                        "stationid": "101010900"
                    },
                    {
                        "district": "石景山",
                        "stationid": "101011000"
                    },
                    {
                        "district": "大兴",
                        "stationid": "101011100"
                    },
                    {
                        "district": "房山",
                        "stationid": "101011200"
                    },
                    {
                        "district": "密云",
                        "stationid": "101011300"
                    },
                    {
                        "district": "门头沟",
                        "stationid": "101011400"
                    },
                    {
                        "district": "平谷",
                        "stationid": "101011500"
                    },
                    {
                        "district": "东城",
                        "stationid": "101011600"
                    },
                    {
                        "district": "西城",
                        "stationid": "101011700"
                    }
                ]
            }
        ]
    },
    {
        "province": "上海",
        "cityList": [
            {
                "city": "上海",
                "disList": [
                    {
                        "district": "上海",
                        "stationid": "101020100"
                    },
                    {
                        "district": "闵行",
                        "stationid": "101020200"
                    },
                    {
                        "district": "宝山",
                        "stationid": "101020300"
                    },
                    {
                        "district": "黄浦",
                        "stationid": "101020400"
                    },
                    {
                        "district": "嘉定",
                        "stationid": "101020500"
                    },
                    {
                        "district": "浦东新区",
                        "stationid": "101020600"
                    },
                    {
                        "district": "金山",
                        "stationid": "101020700"
                    },
                    {
                        "district": "青浦",
                        "stationid": "101020800"
                    },
                    {
                        "district": "松江",
                        "stationid": "101020900"
                    },
                    {
                        "district": "奉贤",
                        "stationid": "101021000"
                    },
                    {
                        "district": "崇明",
                        "stationid": "101021100"
                    },
                    {
                        "district": "徐汇",
                        "stationid": "101021200"
                    },
                    {
                        "district": "长宁",
                        "stationid": "101021300"
                    },
                    {
                        "district": "静安",
                        "stationid": "101021400"
                    },
                    {
                        "district": "普陀",
                        "stationid": "101021500"
                    },
                    {
                        "district": "虹口",
                        "stationid": "101021600"
                    },
                    {
                        "district": "杨浦",
                        "stationid": "101021700"
                    }
                ]
            }
        ]
    },
    {
        "province": "天津",
        "cityList": [
            {
                "city": "天津",
                "disList": [
                    {
                        "district": "天津",
                        "stationid": "101030100"
                    },
                    {
                        "district": "武清",
                        "stationid": "101030200"
                    },
                    {
                        "district": "宝坻",
                        "stationid": "101030300"
                    },
                    {
                        "district": "东丽",
                        "stationid": "101030400"
                    },
                    {
                        "district": "西青",
                        "stationid": "101030500"
                    },
                    {
                        "district": "北辰",
                        "stationid": "101030600"
                    },
                    {
                        "district": "宁河",
                        "stationid": "101030700"
                    },
                    {
                        "district": "和平",
                        "stationid": "101030800"
                    },
                    {
                        "district": "静海",
                        "stationid": "101030900"
                    },
                    {
                        "district": "津南",
                        "stationid": "101031000"
                    },
                    {
                        "district": "滨海新区",
                        "stationid": "101031100"
                    },
                    {
                        "district": "河东",
                        "stationid": "101031200"
                    },
                    {
                        "district": "河西",
                        "stationid": "101031300"
                    },
                    {
                        "district": "蓟州",
                        "stationid": "101031400"
                    },
                    {
                        "district": "南开",
                        "stationid": "101031500"
                    },
                    {
                        "district": "河北",
                        "stationid": "101031600"
                    },
                    {
                        "district": "红桥",
                        "stationid": "101031700"
                    }
                ]
            }
        ]
    },
    {
        "province": "重庆",
        "cityList": [
            {
                "city": "重庆",
                "disList": [
                    {
                        "district": "重庆",
                        "stationid": "101040100"
                    },
                    {
                        "district": "永川",
                        "stationid": "101040200"
                    },
                    {
                        "district": "合川",
                        "stationid": "101040300"
                    },
                    {
                        "district": "南川",
                        "stationid": "101040400"
                    },
                    {
                        "district": "江津",
                        "stationid": "101040500"
                    },
                    {
                        "district": "渝北",
                        "stationid": "101040700"
                    },
                    {
                        "district": "北碚",
                        "stationid": "101040800"
                    },
                    {
                        "district": "巴南",
                        "stationid": "101040900"
                    },
                    {
                        "district": "长寿",
                        "stationid": "101041000"
                    },
                    {
                        "district": "黔江",
                        "stationid": "101041100"
                    },
                    {
                        "district": "渝中",
                        "stationid": "101041200"
                    },
                    {
                        "district": "万州",
                        "stationid": "101041300"
                    },
                    {
                        "district": "涪陵",
                        "stationid": "101041400"
                    },
                    {
                        "district": "城口",
                        "stationid": "101041600"
                    },
                    {
                        "district": "云阳",
                        "stationid": "101041700"
                    },
                    {
                        "district": "巫溪",
                        "stationid": "101041800"
                    },
                    {
                        "district": "奉节",
                        "stationid": "101041900"
                    },
                    {
                        "district": "巫山",
                        "stationid": "101042000"
                    },
                    {
                        "district": "潼南",
                        "stationid": "101042100"
                    },
                    {
                        "district": "垫江",
                        "stationid": "101042200"
                    },
                    {
                        "district": "梁平",
                        "stationid": "101042300"
                    },
                    {
                        "district": "忠县",
                        "stationid": "101042400"
                    },
                    {
                        "district": "石柱",
                        "stationid": "101042500"
                    },
                    {
                        "district": "大足",
                        "stationid": "101042600"
                    },
                    {
                        "district": "荣昌",
                        "stationid": "101042700"
                    },
                    {
                        "district": "铜梁",
                        "stationid": "101042800"
                    },
                    {
                        "district": "璧山",
                        "stationid": "101042900"
                    },
                    {
                        "district": "丰都",
                        "stationid": "101043000"
                    },
                    {
                        "district": "武隆",
                        "stationid": "101043100"
                    },
                    {
                        "district": "彭水",
                        "stationid": "101043200"
                    },
                    {
                        "district": "綦江",
                        "stationid": "101043300"
                    },
                    {
                        "district": "酉阳",
                        "stationid": "101043400"
                    },
                    {
                        "district": "大渡口",
                        "stationid": "101043500"
                    },
                    {
                        "district": "秀山",
                        "stationid": "101043600"
                    },
                    {
                        "district": "江北",
                        "stationid": "101043700"
                    },
                    {
                        "district": "沙坪坝",
                        "stationid": "101043800"
                    },
                    {
                        "district": "九龙坡",
                        "stationid": "101043900"
                    },
                    {
                        "district": "南岸",
                        "stationid": "101044000"
                    },
                    {
                        "district": "开州",
                        "stationid": "101044100"
                    }
                ]
            }
        ]
    },
    {
        "province": "黑龙江",
        "cityList": [
            {
                "city": "哈尔滨",
                "disList": [
                    {
                        "district": "哈尔滨",
                        "stationid": "101050101"
                    },
                    {
                        "district": "双城",
                        "stationid": "101050102"
                    },
                    {
                        "district": "呼兰",
                        "stationid": "101050103"
                    },
                    {
                        "district": "阿城",
                        "stationid": "101050104"
                    },
                    {
                        "district": "宾县",
                        "stationid": "101050105"
                    },
                    {
                        "district": "依兰",
                        "stationid": "101050106"
                    },
                    {
                        "district": "巴彦",
                        "stationid": "101050107"
                    },
                    {
                        "district": "通河",
                        "stationid": "101050108"
                    },
                    {
                        "district": "方正",
                        "stationid": "101050109"
                    },
                    {
                        "district": "延寿",
                        "stationid": "101050110"
                    },
                    {
                        "district": "尚志",
                        "stationid": "101050111"
                    },
                    {
                        "district": "五常",
                        "stationid": "101050112"
                    },
                    {
                        "district": "木兰",
                        "stationid": "101050113"
                    },
                    {
                        "district": "道里",
                        "stationid": "101050114"
                    },
                    {
                        "district": "南岗",
                        "stationid": "101050115"
                    },
                    {
                        "district": "道外",
                        "stationid": "101050116"
                    },
                    {
                        "district": "平房",
                        "stationid": "101050117"
                    },
                    {
                        "district": "松北",
                        "stationid": "101050118"
                    },
                    {
                        "district": "香坊",
                        "stationid": "101050119"
                    }
                ]
            },
            {
                "city": "齐齐哈尔",
                "disList": [
                    {
                        "district": "齐齐哈尔",
                        "stationid": "101050201"
                    },
                    {
                        "district": "讷河",
                        "stationid": "101050202"
                    },
                    {
                        "district": "龙江",
                        "stationid": "101050203"
                    },
                    {
                        "district": "甘南",
                        "stationid": "101050204"
                    },
                    {
                        "district": "富裕",
                        "stationid": "101050205"
                    },
                    {
                        "district": "依安",
                        "stationid": "101050206"
                    },
                    {
                        "district": "拜泉",
                        "stationid": "101050207"
                    },
                    {
                        "district": "克山",
                        "stationid": "101050208"
                    },
                    {
                        "district": "克东",
                        "stationid": "101050209"
                    },
                    {
                        "district": "泰来",
                        "stationid": "101050210"
                    },
                    {
                        "district": "龙沙",
                        "stationid": "101050211"
                    },
                    {
                        "district": "建华",
                        "stationid": "101050212"
                    },
                    {
                        "district": "铁锋",
                        "stationid": "101050213"
                    },
                    {
                        "district": "昂昂溪",
                        "stationid": "101050214"
                    },
                    {
                        "district": "富拉尔基",
                        "stationid": "101050215"
                    },
                    {
                        "district": "碾子山",
                        "stationid": "101050216"
                    },
                    {
                        "district": "梅里斯",
                        "stationid": "101050217"
                    }
                ]
            },
            {
                "city": "牡丹江",
                "disList": [
                    {
                        "district": "牡丹江",
                        "stationid": "101050301"
                    },
                    {
                        "district": "海林",
                        "stationid": "101050302"
                    },
                    {
                        "district": "穆棱",
                        "stationid": "101050303"
                    },
                    {
                        "district": "林口",
                        "stationid": "101050304"
                    },
                    {
                        "district": "绥芬河",
                        "stationid": "101050305"
                    },
                    {
                        "district": "宁安",
                        "stationid": "101050306"
                    },
                    {
                        "district": "东宁",
                        "stationid": "101050307"
                    },
                    {
                        "district": "东安",
                        "stationid": "101050308"
                    },
                    {
                        "district": "阳明",
                        "stationid": "101050309"
                    },
                    {
                        "district": "爱民",
                        "stationid": "101050310"
                    },
                    {
                        "district": "西安",
                        "stationid": "101050311"
                    }
                ]
            },
            {
                "city": "佳木斯",
                "disList": [
                    {
                        "district": "佳木斯",
                        "stationid": "101050401"
                    },
                    {
                        "district": "汤原",
                        "stationid": "101050402"
                    },
                    {
                        "district": "抚远",
                        "stationid": "101050403"
                    },
                    {
                        "district": "桦川",
                        "stationid": "101050404"
                    },
                    {
                        "district": "桦南",
                        "stationid": "101050405"
                    },
                    {
                        "district": "同江",
                        "stationid": "101050406"
                    },
                    {
                        "district": "富锦",
                        "stationid": "101050407"
                    },
                    {
                        "district": "向阳",
                        "stationid": "101050408"
                    },
                    {
                        "district": "前进",
                        "stationid": "101050409"
                    },
                    {
                        "district": "东风",
                        "stationid": "101050410"
                    },
                    {
                        "district": "郊区",
                        "stationid": "101050411"
                    }
                ]
            },
            {
                "city": "绥化",
                "disList": [
                    {
                        "district": "绥化",
                        "stationid": "101050501"
                    },
                    {
                        "district": "肇东",
                        "stationid": "101050502"
                    },
                    {
                        "district": "安达",
                        "stationid": "101050503"
                    },
                    {
                        "district": "海伦",
                        "stationid": "101050504"
                    },
                    {
                        "district": "明水",
                        "stationid": "101050505"
                    },
                    {
                        "district": "望奎",
                        "stationid": "101050506"
                    },
                    {
                        "district": "兰西",
                        "stationid": "101050507"
                    },
                    {
                        "district": "青冈",
                        "stationid": "101050508"
                    },
                    {
                        "district": "庆安",
                        "stationid": "101050509"
                    },
                    {
                        "district": "绥棱",
                        "stationid": "101050510"
                    },
                    {
                        "district": "北林",
                        "stationid": "101050511"
                    }
                ]
            },
            {
                "city": "黑河",
                "disList": [
                    {
                        "district": "黑河",
                        "stationid": "101050601"
                    },
                    {
                        "district": "嫩江",
                        "stationid": "101050602"
                    },
                    {
                        "district": "孙吴",
                        "stationid": "101050603"
                    },
                    {
                        "district": "逊克",
                        "stationid": "101050604"
                    },
                    {
                        "district": "五大连池",
                        "stationid": "101050605"
                    },
                    {
                        "district": "北安",
                        "stationid": "101050606"
                    },
                    {
                        "district": "爱辉",
                        "stationid": "101050607"
                    }
                ]
            },
            {
                "city": "大兴安岭",
                "disList": [
                    {
                        "district": "大兴安岭",
                        "stationid": "101050701"
                    },
                    {
                        "district": "塔河",
                        "stationid": "101050702"
                    },
                    {
                        "district": "漠河",
                        "stationid": "101050703"
                    },
                    {
                        "district": "呼玛",
                        "stationid": "101050704"
                    },
                    {
                        "district": "呼中",
                        "stationid": "101050705"
                    },
                    {
                        "district": "新林",
                        "stationid": "101050706"
                    },
                    {
                        "district": "加格达奇",
                        "stationid": "101050708"
                    }
                ]
            },
            {
                "city": "伊春",
                "disList": [
                    {
                        "district": "伊春",
                        "stationid": "101050801"
                    },
                    {
                        "district": "乌伊岭",
                        "stationid": "101050802"
                    },
                    {
                        "district": "五营",
                        "stationid": "101050803"
                    },
                    {
                        "district": "铁力",
                        "stationid": "101050804"
                    },
                    {
                        "district": "嘉荫",
                        "stationid": "101050805"
                    },
                    {
                        "district": "南岔",
                        "stationid": "101050806"
                    },
                    {
                        "district": "友好",
                        "stationid": "101050807"
                    },
                    {
                        "district": "西林",
                        "stationid": "101050808"
                    },
                    {
                        "district": "翠峦",
                        "stationid": "101050809"
                    },
                    {
                        "district": "新青",
                        "stationid": "101050810"
                    },
                    {
                        "district": "美溪",
                        "stationid": "101050811"
                    },
                    {
                        "district": "金山屯",
                        "stationid": "101050812"
                    },
                    {
                        "district": "乌马河",
                        "stationid": "101050813"
                    },
                    {
                        "district": "汤旺河",
                        "stationid": "101050814"
                    },
                    {
                        "district": "带岭",
                        "stationid": "101050815"
                    },
                    {
                        "district": "红星",
                        "stationid": "101050816"
                    },
                    {
                        "district": "上甘岭",
                        "stationid": "101050817"
                    }
                ]
            },
            {
                "city": "大庆",
                "disList": [
                    {
                        "district": "大庆",
                        "stationid": "101050901"
                    },
                    {
                        "district": "林甸",
                        "stationid": "101050902"
                    },
                    {
                        "district": "肇州",
                        "stationid": "101050903"
                    },
                    {
                        "district": "肇源",
                        "stationid": "101050904"
                    },
                    {
                        "district": "杜尔伯特",
                        "stationid": "101050905"
                    },
                    {
                        "district": "萨尔图",
                        "stationid": "101050906"
                    },
                    {
                        "district": "龙凤",
                        "stationid": "101050907"
                    },
                    {
                        "district": "让胡路",
                        "stationid": "101050908"
                    },
                    {
                        "district": "红岗",
                        "stationid": "101050909"
                    },
                    {
                        "district": "大同",
                        "stationid": "101050910"
                    }
                ]
            },
            {
                "city": "七台河",
                "disList": [
                    {
                        "district": "新兴",
                        "stationid": "101051001"
                    },
                    {
                        "district": "七台河",
                        "stationid": "101051002"
                    },
                    {
                        "district": "勃利",
                        "stationid": "101051003"
                    },
                    {
                        "district": "桃山",
                        "stationid": "101051004"
                    },
                    {
                        "district": "茄子河",
                        "stationid": "101051005"
                    }
                ]
            },
            {
                "city": "鸡西",
                "disList": [
                    {
                        "district": "鸡西",
                        "stationid": "101051101"
                    },
                    {
                        "district": "虎林",
                        "stationid": "101051102"
                    },
                    {
                        "district": "密山",
                        "stationid": "101051103"
                    },
                    {
                        "district": "鸡东",
                        "stationid": "101051104"
                    },
                    {
                        "district": "鸡冠",
                        "stationid": "101051105"
                    },
                    {
                        "district": "恒山",
                        "stationid": "101051106"
                    },
                    {
                        "district": "滴道",
                        "stationid": "101051107"
                    },
                    {
                        "district": "梨树",
                        "stationid": "101051108"
                    },
                    {
                        "district": "城子河",
                        "stationid": "101051109"
                    },
                    {
                        "district": "麻山",
                        "stationid": "101051110"
                    }
                ]
            },
            {
                "city": "鹤岗",
                "disList": [
                    {
                        "district": "鹤岗",
                        "stationid": "101051201"
                    },
                    {
                        "district": "绥滨",
                        "stationid": "101051202"
                    },
                    {
                        "district": "萝北",
                        "stationid": "101051203"
                    },
                    {
                        "district": "向阳",
                        "stationid": "101051204"
                    },
                    {
                        "district": "工农",
                        "stationid": "101051205"
                    },
                    {
                        "district": "南山",
                        "stationid": "101051206"
                    },
                    {
                        "district": "兴安",
                        "stationid": "101051207"
                    },
                    {
                        "district": "东山",
                        "stationid": "101051208"
                    },
                    {
                        "district": "兴山",
                        "stationid": "101051209"
                    }
                ]
            },
            {
                "city": "双鸭山",
                "disList": [
                    {
                        "district": "双鸭山",
                        "stationid": "101051301"
                    },
                    {
                        "district": "集贤",
                        "stationid": "101051302"
                    },
                    {
                        "district": "宝清",
                        "stationid": "101051303"
                    },
                    {
                        "district": "饶河",
                        "stationid": "101051304"
                    },
                    {
                        "district": "友谊",
                        "stationid": "101051305"
                    },
                    {
                        "district": "尖山",
                        "stationid": "101051306"
                    },
                    {
                        "district": "岭东",
                        "stationid": "101051307"
                    },
                    {
                        "district": "四方台",
                        "stationid": "101051308"
                    },
                    {
                        "district": "宝山",
                        "stationid": "101051309"
                    }
                ]
            }
        ]
    },
    {
        "province": "吉林",
        "cityList": [
            {
                "city": "长春",
                "disList": [
                    {
                        "district": "长春",
                        "stationid": "101060101"
                    },
                    {
                        "district": "农安",
                        "stationid": "101060102"
                    },
                    {
                        "district": "德惠",
                        "stationid": "101060103"
                    },
                    {
                        "district": "九台",
                        "stationid": "101060104"
                    },
                    {
                        "district": "榆树",
                        "stationid": "101060105"
                    },
                    {
                        "district": "双阳",
                        "stationid": "101060106"
                    },
                    {
                        "district": "二道",
                        "stationid": "101060107"
                    },
                    {
                        "district": "南关",
                        "stationid": "101060108"
                    },
                    {
                        "district": "宽城",
                        "stationid": "101060109"
                    },
                    {
                        "district": "朝阳",
                        "stationid": "101060110"
                    },
                    {
                        "district": "绿园",
                        "stationid": "101060111"
                    }
                ]
            },
            {
                "city": "吉林",
                "disList": [
                    {
                        "district": "吉林",
                        "stationid": "101060201"
                    },
                    {
                        "district": "舒兰",
                        "stationid": "101060202"
                    },
                    {
                        "district": "永吉",
                        "stationid": "101060203"
                    },
                    {
                        "district": "蛟河",
                        "stationid": "101060204"
                    },
                    {
                        "district": "磐石",
                        "stationid": "101060205"
                    },
                    {
                        "district": "桦甸",
                        "stationid": "101060206"
                    },
                    {
                        "district": "昌邑",
                        "stationid": "101060207"
                    },
                    {
                        "district": "龙潭",
                        "stationid": "101060208"
                    },
                    {
                        "district": "船营",
                        "stationid": "101060209"
                    },
                    {
                        "district": "丰满",
                        "stationid": "101060210"
                    }
                ]
            },
            {
                "city": "延边",
                "disList": [
                    {
                        "district": "延吉",
                        "stationid": "101060301"
                    },
                    {
                        "district": "敦化",
                        "stationid": "101060302"
                    },
                    {
                        "district": "安图",
                        "stationid": "101060303"
                    },
                    {
                        "district": "汪清",
                        "stationid": "101060304"
                    },
                    {
                        "district": "和龙",
                        "stationid": "101060305"
                    },
                    {
                        "district": "延边",
                        "stationid": "101060306"
                    },
                    {
                        "district": "龙井",
                        "stationid": "101060307"
                    },
                    {
                        "district": "珲春",
                        "stationid": "101060308"
                    },
                    {
                        "district": "图们",
                        "stationid": "101060309"
                    }
                ]
            },
            {
                "city": "四平",
                "disList": [
                    {
                        "district": "四平",
                        "stationid": "101060401"
                    },
                    {
                        "district": "双辽",
                        "stationid": "101060402"
                    },
                    {
                        "district": "梨树",
                        "stationid": "101060403"
                    },
                    {
                        "district": "公主岭",
                        "stationid": "101060404"
                    },
                    {
                        "district": "伊通",
                        "stationid": "101060405"
                    },
                    {
                        "district": "铁西",
                        "stationid": "101060406"
                    },
                    {
                        "district": "铁东",
                        "stationid": "101060407"
                    }
                ]
            },
            {
                "city": "通化",
                "disList": [
                    {
                        "district": "通化",
                        "stationid": "101060501"
                    },
                    {
                        "district": "梅河口",
                        "stationid": "101060502"
                    },
                    {
                        "district": "柳河",
                        "stationid": "101060503"
                    },
                    {
                        "district": "辉南",
                        "stationid": "101060504"
                    },
                    {
                        "district": "集安",
                        "stationid": "101060505"
                    },
                    {
                        "district": "通化县",
                        "stationid": "101060506"
                    },
                    {
                        "district": "东昌",
                        "stationid": "101060507"
                    },
                    {
                        "district": "二道江",
                        "stationid": "101060508"
                    }
                ]
            },
            {
                "city": "白城",
                "disList": [
                    {
                        "district": "白城",
                        "stationid": "101060601"
                    },
                    {
                        "district": "洮南",
                        "stationid": "101060602"
                    },
                    {
                        "district": "大安",
                        "stationid": "101060603"
                    },
                    {
                        "district": "镇赉",
                        "stationid": "101060604"
                    },
                    {
                        "district": "通榆",
                        "stationid": "101060605"
                    },
                    {
                        "district": "洮北",
                        "stationid": "101060606"
                    }
                ]
            },
            {
                "city": "辽源",
                "disList": [
                    {
                        "district": "辽源",
                        "stationid": "101060701"
                    },
                    {
                        "district": "东丰",
                        "stationid": "101060702"
                    },
                    {
                        "district": "东辽",
                        "stationid": "101060703"
                    },
                    {
                        "district": "龙山",
                        "stationid": "101060704"
                    },
                    {
                        "district": "西安",
                        "stationid": "101060705"
                    }
                ]
            },
            {
                "city": "松原",
                "disList": [
                    {
                        "district": "松原",
                        "stationid": "101060801"
                    },
                    {
                        "district": "乾安",
                        "stationid": "101060802"
                    },
                    {
                        "district": "前郭",
                        "stationid": "101060803"
                    },
                    {
                        "district": "长岭",
                        "stationid": "101060804"
                    },
                    {
                        "district": "扶余",
                        "stationid": "101060805"
                    },
                    {
                        "district": "宁江",
                        "stationid": "101060806"
                    }
                ]
            },
            {
                "city": "白山",
                "disList": [
                    {
                        "district": "白山",
                        "stationid": "101060901"
                    },
                    {
                        "district": "靖宇",
                        "stationid": "101060902"
                    },
                    {
                        "district": "临江",
                        "stationid": "101060903"
                    },
                    {
                        "district": "长白",
                        "stationid": "101060905"
                    },
                    {
                        "district": "抚松",
                        "stationid": "101060906"
                    },
                    {
                        "district": "江源",
                        "stationid": "101060907"
                    },
                    {
                        "district": "浑江",
                        "stationid": "101060908"
                    },
                    {
                        "district": "东岗",
                        "stationid": "101060904"
                    }
                ]
            }
        ]
    },
    {
        "province": "辽宁",
        "cityList": [
            {
                "city": "沈阳",
                "disList": [
                    {
                        "district": "沈阳",
                        "stationid": "101070101"
                    },
                    {
                        "district": "浑南",
                        "stationid": "101070102"
                    },
                    {
                        "district": "辽中",
                        "stationid": "101070103"
                    },
                    {
                        "district": "康平",
                        "stationid": "101070104"
                    },
                    {
                        "district": "法库",
                        "stationid": "101070105"
                    },
                    {
                        "district": "新民",
                        "stationid": "101070106"
                    },
                    {
                        "district": "和平",
                        "stationid": "101070107"
                    },
                    {
                        "district": "沈河",
                        "stationid": "101070108"
                    },
                    {
                        "district": "大东",
                        "stationid": "101070109"
                    },
                    {
                        "district": "皇姑",
                        "stationid": "101070110"
                    },
                    {
                        "district": "铁西",
                        "stationid": "101070111"
                    },
                    {
                        "district": "苏家屯",
                        "stationid": "101070112"
                    },
                    {
                        "district": "沈北新区",
                        "stationid": "101070113"
                    },
                    {
                        "district": "于洪",
                        "stationid": "101070114"
                    }
                ]
            },
            {
                "city": "大连",
                "disList": [
                    {
                        "district": "大连",
                        "stationid": "101070201"
                    },
                    {
                        "district": "瓦房店",
                        "stationid": "101070202"
                    },
                    {
                        "district": "金州",
                        "stationid": "101070203"
                    },
                    {
                        "district": "普兰店",
                        "stationid": "101070204"
                    },
                    {
                        "district": "旅顺",
                        "stationid": "101070205"
                    },
                    {
                        "district": "长海",
                        "stationid": "101070206"
                    },
                    {
                        "district": "庄河",
                        "stationid": "101070207"
                    },
                    {
                        "district": "中山",
                        "stationid": "101070208"
                    },
                    {
                        "district": "西岗",
                        "stationid": "101070209"
                    },
                    {
                        "district": "沙河口",
                        "stationid": "101070210"
                    },
                    {
                        "district": "甘井子",
                        "stationid": "101070211"
                    }
                ]
            },
            {
                "city": "鞍山",
                "disList": [
                    {
                        "district": "鞍山",
                        "stationid": "101070301"
                    },
                    {
                        "district": "台安",
                        "stationid": "101070302"
                    },
                    {
                        "district": "岫岩",
                        "stationid": "101070303"
                    },
                    {
                        "district": "海城",
                        "stationid": "101070304"
                    },
                    {
                        "district": "铁东",
                        "stationid": "101070305"
                    },
                    {
                        "district": "铁西",
                        "stationid": "101070306"
                    },
                    {
                        "district": "立山",
                        "stationid": "101070307"
                    },
                    {
                        "district": "千山",
                        "stationid": "101070308"
                    }
                ]
            },
            {
                "city": "抚顺",
                "disList": [
                    {
                        "district": "抚顺",
                        "stationid": "101070401"
                    },
                    {
                        "district": "新宾",
                        "stationid": "101070402"
                    },
                    {
                        "district": "清原",
                        "stationid": "101070403"
                    },
                    {
                        "district": "新抚",
                        "stationid": "101070405"
                    },
                    {
                        "district": "东洲",
                        "stationid": "101070406"
                    },
                    {
                        "district": "望花",
                        "stationid": "101070407"
                    },
                    {
                        "district": "顺城",
                        "stationid": "101070408"
                    }
                ]
            },
            {
                "city": "本溪",
                "disList": [
                    {
                        "district": "本溪",
                        "stationid": "101070501"
                    },
                    {
                        "district": "本溪县",
                        "stationid": "101070502"
                    },
                    {
                        "district": "平山",
                        "stationid": "101070503"
                    },
                    {
                        "district": "桓仁",
                        "stationid": "101070504"
                    },
                    {
                        "district": "溪湖",
                        "stationid": "101070505"
                    },
                    {
                        "district": "明山",
                        "stationid": "101070506"
                    },
                    {
                        "district": "南芬",
                        "stationid": "101070507"
                    }
                ]
            },
            {
                "city": "丹东",
                "disList": [
                    {
                        "district": "丹东",
                        "stationid": "101070601"
                    },
                    {
                        "district": "凤城",
                        "stationid": "101070602"
                    },
                    {
                        "district": "宽甸",
                        "stationid": "101070603"
                    },
                    {
                        "district": "东港",
                        "stationid": "101070604"
                    },
                    {
                        "district": "元宝",
                        "stationid": "101070605"
                    },
                    {
                        "district": "振兴",
                        "stationid": "101070606"
                    },
                    {
                        "district": "振安",
                        "stationid": "101070607"
                    }
                ]
            },
            {
                "city": "锦州",
                "disList": [
                    {
                        "district": "锦州",
                        "stationid": "101070701"
                    },
                    {
                        "district": "凌海",
                        "stationid": "101070702"
                    },
                    {
                        "district": "古塔",
                        "stationid": "101070703"
                    },
                    {
                        "district": "义县",
                        "stationid": "101070704"
                    },
                    {
                        "district": "黑山",
                        "stationid": "101070705"
                    },
                    {
                        "district": "北镇",
                        "stationid": "101070706"
                    },
                    {
                        "district": "凌河",
                        "stationid": "101070707"
                    },
                    {
                        "district": "太和",
                        "stationid": "101070708"
                    }
                ]
            },
            {
                "city": "营口",
                "disList": [
                    {
                        "district": "营口",
                        "stationid": "101070801"
                    },
                    {
                        "district": "大石桥",
                        "stationid": "101070802"
                    },
                    {
                        "district": "盖州",
                        "stationid": "101070803"
                    },
                    {
                        "district": "站前",
                        "stationid": "101070804"
                    },
                    {
                        "district": "西市",
                        "stationid": "101070805"
                    },
                    {
                        "district": "鲅鱼圈",
                        "stationid": "101070806"
                    },
                    {
                        "district": "老边",
                        "stationid": "101070807"
                    }
                ]
            },
            {
                "city": "阜新",
                "disList": [
                    {
                        "district": "阜新",
                        "stationid": "101070901"
                    },
                    {
                        "district": "彰武",
                        "stationid": "101070902"
                    },
                    {
                        "district": "海州",
                        "stationid": "101070903"
                    },
                    {
                        "district": "新邱",
                        "stationid": "101070904"
                    },
                    {
                        "district": "太平",
                        "stationid": "101070905"
                    },
                    {
                        "district": "清河门",
                        "stationid": "101070906"
                    },
                    {
                        "district": "细河",
                        "stationid": "101070907"
                    }
                ]
            },
            {
                "city": "辽阳",
                "disList": [
                    {
                        "district": "辽阳",
                        "stationid": "101071001"
                    },
                    {
                        "district": "辽阳县",
                        "stationid": "101071002"
                    },
                    {
                        "district": "灯塔",
                        "stationid": "101071003"
                    },
                    {
                        "district": "弓长岭",
                        "stationid": "101071004"
                    },
                    {
                        "district": "白塔",
                        "stationid": "101071005"
                    },
                    {
                        "district": "文圣",
                        "stationid": "101071006"
                    },
                    {
                        "district": "宏伟",
                        "stationid": "101071007"
                    },
                    {
                        "district": "太子河",
                        "stationid": "101071008"
                    }
                ]
            },
            {
                "city": "铁岭",
                "disList": [
                    {
                        "district": "铁岭",
                        "stationid": "101071101"
                    },
                    {
                        "district": "开原",
                        "stationid": "101071102"
                    },
                    {
                        "district": "昌图",
                        "stationid": "101071103"
                    },
                    {
                        "district": "西丰",
                        "stationid": "101071104"
                    },
                    {
                        "district": "调兵山",
                        "stationid": "101071105"
                    },
                    {
                        "district": "银州",
                        "stationid": "101071106"
                    },
                    {
                        "district": "清河",
                        "stationid": "101071107"
                    }
                ]
            },
            {
                "city": "朝阳",
                "disList": [
                    {
                        "district": "朝阳",
                        "stationid": "101071201"
                    },
                    {
                        "district": "双塔",
                        "stationid": "101071202"
                    },
                    {
                        "district": "凌源",
                        "stationid": "101071203"
                    },
                    {
                        "district": "喀左",
                        "stationid": "101071204"
                    },
                    {
                        "district": "北票",
                        "stationid": "101071205"
                    },
                    {
                        "district": "龙城",
                        "stationid": "101071206"
                    },
                    {
                        "district": "建平县",
                        "stationid": "101071207"
                    }
                ]
            },
            {
                "city": "盘锦",
                "disList": [
                    {
                        "district": "盘锦",
                        "stationid": "101071301"
                    },
                    {
                        "district": "大洼",
                        "stationid": "101071302"
                    },
                    {
                        "district": "盘山",
                        "stationid": "101071303"
                    },
                    {
                        "district": "双台子",
                        "stationid": "101071304"
                    },
                    {
                        "district": "兴隆台",
                        "stationid": "101071305"
                    }
                ]
            },
            {
                "city": "葫芦岛",
                "disList": [
                    {
                        "district": "葫芦岛",
                        "stationid": "101071401"
                    },
                    {
                        "district": "建昌",
                        "stationid": "101071402"
                    },
                    {
                        "district": "绥中",
                        "stationid": "101071403"
                    },
                    {
                        "district": "兴城",
                        "stationid": "101071404"
                    },
                    {
                        "district": "连山",
                        "stationid": "101071405"
                    },
                    {
                        "district": "龙港",
                        "stationid": "101071406"
                    },
                    {
                        "district": "南票",
                        "stationid": "101071407"
                    }
                ]
            }
        ]
    },
    {
        "province": "内蒙古",
        "cityList": [
            {
                "city": "呼和浩特",
                "disList": [
                    {
                        "district": "呼和浩特",
                        "stationid": "101080101"
                    },
                    {
                        "district": "土左旗",
                        "stationid": "101080102"
                    },
                    {
                        "district": "托县",
                        "stationid": "101080103"
                    },
                    {
                        "district": "和林",
                        "stationid": "101080104"
                    },
                    {
                        "district": "清水河",
                        "stationid": "101080105"
                    },
                    {
                        "district": "赛罕",
                        "stationid": "101080106"
                    },
                    {
                        "district": "武川",
                        "stationid": "101080107"
                    },
                    {
                        "district": "新城",
                        "stationid": "101080108"
                    },
                    {
                        "district": "回民",
                        "stationid": "101080109"
                    },
                    {
                        "district": "玉泉",
                        "stationid": "101080110"
                    }
                ]
            },
            {
                "city": "包头",
                "disList": [
                    {
                        "district": "包头",
                        "stationid": "101080201"
                    },
                    {
                        "district": "白云鄂博",
                        "stationid": "101080202"
                    },
                    {
                        "district": "土右旗",
                        "stationid": "101080204"
                    },
                    {
                        "district": "固阳",
                        "stationid": "101080205"
                    },
                    {
                        "district": "达茂旗",
                        "stationid": "101080206"
                    },
                    {
                        "district": "东河",
                        "stationid": "101080208"
                    },
                    {
                        "district": "昆都仑",
                        "stationid": "101080209"
                    },
                    {
                        "district": "青山",
                        "stationid": "101080210"
                    },
                    {
                        "district": "石拐",
                        "stationid": "101080211"
                    },
                    {
                        "district": "九原",
                        "stationid": "101080212"
                    },
                    {
                        "district": "满都拉",
                        "stationid": "101080203"
                    },
                    {
                        "district": "希拉穆仁",
                        "stationid": "101080207"
                    }
                ]
            },
            {
                "city": "乌海",
                "disList": [
                    {
                        "district": "乌海",
                        "stationid": "101080301"
                    },
                    {
                        "district": "海勃湾",
                        "stationid": "101080302"
                    },
                    {
                        "district": "海南",
                        "stationid": "101080303"
                    },
                    {
                        "district": "乌达",
                        "stationid": "101080304"
                    }
                ]
            },
            {
                "city": "乌兰察布",
                "disList": [
                    {
                        "district": "集宁",
                        "stationid": "101080401"
                    },
                    {
                        "district": "卓资",
                        "stationid": "101080402"
                    },
                    {
                        "district": "化德",
                        "stationid": "101080403"
                    },
                    {
                        "district": "商都",
                        "stationid": "101080404"
                    },
                    {
                        "district": "乌兰察布",
                        "stationid": "101080405"
                    },
                    {
                        "district": "兴和",
                        "stationid": "101080406"
                    },
                    {
                        "district": "凉城",
                        "stationid": "101080407"
                    },
                    {
                        "district": "察右前旗",
                        "stationid": "101080408"
                    },
                    {
                        "district": "察右中旗",
                        "stationid": "101080409"
                    },
                    {
                        "district": "察右后旗",
                        "stationid": "101080410"
                    },
                    {
                        "district": "四子王旗",
                        "stationid": "101080411"
                    },
                    {
                        "district": "丰镇",
                        "stationid": "101080412"
                    }
                ]
            },
            {
                "city": "通辽",
                "disList": [
                    {
                        "district": "通辽",
                        "stationid": "101080501"
                    },
                    {
                        "district": "科左中旗",
                        "stationid": "101080503"
                    },
                    {
                        "district": "科左后旗",
                        "stationid": "101080504"
                    },
                    {
                        "district": "开鲁",
                        "stationid": "101080506"
                    },
                    {
                        "district": "库伦",
                        "stationid": "101080507"
                    },
                    {
                        "district": "奈曼",
                        "stationid": "101080508"
                    },
                    {
                        "district": "扎鲁特",
                        "stationid": "101080509"
                    },
                    {
                        "district": "科尔沁",
                        "stationid": "101080510"
                    },
                    {
                        "district": "霍林郭勒",
                        "stationid": "101080512"
                    },
                    {
                        "district": "舍伯吐",
                        "stationid": "101080502"
                    },
                    {
                        "district": "青龙山",
                        "stationid": "101080505"
                    },
                    {
                        "district": "巴雅尔吐胡硕",
                        "stationid": "101080511"
                    }
                ]
            },
            {
                "city": "赤峰",
                "disList": [
                    {
                        "district": "赤峰",
                        "stationid": "101080601"
                    },
                    {
                        "district": "红山",
                        "stationid": "101080602"
                    },
                    {
                        "district": "阿鲁旗",
                        "stationid": "101080603"
                    },
                    {
                        "district": "巴林左旗",
                        "stationid": "101080605"
                    },
                    {
                        "district": "巴林右旗",
                        "stationid": "101080606"
                    },
                    {
                        "district": "林西",
                        "stationid": "101080607"
                    },
                    {
                        "district": "克什克腾",
                        "stationid": "101080608"
                    },
                    {
                        "district": "翁牛特",
                        "stationid": "101080609"
                    },
                    {
                        "district": "喀喇沁",
                        "stationid": "101080611"
                    },
                    {
                        "district": "宁城",
                        "stationid": "101080613"
                    },
                    {
                        "district": "敖汉",
                        "stationid": "101080614"
                    },
                    {
                        "district": "元宝山",
                        "stationid": "101080616"
                    },
                    {
                        "district": "松山",
                        "stationid": "101080617"
                    },
                    {
                        "district": "富河",
                        "stationid": "101080618"
                    },
                    {
                        "district": "宝国图",
                        "stationid": "101080619"
                    },
                    {
                        "district": "岗子",
                        "stationid": "101080610"
                    },
                    {
                        "district": "八里罕",
                        "stationid": "101080612"
                    }
                ]
            },
            {
                "city": "鄂尔多斯",
                "disList": [
                    {
                        "district": "鄂尔多斯",
                        "stationid": "101080701"
                    },
                    {
                        "district": "达拉特",
                        "stationid": "101080703"
                    },
                    {
                        "district": "准格尔",
                        "stationid": "101080704"
                    },
                    {
                        "district": "鄂前旗",
                        "stationid": "101080705"
                    },
                    {
                        "district": "鄂托克",
                        "stationid": "101080708"
                    },
                    {
                        "district": "杭锦旗",
                        "stationid": "101080709"
                    },
                    {
                        "district": "乌审旗",
                        "stationid": "101080710"
                    },
                    {
                        "district": "伊金霍洛",
                        "stationid": "101080711"
                    },
                    {
                        "district": "东胜",
                        "stationid": "101080713"
                    },
                    {
                        "district": "康巴什",
                        "stationid": "101080714"
                    },
                    {
                        "district": "河南",
                        "stationid": "101080706"
                    },
                    {
                        "district": "伊和乌素",
                        "stationid": "101080707"
                    },
                    {
                        "district": "乌审召",
                        "stationid": "101080712"
                    }
                ]
            },
            {
                "city": "巴彦淖尔",
                "disList": [
                    {
                        "district": "临河",
                        "stationid": "101080801"
                    },
                    {
                        "district": "五原",
                        "stationid": "101080802"
                    },
                    {
                        "district": "磴口",
                        "stationid": "101080803"
                    },
                    {
                        "district": "乌前旗",
                        "stationid": "101080804"
                    },
                    {
                        "district": "乌中旗",
                        "stationid": "101080806"
                    },
                    {
                        "district": "乌后旗",
                        "stationid": "101080807"
                    },
                    {
                        "district": "杭锦后旗",
                        "stationid": "101080810"
                    },
                    {
                        "district": "巴彦淖尔",
                        "stationid": "101080811"
                    },
                    {
                        "district": "大佘太",
                        "stationid": "101080805"
                    },
                    {
                        "district": "海力素",
                        "stationid": "101080808"
                    },
                    {
                        "district": "那仁宝力格",
                        "stationid": "101080809"
                    }
                ]
            },
            {
                "city": "锡林郭勒",
                "disList": [
                    {
                        "district": "锡林浩特",
                        "stationid": "101080901"
                    },
                    {
                        "district": "锡林郭勒",
                        "stationid": "101080902"
                    },
                    {
                        "district": "二连浩特",
                        "stationid": "101080903"
                    },
                    {
                        "district": "阿巴嘎",
                        "stationid": "101080904"
                    },
                    {
                        "district": "苏左旗",
                        "stationid": "101080906"
                    },
                    {
                        "district": "苏右旗",
                        "stationid": "101080907"
                    },
                    {
                        "district": "东乌旗",
                        "stationid": "101080909"
                    },
                    {
                        "district": "西乌旗",
                        "stationid": "101080910"
                    },
                    {
                        "district": "太仆寺",
                        "stationid": "101080911"
                    },
                    {
                        "district": "镶黄旗",
                        "stationid": "101080912"
                    },
                    {
                        "district": "正镶白旗",
                        "stationid": "101080913"
                    },
                    {
                        "district": "正蓝旗",
                        "stationid": "101080914"
                    },
                    {
                        "district": "多伦",
                        "stationid": "101080915"
                    },
                    {
                        "district": "朱日和",
                        "stationid": "101080908"
                    },
                    {
                        "district": "博克图",
                        "stationid": "101080916"
                    },
                    {
                        "district": "乌拉盖",
                        "stationid": "101080917"
                    }
                ]
            },
            {
                "city": "呼伦贝尔",
                "disList": [
                    {
                        "district": "海拉尔",
                        "stationid": "101081001"
                    },
                    {
                        "district": "阿荣旗",
                        "stationid": "101081003"
                    },
                    {
                        "district": "莫力达瓦",
                        "stationid": "101081004"
                    },
                    {
                        "district": "鄂伦春旗",
                        "stationid": "101081005"
                    },
                    {
                        "district": "鄂温克旗",
                        "stationid": "101081006"
                    },
                    {
                        "district": "陈旗",
                        "stationid": "101081007"
                    },
                    {
                        "district": "新左旗",
                        "stationid": "101081008"
                    },
                    {
                        "district": "新右旗",
                        "stationid": "101081009"
                    },
                    {
                        "district": "满洲里",
                        "stationid": "101081010"
                    },
                    {
                        "district": "牙克石",
                        "stationid": "101081011"
                    },
                    {
                        "district": "扎兰屯",
                        "stationid": "101081012"
                    },
                    {
                        "district": "呼伦贝尔",
                        "stationid": "101081013"
                    },
                    {
                        "district": "额尔古纳",
                        "stationid": "101081014"
                    },
                    {
                        "district": "根河",
                        "stationid": "101081015"
                    },
                    {
                        "district": "扎赉诺尔",
                        "stationid": "101081017"
                    },
                    {
                        "district": "小二沟",
                        "stationid": "101081002"
                    },
                    {
                        "district": "图里河",
                        "stationid": "101081016"
                    }
                ]
            },
            {
                "city": "兴安盟",
                "disList": [
                    {
                        "district": "乌兰浩特",
                        "stationid": "101081101"
                    },
                    {
                        "district": "阿尔山",
                        "stationid": "101081102"
                    },
                    {
                        "district": "科右中旗",
                        "stationid": "101081103"
                    },
                    {
                        "district": "扎赉特",
                        "stationid": "101081105"
                    },
                    {
                        "district": "突泉",
                        "stationid": "101081107"
                    },
                    {
                        "district": "兴安盟",
                        "stationid": "101081108"
                    },
                    {
                        "district": "科右前旗",
                        "stationid": "101081109"
                    },
                    {
                        "district": "胡尔勒",
                        "stationid": "101081104"
                    },
                    {
                        "district": "索伦",
                        "stationid": "101081106"
                    },
                    {
                        "district": "高力板",
                        "stationid": "101081110"
                    }
                ]
            },
            {
                "city": "阿拉善盟",
                "disList": [
                    {
                        "district": "阿左旗",
                        "stationid": "101081201"
                    },
                    {
                        "district": "阿右旗",
                        "stationid": "101081202"
                    },
                    {
                        "district": "额济纳",
                        "stationid": "101081203"
                    },
                    {
                        "district": "阿拉善盟",
                        "stationid": "101081213"
                    },
                    {
                        "district": "拐子湖",
                        "stationid": "101081204"
                    },
                    {
                        "district": "吉兰太",
                        "stationid": "101081205"
                    },
                    {
                        "district": "巴彦诺日公",
                        "stationid": "101081209"
                    },
                    {
                        "district": "雅布赖",
                        "stationid": "101081210"
                    },
                    {
                        "district": "乌斯太",
                        "stationid": "101081211"
                    },
                    {
                        "district": "孪井滩",
                        "stationid": "101081212"
                    }
                ]
            }
        ]
    },
    {
        "province": "河北",
        "cityList": [
            {
                "city": "石家庄",
                "disList": [
                    {
                        "district": "石家庄",
                        "stationid": "101090101"
                    },
                    {
                        "district": "井陉",
                        "stationid": "101090102"
                    },
                    {
                        "district": "正定",
                        "stationid": "101090103"
                    },
                    {
                        "district": "栾城",
                        "stationid": "101090104"
                    },
                    {
                        "district": "行唐",
                        "stationid": "101090105"
                    },
                    {
                        "district": "灵寿",
                        "stationid": "101090106"
                    },
                    {
                        "district": "高邑",
                        "stationid": "101090107"
                    },
                    {
                        "district": "深泽",
                        "stationid": "101090108"
                    },
                    {
                        "district": "赞皇",
                        "stationid": "101090109"
                    },
                    {
                        "district": "无极",
                        "stationid": "101090110"
                    },
                    {
                        "district": "平山",
                        "stationid": "101090111"
                    },
                    {
                        "district": "元氏",
                        "stationid": "101090112"
                    },
                    {
                        "district": "赵县",
                        "stationid": "101090113"
                    },
                    {
                        "district": "辛集",
                        "stationid": "101090114"
                    },
                    {
                        "district": "藁城",
                        "stationid": "101090115"
                    },
                    {
                        "district": "晋州",
                        "stationid": "101090116"
                    },
                    {
                        "district": "新乐",
                        "stationid": "101090117"
                    },
                    {
                        "district": "鹿泉",
                        "stationid": "101090118"
                    },
                    {
                        "district": "长安",
                        "stationid": "101090119"
                    },
                    {
                        "district": "桥西",
                        "stationid": "101090120"
                    },
                    {
                        "district": "新华",
                        "stationid": "101090121"
                    },
                    {
                        "district": "井陉矿区",
                        "stationid": "101090122"
                    },
                    {
                        "district": "裕华",
                        "stationid": "101090123"
                    }
                ]
            },
            {
                "city": "保定",
                "disList": [
                    {
                        "district": "保定",
                        "stationid": "101090201"
                    },
                    {
                        "district": "满城",
                        "stationid": "101090202"
                    },
                    {
                        "district": "阜平",
                        "stationid": "101090203"
                    },
                    {
                        "district": "徐水",
                        "stationid": "101090204"
                    },
                    {
                        "district": "唐县",
                        "stationid": "101090205"
                    },
                    {
                        "district": "高阳",
                        "stationid": "101090206"
                    },
                    {
                        "district": "竞秀",
                        "stationid": "101090208"
                    },
                    {
                        "district": "涞源",
                        "stationid": "101090209"
                    },
                    {
                        "district": "望都",
                        "stationid": "101090210"
                    },
                    {
                        "district": "易县",
                        "stationid": "101090212"
                    },
                    {
                        "district": "莲池",
                        "stationid": "101090213"
                    },
                    {
                        "district": "曲阳",
                        "stationid": "101090214"
                    },
                    {
                        "district": "蠡县",
                        "stationid": "101090215"
                    },
                    {
                        "district": "顺平",
                        "stationid": "101090216"
                    },
                    {
                        "district": "涿州",
                        "stationid": "101090218"
                    },
                    {
                        "district": "定州",
                        "stationid": "101090219"
                    },
                    {
                        "district": "安国",
                        "stationid": "101090220"
                    },
                    {
                        "district": "高碑店",
                        "stationid": "101090221"
                    },
                    {
                        "district": "涞水",
                        "stationid": "101090222"
                    },
                    {
                        "district": "定兴",
                        "stationid": "101090223"
                    },
                    {
                        "district": "清苑",
                        "stationid": "101090224"
                    },
                    {
                        "district": "博野",
                        "stationid": "101090225"
                    }
                ]
            },
            {
                "city": "张家口",
                "disList": [
                    {
                        "district": "张家口",
                        "stationid": "101090301"
                    },
                    {
                        "district": "宣化",
                        "stationid": "101090302"
                    },
                    {
                        "district": "张北",
                        "stationid": "101090303"
                    },
                    {
                        "district": "康保",
                        "stationid": "101090304"
                    },
                    {
                        "district": "沽源",
                        "stationid": "101090305"
                    },
                    {
                        "district": "尚义",
                        "stationid": "101090306"
                    },
                    {
                        "district": "蔚县",
                        "stationid": "101090307"
                    },
                    {
                        "district": "阳原",
                        "stationid": "101090308"
                    },
                    {
                        "district": "怀安",
                        "stationid": "101090309"
                    },
                    {
                        "district": "万全",
                        "stationid": "101090310"
                    },
                    {
                        "district": "怀来",
                        "stationid": "101090311"
                    },
                    {
                        "district": "涿鹿",
                        "stationid": "101090312"
                    },
                    {
                        "district": "赤城",
                        "stationid": "101090313"
                    },
                    {
                        "district": "崇礼",
                        "stationid": "101090314"
                    },
                    {
                        "district": "桥东",
                        "stationid": "101090315"
                    },
                    {
                        "district": "桥西",
                        "stationid": "101090316"
                    },
                    {
                        "district": "下花园",
                        "stationid": "101090317"
                    }
                ]
            },
            {
                "city": "承德",
                "disList": [
                    {
                        "district": "双桥",
                        "stationid": "101090401"
                    },
                    {
                        "district": "承德",
                        "stationid": "101090402"
                    },
                    {
                        "district": "承德县",
                        "stationid": "101090403"
                    },
                    {
                        "district": "兴隆",
                        "stationid": "101090404"
                    },
                    {
                        "district": "平泉",
                        "stationid": "101090405"
                    },
                    {
                        "district": "滦平",
                        "stationid": "101090406"
                    },
                    {
                        "district": "隆化",
                        "stationid": "101090407"
                    },
                    {
                        "district": "丰宁",
                        "stationid": "101090408"
                    },
                    {
                        "district": "宽城",
                        "stationid": "101090409"
                    },
                    {
                        "district": "围场",
                        "stationid": "101090410"
                    },
                    {
                        "district": "双滦",
                        "stationid": "101090411"
                    },
                    {
                        "district": "鹰手营子矿",
                        "stationid": "101090412"
                    }
                ]
            },
            {
                "city": "唐山",
                "disList": [
                    {
                        "district": "唐山",
                        "stationid": "101090501"
                    },
                    {
                        "district": "丰南",
                        "stationid": "101090502"
                    },
                    {
                        "district": "丰润",
                        "stationid": "101090503"
                    },
                    {
                        "district": "滦县",
                        "stationid": "101090504"
                    },
                    {
                        "district": "滦南",
                        "stationid": "101090505"
                    },
                    {
                        "district": "乐亭",
                        "stationid": "101090506"
                    },
                    {
                        "district": "迁西",
                        "stationid": "101090507"
                    },
                    {
                        "district": "玉田",
                        "stationid": "101090508"
                    },
                    {
                        "district": "曹妃甸",
                        "stationid": "101090509"
                    },
                    {
                        "district": "遵化",
                        "stationid": "101090510"
                    },
                    {
                        "district": "迁安",
                        "stationid": "101090511"
                    },
                    {
                        "district": "路南",
                        "stationid": "101090513"
                    },
                    {
                        "district": "路北",
                        "stationid": "101090514"
                    },
                    {
                        "district": "古冶",
                        "stationid": "101090515"
                    },
                    {
                        "district": "开平",
                        "stationid": "101090516"
                    }
                ]
            },
            {
                "city": "廊坊",
                "disList": [
                    {
                        "district": "廊坊",
                        "stationid": "101090601"
                    },
                    {
                        "district": "固安",
                        "stationid": "101090602"
                    },
                    {
                        "district": "永清",
                        "stationid": "101090603"
                    },
                    {
                        "district": "香河",
                        "stationid": "101090604"
                    },
                    {
                        "district": "大城",
                        "stationid": "101090605"
                    },
                    {
                        "district": "文安",
                        "stationid": "101090606"
                    },
                    {
                        "district": "大厂",
                        "stationid": "101090607"
                    },
                    {
                        "district": "霸州",
                        "stationid": "101090608"
                    },
                    {
                        "district": "三河",
                        "stationid": "101090609"
                    },
                    {
                        "district": "安次",
                        "stationid": "101090610"
                    },
                    {
                        "district": "广阳",
                        "stationid": "101090611"
                    }
                ]
            },
            {
                "city": "沧州",
                "disList": [
                    {
                        "district": "沧州",
                        "stationid": "101090701"
                    },
                    {
                        "district": "青县",
                        "stationid": "101090702"
                    },
                    {
                        "district": "东光",
                        "stationid": "101090703"
                    },
                    {
                        "district": "海兴",
                        "stationid": "101090704"
                    },
                    {
                        "district": "盐山",
                        "stationid": "101090705"
                    },
                    {
                        "district": "肃宁",
                        "stationid": "101090706"
                    },
                    {
                        "district": "南皮",
                        "stationid": "101090707"
                    },
                    {
                        "district": "吴桥",
                        "stationid": "101090708"
                    },
                    {
                        "district": "献县",
                        "stationid": "101090709"
                    },
                    {
                        "district": "孟村",
                        "stationid": "101090710"
                    },
                    {
                        "district": "泊头",
                        "stationid": "101090711"
                    },
                    {
                        "district": "任丘",
                        "stationid": "101090712"
                    },
                    {
                        "district": "黄骅",
                        "stationid": "101090713"
                    },
                    {
                        "district": "河间",
                        "stationid": "101090714"
                    },
                    {
                        "district": "新华",
                        "stationid": "101090715"
                    },
                    {
                        "district": "沧县",
                        "stationid": "101090716"
                    },
                    {
                        "district": "运河",
                        "stationid": "101090717"
                    }
                ]
            },
            {
                "city": "衡水",
                "disList": [
                    {
                        "district": "衡水",
                        "stationid": "101090801"
                    },
                    {
                        "district": "枣强",
                        "stationid": "101090802"
                    },
                    {
                        "district": "武邑",
                        "stationid": "101090803"
                    },
                    {
                        "district": "武强",
                        "stationid": "101090804"
                    },
                    {
                        "district": "饶阳",
                        "stationid": "101090805"
                    },
                    {
                        "district": "安平",
                        "stationid": "101090806"
                    },
                    {
                        "district": "故城",
                        "stationid": "101090807"
                    },
                    {
                        "district": "景县",
                        "stationid": "101090808"
                    },
                    {
                        "district": "阜城",
                        "stationid": "101090809"
                    },
                    {
                        "district": "冀州",
                        "stationid": "101090810"
                    },
                    {
                        "district": "深州",
                        "stationid": "101090811"
                    },
                    {
                        "district": "桃城",
                        "stationid": "101090812"
                    }
                ]
            },
            {
                "city": "邢台",
                "disList": [
                    {
                        "district": "邢台",
                        "stationid": "101090901"
                    },
                    {
                        "district": "临城",
                        "stationid": "101090902"
                    },
                    {
                        "district": "桥东",
                        "stationid": "101090903"
                    },
                    {
                        "district": "内丘",
                        "stationid": "101090904"
                    },
                    {
                        "district": "柏乡",
                        "stationid": "101090905"
                    },
                    {
                        "district": "隆尧",
                        "stationid": "101090906"
                    },
                    {
                        "district": "南和",
                        "stationid": "101090907"
                    },
                    {
                        "district": "宁晋",
                        "stationid": "101090908"
                    },
                    {
                        "district": "巨鹿",
                        "stationid": "101090909"
                    },
                    {
                        "district": "新河",
                        "stationid": "101090910"
                    },
                    {
                        "district": "广宗",
                        "stationid": "101090911"
                    },
                    {
                        "district": "平乡",
                        "stationid": "101090912"
                    },
                    {
                        "district": "威县",
                        "stationid": "101090913"
                    },
                    {
                        "district": "清河",
                        "stationid": "101090914"
                    },
                    {
                        "district": "临西",
                        "stationid": "101090915"
                    },
                    {
                        "district": "南宫",
                        "stationid": "101090916"
                    },
                    {
                        "district": "沙河",
                        "stationid": "101090917"
                    },
                    {
                        "district": "任县",
                        "stationid": "101090918"
                    },
                    {
                        "district": "桥西",
                        "stationid": "101090919"
                    }
                ]
            },
            {
                "city": "邯郸",
                "disList": [
                    {
                        "district": "邯郸",
                        "stationid": "101091001"
                    },
                    {
                        "district": "峰峰",
                        "stationid": "101091002"
                    },
                    {
                        "district": "临漳",
                        "stationid": "101091003"
                    },
                    {
                        "district": "成安",
                        "stationid": "101091004"
                    },
                    {
                        "district": "大名",
                        "stationid": "101091005"
                    },
                    {
                        "district": "涉县",
                        "stationid": "101091006"
                    },
                    {
                        "district": "磁县",
                        "stationid": "101091007"
                    },
                    {
                        "district": "肥乡",
                        "stationid": "101091008"
                    },
                    {
                        "district": "永年",
                        "stationid": "101091009"
                    },
                    {
                        "district": "邱县",
                        "stationid": "101091010"
                    },
                    {
                        "district": "鸡泽",
                        "stationid": "101091011"
                    },
                    {
                        "district": "广平",
                        "stationid": "101091012"
                    },
                    {
                        "district": "馆陶",
                        "stationid": "101091013"
                    },
                    {
                        "district": "魏县",
                        "stationid": "101091014"
                    },
                    {
                        "district": "曲周",
                        "stationid": "101091015"
                    },
                    {
                        "district": "武安",
                        "stationid": "101091016"
                    },
                    {
                        "district": "邯山",
                        "stationid": "101091017"
                    },
                    {
                        "district": "丛台",
                        "stationid": "101091018"
                    },
                    {
                        "district": "复兴",
                        "stationid": "101091019"
                    }
                ]
            },
            {
                "city": "秦皇岛",
                "disList": [
                    {
                        "district": "秦皇岛",
                        "stationid": "101091101"
                    },
                    {
                        "district": "青龙",
                        "stationid": "101091102"
                    },
                    {
                        "district": "昌黎",
                        "stationid": "101091103"
                    },
                    {
                        "district": "抚宁",
                        "stationid": "101091104"
                    },
                    {
                        "district": "卢龙",
                        "stationid": "101091105"
                    },
                    {
                        "district": "北戴河",
                        "stationid": "101091106"
                    },
                    {
                        "district": "海港",
                        "stationid": "101091107"
                    },
                    {
                        "district": "山海关",
                        "stationid": "101091108"
                    }
                ]
            },
            {
                "city": "雄安新区",
                "disList": [
                    {
                        "district": "雄安新区",
                        "stationid": "101091201"
                    },
                    {
                        "district": "容城",
                        "stationid": "101091202"
                    },
                    {
                        "district": "安新",
                        "stationid": "101091203"
                    },
                    {
                        "district": "雄县",
                        "stationid": "101091204"
                    }
                ]
            }
        ]
    },
    {
        "province": "山西",
        "cityList": [
            {
                "city": "太原",
                "disList": [
                    {
                        "district": "太原",
                        "stationid": "101100101"
                    },
                    {
                        "district": "清徐",
                        "stationid": "101100102"
                    },
                    {
                        "district": "阳曲",
                        "stationid": "101100103"
                    },
                    {
                        "district": "娄烦",
                        "stationid": "101100104"
                    },
                    {
                        "district": "古交",
                        "stationid": "101100105"
                    },
                    {
                        "district": "尖草坪区",
                        "stationid": "101100106"
                    },
                    {
                        "district": "小店区",
                        "stationid": "101100107"
                    },
                    {
                        "district": "迎泽",
                        "stationid": "101100108"
                    },
                    {
                        "district": "杏花岭",
                        "stationid": "101100109"
                    },
                    {
                        "district": "万柏林",
                        "stationid": "101100110"
                    },
                    {
                        "district": "晋源",
                        "stationid": "101100111"
                    }
                ]
            },
            {
                "city": "大同",
                "disList": [
                    {
                        "district": "大同",
                        "stationid": "101100201"
                    },
                    {
                        "district": "阳高",
                        "stationid": "101100202"
                    },
                    {
                        "district": "大同县",
                        "stationid": "101100203"
                    },
                    {
                        "district": "天镇",
                        "stationid": "101100204"
                    },
                    {
                        "district": "广灵",
                        "stationid": "101100205"
                    },
                    {
                        "district": "灵丘",
                        "stationid": "101100206"
                    },
                    {
                        "district": "浑源",
                        "stationid": "101100207"
                    },
                    {
                        "district": "左云",
                        "stationid": "101100208"
                    },
                    {
                        "district": "矿区",
                        "stationid": "101100209"
                    },
                    {
                        "district": "南郊",
                        "stationid": "101100210"
                    },
                    {
                        "district": "新荣",
                        "stationid": "101100211"
                    }
                ]
            },
            {
                "city": "阳泉",
                "disList": [
                    {
                        "district": "阳泉",
                        "stationid": "101100301"
                    },
                    {
                        "district": "盂县",
                        "stationid": "101100302"
                    },
                    {
                        "district": "平定",
                        "stationid": "101100303"
                    },
                    {
                        "district": "矿区",
                        "stationid": "101100304"
                    },
                    {
                        "district": "郊区",
                        "stationid": "101100305"
                    }
                ]
            },
            {
                "city": "晋中",
                "disList": [
                    {
                        "district": "晋中",
                        "stationid": "101100401"
                    },
                    {
                        "district": "榆次",
                        "stationid": "101100402"
                    },
                    {
                        "district": "榆社",
                        "stationid": "101100403"
                    },
                    {
                        "district": "左权",
                        "stationid": "101100404"
                    },
                    {
                        "district": "和顺",
                        "stationid": "101100405"
                    },
                    {
                        "district": "昔阳",
                        "stationid": "101100406"
                    },
                    {
                        "district": "寿阳",
                        "stationid": "101100407"
                    },
                    {
                        "district": "太谷",
                        "stationid": "101100408"
                    },
                    {
                        "district": "祁县",
                        "stationid": "101100409"
                    },
                    {
                        "district": "平遥",
                        "stationid": "101100410"
                    },
                    {
                        "district": "灵石",
                        "stationid": "101100411"
                    },
                    {
                        "district": "介休",
                        "stationid": "101100412"
                    }
                ]
            },
            {
                "city": "长治",
                "disList": [
                    {
                        "district": "长治",
                        "stationid": "101100501"
                    },
                    {
                        "district": "黎城",
                        "stationid": "101100502"
                    },
                    {
                        "district": "屯留",
                        "stationid": "101100503"
                    },
                    {
                        "district": "潞城",
                        "stationid": "101100504"
                    },
                    {
                        "district": "襄垣",
                        "stationid": "101100505"
                    },
                    {
                        "district": "平顺",
                        "stationid": "101100506"
                    },
                    {
                        "district": "武乡",
                        "stationid": "101100507"
                    },
                    {
                        "district": "沁县",
                        "stationid": "101100508"
                    },
                    {
                        "district": "长子",
                        "stationid": "101100509"
                    },
                    {
                        "district": "沁源",
                        "stationid": "101100510"
                    },
                    {
                        "district": "壶关",
                        "stationid": "101100511"
                    },
                    {
                        "district": "郊区",
                        "stationid": "101100512"
                    }
                ]
            },
            {
                "city": "晋城",
                "disList": [
                    {
                        "district": "晋城",
                        "stationid": "101100601"
                    },
                    {
                        "district": "沁水",
                        "stationid": "101100602"
                    },
                    {
                        "district": "阳城",
                        "stationid": "101100603"
                    },
                    {
                        "district": "陵川",
                        "stationid": "101100604"
                    },
                    {
                        "district": "高平",
                        "stationid": "101100605"
                    },
                    {
                        "district": "泽州",
                        "stationid": "101100606"
                    }
                ]
            },
            {
                "city": "临汾",
                "disList": [
                    {
                        "district": "临汾",
                        "stationid": "101100701"
                    },
                    {
                        "district": "曲沃",
                        "stationid": "101100702"
                    },
                    {
                        "district": "永和",
                        "stationid": "101100703"
                    },
                    {
                        "district": "隰县",
                        "stationid": "101100704"
                    },
                    {
                        "district": "大宁",
                        "stationid": "101100705"
                    },
                    {
                        "district": "吉县",
                        "stationid": "101100706"
                    },
                    {
                        "district": "襄汾",
                        "stationid": "101100707"
                    },
                    {
                        "district": "蒲县",
                        "stationid": "101100708"
                    },
                    {
                        "district": "汾西",
                        "stationid": "101100709"
                    },
                    {
                        "district": "洪洞",
                        "stationid": "101100710"
                    },
                    {
                        "district": "霍州",
                        "stationid": "101100711"
                    },
                    {
                        "district": "乡宁",
                        "stationid": "101100712"
                    },
                    {
                        "district": "翼城",
                        "stationid": "101100713"
                    },
                    {
                        "district": "侯马",
                        "stationid": "101100714"
                    },
                    {
                        "district": "浮山",
                        "stationid": "101100715"
                    },
                    {
                        "district": "安泽",
                        "stationid": "101100716"
                    },
                    {
                        "district": "古县",
                        "stationid": "101100717"
                    },
                    {
                        "district": "尧都",
                        "stationid": "101100718"
                    }
                ]
            },
            {
                "city": "运城",
                "disList": [
                    {
                        "district": "运城",
                        "stationid": "101100801"
                    },
                    {
                        "district": "临猗",
                        "stationid": "101100802"
                    },
                    {
                        "district": "稷山",
                        "stationid": "101100803"
                    },
                    {
                        "district": "万荣",
                        "stationid": "101100804"
                    },
                    {
                        "district": "河津",
                        "stationid": "101100805"
                    },
                    {
                        "district": "新绛",
                        "stationid": "101100806"
                    },
                    {
                        "district": "绛县",
                        "stationid": "101100807"
                    },
                    {
                        "district": "闻喜",
                        "stationid": "101100808"
                    },
                    {
                        "district": "垣曲",
                        "stationid": "101100809"
                    },
                    {
                        "district": "永济",
                        "stationid": "101100810"
                    },
                    {
                        "district": "芮城",
                        "stationid": "101100811"
                    },
                    {
                        "district": "夏县",
                        "stationid": "101100812"
                    },
                    {
                        "district": "平陆",
                        "stationid": "101100813"
                    },
                    {
                        "district": "盐湖",
                        "stationid": "101100814"
                    }
                ]
            },
            {
                "city": "朔州",
                "disList": [
                    {
                        "district": "朔州",
                        "stationid": "101100901"
                    },
                    {
                        "district": "平鲁",
                        "stationid": "101100902"
                    },
                    {
                        "district": "山阴",
                        "stationid": "101100903"
                    },
                    {
                        "district": "右玉",
                        "stationid": "101100904"
                    },
                    {
                        "district": "应县",
                        "stationid": "101100905"
                    },
                    {
                        "district": "怀仁",
                        "stationid": "101100906"
                    },
                    {
                        "district": "朔城",
                        "stationid": "101100907"
                    }
                ]
            },
            {
                "city": "忻州",
                "disList": [
                    {
                        "district": "忻州",
                        "stationid": "101101001"
                    },
                    {
                        "district": "定襄",
                        "stationid": "101101002"
                    },
                    {
                        "district": "五台县",
                        "stationid": "101101003"
                    },
                    {
                        "district": "河曲",
                        "stationid": "101101004"
                    },
                    {
                        "district": "偏关",
                        "stationid": "101101005"
                    },
                    {
                        "district": "神池",
                        "stationid": "101101006"
                    },
                    {
                        "district": "宁武",
                        "stationid": "101101007"
                    },
                    {
                        "district": "代县",
                        "stationid": "101101008"
                    },
                    {
                        "district": "繁峙",
                        "stationid": "101101009"
                    },
                    {
                        "district": "保德",
                        "stationid": "101101011"
                    },
                    {
                        "district": "静乐",
                        "stationid": "101101012"
                    },
                    {
                        "district": "岢岚",
                        "stationid": "101101013"
                    },
                    {
                        "district": "五寨",
                        "stationid": "101101014"
                    },
                    {
                        "district": "原平",
                        "stationid": "101101015"
                    },
                    {
                        "district": "忻府",
                        "stationid": "101101016"
                    },
                    {
                        "district": "五台山",
                        "stationid": "101101010"
                    }
                ]
            },
            {
                "city": "吕梁",
                "disList": [
                    {
                        "district": "吕梁",
                        "stationid": "101101100"
                    },
                    {
                        "district": "离石",
                        "stationid": "101101101"
                    },
                    {
                        "district": "临县",
                        "stationid": "101101102"
                    },
                    {
                        "district": "兴县",
                        "stationid": "101101103"
                    },
                    {
                        "district": "岚县",
                        "stationid": "101101104"
                    },
                    {
                        "district": "柳林",
                        "stationid": "101101105"
                    },
                    {
                        "district": "石楼",
                        "stationid": "101101106"
                    },
                    {
                        "district": "方山",
                        "stationid": "101101107"
                    },
                    {
                        "district": "交口",
                        "stationid": "101101108"
                    },
                    {
                        "district": "中阳",
                        "stationid": "101101109"
                    },
                    {
                        "district": "孝义",
                        "stationid": "101101110"
                    },
                    {
                        "district": "汾阳",
                        "stationid": "101101111"
                    },
                    {
                        "district": "文水",
                        "stationid": "101101112"
                    },
                    {
                        "district": "交城",
                        "stationid": "101101113"
                    }
                ]
            }
        ]
    },
    {
        "province": "陕西",
        "cityList": [
            {
                "city": "西安",
                "disList": [
                    {
                        "district": "西安",
                        "stationid": "101110101"
                    },
                    {
                        "district": "长安",
                        "stationid": "101110102"
                    },
                    {
                        "district": "临潼",
                        "stationid": "101110103"
                    },
                    {
                        "district": "蓝田",
                        "stationid": "101110104"
                    },
                    {
                        "district": "周至",
                        "stationid": "101110105"
                    },
                    {
                        "district": "高陵",
                        "stationid": "101110107"
                    },
                    {
                        "district": "新城",
                        "stationid": "101110108"
                    },
                    {
                        "district": "碑林",
                        "stationid": "101110109"
                    },
                    {
                        "district": "莲湖",
                        "stationid": "101110110"
                    },
                    {
                        "district": "灞桥",
                        "stationid": "101110111"
                    },
                    {
                        "district": "未央",
                        "stationid": "101110112"
                    },
                    {
                        "district": "雁塔",
                        "stationid": "101110113"
                    },
                    {
                        "district": "阎良",
                        "stationid": "101110114"
                    },
                    {
                        "district": "鄠邑",
                        "stationid": "101110106"
                    }
                ]
            },
            {
                "city": "咸阳",
                "disList": [
                    {
                        "district": "咸阳",
                        "stationid": "101110200"
                    },
                    {
                        "district": "三原",
                        "stationid": "101110201"
                    },
                    {
                        "district": "礼泉",
                        "stationid": "101110202"
                    },
                    {
                        "district": "永寿",
                        "stationid": "101110203"
                    },
                    {
                        "district": "淳化",
                        "stationid": "101110204"
                    },
                    {
                        "district": "泾阳",
                        "stationid": "101110205"
                    },
                    {
                        "district": "武功",
                        "stationid": "101110206"
                    },
                    {
                        "district": "乾县",
                        "stationid": "101110207"
                    },
                    {
                        "district": "彬县",
                        "stationid": "101110208"
                    },
                    {
                        "district": "长武",
                        "stationid": "101110209"
                    },
                    {
                        "district": "旬邑",
                        "stationid": "101110210"
                    },
                    {
                        "district": "兴平",
                        "stationid": "101110211"
                    },
                    {
                        "district": "秦都",
                        "stationid": "101110212"
                    },
                    {
                        "district": "渭城",
                        "stationid": "101110213"
                    }
                ]
            },
            {
                "city": "延安",
                "disList": [
                    {
                        "district": "延安",
                        "stationid": "101110300"
                    },
                    {
                        "district": "延长",
                        "stationid": "101110301"
                    },
                    {
                        "district": "延川",
                        "stationid": "101110302"
                    },
                    {
                        "district": "子长",
                        "stationid": "101110303"
                    },
                    {
                        "district": "宜川",
                        "stationid": "101110304"
                    },
                    {
                        "district": "富县",
                        "stationid": "101110305"
                    },
                    {
                        "district": "志丹",
                        "stationid": "101110306"
                    },
                    {
                        "district": "安塞",
                        "stationid": "101110307"
                    },
                    {
                        "district": "甘泉",
                        "stationid": "101110308"
                    },
                    {
                        "district": "洛川",
                        "stationid": "101110309"
                    },
                    {
                        "district": "黄陵",
                        "stationid": "101110310"
                    },
                    {
                        "district": "黄龙",
                        "stationid": "101110311"
                    },
                    {
                        "district": "吴起",
                        "stationid": "101110312"
                    },
                    {
                        "district": "宝塔",
                        "stationid": "101110313"
                    }
                ]
            },
            {
                "city": "榆林",
                "disList": [
                    {
                        "district": "榆林",
                        "stationid": "101110401"
                    },
                    {
                        "district": "府谷",
                        "stationid": "101110402"
                    },
                    {
                        "district": "神木",
                        "stationid": "101110403"
                    },
                    {
                        "district": "佳县",
                        "stationid": "101110404"
                    },
                    {
                        "district": "定边",
                        "stationid": "101110405"
                    },
                    {
                        "district": "靖边",
                        "stationid": "101110406"
                    },
                    {
                        "district": "横山",
                        "stationid": "101110407"
                    },
                    {
                        "district": "米脂",
                        "stationid": "101110408"
                    },
                    {
                        "district": "子洲",
                        "stationid": "101110409"
                    },
                    {
                        "district": "绥德",
                        "stationid": "101110410"
                    },
                    {
                        "district": "吴堡",
                        "stationid": "101110411"
                    },
                    {
                        "district": "清涧",
                        "stationid": "101110412"
                    },
                    {
                        "district": "榆阳",
                        "stationid": "101110413"
                    }
                ]
            },
            {
                "city": "渭南",
                "disList": [
                    {
                        "district": "渭南",
                        "stationid": "101110501"
                    },
                    {
                        "district": "潼关",
                        "stationid": "101110503"
                    },
                    {
                        "district": "大荔",
                        "stationid": "101110504"
                    },
                    {
                        "district": "白水",
                        "stationid": "101110505"
                    },
                    {
                        "district": "富平",
                        "stationid": "101110506"
                    },
                    {
                        "district": "蒲城",
                        "stationid": "101110507"
                    },
                    {
                        "district": "澄城",
                        "stationid": "101110508"
                    },
                    {
                        "district": "合阳",
                        "stationid": "101110509"
                    },
                    {
                        "district": "韩城",
                        "stationid": "101110510"
                    },
                    {
                        "district": "华阴",
                        "stationid": "101110511"
                    },
                    {
                        "district": "临渭",
                        "stationid": "101110512"
                    },
                    {
                        "district": "华州",
                        "stationid": "101110513"
                    }
                ]
            },
            {
                "city": "商洛",
                "disList": [
                    {
                        "district": "商洛",
                        "stationid": "101110601"
                    },
                    {
                        "district": "洛南",
                        "stationid": "101110602"
                    },
                    {
                        "district": "柞水",
                        "stationid": "101110603"
                    },
                    {
                        "district": "商州",
                        "stationid": "101110604"
                    },
                    {
                        "district": "镇安",
                        "stationid": "101110605"
                    },
                    {
                        "district": "丹凤",
                        "stationid": "101110606"
                    },
                    {
                        "district": "商南",
                        "stationid": "101110607"
                    },
                    {
                        "district": "山阳",
                        "stationid": "101110608"
                    }
                ]
            },
            {
                "city": "安康",
                "disList": [
                    {
                        "district": "安康",
                        "stationid": "101110701"
                    },
                    {
                        "district": "紫阳",
                        "stationid": "101110702"
                    },
                    {
                        "district": "石泉",
                        "stationid": "101110703"
                    },
                    {
                        "district": "汉阴",
                        "stationid": "101110704"
                    },
                    {
                        "district": "旬阳",
                        "stationid": "101110705"
                    },
                    {
                        "district": "岚皋",
                        "stationid": "101110706"
                    },
                    {
                        "district": "平利",
                        "stationid": "101110707"
                    },
                    {
                        "district": "白河",
                        "stationid": "101110708"
                    },
                    {
                        "district": "镇坪",
                        "stationid": "101110709"
                    },
                    {
                        "district": "宁陕",
                        "stationid": "101110710"
                    },
                    {
                        "district": "汉滨",
                        "stationid": "101110711"
                    }
                ]
            },
            {
                "city": "汉中",
                "disList": [
                    {
                        "district": "汉中",
                        "stationid": "101110801"
                    },
                    {
                        "district": "略阳",
                        "stationid": "101110802"
                    },
                    {
                        "district": "勉县",
                        "stationid": "101110803"
                    },
                    {
                        "district": "留坝",
                        "stationid": "101110804"
                    },
                    {
                        "district": "洋县",
                        "stationid": "101110805"
                    },
                    {
                        "district": "城固",
                        "stationid": "101110806"
                    },
                    {
                        "district": "西乡",
                        "stationid": "101110807"
                    },
                    {
                        "district": "佛坪",
                        "stationid": "101110808"
                    },
                    {
                        "district": "宁强",
                        "stationid": "101110809"
                    },
                    {
                        "district": "南郑",
                        "stationid": "101110810"
                    },
                    {
                        "district": "镇巴",
                        "stationid": "101110811"
                    },
                    {
                        "district": "汉台",
                        "stationid": "101110812"
                    }
                ]
            },
            {
                "city": "宝鸡",
                "disList": [
                    {
                        "district": "宝鸡",
                        "stationid": "101110901"
                    },
                    {
                        "district": "渭滨",
                        "stationid": "101110902"
                    },
                    {
                        "district": "千阳",
                        "stationid": "101110903"
                    },
                    {
                        "district": "麟游",
                        "stationid": "101110904"
                    },
                    {
                        "district": "岐山",
                        "stationid": "101110905"
                    },
                    {
                        "district": "凤翔",
                        "stationid": "101110906"
                    },
                    {
                        "district": "扶风",
                        "stationid": "101110907"
                    },
                    {
                        "district": "眉县",
                        "stationid": "101110908"
                    },
                    {
                        "district": "太白",
                        "stationid": "101110909"
                    },
                    {
                        "district": "凤县",
                        "stationid": "101110910"
                    },
                    {
                        "district": "陇县",
                        "stationid": "101110911"
                    },
                    {
                        "district": "陈仓",
                        "stationid": "101110912"
                    },
                    {
                        "district": "金台",
                        "stationid": "101110913"
                    }
                ]
            },
            {
                "city": "铜川",
                "disList": [
                    {
                        "district": "铜川",
                        "stationid": "101111001"
                    },
                    {
                        "district": "宜君",
                        "stationid": "101111003"
                    },
                    {
                        "district": "耀州",
                        "stationid": "101111004"
                    },
                    {
                        "district": "王益",
                        "stationid": "101111005"
                    },
                    {
                        "district": "印台",
                        "stationid": "101111006"
                    }
                ]
            },
            {
                "city": "杨凌",
                "disList": [
                    {
                        "district": "杨凌",
                        "stationid": "101111101"
                    },
                    {
                        "district": "杨陵",
                        "stationid": "101111102"
                    }
                ]
            }
        ]
    },
    {
        "province": "山东",
        "cityList": [
            {
                "city": "济南",
                "disList": [
                    {
                        "district": "济南",
                        "stationid": "101120101"
                    },
                    {
                        "district": "长清",
                        "stationid": "101120102"
                    },
                    {
                        "district": "商河",
                        "stationid": "101120103"
                    },
                    {
                        "district": "章丘",
                        "stationid": "101120104"
                    },
                    {
                        "district": "平阴",
                        "stationid": "101120105"
                    },
                    {
                        "district": "济阳",
                        "stationid": "101120106"
                    },
                    {
                        "district": "历下",
                        "stationid": "101120107"
                    },
                    {
                        "district": "市中",
                        "stationid": "101120108"
                    },
                    {
                        "district": "槐荫",
                        "stationid": "101120109"
                    },
                    {
                        "district": "天桥",
                        "stationid": "101120110"
                    },
                    {
                        "district": "历城",
                        "stationid": "101120111"
                    }
                ]
            },
            {
                "city": "青岛",
                "disList": [
                    {
                        "district": "青岛",
                        "stationid": "101120201"
                    },
                    {
                        "district": "崂山",
                        "stationid": "101120202"
                    },
                    {
                        "district": "市南",
                        "stationid": "101120203"
                    },
                    {
                        "district": "即墨",
                        "stationid": "101120204"
                    },
                    {
                        "district": "胶州",
                        "stationid": "101120205"
                    },
                    {
                        "district": "黄岛",
                        "stationid": "101120206"
                    },
                    {
                        "district": "莱西",
                        "stationid": "101120207"
                    },
                    {
                        "district": "平度",
                        "stationid": "101120208"
                    },
                    {
                        "district": "市北",
                        "stationid": "101120209"
                    },
                    {
                        "district": "李沧",
                        "stationid": "101120210"
                    },
                    {
                        "district": "城阳",
                        "stationid": "101120211"
                    }
                ]
            },
            {
                "city": "淄博",
                "disList": [
                    {
                        "district": "淄博",
                        "stationid": "101120301"
                    },
                    {
                        "district": "淄川",
                        "stationid": "101120302"
                    },
                    {
                        "district": "博山",
                        "stationid": "101120303"
                    },
                    {
                        "district": "高青",
                        "stationid": "101120304"
                    },
                    {
                        "district": "周村",
                        "stationid": "101120305"
                    },
                    {
                        "district": "沂源",
                        "stationid": "101120306"
                    },
                    {
                        "district": "桓台",
                        "stationid": "101120307"
                    },
                    {
                        "district": "临淄",
                        "stationid": "101120308"
                    },
                    {
                        "district": "张店",
                        "stationid": "101120309"
                    }
                ]
            },
            {
                "city": "德州",
                "disList": [
                    {
                        "district": "德州",
                        "stationid": "101120401"
                    },
                    {
                        "district": "武城",
                        "stationid": "101120402"
                    },
                    {
                        "district": "临邑",
                        "stationid": "101120403"
                    },
                    {
                        "district": "齐河",
                        "stationid": "101120405"
                    },
                    {
                        "district": "乐陵",
                        "stationid": "101120406"
                    },
                    {
                        "district": "庆云",
                        "stationid": "101120407"
                    },
                    {
                        "district": "平原",
                        "stationid": "101120408"
                    },
                    {
                        "district": "宁津",
                        "stationid": "101120409"
                    },
                    {
                        "district": "夏津",
                        "stationid": "101120410"
                    },
                    {
                        "district": "禹城",
                        "stationid": "101120411"
                    },
                    {
                        "district": "德城",
                        "stationid": "101120412"
                    },
                    {
                        "district": "陵城",
                        "stationid": "101120413"
                    },
                    {
                        "district": "陵县",
                        "stationid": "101120404"
                    }
                ]
            },
            {
                "city": "烟台",
                "disList": [
                    {
                        "district": "烟台",
                        "stationid": "101120501"
                    },
                    {
                        "district": "莱州",
                        "stationid": "101120502"
                    },
                    {
                        "district": "长岛",
                        "stationid": "101120503"
                    },
                    {
                        "district": "蓬莱",
                        "stationid": "101120504"
                    },
                    {
                        "district": "龙口",
                        "stationid": "101120505"
                    },
                    {
                        "district": "招远",
                        "stationid": "101120506"
                    },
                    {
                        "district": "栖霞",
                        "stationid": "101120507"
                    },
                    {
                        "district": "福山",
                        "stationid": "101120508"
                    },
                    {
                        "district": "牟平",
                        "stationid": "101120509"
                    },
                    {
                        "district": "莱阳",
                        "stationid": "101120510"
                    },
                    {
                        "district": "海阳",
                        "stationid": "101120511"
                    },
                    {
                        "district": "芝罘",
                        "stationid": "101120512"
                    },
                    {
                        "district": "莱山",
                        "stationid": "101120513"
                    }
                ]
            },
            {
                "city": "潍坊",
                "disList": [
                    {
                        "district": "潍坊",
                        "stationid": "101120601"
                    },
                    {
                        "district": "青州",
                        "stationid": "101120602"
                    },
                    {
                        "district": "寿光",
                        "stationid": "101120603"
                    },
                    {
                        "district": "临朐",
                        "stationid": "101120604"
                    },
                    {
                        "district": "昌乐",
                        "stationid": "101120605"
                    },
                    {
                        "district": "昌邑",
                        "stationid": "101120606"
                    },
                    {
                        "district": "安丘",
                        "stationid": "101120607"
                    },
                    {
                        "district": "高密",
                        "stationid": "101120608"
                    },
                    {
                        "district": "诸城",
                        "stationid": "101120609"
                    },
                    {
                        "district": "潍城",
                        "stationid": "101120610"
                    },
                    {
                        "district": "寒亭",
                        "stationid": "101120611"
                    },
                    {
                        "district": "坊子",
                        "stationid": "101120612"
                    },
                    {
                        "district": "奎文",
                        "stationid": "101120613"
                    }
                ]
            },
            {
                "city": "济宁",
                "disList": [
                    {
                        "district": "济宁",
                        "stationid": "101120701"
                    },
                    {
                        "district": "嘉祥",
                        "stationid": "101120702"
                    },
                    {
                        "district": "微山",
                        "stationid": "101120703"
                    },
                    {
                        "district": "鱼台",
                        "stationid": "101120704"
                    },
                    {
                        "district": "兖州",
                        "stationid": "101120705"
                    },
                    {
                        "district": "金乡",
                        "stationid": "101120706"
                    },
                    {
                        "district": "汶上",
                        "stationid": "101120707"
                    },
                    {
                        "district": "泗水",
                        "stationid": "101120708"
                    },
                    {
                        "district": "梁山",
                        "stationid": "101120709"
                    },
                    {
                        "district": "曲阜",
                        "stationid": "101120710"
                    },
                    {
                        "district": "邹城",
                        "stationid": "101120711"
                    },
                    {
                        "district": "任城",
                        "stationid": "101120712"
                    }
                ]
            },
            {
                "city": "泰安",
                "disList": [
                    {
                        "district": "泰安",
                        "stationid": "101120801"
                    },
                    {
                        "district": "新泰",
                        "stationid": "101120802"
                    },
                    {
                        "district": "泰山",
                        "stationid": "101120803"
                    },
                    {
                        "district": "肥城",
                        "stationid": "101120804"
                    },
                    {
                        "district": "东平",
                        "stationid": "101120805"
                    },
                    {
                        "district": "宁阳",
                        "stationid": "101120806"
                    },
                    {
                        "district": "岱岳",
                        "stationid": "101120807"
                    }
                ]
            },
            {
                "city": "临沂",
                "disList": [
                    {
                        "district": "临沂",
                        "stationid": "101120901"
                    },
                    {
                        "district": "莒南",
                        "stationid": "101120902"
                    },
                    {
                        "district": "沂南",
                        "stationid": "101120903"
                    },
                    {
                        "district": "兰陵",
                        "stationid": "101120904"
                    },
                    {
                        "district": "临沭",
                        "stationid": "101120905"
                    },
                    {
                        "district": "郯城",
                        "stationid": "101120906"
                    },
                    {
                        "district": "蒙阴",
                        "stationid": "101120907"
                    },
                    {
                        "district": "平邑",
                        "stationid": "101120908"
                    },
                    {
                        "district": "费县",
                        "stationid": "101120909"
                    },
                    {
                        "district": "沂水",
                        "stationid": "101120910"
                    },
                    {
                        "district": "兰山",
                        "stationid": "101120911"
                    },
                    {
                        "district": "罗庄",
                        "stationid": "101120912"
                    },
                    {
                        "district": "河东",
                        "stationid": "101120913"
                    }
                ]
            },
            {
                "city": "菏泽",
                "disList": [
                    {
                        "district": "菏泽",
                        "stationid": "101121001"
                    },
                    {
                        "district": "鄄城",
                        "stationid": "101121002"
                    },
                    {
                        "district": "郓城",
                        "stationid": "101121003"
                    },
                    {
                        "district": "东明",
                        "stationid": "101121004"
                    },
                    {
                        "district": "定陶",
                        "stationid": "101121005"
                    },
                    {
                        "district": "巨野",
                        "stationid": "101121006"
                    },
                    {
                        "district": "曹县",
                        "stationid": "101121007"
                    },
                    {
                        "district": "成武",
                        "stationid": "101121008"
                    },
                    {
                        "district": "单县",
                        "stationid": "101121009"
                    },
                    {
                        "district": "牡丹",
                        "stationid": "101121010"
                    }
                ]
            },
            {
                "city": "滨州",
                "disList": [
                    {
                        "district": "滨州",
                        "stationid": "101121101"
                    },
                    {
                        "district": "博兴",
                        "stationid": "101121102"
                    },
                    {
                        "district": "无棣",
                        "stationid": "101121103"
                    },
                    {
                        "district": "阳信",
                        "stationid": "101121104"
                    },
                    {
                        "district": "惠民",
                        "stationid": "101121105"
                    },
                    {
                        "district": "沾化",
                        "stationid": "101121106"
                    },
                    {
                        "district": "邹平",
                        "stationid": "101121107"
                    },
                    {
                        "district": "滨城",
                        "stationid": "101121108"
                    }
                ]
            },
            {
                "city": "东营",
                "disList": [
                    {
                        "district": "东营",
                        "stationid": "101121201"
                    },
                    {
                        "district": "河口",
                        "stationid": "101121202"
                    },
                    {
                        "district": "垦利",
                        "stationid": "101121203"
                    },
                    {
                        "district": "利津",
                        "stationid": "101121204"
                    },
                    {
                        "district": "广饶",
                        "stationid": "101121205"
                    }
                ]
            },
            {
                "city": "威海",
                "disList": [
                    {
                        "district": "威海",
                        "stationid": "101121301"
                    },
                    {
                        "district": "文登",
                        "stationid": "101121302"
                    },
                    {
                        "district": "荣成",
                        "stationid": "101121303"
                    },
                    {
                        "district": "乳山",
                        "stationid": "101121304"
                    },
                    {
                        "district": "环翠",
                        "stationid": "101121307"
                    },
                    {
                        "district": "成山头",
                        "stationid": "101121305"
                    },
                    {
                        "district": "石岛",
                        "stationid": "101121306"
                    }
                ]
            },
            {
                "city": "枣庄",
                "disList": [
                    {
                        "district": "枣庄",
                        "stationid": "101121401"
                    },
                    {
                        "district": "薛城",
                        "stationid": "101121402"
                    },
                    {
                        "district": "峄城",
                        "stationid": "101121403"
                    },
                    {
                        "district": "台儿庄",
                        "stationid": "101121404"
                    },
                    {
                        "district": "滕州",
                        "stationid": "101121405"
                    },
                    {
                        "district": "市中",
                        "stationid": "101121406"
                    },
                    {
                        "district": "山亭",
                        "stationid": "101121407"
                    }
                ]
            },
            {
                "city": "日照",
                "disList": [
                    {
                        "district": "日照",
                        "stationid": "101121501"
                    },
                    {
                        "district": "五莲",
                        "stationid": "101121502"
                    },
                    {
                        "district": "莒县",
                        "stationid": "101121503"
                    },
                    {
                        "district": "东港",
                        "stationid": "101121504"
                    },
                    {
                        "district": "岚山",
                        "stationid": "101121505"
                    }
                ]
            },
            {
                "city": "莱芜",
                "disList": [
                    {
                        "district": "莱芜",
                        "stationid": "101121601"
                    },
                    {
                        "district": "莱城",
                        "stationid": "101121602"
                    },
                    {
                        "district": "钢城",
                        "stationid": "101121603"
                    }
                ]
            },
            {
                "city": "聊城",
                "disList": [
                    {
                        "district": "聊城",
                        "stationid": "101121701"
                    },
                    {
                        "district": "冠县",
                        "stationid": "101121702"
                    },
                    {
                        "district": "阳谷",
                        "stationid": "101121703"
                    },
                    {
                        "district": "高唐",
                        "stationid": "101121704"
                    },
                    {
                        "district": "茌平",
                        "stationid": "101121705"
                    },
                    {
                        "district": "东阿",
                        "stationid": "101121706"
                    },
                    {
                        "district": "临清",
                        "stationid": "101121707"
                    },
                    {
                        "district": "东昌府",
                        "stationid": "101121708"
                    },
                    {
                        "district": "莘县",
                        "stationid": "101121709"
                    }
                ]
            }
        ]
    },
    {
        "province": "新疆",
        "cityList": [
            {
                "city": "乌鲁木齐",
                "disList": [
                    {
                        "district": "乌鲁木齐",
                        "stationid": "101130101"
                    },
                    {
                        "district": "天山",
                        "stationid": "101130102"
                    },
                    {
                        "district": "沙依巴克",
                        "stationid": "101130104"
                    },
                    {
                        "district": "达坂城",
                        "stationid": "101130105"
                    },
                    {
                        "district": "新市",
                        "stationid": "101130106"
                    },
                    {
                        "district": "水磨沟",
                        "stationid": "101130107"
                    },
                    {
                        "district": "头屯河",
                        "stationid": "101130111"
                    },
                    {
                        "district": "米东",
                        "stationid": "101130112"
                    },
                    {
                        "district": "乌鲁木齐县",
                        "stationid": "101130113"
                    },
                    {
                        "district": "西白杨沟",
                        "stationid": "101130114"
                    },
                    {
                        "district": "小渠子",
                        "stationid": "101130103"
                    },
                    {
                        "district": "天池",
                        "stationid": "101130109"
                    }
                ]
            },
            {
                "city": "克拉玛依",
                "disList": [
                    {
                        "district": "克拉玛依",
                        "stationid": "101130201"
                    },
                    {
                        "district": "乌尔禾",
                        "stationid": "101130202"
                    },
                    {
                        "district": "白碱滩",
                        "stationid": "101130203"
                    },
                    {
                        "district": "独山子",
                        "stationid": "101130204"
                    }
                ]
            },
            {
                "city": "石河子",
                "disList": [
                    {
                        "district": "石河子",
                        "stationid": "101130301"
                    },
                    {
                        "district": "炮台",
                        "stationid": "101130302"
                    },
                    {
                        "district": "莫索湾",
                        "stationid": "101130303"
                    }
                ]
            },
            {
                "city": "昌吉",
                "disList": [
                    {
                        "district": "昌吉",
                        "stationid": "101130401"
                    },
                    {
                        "district": "呼图壁",
                        "stationid": "101130402"
                    },
                    {
                        "district": "阜康",
                        "stationid": "101130404"
                    },
                    {
                        "district": "吉木萨尔",
                        "stationid": "101130405"
                    },
                    {
                        "district": "奇台",
                        "stationid": "101130406"
                    },
                    {
                        "district": "玛纳斯",
                        "stationid": "101130407"
                    },
                    {
                        "district": "木垒",
                        "stationid": "101130408"
                    },
                    {
                        "district": "蔡家湖",
                        "stationid": "101130409"
                    }
                ]
            },
            {
                "city": "吐鲁番",
                "disList": [
                    {
                        "district": "吐鲁番",
                        "stationid": "101130501"
                    },
                    {
                        "district": "托克逊",
                        "stationid": "101130502"
                    },
                    {
                        "district": "高昌",
                        "stationid": "101130503"
                    },
                    {
                        "district": "鄯善",
                        "stationid": "101130504"
                    }
                ]
            },
            {
                "city": "巴音郭楞",
                "disList": [
                    {
                        "district": "库尔勒",
                        "stationid": "101130601"
                    },
                    {
                        "district": "轮台",
                        "stationid": "101130602"
                    },
                    {
                        "district": "尉犁",
                        "stationid": "101130603"
                    },
                    {
                        "district": "若羌",
                        "stationid": "101130604"
                    },
                    {
                        "district": "且末",
                        "stationid": "101130605"
                    },
                    {
                        "district": "和静",
                        "stationid": "101130606"
                    },
                    {
                        "district": "焉耆",
                        "stationid": "101130607"
                    },
                    {
                        "district": "和硕",
                        "stationid": "101130608"
                    },
                    {
                        "district": "巴音郭楞",
                        "stationid": "101130609"
                    },
                    {
                        "district": "博湖",
                        "stationid": "101130612"
                    },
                    {
                        "district": "巴音布鲁克",
                        "stationid": "101130610"
                    },
                    {
                        "district": "铁干里克",
                        "stationid": "101130611"
                    },
                    {
                        "district": "塔中",
                        "stationid": "101130613"
                    },
                    {
                        "district": "巴仑台",
                        "stationid": "101130614"
                    }
                ]
            },
            {
                "city": "阿拉尔",
                "disList": [
                    {
                        "district": "阿拉尔",
                        "stationid": "101130701"
                    }
                ]
            },
            {
                "city": "阿克苏",
                "disList": [
                    {
                        "district": "阿克苏",
                        "stationid": "101130801"
                    },
                    {
                        "district": "乌什",
                        "stationid": "101130802"
                    },
                    {
                        "district": "温宿",
                        "stationid": "101130803"
                    },
                    {
                        "district": "拜城",
                        "stationid": "101130804"
                    },
                    {
                        "district": "新和",
                        "stationid": "101130805"
                    },
                    {
                        "district": "沙雅",
                        "stationid": "101130806"
                    },
                    {
                        "district": "库车",
                        "stationid": "101130807"
                    },
                    {
                        "district": "柯坪",
                        "stationid": "101130808"
                    },
                    {
                        "district": "阿瓦提",
                        "stationid": "101130809"
                    }
                ]
            },
            {
                "city": "喀什",
                "disList": [
                    {
                        "district": "喀什",
                        "stationid": "101130901"
                    },
                    {
                        "district": "英吉沙",
                        "stationid": "101130902"
                    },
                    {
                        "district": "塔什库尔干",
                        "stationid": "101130903"
                    },
                    {
                        "district": "麦盖提",
                        "stationid": "101130904"
                    },
                    {
                        "district": "莎车",
                        "stationid": "101130905"
                    },
                    {
                        "district": "叶城",
                        "stationid": "101130906"
                    },
                    {
                        "district": "泽普",
                        "stationid": "101130907"
                    },
                    {
                        "district": "巴楚",
                        "stationid": "101130908"
                    },
                    {
                        "district": "岳普湖",
                        "stationid": "101130909"
                    },
                    {
                        "district": "伽师",
                        "stationid": "101130910"
                    },
                    {
                        "district": "疏附",
                        "stationid": "101130911"
                    },
                    {
                        "district": "疏勒",
                        "stationid": "101130912"
                    }
                ]
            },
            {
                "city": "伊犁",
                "disList": [
                    {
                        "district": "伊宁",
                        "stationid": "101131001"
                    },
                    {
                        "district": "察布查尔",
                        "stationid": "101131002"
                    },
                    {
                        "district": "尼勒克",
                        "stationid": "101131003"
                    },
                    {
                        "district": "伊宁县",
                        "stationid": "101131004"
                    },
                    {
                        "district": "巩留",
                        "stationid": "101131005"
                    },
                    {
                        "district": "新源",
                        "stationid": "101131006"
                    },
                    {
                        "district": "昭苏",
                        "stationid": "101131007"
                    },
                    {
                        "district": "特克斯",
                        "stationid": "101131008"
                    },
                    {
                        "district": "霍城",
                        "stationid": "101131009"
                    },
                    {
                        "district": "霍尔果斯",
                        "stationid": "101131010"
                    },
                    {
                        "district": "奎屯",
                        "stationid": "101131011"
                    },
                    {
                        "district": "伊犁",
                        "stationid": "101131012"
                    }
                ]
            },
            {
                "city": "塔城",
                "disList": [
                    {
                        "district": "塔城",
                        "stationid": "101131101"
                    },
                    {
                        "district": "裕民",
                        "stationid": "101131102"
                    },
                    {
                        "district": "额敏",
                        "stationid": "101131103"
                    },
                    {
                        "district": "和布克赛尔",
                        "stationid": "101131104"
                    },
                    {
                        "district": "托里",
                        "stationid": "101131105"
                    },
                    {
                        "district": "乌苏",
                        "stationid": "101131106"
                    },
                    {
                        "district": "沙湾",
                        "stationid": "101131107"
                    }
                ]
            },
            {
                "city": "哈密",
                "disList": [
                    {
                        "district": "哈密",
                        "stationid": "101131201"
                    },
                    {
                        "district": "伊州",
                        "stationid": "101131202"
                    },
                    {
                        "district": "巴里坤",
                        "stationid": "101131203"
                    },
                    {
                        "district": "伊吾",
                        "stationid": "101131204"
                    }
                ]
            },
            {
                "city": "和田",
                "disList": [
                    {
                        "district": "和田",
                        "stationid": "101131301"
                    },
                    {
                        "district": "皮山",
                        "stationid": "101131302"
                    },
                    {
                        "district": "策勒",
                        "stationid": "101131303"
                    },
                    {
                        "district": "墨玉",
                        "stationid": "101131304"
                    },
                    {
                        "district": "洛浦",
                        "stationid": "101131305"
                    },
                    {
                        "district": "民丰",
                        "stationid": "101131306"
                    },
                    {
                        "district": "于田",
                        "stationid": "101131307"
                    }
                ]
            },
            {
                "city": "阿勒泰",
                "disList": [
                    {
                        "district": "阿勒泰",
                        "stationid": "101131401"
                    },
                    {
                        "district": "哈巴河",
                        "stationid": "101131402"
                    },
                    {
                        "district": "吉木乃",
                        "stationid": "101131405"
                    },
                    {
                        "district": "布尔津",
                        "stationid": "101131406"
                    },
                    {
                        "district": "福海",
                        "stationid": "101131407"
                    },
                    {
                        "district": "富蕴",
                        "stationid": "101131408"
                    },
                    {
                        "district": "青河",
                        "stationid": "101131409"
                    }
                ]
            },
            {
                "city": "克州",
                "disList": [
                    {
                        "district": "阿图什",
                        "stationid": "101131501"
                    },
                    {
                        "district": "乌恰",
                        "stationid": "101131502"
                    },
                    {
                        "district": "阿克陶",
                        "stationid": "101131503"
                    },
                    {
                        "district": "阿合奇",
                        "stationid": "101131504"
                    },
                    {
                        "district": "克州",
                        "stationid": "101131505"
                    }
                ]
            },
            {
                "city": "博尔塔拉",
                "disList": [
                    {
                        "district": "博乐",
                        "stationid": "101131601"
                    },
                    {
                        "district": "温泉",
                        "stationid": "101131602"
                    },
                    {
                        "district": "精河",
                        "stationid": "101131603"
                    },
                    {
                        "district": "博尔塔拉",
                        "stationid": "101131604"
                    },
                    {
                        "district": "阿拉山口",
                        "stationid": "101131606"
                    }
                ]
            },
            {
                "city": "图木舒克",
                "disList": [
                    {
                        "district": "图木舒克",
                        "stationid": "101131701"
                    }
                ]
            },
            {
                "city": "五家渠",
                "disList": [
                    {
                        "district": "五家渠",
                        "stationid": "101131801"
                    }
                ]
            },
            {
                "city": "铁门关",
                "disList": [
                    {
                        "district": "铁门关",
                        "stationid": "101131901"
                    }
                ]
            },
            {
                "city": "昆玉",
                "disList": [
                    {
                        "district": "昆玉",
                        "stationid": "101131920"
                    }
                ]
            },
            {
                "city": "北屯",
                "disList": [
                    {
                        "district": "北屯",
                        "stationid": "101132101"
                    }
                ]
            },
            {
                "city": "双河",
                "disList": [
                    {
                        "district": "双河",
                        "stationid": "101132201"
                    }
                ]
            },
            {
                "city": "可克达拉",
                "disList": [
                    {
                        "district": "可克达拉",
                        "stationid": "101132301"
                    }
                ]
            }
        ]
    },
    {
        "province": "西藏",
        "cityList": [
            {
                "city": "拉萨",
                "disList": [
                    {
                        "district": "拉萨",
                        "stationid": "101140101"
                    },
                    {
                        "district": "当雄",
                        "stationid": "101140102"
                    },
                    {
                        "district": "尼木",
                        "stationid": "101140103"
                    },
                    {
                        "district": "林周",
                        "stationid": "101140104"
                    },
                    {
                        "district": "堆龙德庆",
                        "stationid": "101140105"
                    },
                    {
                        "district": "曲水",
                        "stationid": "101140106"
                    },
                    {
                        "district": "达孜",
                        "stationid": "101140107"
                    },
                    {
                        "district": "墨竹工卡",
                        "stationid": "101140108"
                    },
                    {
                        "district": "城关",
                        "stationid": "101140109"
                    }
                ]
            },
            {
                "city": "日喀则",
                "disList": [
                    {
                        "district": "日喀则",
                        "stationid": "101140201"
                    },
                    {
                        "district": "拉孜",
                        "stationid": "101140202"
                    },
                    {
                        "district": "南木林",
                        "stationid": "101140203"
                    },
                    {
                        "district": "聂拉木",
                        "stationid": "101140204"
                    },
                    {
                        "district": "定日",
                        "stationid": "101140205"
                    },
                    {
                        "district": "江孜",
                        "stationid": "101140206"
                    },
                    {
                        "district": "仲巴",
                        "stationid": "101140208"
                    },
                    {
                        "district": "萨嘎",
                        "stationid": "101140209"
                    },
                    {
                        "district": "吉隆",
                        "stationid": "101140210"
                    },
                    {
                        "district": "昂仁",
                        "stationid": "101140211"
                    },
                    {
                        "district": "定结",
                        "stationid": "101140212"
                    },
                    {
                        "district": "萨迦",
                        "stationid": "101140213"
                    },
                    {
                        "district": "谢通门",
                        "stationid": "101140214"
                    },
                    {
                        "district": "桑珠孜",
                        "stationid": "101140215"
                    },
                    {
                        "district": "岗巴",
                        "stationid": "101140216"
                    },
                    {
                        "district": "白朗",
                        "stationid": "101140217"
                    },
                    {
                        "district": "亚东",
                        "stationid": "101140218"
                    },
                    {
                        "district": "康马",
                        "stationid": "101140219"
                    },
                    {
                        "district": "仁布",
                        "stationid": "101140220"
                    },
                    {
                        "district": "帕里",
                        "stationid": "101140207"
                    }
                ]
            },
            {
                "city": "山南",
                "disList": [
                    {
                        "district": "山南",
                        "stationid": "101140301"
                    },
                    {
                        "district": "贡嘎",
                        "stationid": "101140302"
                    },
                    {
                        "district": "扎囊",
                        "stationid": "101140303"
                    },
                    {
                        "district": "加查",
                        "stationid": "101140304"
                    },
                    {
                        "district": "浪卡子",
                        "stationid": "101140305"
                    },
                    {
                        "district": "错那",
                        "stationid": "101140306"
                    },
                    {
                        "district": "隆子",
                        "stationid": "101140307"
                    },
                    {
                        "district": "乃东",
                        "stationid": "101140309"
                    },
                    {
                        "district": "桑日",
                        "stationid": "101140310"
                    },
                    {
                        "district": "洛扎",
                        "stationid": "101140311"
                    },
                    {
                        "district": "措美",
                        "stationid": "101140312"
                    },
                    {
                        "district": "琼结",
                        "stationid": "101140313"
                    },
                    {
                        "district": "曲松",
                        "stationid": "101140314"
                    },
                    {
                        "district": "泽当",
                        "stationid": "101140308"
                    }
                ]
            },
            {
                "city": "林芝",
                "disList": [
                    {
                        "district": "林芝",
                        "stationid": "101140401"
                    },
                    {
                        "district": "波密",
                        "stationid": "101140402"
                    },
                    {
                        "district": "米林",
                        "stationid": "101140403"
                    },
                    {
                        "district": "察隅",
                        "stationid": "101140404"
                    },
                    {
                        "district": "工布江达",
                        "stationid": "101140405"
                    },
                    {
                        "district": "朗县",
                        "stationid": "101140406"
                    },
                    {
                        "district": "墨脱",
                        "stationid": "101140407"
                    },
                    {
                        "district": "巴宜",
                        "stationid": "101140408"
                    }
                ]
            },
            {
                "city": "昌都",
                "disList": [
                    {
                        "district": "昌都",
                        "stationid": "101140501"
                    },
                    {
                        "district": "丁青",
                        "stationid": "101140502"
                    },
                    {
                        "district": "边坝",
                        "stationid": "101140503"
                    },
                    {
                        "district": "洛隆",
                        "stationid": "101140504"
                    },
                    {
                        "district": "左贡",
                        "stationid": "101140505"
                    },
                    {
                        "district": "芒康",
                        "stationid": "101140506"
                    },
                    {
                        "district": "类乌齐",
                        "stationid": "101140507"
                    },
                    {
                        "district": "八宿",
                        "stationid": "101140508"
                    },
                    {
                        "district": "江达",
                        "stationid": "101140509"
                    },
                    {
                        "district": "察雅",
                        "stationid": "101140510"
                    },
                    {
                        "district": "贡觉",
                        "stationid": "101140511"
                    },
                    {
                        "district": "卡若",
                        "stationid": "101140512"
                    }
                ]
            },
            {
                "city": "那曲",
                "disList": [
                    {
                        "district": "那曲",
                        "stationid": "101140601"
                    },
                    {
                        "district": "尼玛",
                        "stationid": "101140602"
                    },
                    {
                        "district": "嘉黎",
                        "stationid": "101140603"
                    },
                    {
                        "district": "班戈",
                        "stationid": "101140604"
                    },
                    {
                        "district": "安多",
                        "stationid": "101140605"
                    },
                    {
                        "district": "索县",
                        "stationid": "101140606"
                    },
                    {
                        "district": "聂荣",
                        "stationid": "101140607"
                    },
                    {
                        "district": "巴青",
                        "stationid": "101140608"
                    },
                    {
                        "district": "比如",
                        "stationid": "101140609"
                    },
                    {
                        "district": "双湖",
                        "stationid": "101140610"
                    },
                    {
                        "district": "申扎",
                        "stationid": "101140611"
                    },
                    {
                        "district": "色尼",
                        "stationid": "101140612"
                    }
                ]
            },
            {
                "city": "阿里",
                "disList": [
                    {
                        "district": "阿里",
                        "stationid": "101140701"
                    },
                    {
                        "district": "改则",
                        "stationid": "101140702"
                    },
                    {
                        "district": "普兰",
                        "stationid": "101140705"
                    },
                    {
                        "district": "札达",
                        "stationid": "101140706"
                    },
                    {
                        "district": "噶尔",
                        "stationid": "101140707"
                    },
                    {
                        "district": "日土",
                        "stationid": "101140708"
                    },
                    {
                        "district": "革吉",
                        "stationid": "101140709"
                    },
                    {
                        "district": "措勤",
                        "stationid": "101140710"
                    },
                    {
                        "district": "狮泉河",
                        "stationid": "101140704"
                    }
                ]
            }
        ]
    },
    {
        "province": "青海",
        "cityList": [
            {
                "city": "西宁",
                "disList": [
                    {
                        "district": "西宁",
                        "stationid": "101150101"
                    },
                    {
                        "district": "大通",
                        "stationid": "101150102"
                    },
                    {
                        "district": "湟源",
                        "stationid": "101150103"
                    },
                    {
                        "district": "湟中",
                        "stationid": "101150104"
                    },
                    {
                        "district": "城东",
                        "stationid": "101150105"
                    },
                    {
                        "district": "城中",
                        "stationid": "101150106"
                    },
                    {
                        "district": "城西",
                        "stationid": "101150107"
                    },
                    {
                        "district": "城北",
                        "stationid": "101150108"
                    }
                ]
            },
            {
                "city": "海东",
                "disList": [
                    {
                        "district": "平安",
                        "stationid": "101150201"
                    },
                    {
                        "district": "乐都",
                        "stationid": "101150202"
                    },
                    {
                        "district": "民和",
                        "stationid": "101150203"
                    },
                    {
                        "district": "互助",
                        "stationid": "101150204"
                    },
                    {
                        "district": "化隆",
                        "stationid": "101150205"
                    },
                    {
                        "district": "循化",
                        "stationid": "101150206"
                    },
                    {
                        "district": "海东",
                        "stationid": "101150207"
                    }
                ]
            },
            {
                "city": "黄南",
                "disList": [
                    {
                        "district": "同仁",
                        "stationid": "101150301"
                    },
                    {
                        "district": "尖扎",
                        "stationid": "101150302"
                    },
                    {
                        "district": "泽库",
                        "stationid": "101150303"
                    },
                    {
                        "district": "河南",
                        "stationid": "101150304"
                    },
                    {
                        "district": "黄南",
                        "stationid": "101150305"
                    }
                ]
            },
            {
                "city": "海南",
                "disList": [
                    {
                        "district": "共和",
                        "stationid": "101150401"
                    },
                    {
                        "district": "海南",
                        "stationid": "101150402"
                    },
                    {
                        "district": "贵德",
                        "stationid": "101150404"
                    },
                    {
                        "district": "兴海",
                        "stationid": "101150406"
                    },
                    {
                        "district": "贵南",
                        "stationid": "101150407"
                    },
                    {
                        "district": "同德",
                        "stationid": "101150408"
                    }
                ]
            },
            {
                "city": "果洛",
                "disList": [
                    {
                        "district": "玛沁",
                        "stationid": "101150501"
                    },
                    {
                        "district": "班玛",
                        "stationid": "101150502"
                    },
                    {
                        "district": "甘德",
                        "stationid": "101150503"
                    },
                    {
                        "district": "达日",
                        "stationid": "101150504"
                    },
                    {
                        "district": "久治",
                        "stationid": "101150505"
                    },
                    {
                        "district": "玛多",
                        "stationid": "101150506"
                    },
                    {
                        "district": "果洛",
                        "stationid": "101150507"
                    }
                ]
            },
            {
                "city": "玉树",
                "disList": [
                    {
                        "district": "玉树",
                        "stationid": "101150601"
                    },
                    {
                        "district": "称多",
                        "stationid": "101150602"
                    },
                    {
                        "district": "治多",
                        "stationid": "101150603"
                    },
                    {
                        "district": "杂多",
                        "stationid": "101150604"
                    },
                    {
                        "district": "囊谦",
                        "stationid": "101150605"
                    },
                    {
                        "district": "曲麻莱",
                        "stationid": "101150606"
                    }
                ]
            },
            {
                "city": "海西",
                "disList": [
                    {
                        "district": "德令哈",
                        "stationid": "101150701"
                    },
                    {
                        "district": "海西",
                        "stationid": "101150702"
                    },
                    {
                        "district": "天峻",
                        "stationid": "101150708"
                    },
                    {
                        "district": "乌兰",
                        "stationid": "101150709"
                    },
                    {
                        "district": "茫崖",
                        "stationid": "101150712"
                    },
                    {
                        "district": "大柴旦",
                        "stationid": "101150713"
                    },
                    {
                        "district": "格尔木",
                        "stationid": "101150714"
                    },
                    {
                        "district": "都兰",
                        "stationid": "101150715"
                    },
                    {
                        "district": "冷湖",
                        "stationid": "101150716"
                    }
                ]
            },
            {
                "city": "海北",
                "disList": [
                    {
                        "district": "海晏",
                        "stationid": "101150801"
                    },
                    {
                        "district": "门源",
                        "stationid": "101150802"
                    },
                    {
                        "district": "祁连",
                        "stationid": "101150803"
                    },
                    {
                        "district": "海北",
                        "stationid": "101150804"
                    },
                    {
                        "district": "刚察",
                        "stationid": "101150806"
                    }
                ]
            }
        ]
    },
    {
        "province": "甘肃",
        "cityList": [
            {
                "city": "兰州",
                "disList": [
                    {
                        "district": "兰州",
                        "stationid": "101160101"
                    },
                    {
                        "district": "皋兰",
                        "stationid": "101160102"
                    },
                    {
                        "district": "永登",
                        "stationid": "101160103"
                    },
                    {
                        "district": "榆中",
                        "stationid": "101160104"
                    },
                    {
                        "district": "城关",
                        "stationid": "101160105"
                    },
                    {
                        "district": "七里河",
                        "stationid": "101160106"
                    },
                    {
                        "district": "西固",
                        "stationid": "101160107"
                    },
                    {
                        "district": "安宁",
                        "stationid": "101160108"
                    },
                    {
                        "district": "红古",
                        "stationid": "101160109"
                    }
                ]
            },
            {
                "city": "定西",
                "disList": [
                    {
                        "district": "定西",
                        "stationid": "101160201"
                    },
                    {
                        "district": "通渭",
                        "stationid": "101160202"
                    },
                    {
                        "district": "陇西",
                        "stationid": "101160203"
                    },
                    {
                        "district": "渭源",
                        "stationid": "101160204"
                    },
                    {
                        "district": "临洮",
                        "stationid": "101160205"
                    },
                    {
                        "district": "漳县",
                        "stationid": "101160206"
                    },
                    {
                        "district": "岷县",
                        "stationid": "101160207"
                    },
                    {
                        "district": "安定",
                        "stationid": "101160208"
                    }
                ]
            },
            {
                "city": "平凉",
                "disList": [
                    {
                        "district": "平凉",
                        "stationid": "101160301"
                    },
                    {
                        "district": "泾川",
                        "stationid": "101160302"
                    },
                    {
                        "district": "灵台",
                        "stationid": "101160303"
                    },
                    {
                        "district": "崇信",
                        "stationid": "101160304"
                    },
                    {
                        "district": "华亭",
                        "stationid": "101160305"
                    },
                    {
                        "district": "庄浪",
                        "stationid": "101160306"
                    },
                    {
                        "district": "静宁",
                        "stationid": "101160307"
                    },
                    {
                        "district": "崆峒",
                        "stationid": "101160308"
                    }
                ]
            },
            {
                "city": "庆阳",
                "disList": [
                    {
                        "district": "庆阳",
                        "stationid": "101160401"
                    },
                    {
                        "district": "西峰",
                        "stationid": "101160402"
                    },
                    {
                        "district": "环县",
                        "stationid": "101160403"
                    },
                    {
                        "district": "华池",
                        "stationid": "101160404"
                    },
                    {
                        "district": "合水",
                        "stationid": "101160405"
                    },
                    {
                        "district": "正宁",
                        "stationid": "101160406"
                    },
                    {
                        "district": "宁县",
                        "stationid": "101160407"
                    },
                    {
                        "district": "镇原",
                        "stationid": "101160408"
                    },
                    {
                        "district": "庆城",
                        "stationid": "101160409"
                    }
                ]
            },
            {
                "city": "武威",
                "disList": [
                    {
                        "district": "武威",
                        "stationid": "101160501"
                    },
                    {
                        "district": "民勤",
                        "stationid": "101160502"
                    },
                    {
                        "district": "古浪",
                        "stationid": "101160503"
                    },
                    {
                        "district": "凉州",
                        "stationid": "101160504"
                    },
                    {
                        "district": "天祝",
                        "stationid": "101160505"
                    }
                ]
            },
            {
                "city": "金昌",
                "disList": [
                    {
                        "district": "金昌",
                        "stationid": "101160601"
                    },
                    {
                        "district": "永昌",
                        "stationid": "101160602"
                    },
                    {
                        "district": "金川",
                        "stationid": "101160603"
                    }
                ]
            },
            {
                "city": "张掖",
                "disList": [
                    {
                        "district": "张掖",
                        "stationid": "101160701"
                    },
                    {
                        "district": "肃南",
                        "stationid": "101160702"
                    },
                    {
                        "district": "民乐",
                        "stationid": "101160703"
                    },
                    {
                        "district": "临泽",
                        "stationid": "101160704"
                    },
                    {
                        "district": "高台",
                        "stationid": "101160705"
                    },
                    {
                        "district": "山丹",
                        "stationid": "101160706"
                    },
                    {
                        "district": "甘州",
                        "stationid": "101160707"
                    }
                ]
            },
            {
                "city": "酒泉",
                "disList": [
                    {
                        "district": "酒泉",
                        "stationid": "101160801"
                    },
                    {
                        "district": "肃州",
                        "stationid": "101160802"
                    },
                    {
                        "district": "金塔",
                        "stationid": "101160803"
                    },
                    {
                        "district": "阿克塞",
                        "stationid": "101160804"
                    },
                    {
                        "district": "瓜州",
                        "stationid": "101160805"
                    },
                    {
                        "district": "肃北",
                        "stationid": "101160806"
                    },
                    {
                        "district": "玉门",
                        "stationid": "101160807"
                    },
                    {
                        "district": "敦煌",
                        "stationid": "101160808"
                    }
                ]
            },
            {
                "city": "天水",
                "disList": [
                    {
                        "district": "天水",
                        "stationid": "101160901"
                    },
                    {
                        "district": "秦州",
                        "stationid": "101160902"
                    },
                    {
                        "district": "清水",
                        "stationid": "101160903"
                    },
                    {
                        "district": "秦安",
                        "stationid": "101160904"
                    },
                    {
                        "district": "甘谷",
                        "stationid": "101160905"
                    },
                    {
                        "district": "武山",
                        "stationid": "101160906"
                    },
                    {
                        "district": "张家川",
                        "stationid": "101160907"
                    },
                    {
                        "district": "麦积",
                        "stationid": "101160908"
                    }
                ]
            },
            {
                "city": "陇南",
                "disList": [
                    {
                        "district": "武都",
                        "stationid": "101161001"
                    },
                    {
                        "district": "成县",
                        "stationid": "101161002"
                    },
                    {
                        "district": "文县",
                        "stationid": "101161003"
                    },
                    {
                        "district": "宕昌",
                        "stationid": "101161004"
                    },
                    {
                        "district": "康县",
                        "stationid": "101161005"
                    },
                    {
                        "district": "西和",
                        "stationid": "101161006"
                    },
                    {
                        "district": "礼县",
                        "stationid": "101161007"
                    },
                    {
                        "district": "徽县",
                        "stationid": "101161008"
                    },
                    {
                        "district": "两当",
                        "stationid": "101161009"
                    },
                    {
                        "district": "陇南",
                        "stationid": "101161010"
                    }
                ]
            },
            {
                "city": "临夏",
                "disList": [
                    {
                        "district": "临夏",
                        "stationid": "101161101"
                    },
                    {
                        "district": "康乐",
                        "stationid": "101161102"
                    },
                    {
                        "district": "永靖",
                        "stationid": "101161103"
                    },
                    {
                        "district": "广河",
                        "stationid": "101161104"
                    },
                    {
                        "district": "和政",
                        "stationid": "101161105"
                    },
                    {
                        "district": "东乡",
                        "stationid": "101161106"
                    },
                    {
                        "district": "积石山",
                        "stationid": "101161107"
                    }
                ]
            },
            {
                "city": "甘南",
                "disList": [
                    {
                        "district": "合作",
                        "stationid": "101161201"
                    },
                    {
                        "district": "临潭",
                        "stationid": "101161202"
                    },
                    {
                        "district": "卓尼",
                        "stationid": "101161203"
                    },
                    {
                        "district": "舟曲",
                        "stationid": "101161204"
                    },
                    {
                        "district": "迭部",
                        "stationid": "101161205"
                    },
                    {
                        "district": "玛曲",
                        "stationid": "101161206"
                    },
                    {
                        "district": "碌曲",
                        "stationid": "101161207"
                    },
                    {
                        "district": "夏河",
                        "stationid": "101161208"
                    },
                    {
                        "district": "甘南",
                        "stationid": "101161209"
                    }
                ]
            },
            {
                "city": "白银",
                "disList": [
                    {
                        "district": "白银",
                        "stationid": "101161301"
                    },
                    {
                        "district": "靖远",
                        "stationid": "101161302"
                    },
                    {
                        "district": "会宁",
                        "stationid": "101161303"
                    },
                    {
                        "district": "平川",
                        "stationid": "101161304"
                    },
                    {
                        "district": "景泰",
                        "stationid": "101161305"
                    }
                ]
            },
            {
                "city": "嘉峪关",
                "disList": [
                    {
                        "district": "嘉峪关",
                        "stationid": "101161401"
                    }
                ]
            }
        ]
    },
    {
        "province": "宁夏",
        "cityList": [
            {
                "city": "银川",
                "disList": [
                    {
                        "district": "银川",
                        "stationid": "101170101"
                    },
                    {
                        "district": "永宁",
                        "stationid": "101170102"
                    },
                    {
                        "district": "灵武",
                        "stationid": "101170103"
                    },
                    {
                        "district": "贺兰",
                        "stationid": "101170104"
                    },
                    {
                        "district": "兴庆",
                        "stationid": "101170105"
                    },
                    {
                        "district": "西夏",
                        "stationid": "101170106"
                    },
                    {
                        "district": "金凤",
                        "stationid": "101170107"
                    }
                ]
            },
            {
                "city": "石嘴山",
                "disList": [
                    {
                        "district": "石嘴山",
                        "stationid": "101170201"
                    },
                    {
                        "district": "惠农",
                        "stationid": "101170202"
                    },
                    {
                        "district": "平罗",
                        "stationid": "101170203"
                    },
                    {
                        "district": "大武口",
                        "stationid": "101170205"
                    },
                    {
                        "district": "陶乐",
                        "stationid": "101170204"
                    }
                ]
            },
            {
                "city": "吴忠",
                "disList": [
                    {
                        "district": "吴忠",
                        "stationid": "101170301"
                    },
                    {
                        "district": "同心",
                        "stationid": "101170302"
                    },
                    {
                        "district": "盐池",
                        "stationid": "101170303"
                    },
                    {
                        "district": "利通",
                        "stationid": "101170304"
                    },
                    {
                        "district": "红寺堡",
                        "stationid": "101170305"
                    },
                    {
                        "district": "青铜峡",
                        "stationid": "101170306"
                    }
                ]
            },
            {
                "city": "固原",
                "disList": [
                    {
                        "district": "固原",
                        "stationid": "101170401"
                    },
                    {
                        "district": "西吉",
                        "stationid": "101170402"
                    },
                    {
                        "district": "隆德",
                        "stationid": "101170403"
                    },
                    {
                        "district": "泾源",
                        "stationid": "101170404"
                    },
                    {
                        "district": "原州",
                        "stationid": "101170405"
                    },
                    {
                        "district": "彭阳",
                        "stationid": "101170406"
                    }
                ]
            },
            {
                "city": "中卫",
                "disList": [
                    {
                        "district": "中卫",
                        "stationid": "101170501"
                    },
                    {
                        "district": "中宁",
                        "stationid": "101170502"
                    },
                    {
                        "district": "沙坡头",
                        "stationid": "101170503"
                    },
                    {
                        "district": "海原",
                        "stationid": "101170504"
                    }
                ]
            }
        ]
    },
    {
        "province": "河南",
        "cityList": [
            {
                "city": "郑州",
                "disList": [
                    {
                        "district": "郑州",
                        "stationid": "101180101"
                    },
                    {
                        "district": "巩义",
                        "stationid": "101180102"
                    },
                    {
                        "district": "荥阳",
                        "stationid": "101180103"
                    },
                    {
                        "district": "登封",
                        "stationid": "101180104"
                    },
                    {
                        "district": "新密",
                        "stationid": "101180105"
                    },
                    {
                        "district": "新郑",
                        "stationid": "101180106"
                    },
                    {
                        "district": "中牟",
                        "stationid": "101180107"
                    },
                    {
                        "district": "上街",
                        "stationid": "101180108"
                    },
                    {
                        "district": "中原",
                        "stationid": "101180109"
                    },
                    {
                        "district": "二七",
                        "stationid": "101180110"
                    },
                    {
                        "district": "管城",
                        "stationid": "101180111"
                    },
                    {
                        "district": "金水",
                        "stationid": "101180112"
                    },
                    {
                        "district": "惠济",
                        "stationid": "101180113"
                    }
                ]
            },
            {
                "city": "安阳",
                "disList": [
                    {
                        "district": "安阳",
                        "stationid": "101180201"
                    },
                    {
                        "district": "汤阴",
                        "stationid": "101180202"
                    },
                    {
                        "district": "滑县",
                        "stationid": "101180203"
                    },
                    {
                        "district": "内黄",
                        "stationid": "101180204"
                    },
                    {
                        "district": "林州",
                        "stationid": "101180205"
                    },
                    {
                        "district": "文峰",
                        "stationid": "101180206"
                    },
                    {
                        "district": "北关",
                        "stationid": "101180207"
                    },
                    {
                        "district": "殷都",
                        "stationid": "101180208"
                    },
                    {
                        "district": "龙安",
                        "stationid": "101180209"
                    }
                ]
            },
            {
                "city": "新乡",
                "disList": [
                    {
                        "district": "新乡",
                        "stationid": "101180301"
                    },
                    {
                        "district": "获嘉",
                        "stationid": "101180302"
                    },
                    {
                        "district": "原阳",
                        "stationid": "101180303"
                    },
                    {
                        "district": "辉县",
                        "stationid": "101180304"
                    },
                    {
                        "district": "卫辉",
                        "stationid": "101180305"
                    },
                    {
                        "district": "延津",
                        "stationid": "101180306"
                    },
                    {
                        "district": "封丘",
                        "stationid": "101180307"
                    },
                    {
                        "district": "长垣",
                        "stationid": "101180308"
                    },
                    {
                        "district": "红旗",
                        "stationid": "101180309"
                    },
                    {
                        "district": "卫滨",
                        "stationid": "101180310"
                    },
                    {
                        "district": "凤泉",
                        "stationid": "101180311"
                    },
                    {
                        "district": "牧野",
                        "stationid": "101180312"
                    }
                ]
            },
            {
                "city": "许昌",
                "disList": [
                    {
                        "district": "许昌",
                        "stationid": "101180401"
                    },
                    {
                        "district": "鄢陵",
                        "stationid": "101180402"
                    },
                    {
                        "district": "襄城",
                        "stationid": "101180403"
                    },
                    {
                        "district": "长葛",
                        "stationid": "101180404"
                    },
                    {
                        "district": "禹州",
                        "stationid": "101180405"
                    },
                    {
                        "district": "魏都",
                        "stationid": "101180406"
                    },
                    {
                        "district": "建安",
                        "stationid": "101180407"
                    }
                ]
            },
            {
                "city": "平顶山",
                "disList": [
                    {
                        "district": "平顶山",
                        "stationid": "101180501"
                    },
                    {
                        "district": "郏县",
                        "stationid": "101180502"
                    },
                    {
                        "district": "宝丰",
                        "stationid": "101180503"
                    },
                    {
                        "district": "汝州",
                        "stationid": "101180504"
                    },
                    {
                        "district": "叶县",
                        "stationid": "101180505"
                    },
                    {
                        "district": "舞钢",
                        "stationid": "101180506"
                    },
                    {
                        "district": "鲁山",
                        "stationid": "101180507"
                    },
                    {
                        "district": "石龙",
                        "stationid": "101180508"
                    },
                    {
                        "district": "新华",
                        "stationid": "101180509"
                    },
                    {
                        "district": "卫东",
                        "stationid": "101180510"
                    },
                    {
                        "district": "湛河",
                        "stationid": "101180511"
                    }
                ]
            },
            {
                "city": "信阳",
                "disList": [
                    {
                        "district": "信阳",
                        "stationid": "101180601"
                    },
                    {
                        "district": "息县",
                        "stationid": "101180602"
                    },
                    {
                        "district": "罗山",
                        "stationid": "101180603"
                    },
                    {
                        "district": "光山",
                        "stationid": "101180604"
                    },
                    {
                        "district": "新县",
                        "stationid": "101180605"
                    },
                    {
                        "district": "淮滨",
                        "stationid": "101180606"
                    },
                    {
                        "district": "潢川",
                        "stationid": "101180607"
                    },
                    {
                        "district": "固始",
                        "stationid": "101180608"
                    },
                    {
                        "district": "商城",
                        "stationid": "101180609"
                    },
                    {
                        "district": "浉河",
                        "stationid": "101180610"
                    },
                    {
                        "district": "平桥",
                        "stationid": "101180611"
                    }
                ]
            },
            {
                "city": "南阳",
                "disList": [
                    {
                        "district": "南阳",
                        "stationid": "101180701"
                    },
                    {
                        "district": "南召",
                        "stationid": "101180702"
                    },
                    {
                        "district": "方城",
                        "stationid": "101180703"
                    },
                    {
                        "district": "社旗",
                        "stationid": "101180704"
                    },
                    {
                        "district": "西峡",
                        "stationid": "101180705"
                    },
                    {
                        "district": "内乡",
                        "stationid": "101180706"
                    },
                    {
                        "district": "镇平",
                        "stationid": "101180707"
                    },
                    {
                        "district": "淅川",
                        "stationid": "101180708"
                    },
                    {
                        "district": "新野",
                        "stationid": "101180709"
                    },
                    {
                        "district": "唐河",
                        "stationid": "101180710"
                    },
                    {
                        "district": "邓州",
                        "stationid": "101180711"
                    },
                    {
                        "district": "桐柏",
                        "stationid": "101180712"
                    },
                    {
                        "district": "宛城",
                        "stationid": "101180713"
                    },
                    {
                        "district": "卧龙",
                        "stationid": "101180714"
                    }
                ]
            },
            {
                "city": "开封",
                "disList": [
                    {
                        "district": "开封",
                        "stationid": "101180801"
                    },
                    {
                        "district": "杞县",
                        "stationid": "101180802"
                    },
                    {
                        "district": "尉氏",
                        "stationid": "101180803"
                    },
                    {
                        "district": "通许",
                        "stationid": "101180804"
                    },
                    {
                        "district": "兰考",
                        "stationid": "101180805"
                    },
                    {
                        "district": "龙亭",
                        "stationid": "101180806"
                    },
                    {
                        "district": "顺河",
                        "stationid": "101180807"
                    },
                    {
                        "district": "鼓楼",
                        "stationid": "101180808"
                    },
                    {
                        "district": "禹王台",
                        "stationid": "101180809"
                    },
                    {
                        "district": "祥符",
                        "stationid": "101180810"
                    }
                ]
            },
            {
                "city": "洛阳",
                "disList": [
                    {
                        "district": "洛阳",
                        "stationid": "101180901"
                    },
                    {
                        "district": "新安",
                        "stationid": "101180902"
                    },
                    {
                        "district": "孟津",
                        "stationid": "101180903"
                    },
                    {
                        "district": "宜阳",
                        "stationid": "101180904"
                    },
                    {
                        "district": "洛宁",
                        "stationid": "101180905"
                    },
                    {
                        "district": "伊川",
                        "stationid": "101180906"
                    },
                    {
                        "district": "嵩县",
                        "stationid": "101180907"
                    },
                    {
                        "district": "偃师",
                        "stationid": "101180908"
                    },
                    {
                        "district": "栾川",
                        "stationid": "101180909"
                    },
                    {
                        "district": "汝阳",
                        "stationid": "101180910"
                    },
                    {
                        "district": "吉利",
                        "stationid": "101180911"
                    },
                    {
                        "district": "老城",
                        "stationid": "101180912"
                    },
                    {
                        "district": "西工",
                        "stationid": "101180913"
                    },
                    {
                        "district": "瀍河",
                        "stationid": "101180914"
                    },
                    {
                        "district": "涧西",
                        "stationid": "101180915"
                    },
                    {
                        "district": "洛龙",
                        "stationid": "101180916"
                    }
                ]
            },
            {
                "city": "商丘",
                "disList": [
                    {
                        "district": "商丘",
                        "stationid": "101181001"
                    },
                    {
                        "district": "梁园",
                        "stationid": "101181002"
                    },
                    {
                        "district": "睢县",
                        "stationid": "101181003"
                    },
                    {
                        "district": "民权",
                        "stationid": "101181004"
                    },
                    {
                        "district": "虞城",
                        "stationid": "101181005"
                    },
                    {
                        "district": "柘城",
                        "stationid": "101181006"
                    },
                    {
                        "district": "宁陵",
                        "stationid": "101181007"
                    },
                    {
                        "district": "夏邑",
                        "stationid": "101181008"
                    },
                    {
                        "district": "永城",
                        "stationid": "101181009"
                    },
                    {
                        "district": "睢阳",
                        "stationid": "101181010"
                    }
                ]
            },
            {
                "city": "焦作",
                "disList": [
                    {
                        "district": "焦作",
                        "stationid": "101181101"
                    },
                    {
                        "district": "修武",
                        "stationid": "101181102"
                    },
                    {
                        "district": "武陟",
                        "stationid": "101181103"
                    },
                    {
                        "district": "沁阳",
                        "stationid": "101181104"
                    },
                    {
                        "district": "解放",
                        "stationid": "101181105"
                    },
                    {
                        "district": "博爱",
                        "stationid": "101181106"
                    },
                    {
                        "district": "温县",
                        "stationid": "101181107"
                    },
                    {
                        "district": "孟州",
                        "stationid": "101181108"
                    },
                    {
                        "district": "中站",
                        "stationid": "101181109"
                    },
                    {
                        "district": "马村",
                        "stationid": "101181110"
                    },
                    {
                        "district": "山阳",
                        "stationid": "101181111"
                    }
                ]
            },
            {
                "city": "鹤壁",
                "disList": [
                    {
                        "district": "鹤壁",
                        "stationid": "101181201"
                    },
                    {
                        "district": "浚县",
                        "stationid": "101181202"
                    },
                    {
                        "district": "淇县",
                        "stationid": "101181203"
                    },
                    {
                        "district": "鹤山",
                        "stationid": "101181204"
                    },
                    {
                        "district": "山城",
                        "stationid": "101181205"
                    },
                    {
                        "district": "淇滨",
                        "stationid": "101181206"
                    }
                ]
            },
            {
                "city": "濮阳",
                "disList": [
                    {
                        "district": "濮阳",
                        "stationid": "101181301"
                    },
                    {
                        "district": "台前",
                        "stationid": "101181302"
                    },
                    {
                        "district": "南乐",
                        "stationid": "101181303"
                    },
                    {
                        "district": "清丰",
                        "stationid": "101181304"
                    },
                    {
                        "district": "范县",
                        "stationid": "101181305"
                    },
                    {
                        "district": "华龙",
                        "stationid": "101181306"
                    }
                ]
            },
            {
                "city": "周口",
                "disList": [
                    {
                        "district": "周口",
                        "stationid": "101181401"
                    },
                    {
                        "district": "扶沟",
                        "stationid": "101181402"
                    },
                    {
                        "district": "太康",
                        "stationid": "101181403"
                    },
                    {
                        "district": "淮阳",
                        "stationid": "101181404"
                    },
                    {
                        "district": "西华",
                        "stationid": "101181405"
                    },
                    {
                        "district": "商水",
                        "stationid": "101181406"
                    },
                    {
                        "district": "项城",
                        "stationid": "101181407"
                    },
                    {
                        "district": "郸城",
                        "stationid": "101181408"
                    },
                    {
                        "district": "鹿邑",
                        "stationid": "101181409"
                    },
                    {
                        "district": "沈丘",
                        "stationid": "101181410"
                    },
                    {
                        "district": "川汇",
                        "stationid": "101181411"
                    }
                ]
            },
            {
                "city": "漯河",
                "disList": [
                    {
                        "district": "漯河",
                        "stationid": "101181501"
                    },
                    {
                        "district": "临颍",
                        "stationid": "101181502"
                    },
                    {
                        "district": "舞阳",
                        "stationid": "101181503"
                    },
                    {
                        "district": "源汇",
                        "stationid": "101181504"
                    },
                    {
                        "district": "郾城",
                        "stationid": "101181505"
                    },
                    {
                        "district": "召陵",
                        "stationid": "101181506"
                    }
                ]
            },
            {
                "city": "驻马店",
                "disList": [
                    {
                        "district": "驻马店",
                        "stationid": "101181601"
                    },
                    {
                        "district": "西平",
                        "stationid": "101181602"
                    },
                    {
                        "district": "遂平",
                        "stationid": "101181603"
                    },
                    {
                        "district": "上蔡",
                        "stationid": "101181604"
                    },
                    {
                        "district": "汝南",
                        "stationid": "101181605"
                    },
                    {
                        "district": "泌阳",
                        "stationid": "101181606"
                    },
                    {
                        "district": "平舆",
                        "stationid": "101181607"
                    },
                    {
                        "district": "新蔡",
                        "stationid": "101181608"
                    },
                    {
                        "district": "确山",
                        "stationid": "101181609"
                    },
                    {
                        "district": "正阳",
                        "stationid": "101181610"
                    },
                    {
                        "district": "驿城",
                        "stationid": "101181611"
                    }
                ]
            },
            {
                "city": "三门峡",
                "disList": [
                    {
                        "district": "三门峡",
                        "stationid": "101181701"
                    },
                    {
                        "district": "灵宝",
                        "stationid": "101181702"
                    },
                    {
                        "district": "渑池",
                        "stationid": "101181703"
                    },
                    {
                        "district": "卢氏",
                        "stationid": "101181704"
                    },
                    {
                        "district": "义马",
                        "stationid": "101181705"
                    },
                    {
                        "district": "湖滨",
                        "stationid": "101181707"
                    },
                    {
                        "district": "陕州",
                        "stationid": "101181708"
                    }
                ]
            },
            {
                "city": "济源",
                "disList": [
                    {
                        "district": "济源",
                        "stationid": "101181801"
                    }
                ]
            }
        ]
    },
    {
        "province": "江苏",
        "cityList": [
            {
                "city": "南京",
                "disList": [
                    {
                        "district": "南京",
                        "stationid": "101190101"
                    },
                    {
                        "district": "溧水",
                        "stationid": "101190102"
                    },
                    {
                        "district": "高淳",
                        "stationid": "101190103"
                    },
                    {
                        "district": "江宁",
                        "stationid": "101190104"
                    },
                    {
                        "district": "六合",
                        "stationid": "101190105"
                    },
                    {
                        "district": "浦口",
                        "stationid": "101190107"
                    },
                    {
                        "district": "玄武",
                        "stationid": "101190108"
                    },
                    {
                        "district": "秦淮",
                        "stationid": "101190109"
                    },
                    {
                        "district": "建邺",
                        "stationid": "101190110"
                    },
                    {
                        "district": "鼓楼",
                        "stationid": "101190111"
                    },
                    {
                        "district": "栖霞",
                        "stationid": "101190112"
                    },
                    {
                        "district": "雨花台",
                        "stationid": "101190113"
                    }
                ]
            },
            {
                "city": "无锡",
                "disList": [
                    {
                        "district": "无锡",
                        "stationid": "101190201"
                    },
                    {
                        "district": "江阴",
                        "stationid": "101190202"
                    },
                    {
                        "district": "宜兴",
                        "stationid": "101190203"
                    },
                    {
                        "district": "锡山",
                        "stationid": "101190204"
                    },
                    {
                        "district": "惠山",
                        "stationid": "101190205"
                    },
                    {
                        "district": "滨湖",
                        "stationid": "101190206"
                    },
                    {
                        "district": "梁溪",
                        "stationid": "101190207"
                    },
                    {
                        "district": "新吴",
                        "stationid": "101190208"
                    }
                ]
            },
            {
                "city": "镇江",
                "disList": [
                    {
                        "district": "镇江",
                        "stationid": "101190301"
                    },
                    {
                        "district": "丹阳",
                        "stationid": "101190302"
                    },
                    {
                        "district": "扬中",
                        "stationid": "101190303"
                    },
                    {
                        "district": "句容",
                        "stationid": "101190304"
                    },
                    {
                        "district": "丹徒",
                        "stationid": "101190305"
                    },
                    {
                        "district": "京口",
                        "stationid": "101190306"
                    },
                    {
                        "district": "润州",
                        "stationid": "101190307"
                    }
                ]
            },
            {
                "city": "苏州",
                "disList": [
                    {
                        "district": "苏州",
                        "stationid": "101190401"
                    },
                    {
                        "district": "常熟",
                        "stationid": "101190402"
                    },
                    {
                        "district": "张家港",
                        "stationid": "101190403"
                    },
                    {
                        "district": "昆山",
                        "stationid": "101190404"
                    },
                    {
                        "district": "吴中",
                        "stationid": "101190405"
                    },
                    {
                        "district": "虎丘",
                        "stationid": "101190406"
                    },
                    {
                        "district": "吴江",
                        "stationid": "101190407"
                    },
                    {
                        "district": "太仓",
                        "stationid": "101190408"
                    },
                    {
                        "district": "相城",
                        "stationid": "101190409"
                    },
                    {
                        "district": "姑苏",
                        "stationid": "101190410"
                    }
                ]
            },
            {
                "city": "南通",
                "disList": [
                    {
                        "district": "南通",
                        "stationid": "101190501"
                    },
                    {
                        "district": "海安",
                        "stationid": "101190502"
                    },
                    {
                        "district": "如皋",
                        "stationid": "101190503"
                    },
                    {
                        "district": "如东",
                        "stationid": "101190504"
                    },
                    {
                        "district": "崇川",
                        "stationid": "101190505"
                    },
                    {
                        "district": "港闸",
                        "stationid": "101190506"
                    },
                    {
                        "district": "启东",
                        "stationid": "101190507"
                    },
                    {
                        "district": "海门",
                        "stationid": "101190508"
                    },
                    {
                        "district": "通州",
                        "stationid": "101190509"
                    }
                ]
            },
            {
                "city": "扬州",
                "disList": [
                    {
                        "district": "扬州",
                        "stationid": "101190601"
                    },
                    {
                        "district": "宝应",
                        "stationid": "101190602"
                    },
                    {
                        "district": "仪征",
                        "stationid": "101190603"
                    },
                    {
                        "district": "高邮",
                        "stationid": "101190604"
                    },
                    {
                        "district": "江都",
                        "stationid": "101190605"
                    },
                    {
                        "district": "邗江",
                        "stationid": "101190606"
                    },
                    {
                        "district": "广陵",
                        "stationid": "101190607"
                    }
                ]
            },
            {
                "city": "盐城",
                "disList": [
                    {
                        "district": "盐城",
                        "stationid": "101190701"
                    },
                    {
                        "district": "响水",
                        "stationid": "101190702"
                    },
                    {
                        "district": "滨海",
                        "stationid": "101190703"
                    },
                    {
                        "district": "阜宁",
                        "stationid": "101190704"
                    },
                    {
                        "district": "射阳",
                        "stationid": "101190705"
                    },
                    {
                        "district": "建湖",
                        "stationid": "101190706"
                    },
                    {
                        "district": "东台",
                        "stationid": "101190707"
                    },
                    {
                        "district": "大丰",
                        "stationid": "101190708"
                    },
                    {
                        "district": "盐都",
                        "stationid": "101190709"
                    },
                    {
                        "district": "亭湖",
                        "stationid": "101190710"
                    }
                ]
            },
            {
                "city": "徐州",
                "disList": [
                    {
                        "district": "徐州",
                        "stationid": "101190801"
                    },
                    {
                        "district": "铜山",
                        "stationid": "101190802"
                    },
                    {
                        "district": "丰县",
                        "stationid": "101190803"
                    },
                    {
                        "district": "沛县",
                        "stationid": "101190804"
                    },
                    {
                        "district": "邳州",
                        "stationid": "101190805"
                    },
                    {
                        "district": "睢宁",
                        "stationid": "101190806"
                    },
                    {
                        "district": "新沂",
                        "stationid": "101190807"
                    },
                    {
                        "district": "鼓楼",
                        "stationid": "101190808"
                    },
                    {
                        "district": "云龙",
                        "stationid": "101190809"
                    },
                    {
                        "district": "贾汪",
                        "stationid": "101190810"
                    },
                    {
                        "district": "泉山",
                        "stationid": "101190811"
                    }
                ]
            },
            {
                "city": "淮安",
                "disList": [
                    {
                        "district": "淮安",
                        "stationid": "101190901"
                    },
                    {
                        "district": "金湖",
                        "stationid": "101190902"
                    },
                    {
                        "district": "盱眙",
                        "stationid": "101190903"
                    },
                    {
                        "district": "洪泽",
                        "stationid": "101190904"
                    },
                    {
                        "district": "涟水",
                        "stationid": "101190905"
                    },
                    {
                        "district": "淮阴区",
                        "stationid": "101190906"
                    },
                    {
                        "district": "淮安区",
                        "stationid": "101190908"
                    },
                    {
                        "district": "清江浦",
                        "stationid": "101190907"
                    }
                ]
            },
            {
                "city": "连云港",
                "disList": [
                    {
                        "district": "连云港",
                        "stationid": "101191001"
                    },
                    {
                        "district": "东海",
                        "stationid": "101191002"
                    },
                    {
                        "district": "赣榆",
                        "stationid": "101191003"
                    },
                    {
                        "district": "灌云",
                        "stationid": "101191004"
                    },
                    {
                        "district": "灌南",
                        "stationid": "101191005"
                    },
                    {
                        "district": "海州",
                        "stationid": "101191006"
                    },
                    {
                        "district": "连云",
                        "stationid": "101191007"
                    }
                ]
            },
            {
                "city": "常州",
                "disList": [
                    {
                        "district": "常州",
                        "stationid": "101191101"
                    },
                    {
                        "district": "溧阳",
                        "stationid": "101191102"
                    },
                    {
                        "district": "金坛",
                        "stationid": "101191103"
                    },
                    {
                        "district": "武进",
                        "stationid": "101191104"
                    },
                    {
                        "district": "天宁",
                        "stationid": "101191105"
                    },
                    {
                        "district": "钟楼",
                        "stationid": "101191106"
                    },
                    {
                        "district": "新北",
                        "stationid": "101191107"
                    }
                ]
            },
            {
                "city": "泰州",
                "disList": [
                    {
                        "district": "泰州",
                        "stationid": "101191201"
                    },
                    {
                        "district": "兴化",
                        "stationid": "101191202"
                    },
                    {
                        "district": "泰兴",
                        "stationid": "101191203"
                    },
                    {
                        "district": "姜堰",
                        "stationid": "101191204"
                    },
                    {
                        "district": "靖江",
                        "stationid": "101191205"
                    },
                    {
                        "district": "海陵",
                        "stationid": "101191206"
                    },
                    {
                        "district": "高港",
                        "stationid": "101191207"
                    }
                ]
            },
            {
                "city": "宿迁",
                "disList": [
                    {
                        "district": "宿迁",
                        "stationid": "101191301"
                    },
                    {
                        "district": "沭阳",
                        "stationid": "101191302"
                    },
                    {
                        "district": "泗阳",
                        "stationid": "101191303"
                    },
                    {
                        "district": "泗洪",
                        "stationid": "101191304"
                    },
                    {
                        "district": "宿豫",
                        "stationid": "101191305"
                    },
                    {
                        "district": "宿城",
                        "stationid": "101191306"
                    }
                ]
            }
        ]
    },
    {
        "province": "湖北",
        "cityList": [
            {
                "city": "武汉",
                "disList": [
                    {
                        "district": "武汉",
                        "stationid": "101200101"
                    },
                    {
                        "district": "蔡甸",
                        "stationid": "101200102"
                    },
                    {
                        "district": "黄陂",
                        "stationid": "101200103"
                    },
                    {
                        "district": "新洲",
                        "stationid": "101200104"
                    },
                    {
                        "district": "江夏",
                        "stationid": "101200105"
                    },
                    {
                        "district": "东西湖",
                        "stationid": "101200106"
                    },
                    {
                        "district": "江岸",
                        "stationid": "101200107"
                    },
                    {
                        "district": "江汉",
                        "stationid": "101200108"
                    },
                    {
                        "district": "硚口",
                        "stationid": "101200109"
                    },
                    {
                        "district": "汉阳",
                        "stationid": "101200110"
                    },
                    {
                        "district": "武昌",
                        "stationid": "101200111"
                    },
                    {
                        "district": "青山",
                        "stationid": "101200112"
                    },
                    {
                        "district": "洪山",
                        "stationid": "101200113"
                    },
                    {
                        "district": "汉南",
                        "stationid": "101200114"
                    }
                ]
            },
            {
                "city": "襄阳",
                "disList": [
                    {
                        "district": "襄阳",
                        "stationid": "101200201"
                    },
                    {
                        "district": "襄州",
                        "stationid": "101200202"
                    },
                    {
                        "district": "保康",
                        "stationid": "101200203"
                    },
                    {
                        "district": "南漳",
                        "stationid": "101200204"
                    },
                    {
                        "district": "宜城",
                        "stationid": "101200205"
                    },
                    {
                        "district": "老河口",
                        "stationid": "101200206"
                    },
                    {
                        "district": "谷城",
                        "stationid": "101200207"
                    },
                    {
                        "district": "枣阳",
                        "stationid": "101200208"
                    },
                    {
                        "district": "襄城",
                        "stationid": "101200209"
                    },
                    {
                        "district": "樊城",
                        "stationid": "101200210"
                    }
                ]
            },
            {
                "city": "鄂州",
                "disList": [
                    {
                        "district": "鄂州",
                        "stationid": "101200301"
                    },
                    {
                        "district": "梁子湖",
                        "stationid": "101200302"
                    },
                    {
                        "district": "华容",
                        "stationid": "101200303"
                    },
                    {
                        "district": "鄂城",
                        "stationid": "101200304"
                    }
                ]
            },
            {
                "city": "孝感",
                "disList": [
                    {
                        "district": "孝感",
                        "stationid": "101200401"
                    },
                    {
                        "district": "安陆",
                        "stationid": "101200402"
                    },
                    {
                        "district": "云梦",
                        "stationid": "101200403"
                    },
                    {
                        "district": "大悟",
                        "stationid": "101200404"
                    },
                    {
                        "district": "应城",
                        "stationid": "101200405"
                    },
                    {
                        "district": "汉川",
                        "stationid": "101200406"
                    },
                    {
                        "district": "孝昌",
                        "stationid": "101200407"
                    },
                    {
                        "district": "孝南",
                        "stationid": "101200408"
                    }
                ]
            },
            {
                "city": "黄冈",
                "disList": [
                    {
                        "district": "黄冈",
                        "stationid": "101200501"
                    },
                    {
                        "district": "红安",
                        "stationid": "101200502"
                    },
                    {
                        "district": "麻城",
                        "stationid": "101200503"
                    },
                    {
                        "district": "罗田",
                        "stationid": "101200504"
                    },
                    {
                        "district": "英山",
                        "stationid": "101200505"
                    },
                    {
                        "district": "浠水",
                        "stationid": "101200506"
                    },
                    {
                        "district": "蕲春",
                        "stationid": "101200507"
                    },
                    {
                        "district": "黄梅",
                        "stationid": "101200508"
                    },
                    {
                        "district": "武穴",
                        "stationid": "101200509"
                    },
                    {
                        "district": "团风",
                        "stationid": "101200510"
                    },
                    {
                        "district": "黄州",
                        "stationid": "101200511"
                    }
                ]
            },
            {
                "city": "黄石",
                "disList": [
                    {
                        "district": "黄石",
                        "stationid": "101200601"
                    },
                    {
                        "district": "大冶",
                        "stationid": "101200602"
                    },
                    {
                        "district": "阳新",
                        "stationid": "101200603"
                    },
                    {
                        "district": "铁山",
                        "stationid": "101200604"
                    },
                    {
                        "district": "下陆",
                        "stationid": "101200605"
                    },
                    {
                        "district": "西塞山",
                        "stationid": "101200606"
                    },
                    {
                        "district": "黄石港",
                        "stationid": "101200607"
                    }
                ]
            },
            {
                "city": "咸宁",
                "disList": [
                    {
                        "district": "咸宁",
                        "stationid": "101200701"
                    },
                    {
                        "district": "赤壁",
                        "stationid": "101200702"
                    },
                    {
                        "district": "嘉鱼",
                        "stationid": "101200703"
                    },
                    {
                        "district": "崇阳",
                        "stationid": "101200704"
                    },
                    {
                        "district": "通城",
                        "stationid": "101200705"
                    },
                    {
                        "district": "通山",
                        "stationid": "101200706"
                    },
                    {
                        "district": "咸安",
                        "stationid": "101200707"
                    }
                ]
            },
            {
                "city": "荆州",
                "disList": [
                    {
                        "district": "荆州",
                        "stationid": "101200801"
                    },
                    {
                        "district": "江陵",
                        "stationid": "101200802"
                    },
                    {
                        "district": "公安",
                        "stationid": "101200803"
                    },
                    {
                        "district": "石首",
                        "stationid": "101200804"
                    },
                    {
                        "district": "监利",
                        "stationid": "101200805"
                    },
                    {
                        "district": "洪湖",
                        "stationid": "101200806"
                    },
                    {
                        "district": "松滋",
                        "stationid": "101200807"
                    },
                    {
                        "district": "沙市",
                        "stationid": "101200808"
                    }
                ]
            },
            {
                "city": "宜昌",
                "disList": [
                    {
                        "district": "宜昌",
                        "stationid": "101200901"
                    },
                    {
                        "district": "远安",
                        "stationid": "101200902"
                    },
                    {
                        "district": "秭归",
                        "stationid": "101200903"
                    },
                    {
                        "district": "兴山",
                        "stationid": "101200904"
                    },
                    {
                        "district": "西陵",
                        "stationid": "101200905"
                    },
                    {
                        "district": "五峰",
                        "stationid": "101200906"
                    },
                    {
                        "district": "当阳",
                        "stationid": "101200907"
                    },
                    {
                        "district": "长阳",
                        "stationid": "101200908"
                    },
                    {
                        "district": "宜都",
                        "stationid": "101200909"
                    },
                    {
                        "district": "枝江",
                        "stationid": "101200910"
                    },
                    {
                        "district": "夷陵",
                        "stationid": "101200912"
                    },
                    {
                        "district": "伍家岗",
                        "stationid": "101200913"
                    },
                    {
                        "district": "点军",
                        "stationid": "101200914"
                    },
                    {
                        "district": "猇亭",
                        "stationid": "101200915"
                    },
                    {
                        "district": "三峡",
                        "stationid": "101200911"
                    }
                ]
            },
            {
                "city": "恩施",
                "disList": [
                    {
                        "district": "恩施",
                        "stationid": "101201001"
                    },
                    {
                        "district": "利川",
                        "stationid": "101201002"
                    },
                    {
                        "district": "建始",
                        "stationid": "101201003"
                    },
                    {
                        "district": "咸丰",
                        "stationid": "101201004"
                    },
                    {
                        "district": "宣恩",
                        "stationid": "101201005"
                    },
                    {
                        "district": "鹤峰",
                        "stationid": "101201006"
                    },
                    {
                        "district": "来凤",
                        "stationid": "101201007"
                    },
                    {
                        "district": "巴东",
                        "stationid": "101201008"
                    }
                ]
            },
            {
                "city": "十堰",
                "disList": [
                    {
                        "district": "十堰",
                        "stationid": "101201101"
                    },
                    {
                        "district": "竹溪",
                        "stationid": "101201102"
                    },
                    {
                        "district": "郧西",
                        "stationid": "101201103"
                    },
                    {
                        "district": "郧阳",
                        "stationid": "101201104"
                    },
                    {
                        "district": "竹山",
                        "stationid": "101201105"
                    },
                    {
                        "district": "房县",
                        "stationid": "101201106"
                    },
                    {
                        "district": "丹江口",
                        "stationid": "101201107"
                    },
                    {
                        "district": "茅箭",
                        "stationid": "101201108"
                    },
                    {
                        "district": "张湾",
                        "stationid": "101201109"
                    }
                ]
            },
            {
                "city": "神农架",
                "disList": [
                    {
                        "district": "神农架",
                        "stationid": "101201201"
                    }
                ]
            },
            {
                "city": "随州",
                "disList": [
                    {
                        "district": "随州",
                        "stationid": "101201301"
                    },
                    {
                        "district": "广水",
                        "stationid": "101201302"
                    },
                    {
                        "district": "曾都",
                        "stationid": "101201303"
                    },
                    {
                        "district": "随县",
                        "stationid": "101201304"
                    }
                ]
            },
            {
                "city": "荆门",
                "disList": [
                    {
                        "district": "荆门",
                        "stationid": "101201401"
                    },
                    {
                        "district": "钟祥",
                        "stationid": "101201402"
                    },
                    {
                        "district": "京山",
                        "stationid": "101201403"
                    },
                    {
                        "district": "掇刀",
                        "stationid": "101201404"
                    },
                    {
                        "district": "沙洋",
                        "stationid": "101201405"
                    },
                    {
                        "district": "东宝",
                        "stationid": "101201406"
                    }
                ]
            },
            {
                "city": "天门",
                "disList": [
                    {
                        "district": "天门",
                        "stationid": "101201501"
                    }
                ]
            },
            {
                "city": "仙桃",
                "disList": [
                    {
                        "district": "仙桃",
                        "stationid": "101201601"
                    }
                ]
            },
            {
                "city": "潜江",
                "disList": [
                    {
                        "district": "潜江",
                        "stationid": "101201701"
                    }
                ]
            }
        ]
    },
    {
        "province": "浙江",
        "cityList": [
            {
                "city": "杭州",
                "disList": [
                    {
                        "district": "杭州",
                        "stationid": "101210101"
                    },
                    {
                        "district": "萧山",
                        "stationid": "101210102"
                    },
                    {
                        "district": "桐庐",
                        "stationid": "101210103"
                    },
                    {
                        "district": "淳安",
                        "stationid": "101210104"
                    },
                    {
                        "district": "建德",
                        "stationid": "101210105"
                    },
                    {
                        "district": "余杭",
                        "stationid": "101210106"
                    },
                    {
                        "district": "临安",
                        "stationid": "101210107"
                    },
                    {
                        "district": "富阳",
                        "stationid": "101210108"
                    },
                    {
                        "district": "上城",
                        "stationid": "101210109"
                    },
                    {
                        "district": "下城",
                        "stationid": "101210110"
                    },
                    {
                        "district": "江干",
                        "stationid": "101210111"
                    },
                    {
                        "district": "拱墅",
                        "stationid": "101210112"
                    },
                    {
                        "district": "西湖",
                        "stationid": "101210113"
                    },
                    {
                        "district": "滨江",
                        "stationid": "101210114"
                    }
                ]
            },
            {
                "city": "湖州",
                "disList": [
                    {
                        "district": "湖州",
                        "stationid": "101210201"
                    },
                    {
                        "district": "长兴",
                        "stationid": "101210202"
                    },
                    {
                        "district": "安吉",
                        "stationid": "101210203"
                    },
                    {
                        "district": "德清",
                        "stationid": "101210204"
                    },
                    {
                        "district": "吴兴",
                        "stationid": "101210205"
                    },
                    {
                        "district": "南浔",
                        "stationid": "101210206"
                    }
                ]
            },
            {
                "city": "嘉兴",
                "disList": [
                    {
                        "district": "嘉兴",
                        "stationid": "101210301"
                    },
                    {
                        "district": "嘉善",
                        "stationid": "101210302"
                    },
                    {
                        "district": "海宁",
                        "stationid": "101210303"
                    },
                    {
                        "district": "桐乡",
                        "stationid": "101210304"
                    },
                    {
                        "district": "平湖",
                        "stationid": "101210305"
                    },
                    {
                        "district": "海盐",
                        "stationid": "101210306"
                    },
                    {
                        "district": "南湖",
                        "stationid": "101210307"
                    },
                    {
                        "district": "秀洲",
                        "stationid": "101210308"
                    }
                ]
            },
            {
                "city": "宁波",
                "disList": [
                    {
                        "district": "宁波",
                        "stationid": "101210401"
                    },
                    {
                        "district": "海曙",
                        "stationid": "101210402"
                    },
                    {
                        "district": "慈溪",
                        "stationid": "101210403"
                    },
                    {
                        "district": "余姚",
                        "stationid": "101210404"
                    },
                    {
                        "district": "奉化",
                        "stationid": "101210405"
                    },
                    {
                        "district": "象山",
                        "stationid": "101210406"
                    },
                    {
                        "district": "宁海",
                        "stationid": "101210408"
                    },
                    {
                        "district": "江北",
                        "stationid": "101210409"
                    },
                    {
                        "district": "北仑",
                        "stationid": "101210410"
                    },
                    {
                        "district": "鄞州",
                        "stationid": "101210411"
                    },
                    {
                        "district": "镇海",
                        "stationid": "101210412"
                    }
                ]
            },
            {
                "city": "绍兴",
                "disList": [
                    {
                        "district": "越城",
                        "stationid": "101210501"
                    },
                    {
                        "district": "诸暨",
                        "stationid": "101210502"
                    },
                    {
                        "district": "上虞",
                        "stationid": "101210503"
                    },
                    {
                        "district": "新昌",
                        "stationid": "101210504"
                    },
                    {
                        "district": "嵊州",
                        "stationid": "101210505"
                    },
                    {
                        "district": "柯桥",
                        "stationid": "101210506"
                    },
                    {
                        "district": "绍兴",
                        "stationid": "101210507"
                    }
                ]
            },
            {
                "city": "台州",
                "disList": [
                    {
                        "district": "台州",
                        "stationid": "101210601"
                    },
                    {
                        "district": "玉环",
                        "stationid": "101210603"
                    },
                    {
                        "district": "三门",
                        "stationid": "101210604"
                    },
                    {
                        "district": "天台",
                        "stationid": "101210605"
                    },
                    {
                        "district": "仙居",
                        "stationid": "101210606"
                    },
                    {
                        "district": "温岭",
                        "stationid": "101210607"
                    },
                    {
                        "district": "临海",
                        "stationid": "101210610"
                    },
                    {
                        "district": "椒江",
                        "stationid": "101210611"
                    },
                    {
                        "district": "黄岩",
                        "stationid": "101210612"
                    },
                    {
                        "district": "路桥",
                        "stationid": "101210613"
                    }
                ]
            },
            {
                "city": "温州",
                "disList": [
                    {
                        "district": "温州",
                        "stationid": "101210701"
                    },
                    {
                        "district": "泰顺",
                        "stationid": "101210702"
                    },
                    {
                        "district": "文成",
                        "stationid": "101210703"
                    },
                    {
                        "district": "平阳",
                        "stationid": "101210704"
                    },
                    {
                        "district": "瑞安",
                        "stationid": "101210705"
                    },
                    {
                        "district": "洞头",
                        "stationid": "101210706"
                    },
                    {
                        "district": "乐清",
                        "stationid": "101210707"
                    },
                    {
                        "district": "永嘉",
                        "stationid": "101210708"
                    },
                    {
                        "district": "苍南",
                        "stationid": "101210709"
                    },
                    {
                        "district": "鹿城",
                        "stationid": "101210710"
                    },
                    {
                        "district": "龙湾",
                        "stationid": "101210711"
                    },
                    {
                        "district": "瓯海",
                        "stationid": "101210712"
                    }
                ]
            },
            {
                "city": "丽水",
                "disList": [
                    {
                        "district": "丽水",
                        "stationid": "101210801"
                    },
                    {
                        "district": "遂昌",
                        "stationid": "101210802"
                    },
                    {
                        "district": "龙泉",
                        "stationid": "101210803"
                    },
                    {
                        "district": "缙云",
                        "stationid": "101210804"
                    },
                    {
                        "district": "青田",
                        "stationid": "101210805"
                    },
                    {
                        "district": "云和",
                        "stationid": "101210806"
                    },
                    {
                        "district": "庆元",
                        "stationid": "101210807"
                    },
                    {
                        "district": "松阳",
                        "stationid": "101210808"
                    },
                    {
                        "district": "景宁",
                        "stationid": "101210809"
                    },
                    {
                        "district": "莲都",
                        "stationid": "101210810"
                    }
                ]
            },
            {
                "city": "金华",
                "disList": [
                    {
                        "district": "金华",
                        "stationid": "101210901"
                    },
                    {
                        "district": "浦江",
                        "stationid": "101210902"
                    },
                    {
                        "district": "兰溪",
                        "stationid": "101210903"
                    },
                    {
                        "district": "义乌",
                        "stationid": "101210904"
                    },
                    {
                        "district": "东阳",
                        "stationid": "101210905"
                    },
                    {
                        "district": "武义",
                        "stationid": "101210906"
                    },
                    {
                        "district": "永康",
                        "stationid": "101210907"
                    },
                    {
                        "district": "磐安",
                        "stationid": "101210908"
                    },
                    {
                        "district": "婺城",
                        "stationid": "101210909"
                    },
                    {
                        "district": "金东",
                        "stationid": "101210910"
                    }
                ]
            },
            {
                "city": "衢州",
                "disList": [
                    {
                        "district": "衢州",
                        "stationid": "101211001"
                    },
                    {
                        "district": "常山",
                        "stationid": "101211002"
                    },
                    {
                        "district": "开化",
                        "stationid": "101211003"
                    },
                    {
                        "district": "龙游",
                        "stationid": "101211004"
                    },
                    {
                        "district": "江山",
                        "stationid": "101211005"
                    },
                    {
                        "district": "衢江",
                        "stationid": "101211006"
                    },
                    {
                        "district": "柯城",
                        "stationid": "101211007"
                    }
                ]
            },
            {
                "city": "舟山",
                "disList": [
                    {
                        "district": "舟山",
                        "stationid": "101211101"
                    },
                    {
                        "district": "嵊泗",
                        "stationid": "101211102"
                    },
                    {
                        "district": "岱山",
                        "stationid": "101211104"
                    },
                    {
                        "district": "普陀",
                        "stationid": "101211105"
                    },
                    {
                        "district": "定海",
                        "stationid": "101211106"
                    }
                ]
            }
        ]
    },
    {
        "province": "安徽",
        "cityList": [
            {
                "city": "合肥",
                "disList": [
                    {
                        "district": "合肥",
                        "stationid": "101220101"
                    },
                    {
                        "district": "长丰",
                        "stationid": "101220102"
                    },
                    {
                        "district": "肥东",
                        "stationid": "101220103"
                    },
                    {
                        "district": "肥西",
                        "stationid": "101220104"
                    },
                    {
                        "district": "巢湖",
                        "stationid": "101220105"
                    },
                    {
                        "district": "庐江",
                        "stationid": "101220106"
                    },
                    {
                        "district": "瑶海",
                        "stationid": "101220107"
                    },
                    {
                        "district": "庐阳",
                        "stationid": "101220108"
                    },
                    {
                        "district": "蜀山",
                        "stationid": "101220109"
                    },
                    {
                        "district": "包河",
                        "stationid": "101220110"
                    }
                ]
            },
            {
                "city": "蚌埠",
                "disList": [
                    {
                        "district": "蚌埠",
                        "stationid": "101220201"
                    },
                    {
                        "district": "怀远",
                        "stationid": "101220202"
                    },
                    {
                        "district": "固镇",
                        "stationid": "101220203"
                    },
                    {
                        "district": "五河",
                        "stationid": "101220204"
                    },
                    {
                        "district": "龙子湖",
                        "stationid": "101220205"
                    },
                    {
                        "district": "蚌山",
                        "stationid": "101220206"
                    },
                    {
                        "district": "禹会",
                        "stationid": "101220207"
                    },
                    {
                        "district": "淮上",
                        "stationid": "101220208"
                    }
                ]
            },
            {
                "city": "芜湖",
                "disList": [
                    {
                        "district": "芜湖",
                        "stationid": "101220301"
                    },
                    {
                        "district": "繁昌",
                        "stationid": "101220302"
                    },
                    {
                        "district": "芜湖县",
                        "stationid": "101220303"
                    },
                    {
                        "district": "南陵",
                        "stationid": "101220304"
                    },
                    {
                        "district": "无为",
                        "stationid": "101220305"
                    },
                    {
                        "district": "镜湖",
                        "stationid": "101220306"
                    },
                    {
                        "district": "弋江",
                        "stationid": "101220307"
                    },
                    {
                        "district": "鸠江",
                        "stationid": "101220308"
                    },
                    {
                        "district": "三山",
                        "stationid": "101220309"
                    }
                ]
            },
            {
                "city": "淮南",
                "disList": [
                    {
                        "district": "淮南",
                        "stationid": "101220401"
                    },
                    {
                        "district": "凤台",
                        "stationid": "101220402"
                    },
                    {
                        "district": "潘集",
                        "stationid": "101220403"
                    },
                    {
                        "district": "大通",
                        "stationid": "101220404"
                    },
                    {
                        "district": "田家庵",
                        "stationid": "101220405"
                    },
                    {
                        "district": "谢家集",
                        "stationid": "101220406"
                    },
                    {
                        "district": "八公山",
                        "stationid": "101220407"
                    },
                    {
                        "district": "寿县",
                        "stationid": "101220408"
                    }
                ]
            },
            {
                "city": "马鞍山",
                "disList": [
                    {
                        "district": "马鞍山",
                        "stationid": "101220501"
                    },
                    {
                        "district": "当涂",
                        "stationid": "101220502"
                    },
                    {
                        "district": "含山",
                        "stationid": "101220503"
                    },
                    {
                        "district": "和县",
                        "stationid": "101220504"
                    },
                    {
                        "district": "花山",
                        "stationid": "101220505"
                    },
                    {
                        "district": "雨山",
                        "stationid": "101220506"
                    },
                    {
                        "district": "博望",
                        "stationid": "101220507"
                    }
                ]
            },
            {
                "city": "安庆",
                "disList": [
                    {
                        "district": "安庆",
                        "stationid": "101220601"
                    },
                    {
                        "district": "太湖",
                        "stationid": "101220603"
                    },
                    {
                        "district": "潜山",
                        "stationid": "101220604"
                    },
                    {
                        "district": "怀宁",
                        "stationid": "101220605"
                    },
                    {
                        "district": "宿松",
                        "stationid": "101220606"
                    },
                    {
                        "district": "望江",
                        "stationid": "101220607"
                    },
                    {
                        "district": "岳西",
                        "stationid": "101220608"
                    },
                    {
                        "district": "桐城",
                        "stationid": "101220609"
                    },
                    {
                        "district": "迎江",
                        "stationid": "101220610"
                    },
                    {
                        "district": "大观",
                        "stationid": "101220611"
                    },
                    {
                        "district": "宜秀",
                        "stationid": "101220612"
                    }
                ]
            },
            {
                "city": "宿州",
                "disList": [
                    {
                        "district": "宿州",
                        "stationid": "101220701"
                    },
                    {
                        "district": "砀山",
                        "stationid": "101220702"
                    },
                    {
                        "district": "灵璧",
                        "stationid": "101220703"
                    },
                    {
                        "district": "泗县",
                        "stationid": "101220704"
                    },
                    {
                        "district": "萧县",
                        "stationid": "101220705"
                    },
                    {
                        "district": "埇桥",
                        "stationid": "101220706"
                    }
                ]
            },
            {
                "city": "阜阳",
                "disList": [
                    {
                        "district": "阜阳",
                        "stationid": "101220801"
                    },
                    {
                        "district": "阜南",
                        "stationid": "101220802"
                    },
                    {
                        "district": "颍上",
                        "stationid": "101220803"
                    },
                    {
                        "district": "临泉",
                        "stationid": "101220804"
                    },
                    {
                        "district": "界首",
                        "stationid": "101220805"
                    },
                    {
                        "district": "太和",
                        "stationid": "101220806"
                    },
                    {
                        "district": "颍州",
                        "stationid": "101220807"
                    },
                    {
                        "district": "颍东",
                        "stationid": "101220808"
                    },
                    {
                        "district": "颍泉",
                        "stationid": "101220809"
                    }
                ]
            },
            {
                "city": "亳州",
                "disList": [
                    {
                        "district": "亳州",
                        "stationid": "101220901"
                    },
                    {
                        "district": "涡阳",
                        "stationid": "101220902"
                    },
                    {
                        "district": "利辛",
                        "stationid": "101220903"
                    },
                    {
                        "district": "蒙城",
                        "stationid": "101220904"
                    },
                    {
                        "district": "谯城",
                        "stationid": "101220905"
                    }
                ]
            },
            {
                "city": "黄山",
                "disList": [
                    {
                        "district": "黄山",
                        "stationid": "101221001"
                    },
                    {
                        "district": "黄山区",
                        "stationid": "101221002"
                    },
                    {
                        "district": "屯溪",
                        "stationid": "101221003"
                    },
                    {
                        "district": "祁门",
                        "stationid": "101221004"
                    },
                    {
                        "district": "黟县",
                        "stationid": "101221005"
                    },
                    {
                        "district": "歙县",
                        "stationid": "101221006"
                    },
                    {
                        "district": "休宁",
                        "stationid": "101221007"
                    },
                    {
                        "district": "徽州",
                        "stationid": "101221009"
                    },
                    {
                        "district": "黄山风景区(光明顶)",
                        "stationid": "101221008"
                    }
                ]
            },
            {
                "city": "滁州",
                "disList": [
                    {
                        "district": "滁州",
                        "stationid": "101221101"
                    },
                    {
                        "district": "凤阳",
                        "stationid": "101221102"
                    },
                    {
                        "district": "明光",
                        "stationid": "101221103"
                    },
                    {
                        "district": "定远",
                        "stationid": "101221104"
                    },
                    {
                        "district": "全椒",
                        "stationid": "101221105"
                    },
                    {
                        "district": "来安",
                        "stationid": "101221106"
                    },
                    {
                        "district": "天长",
                        "stationid": "101221107"
                    },
                    {
                        "district": "琅琊",
                        "stationid": "101221108"
                    },
                    {
                        "district": "南谯",
                        "stationid": "101221109"
                    }
                ]
            },
            {
                "city": "淮北",
                "disList": [
                    {
                        "district": "淮北",
                        "stationid": "101221201"
                    },
                    {
                        "district": "濉溪",
                        "stationid": "101221202"
                    },
                    {
                        "district": "杜集",
                        "stationid": "101221203"
                    },
                    {
                        "district": "相山",
                        "stationid": "101221204"
                    },
                    {
                        "district": "烈山",
                        "stationid": "101221205"
                    }
                ]
            },
            {
                "city": "铜陵",
                "disList": [
                    {
                        "district": "铜陵",
                        "stationid": "101221301"
                    },
                    {
                        "district": "铜官",
                        "stationid": "101221302"
                    },
                    {
                        "district": "义安",
                        "stationid": "101221303"
                    },
                    {
                        "district": "郊区",
                        "stationid": "101221304"
                    },
                    {
                        "district": "枞阳",
                        "stationid": "101221305"
                    }
                ]
            },
            {
                "city": "宣城",
                "disList": [
                    {
                        "district": "宣城",
                        "stationid": "101221401"
                    },
                    {
                        "district": "泾县",
                        "stationid": "101221402"
                    },
                    {
                        "district": "旌德",
                        "stationid": "101221403"
                    },
                    {
                        "district": "宁国",
                        "stationid": "101221404"
                    },
                    {
                        "district": "绩溪",
                        "stationid": "101221405"
                    },
                    {
                        "district": "广德",
                        "stationid": "101221406"
                    },
                    {
                        "district": "郎溪",
                        "stationid": "101221407"
                    },
                    {
                        "district": "宣州",
                        "stationid": "101221408"
                    }
                ]
            },
            {
                "city": "六安",
                "disList": [
                    {
                        "district": "六安",
                        "stationid": "101221501"
                    },
                    {
                        "district": "霍邱",
                        "stationid": "101221502"
                    },
                    {
                        "district": "金安",
                        "stationid": "101221504"
                    },
                    {
                        "district": "金寨",
                        "stationid": "101221505"
                    },
                    {
                        "district": "霍山",
                        "stationid": "101221506"
                    },
                    {
                        "district": "舒城",
                        "stationid": "101221507"
                    },
                    {
                        "district": "裕安",
                        "stationid": "101221508"
                    },
                    {
                        "district": "叶集",
                        "stationid": "101221509"
                    }
                ]
            },
            {
                "city": "池州",
                "disList": [
                    {
                        "district": "池州",
                        "stationid": "101221701"
                    },
                    {
                        "district": "东至",
                        "stationid": "101221702"
                    },
                    {
                        "district": "青阳",
                        "stationid": "101221703"
                    },
                    {
                        "district": "九华山",
                        "stationid": "101221704"
                    },
                    {
                        "district": "石台",
                        "stationid": "101221705"
                    },
                    {
                        "district": "贵池",
                        "stationid": "101221706"
                    }
                ]
            }
        ]
    },
    {
        "province": "福建",
        "cityList": [
            {
                "city": "福州",
                "disList": [
                    {
                        "district": "福州",
                        "stationid": "101230101"
                    },
                    {
                        "district": "闽清",
                        "stationid": "101230102"
                    },
                    {
                        "district": "闽侯",
                        "stationid": "101230103"
                    },
                    {
                        "district": "罗源",
                        "stationid": "101230104"
                    },
                    {
                        "district": "连江",
                        "stationid": "101230105"
                    },
                    {
                        "district": "鼓楼",
                        "stationid": "101230106"
                    },
                    {
                        "district": "永泰",
                        "stationid": "101230107"
                    },
                    {
                        "district": "平潭",
                        "stationid": "101230108"
                    },
                    {
                        "district": "台江",
                        "stationid": "101230109"
                    },
                    {
                        "district": "长乐",
                        "stationid": "101230110"
                    },
                    {
                        "district": "福清",
                        "stationid": "101230111"
                    },
                    {
                        "district": "仓山",
                        "stationid": "101230112"
                    },
                    {
                        "district": "马尾",
                        "stationid": "101230113"
                    },
                    {
                        "district": "晋安",
                        "stationid": "101230114"
                    }
                ]
            },
            {
                "city": "厦门",
                "disList": [
                    {
                        "district": "厦门",
                        "stationid": "101230201"
                    },
                    {
                        "district": "同安",
                        "stationid": "101230202"
                    },
                    {
                        "district": "思明",
                        "stationid": "101230203"
                    },
                    {
                        "district": "海沧",
                        "stationid": "101230204"
                    },
                    {
                        "district": "湖里",
                        "stationid": "101230205"
                    },
                    {
                        "district": "集美",
                        "stationid": "101230206"
                    },
                    {
                        "district": "翔安",
                        "stationid": "101230207"
                    }
                ]
            },
            {
                "city": "宁德",
                "disList": [
                    {
                        "district": "宁德",
                        "stationid": "101230301"
                    },
                    {
                        "district": "古田",
                        "stationid": "101230302"
                    },
                    {
                        "district": "霞浦",
                        "stationid": "101230303"
                    },
                    {
                        "district": "寿宁",
                        "stationid": "101230304"
                    },
                    {
                        "district": "周宁",
                        "stationid": "101230305"
                    },
                    {
                        "district": "福安",
                        "stationid": "101230306"
                    },
                    {
                        "district": "柘荣",
                        "stationid": "101230307"
                    },
                    {
                        "district": "福鼎",
                        "stationid": "101230308"
                    },
                    {
                        "district": "屏南",
                        "stationid": "101230309"
                    },
                    {
                        "district": "蕉城",
                        "stationid": "101230310"
                    }
                ]
            },
            {
                "city": "莆田",
                "disList": [
                    {
                        "district": "莆田",
                        "stationid": "101230401"
                    },
                    {
                        "district": "仙游",
                        "stationid": "101230402"
                    },
                    {
                        "district": "涵江",
                        "stationid": "101230404"
                    },
                    {
                        "district": "秀屿",
                        "stationid": "101230405"
                    },
                    {
                        "district": "荔城",
                        "stationid": "101230406"
                    },
                    {
                        "district": "城厢",
                        "stationid": "101230407"
                    }
                ]
            },
            {
                "city": "泉州",
                "disList": [
                    {
                        "district": "泉州",
                        "stationid": "101230501"
                    },
                    {
                        "district": "安溪",
                        "stationid": "101230502"
                    },
                    {
                        "district": "金门",
                        "stationid": "101230503"
                    },
                    {
                        "district": "永春",
                        "stationid": "101230504"
                    },
                    {
                        "district": "德化",
                        "stationid": "101230505"
                    },
                    {
                        "district": "南安",
                        "stationid": "101230506"
                    },
                    {
                        "district": "惠安",
                        "stationid": "101230508"
                    },
                    {
                        "district": "晋江",
                        "stationid": "101230509"
                    },
                    {
                        "district": "石狮",
                        "stationid": "101230510"
                    },
                    {
                        "district": "鲤城",
                        "stationid": "101230511"
                    },
                    {
                        "district": "丰泽",
                        "stationid": "101230512"
                    },
                    {
                        "district": "洛江",
                        "stationid": "101230513"
                    },
                    {
                        "district": "泉港",
                        "stationid": "101230514"
                    },
                    {
                        "district": "崇武",
                        "stationid": "101230507"
                    }
                ]
            },
            {
                "city": "漳州",
                "disList": [
                    {
                        "district": "漳州",
                        "stationid": "101230601"
                    },
                    {
                        "district": "长泰",
                        "stationid": "101230602"
                    },
                    {
                        "district": "南靖",
                        "stationid": "101230603"
                    },
                    {
                        "district": "平和",
                        "stationid": "101230604"
                    },
                    {
                        "district": "龙海",
                        "stationid": "101230605"
                    },
                    {
                        "district": "漳浦",
                        "stationid": "101230606"
                    },
                    {
                        "district": "诏安",
                        "stationid": "101230607"
                    },
                    {
                        "district": "东山",
                        "stationid": "101230608"
                    },
                    {
                        "district": "云霄",
                        "stationid": "101230609"
                    },
                    {
                        "district": "华安",
                        "stationid": "101230610"
                    },
                    {
                        "district": "芗城",
                        "stationid": "101230611"
                    },
                    {
                        "district": "龙文",
                        "stationid": "101230612"
                    }
                ]
            },
            {
                "city": "龙岩",
                "disList": [
                    {
                        "district": "龙岩",
                        "stationid": "101230701"
                    },
                    {
                        "district": "长汀",
                        "stationid": "101230702"
                    },
                    {
                        "district": "连城",
                        "stationid": "101230703"
                    },
                    {
                        "district": "武平",
                        "stationid": "101230704"
                    },
                    {
                        "district": "上杭",
                        "stationid": "101230705"
                    },
                    {
                        "district": "永定",
                        "stationid": "101230706"
                    },
                    {
                        "district": "漳平",
                        "stationid": "101230707"
                    },
                    {
                        "district": "新罗",
                        "stationid": "101230708"
                    }
                ]
            },
            {
                "city": "三明",
                "disList": [
                    {
                        "district": "三明",
                        "stationid": "101230801"
                    },
                    {
                        "district": "宁化",
                        "stationid": "101230802"
                    },
                    {
                        "district": "清流",
                        "stationid": "101230803"
                    },
                    {
                        "district": "泰宁",
                        "stationid": "101230804"
                    },
                    {
                        "district": "将乐",
                        "stationid": "101230805"
                    },
                    {
                        "district": "建宁",
                        "stationid": "101230806"
                    },
                    {
                        "district": "明溪",
                        "stationid": "101230807"
                    },
                    {
                        "district": "沙县",
                        "stationid": "101230808"
                    },
                    {
                        "district": "尤溪",
                        "stationid": "101230809"
                    },
                    {
                        "district": "永安",
                        "stationid": "101230810"
                    },
                    {
                        "district": "大田",
                        "stationid": "101230811"
                    },
                    {
                        "district": "梅列",
                        "stationid": "101230812"
                    },
                    {
                        "district": "三元",
                        "stationid": "101230813"
                    }
                ]
            },
            {
                "city": "南平",
                "disList": [
                    {
                        "district": "南平",
                        "stationid": "101230901"
                    },
                    {
                        "district": "顺昌",
                        "stationid": "101230902"
                    },
                    {
                        "district": "光泽",
                        "stationid": "101230903"
                    },
                    {
                        "district": "邵武",
                        "stationid": "101230904"
                    },
                    {
                        "district": "武夷山",
                        "stationid": "101230905"
                    },
                    {
                        "district": "浦城",
                        "stationid": "101230906"
                    },
                    {
                        "district": "建阳",
                        "stationid": "101230907"
                    },
                    {
                        "district": "松溪",
                        "stationid": "101230908"
                    },
                    {
                        "district": "政和",
                        "stationid": "101230909"
                    },
                    {
                        "district": "建瓯",
                        "stationid": "101230910"
                    },
                    {
                        "district": "延平",
                        "stationid": "101230911"
                    }
                ]
            },
            {
                "city": "钓鱼岛",
                "disList": [
                    {
                        "district": "钓鱼岛",
                        "stationid": "101231001"
                    }
                ]
            }
        ]
    },
    {
        "province": "江西",
        "cityList": [
            {
                "city": "南昌",
                "disList": [
                    {
                        "district": "南昌",
                        "stationid": "101240101"
                    },
                    {
                        "district": "新建",
                        "stationid": "101240102"
                    },
                    {
                        "district": "南昌县",
                        "stationid": "101240103"
                    },
                    {
                        "district": "安义",
                        "stationid": "101240104"
                    },
                    {
                        "district": "进贤",
                        "stationid": "101240105"
                    },
                    {
                        "district": "东湖",
                        "stationid": "101240106"
                    },
                    {
                        "district": "西湖",
                        "stationid": "101240107"
                    },
                    {
                        "district": "青云谱",
                        "stationid": "101240108"
                    },
                    {
                        "district": "湾里",
                        "stationid": "101240109"
                    },
                    {
                        "district": "青山湖",
                        "stationid": "101240110"
                    }
                ]
            },
            {
                "city": "九江",
                "disList": [
                    {
                        "district": "九江",
                        "stationid": "101240201"
                    },
                    {
                        "district": "瑞昌",
                        "stationid": "101240202"
                    },
                    {
                        "district": "庐山",
                        "stationid": "101240203"
                    },
                    {
                        "district": "武宁",
                        "stationid": "101240204"
                    },
                    {
                        "district": "德安",
                        "stationid": "101240205"
                    },
                    {
                        "district": "永修",
                        "stationid": "101240206"
                    },
                    {
                        "district": "湖口",
                        "stationid": "101240207"
                    },
                    {
                        "district": "彭泽",
                        "stationid": "101240208"
                    },
                    {
                        "district": "都昌",
                        "stationid": "101240210"
                    },
                    {
                        "district": "浔阳",
                        "stationid": "101240211"
                    },
                    {
                        "district": "修水",
                        "stationid": "101240212"
                    },
                    {
                        "district": "共青城",
                        "stationid": "101240213"
                    },
                    {
                        "district": "濂溪",
                        "stationid": "101240214"
                    },
                    {
                        "district": "柴桑",
                        "stationid": "101240215"
                    }
                ]
            },
            {
                "city": "上饶",
                "disList": [
                    {
                        "district": "上饶",
                        "stationid": "101240301"
                    },
                    {
                        "district": "鄱阳",
                        "stationid": "101240302"
                    },
                    {
                        "district": "婺源",
                        "stationid": "101240303"
                    },
                    {
                        "district": "信州",
                        "stationid": "101240304"
                    },
                    {
                        "district": "余干",
                        "stationid": "101240305"
                    },
                    {
                        "district": "万年",
                        "stationid": "101240306"
                    },
                    {
                        "district": "德兴",
                        "stationid": "101240307"
                    },
                    {
                        "district": "上饶县",
                        "stationid": "101240308"
                    },
                    {
                        "district": "弋阳",
                        "stationid": "101240309"
                    },
                    {
                        "district": "横峰",
                        "stationid": "101240310"
                    },
                    {
                        "district": "铅山",
                        "stationid": "101240311"
                    },
                    {
                        "district": "玉山",
                        "stationid": "101240312"
                    },
                    {
                        "district": "广丰",
                        "stationid": "101240313"
                    }
                ]
            },
            {
                "city": "抚州",
                "disList": [
                    {
                        "district": "抚州",
                        "stationid": "101240401"
                    },
                    {
                        "district": "广昌",
                        "stationid": "101240402"
                    },
                    {
                        "district": "乐安",
                        "stationid": "101240403"
                    },
                    {
                        "district": "崇仁",
                        "stationid": "101240404"
                    },
                    {
                        "district": "金溪",
                        "stationid": "101240405"
                    },
                    {
                        "district": "资溪",
                        "stationid": "101240406"
                    },
                    {
                        "district": "宜黄",
                        "stationid": "101240407"
                    },
                    {
                        "district": "南城",
                        "stationid": "101240408"
                    },
                    {
                        "district": "南丰",
                        "stationid": "101240409"
                    },
                    {
                        "district": "黎川",
                        "stationid": "101240410"
                    },
                    {
                        "district": "东乡",
                        "stationid": "101240411"
                    },
                    {
                        "district": "临川",
                        "stationid": "101240412"
                    }
                ]
            },
            {
                "city": "宜春",
                "disList": [
                    {
                        "district": "宜春",
                        "stationid": "101240501"
                    },
                    {
                        "district": "铜鼓",
                        "stationid": "101240502"
                    },
                    {
                        "district": "宜丰",
                        "stationid": "101240503"
                    },
                    {
                        "district": "万载",
                        "stationid": "101240504"
                    },
                    {
                        "district": "上高",
                        "stationid": "101240505"
                    },
                    {
                        "district": "靖安",
                        "stationid": "101240506"
                    },
                    {
                        "district": "奉新",
                        "stationid": "101240507"
                    },
                    {
                        "district": "高安",
                        "stationid": "101240508"
                    },
                    {
                        "district": "樟树",
                        "stationid": "101240509"
                    },
                    {
                        "district": "丰城",
                        "stationid": "101240510"
                    },
                    {
                        "district": "袁州",
                        "stationid": "101240511"
                    }
                ]
            },
            {
                "city": "吉安",
                "disList": [
                    {
                        "district": "吉安",
                        "stationid": "101240601"
                    },
                    {
                        "district": "吉安县",
                        "stationid": "101240602"
                    },
                    {
                        "district": "吉水",
                        "stationid": "101240603"
                    },
                    {
                        "district": "新干",
                        "stationid": "101240604"
                    },
                    {
                        "district": "峡江",
                        "stationid": "101240605"
                    },
                    {
                        "district": "永丰",
                        "stationid": "101240606"
                    },
                    {
                        "district": "永新",
                        "stationid": "101240607"
                    },
                    {
                        "district": "井冈山",
                        "stationid": "101240608"
                    },
                    {
                        "district": "万安",
                        "stationid": "101240609"
                    },
                    {
                        "district": "遂川",
                        "stationid": "101240610"
                    },
                    {
                        "district": "泰和",
                        "stationid": "101240611"
                    },
                    {
                        "district": "安福",
                        "stationid": "101240612"
                    },
                    {
                        "district": "吉州",
                        "stationid": "101240614"
                    },
                    {
                        "district": "青原",
                        "stationid": "101240615"
                    },
                    {
                        "district": "厦坪",
                        "stationid": "101240616"
                    }
                ]
            },
            {
                "city": "赣州",
                "disList": [
                    {
                        "district": "赣州",
                        "stationid": "101240701"
                    },
                    {
                        "district": "崇义",
                        "stationid": "101240702"
                    },
                    {
                        "district": "上犹",
                        "stationid": "101240703"
                    },
                    {
                        "district": "南康",
                        "stationid": "101240704"
                    },
                    {
                        "district": "大余",
                        "stationid": "101240705"
                    },
                    {
                        "district": "信丰",
                        "stationid": "101240706"
                    },
                    {
                        "district": "宁都",
                        "stationid": "101240707"
                    },
                    {
                        "district": "石城",
                        "stationid": "101240708"
                    },
                    {
                        "district": "瑞金",
                        "stationid": "101240709"
                    },
                    {
                        "district": "于都",
                        "stationid": "101240710"
                    },
                    {
                        "district": "会昌",
                        "stationid": "101240711"
                    },
                    {
                        "district": "安远",
                        "stationid": "101240712"
                    },
                    {
                        "district": "全南",
                        "stationid": "101240713"
                    },
                    {
                        "district": "龙南",
                        "stationid": "101240714"
                    },
                    {
                        "district": "定南",
                        "stationid": "101240715"
                    },
                    {
                        "district": "寻乌",
                        "stationid": "101240716"
                    },
                    {
                        "district": "兴国",
                        "stationid": "101240717"
                    },
                    {
                        "district": "赣县",
                        "stationid": "101240718"
                    },
                    {
                        "district": "章贡",
                        "stationid": "101240719"
                    }
                ]
            },
            {
                "city": "景德镇",
                "disList": [
                    {
                        "district": "景德镇",
                        "stationid": "101240801"
                    },
                    {
                        "district": "乐平",
                        "stationid": "101240802"
                    },
                    {
                        "district": "浮梁",
                        "stationid": "101240803"
                    },
                    {
                        "district": "昌江",
                        "stationid": "101240804"
                    },
                    {
                        "district": "珠山",
                        "stationid": "101240805"
                    }
                ]
            },
            {
                "city": "萍乡",
                "disList": [
                    {
                        "district": "萍乡",
                        "stationid": "101240901"
                    },
                    {
                        "district": "莲花",
                        "stationid": "101240902"
                    },
                    {
                        "district": "上栗",
                        "stationid": "101240903"
                    },
                    {
                        "district": "安源",
                        "stationid": "101240904"
                    },
                    {
                        "district": "芦溪",
                        "stationid": "101240905"
                    },
                    {
                        "district": "湘东",
                        "stationid": "101240906"
                    }
                ]
            },
            {
                "city": "新余",
                "disList": [
                    {
                        "district": "新余",
                        "stationid": "101241001"
                    },
                    {
                        "district": "分宜",
                        "stationid": "101241002"
                    },
                    {
                        "district": "渝水",
                        "stationid": "101241003"
                    }
                ]
            },
            {
                "city": "鹰潭",
                "disList": [
                    {
                        "district": "鹰潭",
                        "stationid": "101241101"
                    },
                    {
                        "district": "余江",
                        "stationid": "101241102"
                    },
                    {
                        "district": "贵溪",
                        "stationid": "101241103"
                    },
                    {
                        "district": "月湖",
                        "stationid": "101241104"
                    }
                ]
            }
        ]
    },
    {
        "province": "湖南",
        "cityList": [
            {
                "city": "长沙",
                "disList": [
                    {
                        "district": "长沙",
                        "stationid": "101250101"
                    },
                    {
                        "district": "宁乡",
                        "stationid": "101250102"
                    },
                    {
                        "district": "浏阳",
                        "stationid": "101250103"
                    },
                    {
                        "district": "湘江新区",
                        "stationid": "101250104"
                    },
                    {
                        "district": "望城",
                        "stationid": "101250105"
                    },
                    {
                        "district": "长沙县",
                        "stationid": "101250106"
                    },
                    {
                        "district": "芙蓉",
                        "stationid": "101250107"
                    },
                    {
                        "district": "天心",
                        "stationid": "101250108"
                    },
                    {
                        "district": "岳麓",
                        "stationid": "101250109"
                    },
                    {
                        "district": "开福",
                        "stationid": "101250110"
                    },
                    {
                        "district": "雨花",
                        "stationid": "101250111"
                    }
                ]
            },
            {
                "city": "湘潭",
                "disList": [
                    {
                        "district": "湘潭",
                        "stationid": "101250201"
                    },
                    {
                        "district": "韶山",
                        "stationid": "101250202"
                    },
                    {
                        "district": "湘乡",
                        "stationid": "101250203"
                    },
                    {
                        "district": "雨湖",
                        "stationid": "101250204"
                    },
                    {
                        "district": "岳塘",
                        "stationid": "101250205"
                    }
                ]
            },
            {
                "city": "株洲",
                "disList": [
                    {
                        "district": "株洲",
                        "stationid": "101250301"
                    },
                    {
                        "district": "攸县",
                        "stationid": "101250302"
                    },
                    {
                        "district": "醴陵",
                        "stationid": "101250303"
                    },
                    {
                        "district": "荷塘",
                        "stationid": "101250304"
                    },
                    {
                        "district": "茶陵",
                        "stationid": "101250305"
                    },
                    {
                        "district": "炎陵",
                        "stationid": "101250306"
                    },
                    {
                        "district": "芦淞",
                        "stationid": "101250307"
                    },
                    {
                        "district": "石峰",
                        "stationid": "101250308"
                    },
                    {
                        "district": "天元",
                        "stationid": "101250309"
                    }
                ]
            },
            {
                "city": "衡阳",
                "disList": [
                    {
                        "district": "衡阳",
                        "stationid": "101250401"
                    },
                    {
                        "district": "衡山",
                        "stationid": "101250402"
                    },
                    {
                        "district": "衡东",
                        "stationid": "101250403"
                    },
                    {
                        "district": "祁东",
                        "stationid": "101250404"
                    },
                    {
                        "district": "衡阳县",
                        "stationid": "101250405"
                    },
                    {
                        "district": "常宁",
                        "stationid": "101250406"
                    },
                    {
                        "district": "衡南",
                        "stationid": "101250407"
                    },
                    {
                        "district": "耒阳",
                        "stationid": "101250408"
                    },
                    {
                        "district": "南岳",
                        "stationid": "101250409"
                    },
                    {
                        "district": "珠晖",
                        "stationid": "101250410"
                    },
                    {
                        "district": "雁峰",
                        "stationid": "101250411"
                    },
                    {
                        "district": "石鼓",
                        "stationid": "101250412"
                    },
                    {
                        "district": "蒸湘",
                        "stationid": "101250413"
                    }
                ]
            },
            {
                "city": "郴州",
                "disList": [
                    {
                        "district": "郴州",
                        "stationid": "101250501"
                    },
                    {
                        "district": "桂阳",
                        "stationid": "101250502"
                    },
                    {
                        "district": "嘉禾",
                        "stationid": "101250503"
                    },
                    {
                        "district": "宜章",
                        "stationid": "101250504"
                    },
                    {
                        "district": "临武",
                        "stationid": "101250505"
                    },
                    {
                        "district": "北湖",
                        "stationid": "101250506"
                    },
                    {
                        "district": "资兴",
                        "stationid": "101250507"
                    },
                    {
                        "district": "汝城",
                        "stationid": "101250508"
                    },
                    {
                        "district": "安仁",
                        "stationid": "101250509"
                    },
                    {
                        "district": "永兴",
                        "stationid": "101250510"
                    },
                    {
                        "district": "桂东",
                        "stationid": "101250511"
                    },
                    {
                        "district": "苏仙",
                        "stationid": "101250512"
                    }
                ]
            },
            {
                "city": "常德",
                "disList": [
                    {
                        "district": "常德",
                        "stationid": "101250601"
                    },
                    {
                        "district": "安乡",
                        "stationid": "101250602"
                    },
                    {
                        "district": "桃源",
                        "stationid": "101250603"
                    },
                    {
                        "district": "汉寿",
                        "stationid": "101250604"
                    },
                    {
                        "district": "澧县",
                        "stationid": "101250605"
                    },
                    {
                        "district": "临澧",
                        "stationid": "101250606"
                    },
                    {
                        "district": "石门",
                        "stationid": "101250607"
                    },
                    {
                        "district": "津市",
                        "stationid": "101250608"
                    },
                    {
                        "district": "武陵",
                        "stationid": "101250609"
                    },
                    {
                        "district": "鼎城",
                        "stationid": "101250610"
                    }
                ]
            },
            {
                "city": "益阳",
                "disList": [
                    {
                        "district": "益阳",
                        "stationid": "101250700"
                    },
                    {
                        "district": "赫山区",
                        "stationid": "101250701"
                    },
                    {
                        "district": "南县",
                        "stationid": "101250702"
                    },
                    {
                        "district": "桃江",
                        "stationid": "101250703"
                    },
                    {
                        "district": "安化",
                        "stationid": "101250704"
                    },
                    {
                        "district": "沅江",
                        "stationid": "101250705"
                    },
                    {
                        "district": "资阳",
                        "stationid": "101250706"
                    }
                ]
            },
            {
                "city": "娄底",
                "disList": [
                    {
                        "district": "娄底",
                        "stationid": "101250801"
                    },
                    {
                        "district": "双峰",
                        "stationid": "101250802"
                    },
                    {
                        "district": "冷水江",
                        "stationid": "101250803"
                    },
                    {
                        "district": "娄星",
                        "stationid": "101250804"
                    },
                    {
                        "district": "新化",
                        "stationid": "101250805"
                    },
                    {
                        "district": "涟源",
                        "stationid": "101250806"
                    }
                ]
            },
            {
                "city": "邵阳",
                "disList": [
                    {
                        "district": "邵阳",
                        "stationid": "101250901"
                    },
                    {
                        "district": "隆回",
                        "stationid": "101250902"
                    },
                    {
                        "district": "洞口",
                        "stationid": "101250903"
                    },
                    {
                        "district": "新邵",
                        "stationid": "101250904"
                    },
                    {
                        "district": "邵东",
                        "stationid": "101250905"
                    },
                    {
                        "district": "绥宁",
                        "stationid": "101250906"
                    },
                    {
                        "district": "新宁",
                        "stationid": "101250907"
                    },
                    {
                        "district": "武冈",
                        "stationid": "101250908"
                    },
                    {
                        "district": "城步",
                        "stationid": "101250909"
                    },
                    {
                        "district": "邵阳县",
                        "stationid": "101250910"
                    },
                    {
                        "district": "双清",
                        "stationid": "101250911"
                    },
                    {
                        "district": "大祥",
                        "stationid": "101250912"
                    },
                    {
                        "district": "北塔",
                        "stationid": "101250913"
                    }
                ]
            },
            {
                "city": "岳阳",
                "disList": [
                    {
                        "district": "岳阳",
                        "stationid": "101251001"
                    },
                    {
                        "district": "华容",
                        "stationid": "101251002"
                    },
                    {
                        "district": "湘阴",
                        "stationid": "101251003"
                    },
                    {
                        "district": "汨罗",
                        "stationid": "101251004"
                    },
                    {
                        "district": "平江",
                        "stationid": "101251005"
                    },
                    {
                        "district": "临湘",
                        "stationid": "101251006"
                    },
                    {
                        "district": "岳阳楼区",
                        "stationid": "101251007"
                    },
                    {
                        "district": "云溪",
                        "stationid": "101251008"
                    },
                    {
                        "district": "君山",
                        "stationid": "101251009"
                    }
                ]
            },
            {
                "city": "张家界",
                "disList": [
                    {
                        "district": "张家界",
                        "stationid": "101251101"
                    },
                    {
                        "district": "桑植",
                        "stationid": "101251102"
                    },
                    {
                        "district": "慈利",
                        "stationid": "101251103"
                    },
                    {
                        "district": "武陵源",
                        "stationid": "101251104"
                    },
                    {
                        "district": "永定",
                        "stationid": "101251105"
                    }
                ]
            },
            {
                "city": "怀化",
                "disList": [
                    {
                        "district": "怀化",
                        "stationid": "101251201"
                    },
                    {
                        "district": "鹤城",
                        "stationid": "101251202"
                    },
                    {
                        "district": "沅陵",
                        "stationid": "101251203"
                    },
                    {
                        "district": "辰溪",
                        "stationid": "101251204"
                    },
                    {
                        "district": "靖州",
                        "stationid": "101251205"
                    },
                    {
                        "district": "会同",
                        "stationid": "101251206"
                    },
                    {
                        "district": "通道",
                        "stationid": "101251207"
                    },
                    {
                        "district": "麻阳",
                        "stationid": "101251208"
                    },
                    {
                        "district": "新晃",
                        "stationid": "101251209"
                    },
                    {
                        "district": "芷江",
                        "stationid": "101251210"
                    },
                    {
                        "district": "溆浦",
                        "stationid": "101251211"
                    },
                    {
                        "district": "中方",
                        "stationid": "101251212"
                    },
                    {
                        "district": "洪江",
                        "stationid": "101251213"
                    }
                ]
            },
            {
                "city": "永州",
                "disList": [
                    {
                        "district": "永州",
                        "stationid": "101251401"
                    },
                    {
                        "district": "祁阳",
                        "stationid": "101251402"
                    },
                    {
                        "district": "东安",
                        "stationid": "101251403"
                    },
                    {
                        "district": "双牌",
                        "stationid": "101251404"
                    },
                    {
                        "district": "道县",
                        "stationid": "101251405"
                    },
                    {
                        "district": "宁远",
                        "stationid": "101251406"
                    },
                    {
                        "district": "江永",
                        "stationid": "101251407"
                    },
                    {
                        "district": "蓝山",
                        "stationid": "101251408"
                    },
                    {
                        "district": "新田",
                        "stationid": "101251409"
                    },
                    {
                        "district": "江华",
                        "stationid": "101251410"
                    },
                    {
                        "district": "冷水滩",
                        "stationid": "101251411"
                    },
                    {
                        "district": "零陵",
                        "stationid": "101251412"
                    }
                ]
            },
            {
                "city": "湘西",
                "disList": [
                    {
                        "district": "吉首",
                        "stationid": "101251501"
                    },
                    {
                        "district": "保靖",
                        "stationid": "101251502"
                    },
                    {
                        "district": "永顺",
                        "stationid": "101251503"
                    },
                    {
                        "district": "古丈",
                        "stationid": "101251504"
                    },
                    {
                        "district": "凤凰",
                        "stationid": "101251505"
                    },
                    {
                        "district": "泸溪",
                        "stationid": "101251506"
                    },
                    {
                        "district": "龙山",
                        "stationid": "101251507"
                    },
                    {
                        "district": "花垣",
                        "stationid": "101251508"
                    },
                    {
                        "district": "湘西",
                        "stationid": "101251509"
                    }
                ]
            }
        ]
    },
    {
        "province": "贵州",
        "cityList": [
            {
                "city": "贵阳",
                "disList": [
                    {
                        "district": "贵阳",
                        "stationid": "101260101"
                    },
                    {
                        "district": "白云",
                        "stationid": "101260102"
                    },
                    {
                        "district": "花溪",
                        "stationid": "101260103"
                    },
                    {
                        "district": "乌当",
                        "stationid": "101260104"
                    },
                    {
                        "district": "息烽",
                        "stationid": "101260105"
                    },
                    {
                        "district": "开阳",
                        "stationid": "101260106"
                    },
                    {
                        "district": "修文",
                        "stationid": "101260107"
                    },
                    {
                        "district": "清镇",
                        "stationid": "101260108"
                    },
                    {
                        "district": "云岩",
                        "stationid": "101260110"
                    },
                    {
                        "district": "南明",
                        "stationid": "101260111"
                    },
                    {
                        "district": "观山湖",
                        "stationid": "101260112"
                    }
                ]
            },
            {
                "city": "遵义",
                "disList": [
                    {
                        "district": "遵义",
                        "stationid": "101260201"
                    },
                    {
                        "district": "仁怀",
                        "stationid": "101260203"
                    },
                    {
                        "district": "绥阳",
                        "stationid": "101260204"
                    },
                    {
                        "district": "湄潭",
                        "stationid": "101260205"
                    },
                    {
                        "district": "凤冈",
                        "stationid": "101260206"
                    },
                    {
                        "district": "桐梓",
                        "stationid": "101260207"
                    },
                    {
                        "district": "赤水",
                        "stationid": "101260208"
                    },
                    {
                        "district": "习水",
                        "stationid": "101260209"
                    },
                    {
                        "district": "道真",
                        "stationid": "101260210"
                    },
                    {
                        "district": "正安",
                        "stationid": "101260211"
                    },
                    {
                        "district": "务川",
                        "stationid": "101260212"
                    },
                    {
                        "district": "余庆",
                        "stationid": "101260213"
                    },
                    {
                        "district": "汇川",
                        "stationid": "101260214"
                    },
                    {
                        "district": "红花岗",
                        "stationid": "101260215"
                    },
                    {
                        "district": "播州",
                        "stationid": "101260216"
                    }
                ]
            },
            {
                "city": "安顺",
                "disList": [
                    {
                        "district": "安顺",
                        "stationid": "101260301"
                    },
                    {
                        "district": "普定",
                        "stationid": "101260302"
                    },
                    {
                        "district": "镇宁",
                        "stationid": "101260303"
                    },
                    {
                        "district": "平坝",
                        "stationid": "101260304"
                    },
                    {
                        "district": "紫云",
                        "stationid": "101260305"
                    },
                    {
                        "district": "关岭",
                        "stationid": "101260306"
                    },
                    {
                        "district": "西秀",
                        "stationid": "101260307"
                    }
                ]
            },
            {
                "city": "黔南",
                "disList": [
                    {
                        "district": "都匀",
                        "stationid": "101260401"
                    },
                    {
                        "district": "贵定",
                        "stationid": "101260402"
                    },
                    {
                        "district": "瓮安",
                        "stationid": "101260403"
                    },
                    {
                        "district": "长顺",
                        "stationid": "101260404"
                    },
                    {
                        "district": "福泉",
                        "stationid": "101260405"
                    },
                    {
                        "district": "惠水",
                        "stationid": "101260406"
                    },
                    {
                        "district": "龙里",
                        "stationid": "101260407"
                    },
                    {
                        "district": "罗甸",
                        "stationid": "101260408"
                    },
                    {
                        "district": "平塘",
                        "stationid": "101260409"
                    },
                    {
                        "district": "独山",
                        "stationid": "101260410"
                    },
                    {
                        "district": "三都",
                        "stationid": "101260411"
                    },
                    {
                        "district": "荔波",
                        "stationid": "101260412"
                    },
                    {
                        "district": "黔南",
                        "stationid": "101260413"
                    }
                ]
            },
            {
                "city": "黔东南",
                "disList": [
                    {
                        "district": "凯里",
                        "stationid": "101260501"
                    },
                    {
                        "district": "岑巩",
                        "stationid": "101260502"
                    },
                    {
                        "district": "施秉",
                        "stationid": "101260503"
                    },
                    {
                        "district": "镇远",
                        "stationid": "101260504"
                    },
                    {
                        "district": "黄平",
                        "stationid": "101260505"
                    },
                    {
                        "district": "黔东南",
                        "stationid": "101260506"
                    },
                    {
                        "district": "麻江",
                        "stationid": "101260507"
                    },
                    {
                        "district": "丹寨",
                        "stationid": "101260508"
                    },
                    {
                        "district": "三穗",
                        "stationid": "101260509"
                    },
                    {
                        "district": "台江",
                        "stationid": "101260510"
                    },
                    {
                        "district": "剑河",
                        "stationid": "101260511"
                    },
                    {
                        "district": "雷山",
                        "stationid": "101260512"
                    },
                    {
                        "district": "黎平",
                        "stationid": "101260513"
                    },
                    {
                        "district": "天柱",
                        "stationid": "101260514"
                    },
                    {
                        "district": "锦屏",
                        "stationid": "101260515"
                    },
                    {
                        "district": "榕江",
                        "stationid": "101260516"
                    },
                    {
                        "district": "从江",
                        "stationid": "101260517"
                    }
                ]
            },
            {
                "city": "铜仁",
                "disList": [
                    {
                        "district": "铜仁",
                        "stationid": "101260601"
                    },
                    {
                        "district": "江口",
                        "stationid": "101260602"
                    },
                    {
                        "district": "玉屏",
                        "stationid": "101260603"
                    },
                    {
                        "district": "万山",
                        "stationid": "101260604"
                    },
                    {
                        "district": "思南",
                        "stationid": "101260605"
                    },
                    {
                        "district": "碧江",
                        "stationid": "101260606"
                    },
                    {
                        "district": "印江",
                        "stationid": "101260607"
                    },
                    {
                        "district": "石阡",
                        "stationid": "101260608"
                    },
                    {
                        "district": "沿河",
                        "stationid": "101260609"
                    },
                    {
                        "district": "德江",
                        "stationid": "101260610"
                    },
                    {
                        "district": "松桃",
                        "stationid": "101260611"
                    }
                ]
            },
            {
                "city": "毕节",
                "disList": [
                    {
                        "district": "毕节",
                        "stationid": "101260701"
                    },
                    {
                        "district": "赫章",
                        "stationid": "101260702"
                    },
                    {
                        "district": "金沙",
                        "stationid": "101260703"
                    },
                    {
                        "district": "威宁",
                        "stationid": "101260704"
                    },
                    {
                        "district": "大方",
                        "stationid": "101260705"
                    },
                    {
                        "district": "纳雍",
                        "stationid": "101260706"
                    },
                    {
                        "district": "织金",
                        "stationid": "101260707"
                    },
                    {
                        "district": "黔西",
                        "stationid": "101260708"
                    },
                    {
                        "district": "七星关",
                        "stationid": "101260709"
                    }
                ]
            },
            {
                "city": "六盘水",
                "disList": [
                    {
                        "district": "水城",
                        "stationid": "101260801"
                    },
                    {
                        "district": "六枝",
                        "stationid": "101260802"
                    },
                    {
                        "district": "六盘水",
                        "stationid": "101260803"
                    },
                    {
                        "district": "钟山",
                        "stationid": "101260805"
                    },
                    {
                        "district": "盘州",
                        "stationid": "101260804"
                    }
                ]
            },
            {
                "city": "黔西南",
                "disList": [
                    {
                        "district": "兴义",
                        "stationid": "101260901"
                    },
                    {
                        "district": "晴隆",
                        "stationid": "101260902"
                    },
                    {
                        "district": "兴仁",
                        "stationid": "101260903"
                    },
                    {
                        "district": "贞丰",
                        "stationid": "101260904"
                    },
                    {
                        "district": "望谟",
                        "stationid": "101260905"
                    },
                    {
                        "district": "黔西南",
                        "stationid": "101260906"
                    },
                    {
                        "district": "安龙",
                        "stationid": "101260907"
                    },
                    {
                        "district": "册亨",
                        "stationid": "101260908"
                    },
                    {
                        "district": "普安",
                        "stationid": "101260909"
                    }
                ]
            }
        ]
    },
    {
        "province": "四川",
        "cityList": [
            {
                "city": "成都",
                "disList": [
                    {
                        "district": "成都",
                        "stationid": "101270101"
                    },
                    {
                        "district": "龙泉驿",
                        "stationid": "101270102"
                    },
                    {
                        "district": "新都",
                        "stationid": "101270103"
                    },
                    {
                        "district": "温江",
                        "stationid": "101270104"
                    },
                    {
                        "district": "金堂",
                        "stationid": "101270105"
                    },
                    {
                        "district": "双流",
                        "stationid": "101270106"
                    },
                    {
                        "district": "大邑",
                        "stationid": "101270108"
                    },
                    {
                        "district": "蒲江",
                        "stationid": "101270109"
                    },
                    {
                        "district": "新津",
                        "stationid": "101270110"
                    },
                    {
                        "district": "都江堰",
                        "stationid": "101270111"
                    },
                    {
                        "district": "彭州",
                        "stationid": "101270112"
                    },
                    {
                        "district": "邛崃",
                        "stationid": "101270113"
                    },
                    {
                        "district": "崇州",
                        "stationid": "101270114"
                    },
                    {
                        "district": "青白江",
                        "stationid": "101270115"
                    },
                    {
                        "district": "锦江",
                        "stationid": "101270116"
                    },
                    {
                        "district": "青羊",
                        "stationid": "101270117"
                    },
                    {
                        "district": "金牛",
                        "stationid": "101270118"
                    },
                    {
                        "district": "武侯",
                        "stationid": "101270119"
                    },
                    {
                        "district": "成华",
                        "stationid": "101270120"
                    },
                    {
                        "district": "简阳",
                        "stationid": "101270121"
                    },
                    {
                        "district": "郫都",
                        "stationid": "101270107"
                    }
                ]
            },
            {
                "city": "攀枝花",
                "disList": [
                    {
                        "district": "攀枝花",
                        "stationid": "101270201"
                    },
                    {
                        "district": "仁和",
                        "stationid": "101270202"
                    },
                    {
                        "district": "米易",
                        "stationid": "101270203"
                    },
                    {
                        "district": "盐边",
                        "stationid": "101270204"
                    },
                    {
                        "district": "东区",
                        "stationid": "101270205"
                    },
                    {
                        "district": "西区",
                        "stationid": "101270206"
                    }
                ]
            },
            {
                "city": "自贡",
                "disList": [
                    {
                        "district": "自贡",
                        "stationid": "101270301"
                    },
                    {
                        "district": "富顺",
                        "stationid": "101270302"
                    },
                    {
                        "district": "荣县",
                        "stationid": "101270303"
                    },
                    {
                        "district": "自流井",
                        "stationid": "101270304"
                    },
                    {
                        "district": "贡井",
                        "stationid": "101270305"
                    },
                    {
                        "district": "大安",
                        "stationid": "101270306"
                    },
                    {
                        "district": "沿滩",
                        "stationid": "101270307"
                    }
                ]
            },
            {
                "city": "绵阳",
                "disList": [
                    {
                        "district": "绵阳",
                        "stationid": "101270401"
                    },
                    {
                        "district": "三台",
                        "stationid": "101270402"
                    },
                    {
                        "district": "盐亭",
                        "stationid": "101270403"
                    },
                    {
                        "district": "梓潼",
                        "stationid": "101270405"
                    },
                    {
                        "district": "北川",
                        "stationid": "101270406"
                    },
                    {
                        "district": "平武",
                        "stationid": "101270407"
                    },
                    {
                        "district": "江油",
                        "stationid": "101270408"
                    },
                    {
                        "district": "涪城",
                        "stationid": "101270409"
                    },
                    {
                        "district": "游仙",
                        "stationid": "101270410"
                    },
                    {
                        "district": "安州",
                        "stationid": "101270411"
                    }
                ]
            },
            {
                "city": "南充",
                "disList": [
                    {
                        "district": "南充",
                        "stationid": "101270501"
                    },
                    {
                        "district": "南部",
                        "stationid": "101270502"
                    },
                    {
                        "district": "营山",
                        "stationid": "101270503"
                    },
                    {
                        "district": "蓬安",
                        "stationid": "101270504"
                    },
                    {
                        "district": "仪陇",
                        "stationid": "101270505"
                    },
                    {
                        "district": "西充",
                        "stationid": "101270506"
                    },
                    {
                        "district": "阆中",
                        "stationid": "101270507"
                    },
                    {
                        "district": "顺庆",
                        "stationid": "101270508"
                    },
                    {
                        "district": "高坪",
                        "stationid": "101270509"
                    },
                    {
                        "district": "嘉陵",
                        "stationid": "101270510"
                    }
                ]
            },
            {
                "city": "达州",
                "disList": [
                    {
                        "district": "达州",
                        "stationid": "101270601"
                    },
                    {
                        "district": "宣汉",
                        "stationid": "101270602"
                    },
                    {
                        "district": "开江",
                        "stationid": "101270603"
                    },
                    {
                        "district": "大竹",
                        "stationid": "101270604"
                    },
                    {
                        "district": "渠县",
                        "stationid": "101270605"
                    },
                    {
                        "district": "万源",
                        "stationid": "101270606"
                    },
                    {
                        "district": "通川",
                        "stationid": "101270607"
                    },
                    {
                        "district": "达川",
                        "stationid": "101270608"
                    }
                ]
            },
            {
                "city": "遂宁",
                "disList": [
                    {
                        "district": "遂宁",
                        "stationid": "101270701"
                    },
                    {
                        "district": "蓬溪",
                        "stationid": "101270702"
                    },
                    {
                        "district": "射洪",
                        "stationid": "101270703"
                    },
                    {
                        "district": "船山",
                        "stationid": "101270704"
                    },
                    {
                        "district": "安居",
                        "stationid": "101270705"
                    },
                    {
                        "district": "大英",
                        "stationid": "101270706"
                    }
                ]
            },
            {
                "city": "广安",
                "disList": [
                    {
                        "district": "广安",
                        "stationid": "101270801"
                    },
                    {
                        "district": "岳池",
                        "stationid": "101270802"
                    },
                    {
                        "district": "武胜",
                        "stationid": "101270803"
                    },
                    {
                        "district": "邻水",
                        "stationid": "101270804"
                    },
                    {
                        "district": "华蓥",
                        "stationid": "101270805"
                    },
                    {
                        "district": "前锋",
                        "stationid": "101270806"
                    }
                ]
            },
            {
                "city": "巴中",
                "disList": [
                    {
                        "district": "巴中",
                        "stationid": "101270901"
                    },
                    {
                        "district": "通江",
                        "stationid": "101270902"
                    },
                    {
                        "district": "南江",
                        "stationid": "101270903"
                    },
                    {
                        "district": "平昌",
                        "stationid": "101270904"
                    },
                    {
                        "district": "巴州",
                        "stationid": "101270905"
                    },
                    {
                        "district": "恩阳",
                        "stationid": "101270906"
                    }
                ]
            },
            {
                "city": "泸州",
                "disList": [
                    {
                        "district": "泸州",
                        "stationid": "101271001"
                    },
                    {
                        "district": "江阳",
                        "stationid": "101271002"
                    },
                    {
                        "district": "泸县",
                        "stationid": "101271003"
                    },
                    {
                        "district": "合江",
                        "stationid": "101271004"
                    },
                    {
                        "district": "叙永",
                        "stationid": "101271005"
                    },
                    {
                        "district": "古蔺",
                        "stationid": "101271006"
                    },
                    {
                        "district": "纳溪",
                        "stationid": "101271007"
                    },
                    {
                        "district": "龙马潭",
                        "stationid": "101271008"
                    }
                ]
            },
            {
                "city": "宜宾",
                "disList": [
                    {
                        "district": "宜宾",
                        "stationid": "101271101"
                    },
                    {
                        "district": "翠屏",
                        "stationid": "101271102"
                    },
                    {
                        "district": "宜宾县",
                        "stationid": "101271103"
                    },
                    {
                        "district": "南溪",
                        "stationid": "101271104"
                    },
                    {
                        "district": "江安",
                        "stationid": "101271105"
                    },
                    {
                        "district": "长宁",
                        "stationid": "101271106"
                    },
                    {
                        "district": "高县",
                        "stationid": "101271107"
                    },
                    {
                        "district": "珙县",
                        "stationid": "101271108"
                    },
                    {
                        "district": "筠连",
                        "stationid": "101271109"
                    },
                    {
                        "district": "兴文",
                        "stationid": "101271110"
                    },
                    {
                        "district": "屏山",
                        "stationid": "101271111"
                    }
                ]
            },
            {
                "city": "内江",
                "disList": [
                    {
                        "district": "内江",
                        "stationid": "101271201"
                    },
                    {
                        "district": "东兴",
                        "stationid": "101271202"
                    },
                    {
                        "district": "威远",
                        "stationid": "101271203"
                    },
                    {
                        "district": "资中",
                        "stationid": "101271204"
                    },
                    {
                        "district": "隆昌",
                        "stationid": "101271205"
                    },
                    {
                        "district": "市中",
                        "stationid": "101271206"
                    }
                ]
            },
            {
                "city": "资阳",
                "disList": [
                    {
                        "district": "资阳",
                        "stationid": "101271301"
                    },
                    {
                        "district": "安岳",
                        "stationid": "101271302"
                    },
                    {
                        "district": "乐至",
                        "stationid": "101271303"
                    },
                    {
                        "district": "雁江",
                        "stationid": "101271305"
                    }
                ]
            },
            {
                "city": "乐山",
                "disList": [
                    {
                        "district": "乐山",
                        "stationid": "101271401"
                    },
                    {
                        "district": "犍为",
                        "stationid": "101271402"
                    },
                    {
                        "district": "井研",
                        "stationid": "101271403"
                    },
                    {
                        "district": "夹江",
                        "stationid": "101271404"
                    },
                    {
                        "district": "沐川",
                        "stationid": "101271405"
                    },
                    {
                        "district": "峨边",
                        "stationid": "101271406"
                    },
                    {
                        "district": "马边",
                        "stationid": "101271407"
                    },
                    {
                        "district": "峨眉山",
                        "stationid": "101271409"
                    },
                    {
                        "district": "市中",
                        "stationid": "101271410"
                    },
                    {
                        "district": "沙湾",
                        "stationid": "101271411"
                    },
                    {
                        "district": "五通桥",
                        "stationid": "101271412"
                    },
                    {
                        "district": "金口河",
                        "stationid": "101271413"
                    },
                    {
                        "district": "峨眉山市",
                        "stationid": "101271414"
                    }
                ]
            },
            {
                "city": "眉山",
                "disList": [
                    {
                        "district": "眉山",
                        "stationid": "101271501"
                    },
                    {
                        "district": "仁寿",
                        "stationid": "101271502"
                    },
                    {
                        "district": "彭山",
                        "stationid": "101271503"
                    },
                    {
                        "district": "洪雅",
                        "stationid": "101271504"
                    },
                    {
                        "district": "丹棱",
                        "stationid": "101271505"
                    },
                    {
                        "district": "青神",
                        "stationid": "101271506"
                    },
                    {
                        "district": "东坡",
                        "stationid": "101271507"
                    }
                ]
            },
            {
                "city": "凉山",
                "disList": [
                    {
                        "district": "凉山",
                        "stationid": "101271601"
                    },
                    {
                        "district": "木里",
                        "stationid": "101271603"
                    },
                    {
                        "district": "盐源",
                        "stationid": "101271604"
                    },
                    {
                        "district": "德昌",
                        "stationid": "101271605"
                    },
                    {
                        "district": "会理",
                        "stationid": "101271606"
                    },
                    {
                        "district": "会东",
                        "stationid": "101271607"
                    },
                    {
                        "district": "宁南",
                        "stationid": "101271608"
                    },
                    {
                        "district": "普格",
                        "stationid": "101271609"
                    },
                    {
                        "district": "西昌",
                        "stationid": "101271610"
                    },
                    {
                        "district": "金阳",
                        "stationid": "101271611"
                    },
                    {
                        "district": "昭觉",
                        "stationid": "101271612"
                    },
                    {
                        "district": "喜德",
                        "stationid": "101271613"
                    },
                    {
                        "district": "冕宁",
                        "stationid": "101271614"
                    },
                    {
                        "district": "越西",
                        "stationid": "101271615"
                    },
                    {
                        "district": "甘洛",
                        "stationid": "101271616"
                    },
                    {
                        "district": "雷波",
                        "stationid": "101271617"
                    },
                    {
                        "district": "美姑",
                        "stationid": "101271618"
                    },
                    {
                        "district": "布拖",
                        "stationid": "101271619"
                    }
                ]
            },
            {
                "city": "雅安",
                "disList": [
                    {
                        "district": "雅安",
                        "stationid": "101271701"
                    },
                    {
                        "district": "名山",
                        "stationid": "101271702"
                    },
                    {
                        "district": "荥经",
                        "stationid": "101271703"
                    },
                    {
                        "district": "汉源",
                        "stationid": "101271704"
                    },
                    {
                        "district": "石棉",
                        "stationid": "101271705"
                    },
                    {
                        "district": "天全",
                        "stationid": "101271706"
                    },
                    {
                        "district": "芦山",
                        "stationid": "101271707"
                    },
                    {
                        "district": "宝兴",
                        "stationid": "101271708"
                    },
                    {
                        "district": "雨城",
                        "stationid": "101271709"
                    }
                ]
            },
            {
                "city": "甘孜",
                "disList": [
                    {
                        "district": "甘孜",
                        "stationid": "101271801"
                    },
                    {
                        "district": "康定",
                        "stationid": "101271802"
                    },
                    {
                        "district": "泸定",
                        "stationid": "101271803"
                    },
                    {
                        "district": "丹巴",
                        "stationid": "101271804"
                    },
                    {
                        "district": "九龙",
                        "stationid": "101271805"
                    },
                    {
                        "district": "雅江",
                        "stationid": "101271806"
                    },
                    {
                        "district": "道孚",
                        "stationid": "101271807"
                    },
                    {
                        "district": "炉霍",
                        "stationid": "101271808"
                    },
                    {
                        "district": "新龙",
                        "stationid": "101271809"
                    },
                    {
                        "district": "德格",
                        "stationid": "101271810"
                    },
                    {
                        "district": "白玉",
                        "stationid": "101271811"
                    },
                    {
                        "district": "石渠",
                        "stationid": "101271812"
                    },
                    {
                        "district": "色达",
                        "stationid": "101271813"
                    },
                    {
                        "district": "理塘",
                        "stationid": "101271814"
                    },
                    {
                        "district": "巴塘",
                        "stationid": "101271815"
                    },
                    {
                        "district": "乡城",
                        "stationid": "101271816"
                    },
                    {
                        "district": "稻城",
                        "stationid": "101271817"
                    },
                    {
                        "district": "得荣",
                        "stationid": "101271818"
                    }
                ]
            },
            {
                "city": "阿坝",
                "disList": [
                    {
                        "district": "阿坝",
                        "stationid": "101271901"
                    },
                    {
                        "district": "汶川",
                        "stationid": "101271902"
                    },
                    {
                        "district": "理县",
                        "stationid": "101271903"
                    },
                    {
                        "district": "茂县",
                        "stationid": "101271904"
                    },
                    {
                        "district": "松潘",
                        "stationid": "101271905"
                    },
                    {
                        "district": "九寨沟",
                        "stationid": "101271906"
                    },
                    {
                        "district": "金川",
                        "stationid": "101271907"
                    },
                    {
                        "district": "小金",
                        "stationid": "101271908"
                    },
                    {
                        "district": "黑水",
                        "stationid": "101271909"
                    },
                    {
                        "district": "马尔康",
                        "stationid": "101271910"
                    },
                    {
                        "district": "壤塘",
                        "stationid": "101271911"
                    },
                    {
                        "district": "若尔盖",
                        "stationid": "101271912"
                    },
                    {
                        "district": "红原",
                        "stationid": "101271913"
                    }
                ]
            },
            {
                "city": "德阳",
                "disList": [
                    {
                        "district": "德阳",
                        "stationid": "101272001"
                    },
                    {
                        "district": "中江",
                        "stationid": "101272002"
                    },
                    {
                        "district": "广汉",
                        "stationid": "101272003"
                    },
                    {
                        "district": "什邡",
                        "stationid": "101272004"
                    },
                    {
                        "district": "绵竹",
                        "stationid": "101272005"
                    },
                    {
                        "district": "罗江",
                        "stationid": "101272006"
                    },
                    {
                        "district": "旌阳",
                        "stationid": "101272007"
                    }
                ]
            },
            {
                "city": "广元",
                "disList": [
                    {
                        "district": "广元",
                        "stationid": "101272101"
                    },
                    {
                        "district": "旺苍",
                        "stationid": "101272102"
                    },
                    {
                        "district": "青川",
                        "stationid": "101272103"
                    },
                    {
                        "district": "剑阁",
                        "stationid": "101272104"
                    },
                    {
                        "district": "苍溪",
                        "stationid": "101272105"
                    },
                    {
                        "district": "利州",
                        "stationid": "101272106"
                    },
                    {
                        "district": "昭化",
                        "stationid": "101272107"
                    },
                    {
                        "district": "朝天",
                        "stationid": "101272108"
                    }
                ]
            }
        ]
    },
    {
        "province": "广东",
        "cityList": [
            {
                "city": "广州",
                "disList": [
                    {
                        "district": "广州",
                        "stationid": "101280101"
                    },
                    {
                        "district": "番禺",
                        "stationid": "101280102"
                    },
                    {
                        "district": "从化",
                        "stationid": "101280103"
                    },
                    {
                        "district": "增城",
                        "stationid": "101280104"
                    },
                    {
                        "district": "花都",
                        "stationid": "101280105"
                    },
                    {
                        "district": "荔湾",
                        "stationid": "101280106"
                    },
                    {
                        "district": "越秀",
                        "stationid": "101280107"
                    },
                    {
                        "district": "海珠",
                        "stationid": "101280108"
                    },
                    {
                        "district": "天河",
                        "stationid": "101280109"
                    },
                    {
                        "district": "白云",
                        "stationid": "101280110"
                    },
                    {
                        "district": "黄埔",
                        "stationid": "101280111"
                    },
                    {
                        "district": "南沙",
                        "stationid": "101280112"
                    }
                ]
            },
            {
                "city": "韶关",
                "disList": [
                    {
                        "district": "韶关",
                        "stationid": "101280201"
                    },
                    {
                        "district": "乳源",
                        "stationid": "101280202"
                    },
                    {
                        "district": "始兴",
                        "stationid": "101280203"
                    },
                    {
                        "district": "翁源",
                        "stationid": "101280204"
                    },
                    {
                        "district": "乐昌",
                        "stationid": "101280205"
                    },
                    {
                        "district": "仁化",
                        "stationid": "101280206"
                    },
                    {
                        "district": "南雄",
                        "stationid": "101280207"
                    },
                    {
                        "district": "新丰",
                        "stationid": "101280208"
                    },
                    {
                        "district": "曲江",
                        "stationid": "101280209"
                    },
                    {
                        "district": "浈江",
                        "stationid": "101280210"
                    },
                    {
                        "district": "武江",
                        "stationid": "101280211"
                    }
                ]
            },
            {
                "city": "惠州",
                "disList": [
                    {
                        "district": "惠州",
                        "stationid": "101280301"
                    },
                    {
                        "district": "博罗",
                        "stationid": "101280302"
                    },
                    {
                        "district": "惠阳",
                        "stationid": "101280303"
                    },
                    {
                        "district": "惠东",
                        "stationid": "101280304"
                    },
                    {
                        "district": "龙门",
                        "stationid": "101280305"
                    },
                    {
                        "district": "惠城",
                        "stationid": "101280306"
                    }
                ]
            },
            {
                "city": "梅州",
                "disList": [
                    {
                        "district": "梅州",
                        "stationid": "101280401"
                    },
                    {
                        "district": "兴宁",
                        "stationid": "101280402"
                    },
                    {
                        "district": "蕉岭",
                        "stationid": "101280403"
                    },
                    {
                        "district": "大埔",
                        "stationid": "101280404"
                    },
                    {
                        "district": "梅江",
                        "stationid": "101280405"
                    },
                    {
                        "district": "丰顺",
                        "stationid": "101280406"
                    },
                    {
                        "district": "平远",
                        "stationid": "101280407"
                    },
                    {
                        "district": "五华",
                        "stationid": "101280408"
                    },
                    {
                        "district": "梅县",
                        "stationid": "101280409"
                    }
                ]
            },
            {
                "city": "汕头",
                "disList": [
                    {
                        "district": "汕头",
                        "stationid": "101280501"
                    },
                    {
                        "district": "潮阳",
                        "stationid": "101280502"
                    },
                    {
                        "district": "澄海",
                        "stationid": "101280503"
                    },
                    {
                        "district": "南澳",
                        "stationid": "101280504"
                    },
                    {
                        "district": "龙湖",
                        "stationid": "101280505"
                    },
                    {
                        "district": "金平",
                        "stationid": "101280506"
                    },
                    {
                        "district": "濠江",
                        "stationid": "101280507"
                    },
                    {
                        "district": "潮南",
                        "stationid": "101280508"
                    }
                ]
            },
            {
                "city": "深圳",
                "disList": [
                    {
                        "district": "深圳",
                        "stationid": "101280601"
                    },
                    {
                        "district": "罗湖",
                        "stationid": "101280602"
                    },
                    {
                        "district": "福田",
                        "stationid": "101280603"
                    },
                    {
                        "district": "南山",
                        "stationid": "101280604"
                    },
                    {
                        "district": "宝安",
                        "stationid": "101280605"
                    },
                    {
                        "district": "龙岗",
                        "stationid": "101280606"
                    },
                    {
                        "district": "盐田",
                        "stationid": "101280607"
                    },
                    {
                        "district": "龙华",
                        "stationid": "101280608"
                    },
                    {
                        "district": "坪山",
                        "stationid": "101280609"
                    }
                ]
            },
            {
                "city": "珠海",
                "disList": [
                    {
                        "district": "珠海",
                        "stationid": "101280701"
                    },
                    {
                        "district": "斗门",
                        "stationid": "101280702"
                    },
                    {
                        "district": "金湾",
                        "stationid": "101280703"
                    },
                    {
                        "district": "香洲",
                        "stationid": "101280704"
                    }
                ]
            },
            {
                "city": "佛山",
                "disList": [
                    {
                        "district": "佛山",
                        "stationid": "101280800"
                    },
                    {
                        "district": "顺德",
                        "stationid": "101280801"
                    },
                    {
                        "district": "三水",
                        "stationid": "101280802"
                    },
                    {
                        "district": "南海",
                        "stationid": "101280803"
                    },
                    {
                        "district": "高明",
                        "stationid": "101280804"
                    },
                    {
                        "district": "禅城",
                        "stationid": "101280805"
                    }
                ]
            },
            {
                "city": "肇庆",
                "disList": [
                    {
                        "district": "肇庆",
                        "stationid": "101280901"
                    },
                    {
                        "district": "广宁",
                        "stationid": "101280902"
                    },
                    {
                        "district": "四会",
                        "stationid": "101280903"
                    },
                    {
                        "district": "端州",
                        "stationid": "101280904"
                    },
                    {
                        "district": "德庆",
                        "stationid": "101280905"
                    },
                    {
                        "district": "怀集",
                        "stationid": "101280906"
                    },
                    {
                        "district": "封开",
                        "stationid": "101280907"
                    },
                    {
                        "district": "高要",
                        "stationid": "101280908"
                    },
                    {
                        "district": "鼎湖",
                        "stationid": "101280909"
                    }
                ]
            },
            {
                "city": "湛江",
                "disList": [
                    {
                        "district": "湛江",
                        "stationid": "101281001"
                    },
                    {
                        "district": "吴川",
                        "stationid": "101281002"
                    },
                    {
                        "district": "雷州",
                        "stationid": "101281003"
                    },
                    {
                        "district": "徐闻",
                        "stationid": "101281004"
                    },
                    {
                        "district": "廉江",
                        "stationid": "101281005"
                    },
                    {
                        "district": "赤坎",
                        "stationid": "101281006"
                    },
                    {
                        "district": "遂溪",
                        "stationid": "101281007"
                    },
                    {
                        "district": "坡头",
                        "stationid": "101281008"
                    },
                    {
                        "district": "霞山",
                        "stationid": "101281009"
                    },
                    {
                        "district": "麻章",
                        "stationid": "101281010"
                    }
                ]
            },
            {
                "city": "江门",
                "disList": [
                    {
                        "district": "江门",
                        "stationid": "101281101"
                    },
                    {
                        "district": "开平",
                        "stationid": "101281103"
                    },
                    {
                        "district": "新会",
                        "stationid": "101281104"
                    },
                    {
                        "district": "恩平",
                        "stationid": "101281105"
                    },
                    {
                        "district": "台山",
                        "stationid": "101281106"
                    },
                    {
                        "district": "蓬江",
                        "stationid": "101281107"
                    },
                    {
                        "district": "鹤山",
                        "stationid": "101281108"
                    },
                    {
                        "district": "江海",
                        "stationid": "101281109"
                    }
                ]
            },
            {
                "city": "河源",
                "disList": [
                    {
                        "district": "河源",
                        "stationid": "101281201"
                    },
                    {
                        "district": "紫金",
                        "stationid": "101281202"
                    },
                    {
                        "district": "连平",
                        "stationid": "101281203"
                    },
                    {
                        "district": "和平",
                        "stationid": "101281204"
                    },
                    {
                        "district": "龙川",
                        "stationid": "101281205"
                    },
                    {
                        "district": "东源",
                        "stationid": "101281206"
                    },
                    {
                        "district": "源城",
                        "stationid": "101281207"
                    }
                ]
            },
            {
                "city": "清远",
                "disList": [
                    {
                        "district": "清远",
                        "stationid": "101281301"
                    },
                    {
                        "district": "连南",
                        "stationid": "101281302"
                    },
                    {
                        "district": "连州",
                        "stationid": "101281303"
                    },
                    {
                        "district": "连山",
                        "stationid": "101281304"
                    },
                    {
                        "district": "阳山",
                        "stationid": "101281305"
                    },
                    {
                        "district": "佛冈",
                        "stationid": "101281306"
                    },
                    {
                        "district": "英德",
                        "stationid": "101281307"
                    },
                    {
                        "district": "清新",
                        "stationid": "101281308"
                    },
                    {
                        "district": "清城",
                        "stationid": "101281309"
                    }
                ]
            },
            {
                "city": "云浮",
                "disList": [
                    {
                        "district": "云浮",
                        "stationid": "101281401"
                    },
                    {
                        "district": "罗定",
                        "stationid": "101281402"
                    },
                    {
                        "district": "新兴",
                        "stationid": "101281403"
                    },
                    {
                        "district": "郁南",
                        "stationid": "101281404"
                    },
                    {
                        "district": "云城",
                        "stationid": "101281405"
                    },
                    {
                        "district": "云安",
                        "stationid": "101281406"
                    }
                ]
            },
            {
                "city": "潮州",
                "disList": [
                    {
                        "district": "潮州",
                        "stationid": "101281501"
                    },
                    {
                        "district": "饶平",
                        "stationid": "101281502"
                    },
                    {
                        "district": "潮安",
                        "stationid": "101281503"
                    },
                    {
                        "district": "湘桥",
                        "stationid": "101281504"
                    }
                ]
            },
            {
                "city": "东莞",
                "disList": [
                    {
                        "district": "东莞",
                        "stationid": "101281601"
                    }
                ]
            },
            {
                "city": "中山",
                "disList": [
                    {
                        "district": "中山",
                        "stationid": "101281701"
                    }
                ]
            },
            {
                "city": "阳江",
                "disList": [
                    {
                        "district": "阳江",
                        "stationid": "101281801"
                    },
                    {
                        "district": "阳春",
                        "stationid": "101281802"
                    },
                    {
                        "district": "阳东",
                        "stationid": "101281803"
                    },
                    {
                        "district": "阳西",
                        "stationid": "101281804"
                    },
                    {
                        "district": "江城",
                        "stationid": "101281805"
                    }
                ]
            },
            {
                "city": "揭阳",
                "disList": [
                    {
                        "district": "揭阳",
                        "stationid": "101281901"
                    },
                    {
                        "district": "揭西",
                        "stationid": "101281902"
                    },
                    {
                        "district": "普宁",
                        "stationid": "101281903"
                    },
                    {
                        "district": "惠来",
                        "stationid": "101281904"
                    },
                    {
                        "district": "揭东",
                        "stationid": "101281905"
                    },
                    {
                        "district": "榕城",
                        "stationid": "101281906"
                    }
                ]
            },
            {
                "city": "茂名",
                "disList": [
                    {
                        "district": "茂名",
                        "stationid": "101282001"
                    },
                    {
                        "district": "高州",
                        "stationid": "101282002"
                    },
                    {
                        "district": "化州",
                        "stationid": "101282003"
                    },
                    {
                        "district": "电白",
                        "stationid": "101282004"
                    },
                    {
                        "district": "信宜",
                        "stationid": "101282005"
                    },
                    {
                        "district": "茂南",
                        "stationid": "101282007"
                    }
                ]
            },
            {
                "city": "汕尾",
                "disList": [
                    {
                        "district": "汕尾",
                        "stationid": "101282101"
                    },
                    {
                        "district": "海丰",
                        "stationid": "101282102"
                    },
                    {
                        "district": "陆丰",
                        "stationid": "101282103"
                    },
                    {
                        "district": "陆河",
                        "stationid": "101282104"
                    }
                ]
            }
        ]
    },
    {
        "province": "云南",
        "cityList": [
            {
                "city": "昆明",
                "disList": [
                    {
                        "district": "昆明",
                        "stationid": "101290101"
                    },
                    {
                        "district": "五华",
                        "stationid": "101290102"
                    },
                    {
                        "district": "东川",
                        "stationid": "101290103"
                    },
                    {
                        "district": "寻甸",
                        "stationid": "101290104"
                    },
                    {
                        "district": "晋宁",
                        "stationid": "101290105"
                    },
                    {
                        "district": "宜良",
                        "stationid": "101290106"
                    },
                    {
                        "district": "石林",
                        "stationid": "101290107"
                    },
                    {
                        "district": "呈贡",
                        "stationid": "101290108"
                    },
                    {
                        "district": "富民",
                        "stationid": "101290109"
                    },
                    {
                        "district": "嵩明",
                        "stationid": "101290110"
                    },
                    {
                        "district": "禄劝",
                        "stationid": "101290111"
                    },
                    {
                        "district": "安宁",
                        "stationid": "101290112"
                    },
                    {
                        "district": "盘龙",
                        "stationid": "101290114"
                    },
                    {
                        "district": "官渡",
                        "stationid": "101290115"
                    },
                    {
                        "district": "西山",
                        "stationid": "101290116"
                    },
                    {
                        "district": "太华山",
                        "stationid": "101290113"
                    }
                ]
            },
            {
                "city": "大理",
                "disList": [
                    {
                        "district": "大理",
                        "stationid": "101290201"
                    },
                    {
                        "district": "云龙",
                        "stationid": "101290202"
                    },
                    {
                        "district": "漾濞",
                        "stationid": "101290203"
                    },
                    {
                        "district": "永平",
                        "stationid": "101290204"
                    },
                    {
                        "district": "宾川",
                        "stationid": "101290205"
                    },
                    {
                        "district": "弥渡",
                        "stationid": "101290206"
                    },
                    {
                        "district": "祥云",
                        "stationid": "101290207"
                    },
                    {
                        "district": "巍山",
                        "stationid": "101290208"
                    },
                    {
                        "district": "剑川",
                        "stationid": "101290209"
                    },
                    {
                        "district": "洱源",
                        "stationid": "101290210"
                    },
                    {
                        "district": "鹤庆",
                        "stationid": "101290211"
                    },
                    {
                        "district": "南涧",
                        "stationid": "101290212"
                    }
                ]
            },
            {
                "city": "红河",
                "disList": [
                    {
                        "district": "红河",
                        "stationid": "101290301"
                    },
                    {
                        "district": "石屏",
                        "stationid": "101290302"
                    },
                    {
                        "district": "建水",
                        "stationid": "101290303"
                    },
                    {
                        "district": "弥勒",
                        "stationid": "101290304"
                    },
                    {
                        "district": "元阳",
                        "stationid": "101290305"
                    },
                    {
                        "district": "绿春",
                        "stationid": "101290306"
                    },
                    {
                        "district": "开远",
                        "stationid": "101290307"
                    },
                    {
                        "district": "个旧",
                        "stationid": "101290308"
                    },
                    {
                        "district": "蒙自",
                        "stationid": "101290309"
                    },
                    {
                        "district": "屏边",
                        "stationid": "101290310"
                    },
                    {
                        "district": "泸西",
                        "stationid": "101290311"
                    },
                    {
                        "district": "金平",
                        "stationid": "101290312"
                    },
                    {
                        "district": "河口",
                        "stationid": "101290313"
                    }
                ]
            },
            {
                "city": "曲靖",
                "disList": [
                    {
                        "district": "曲靖",
                        "stationid": "101290401"
                    },
                    {
                        "district": "沾益",
                        "stationid": "101290402"
                    },
                    {
                        "district": "陆良",
                        "stationid": "101290403"
                    },
                    {
                        "district": "富源",
                        "stationid": "101290404"
                    },
                    {
                        "district": "马龙",
                        "stationid": "101290405"
                    },
                    {
                        "district": "师宗",
                        "stationid": "101290406"
                    },
                    {
                        "district": "罗平",
                        "stationid": "101290407"
                    },
                    {
                        "district": "会泽",
                        "stationid": "101290408"
                    },
                    {
                        "district": "宣威",
                        "stationid": "101290409"
                    },
                    {
                        "district": "麒麟",
                        "stationid": "101290410"
                    }
                ]
            },
            {
                "city": "保山",
                "disList": [
                    {
                        "district": "保山",
                        "stationid": "101290501"
                    },
                    {
                        "district": "隆阳",
                        "stationid": "101290502"
                    },
                    {
                        "district": "龙陵",
                        "stationid": "101290503"
                    },
                    {
                        "district": "施甸",
                        "stationid": "101290504"
                    },
                    {
                        "district": "昌宁",
                        "stationid": "101290505"
                    },
                    {
                        "district": "腾冲",
                        "stationid": "101290506"
                    }
                ]
            },
            {
                "city": "文山",
                "disList": [
                    {
                        "district": "文山",
                        "stationid": "101290601"
                    },
                    {
                        "district": "西畴",
                        "stationid": "101290602"
                    },
                    {
                        "district": "马关",
                        "stationid": "101290603"
                    },
                    {
                        "district": "麻栗坡",
                        "stationid": "101290604"
                    },
                    {
                        "district": "砚山",
                        "stationid": "101290605"
                    },
                    {
                        "district": "丘北",
                        "stationid": "101290606"
                    },
                    {
                        "district": "广南",
                        "stationid": "101290607"
                    },
                    {
                        "district": "富宁",
                        "stationid": "101290608"
                    }
                ]
            },
            {
                "city": "普洱",
                "disList": [
                    {
                        "district": "普洱",
                        "stationid": "101290901"
                    },
                    {
                        "district": "景谷",
                        "stationid": "101290902"
                    },
                    {
                        "district": "景东",
                        "stationid": "101290903"
                    },
                    {
                        "district": "澜沧",
                        "stationid": "101290904"
                    },
                    {
                        "district": "思茅",
                        "stationid": "101290905"
                    },
                    {
                        "district": "墨江",
                        "stationid": "101290906"
                    },
                    {
                        "district": "江城",
                        "stationid": "101290907"
                    },
                    {
                        "district": "孟连",
                        "stationid": "101290908"
                    },
                    {
                        "district": "西盟",
                        "stationid": "101290909"
                    },
                    {
                        "district": "镇沅",
                        "stationid": "101290911"
                    },
                    {
                        "district": "宁洱",
                        "stationid": "101290912"
                    }
                ]
            },
            {
                "city": "玉溪",
                "disList": [
                    {
                        "district": "玉溪",
                        "stationid": "101290701"
                    },
                    {
                        "district": "澄江",
                        "stationid": "101290702"
                    },
                    {
                        "district": "江川",
                        "stationid": "101290703"
                    },
                    {
                        "district": "通海",
                        "stationid": "101290704"
                    },
                    {
                        "district": "华宁",
                        "stationid": "101290705"
                    },
                    {
                        "district": "新平",
                        "stationid": "101290706"
                    },
                    {
                        "district": "易门",
                        "stationid": "101290707"
                    },
                    {
                        "district": "峨山",
                        "stationid": "101290708"
                    },
                    {
                        "district": "元江",
                        "stationid": "101290709"
                    },
                    {
                        "district": "红塔",
                        "stationid": "101290710"
                    }
                ]
            },
            {
                "city": "楚雄",
                "disList": [
                    {
                        "district": "楚雄",
                        "stationid": "101290801"
                    },
                    {
                        "district": "大姚",
                        "stationid": "101290802"
                    },
                    {
                        "district": "元谋",
                        "stationid": "101290803"
                    },
                    {
                        "district": "姚安",
                        "stationid": "101290804"
                    },
                    {
                        "district": "牟定",
                        "stationid": "101290805"
                    },
                    {
                        "district": "南华",
                        "stationid": "101290806"
                    },
                    {
                        "district": "武定",
                        "stationid": "101290807"
                    },
                    {
                        "district": "禄丰",
                        "stationid": "101290808"
                    },
                    {
                        "district": "双柏",
                        "stationid": "101290809"
                    },
                    {
                        "district": "永仁",
                        "stationid": "101290810"
                    }
                ]
            },
            {
                "city": "昭通",
                "disList": [
                    {
                        "district": "昭通",
                        "stationid": "101291001"
                    },
                    {
                        "district": "鲁甸",
                        "stationid": "101291002"
                    },
                    {
                        "district": "彝良",
                        "stationid": "101291003"
                    },
                    {
                        "district": "镇雄",
                        "stationid": "101291004"
                    },
                    {
                        "district": "威信",
                        "stationid": "101291005"
                    },
                    {
                        "district": "巧家",
                        "stationid": "101291006"
                    },
                    {
                        "district": "绥江",
                        "stationid": "101291007"
                    },
                    {
                        "district": "永善",
                        "stationid": "101291008"
                    },
                    {
                        "district": "盐津",
                        "stationid": "101291009"
                    },
                    {
                        "district": "大关",
                        "stationid": "101291010"
                    },
                    {
                        "district": "水富",
                        "stationid": "101291011"
                    },
                    {
                        "district": "昭阳",
                        "stationid": "101291012"
                    }
                ]
            },
            {
                "city": "临沧",
                "disList": [
                    {
                        "district": "临沧",
                        "stationid": "101291101"
                    },
                    {
                        "district": "沧源",
                        "stationid": "101291102"
                    },
                    {
                        "district": "耿马",
                        "stationid": "101291103"
                    },
                    {
                        "district": "双江",
                        "stationid": "101291104"
                    },
                    {
                        "district": "凤庆",
                        "stationid": "101291105"
                    },
                    {
                        "district": "永德",
                        "stationid": "101291106"
                    },
                    {
                        "district": "云县",
                        "stationid": "101291107"
                    },
                    {
                        "district": "镇康",
                        "stationid": "101291108"
                    },
                    {
                        "district": "临翔",
                        "stationid": "101291109"
                    }
                ]
            },
            {
                "city": "怒江",
                "disList": [
                    {
                        "district": "怒江",
                        "stationid": "101291201"
                    },
                    {
                        "district": "福贡",
                        "stationid": "101291203"
                    },
                    {
                        "district": "兰坪",
                        "stationid": "101291204"
                    },
                    {
                        "district": "泸水",
                        "stationid": "101291205"
                    },
                    {
                        "district": "贡山",
                        "stationid": "101291207"
                    }
                ]
            },
            {
                "city": "迪庆",
                "disList": [
                    {
                        "district": "香格里拉",
                        "stationid": "101291301"
                    },
                    {
                        "district": "德钦",
                        "stationid": "101291302"
                    },
                    {
                        "district": "维西",
                        "stationid": "101291303"
                    },
                    {
                        "district": "迪庆",
                        "stationid": "101291305"
                    }
                ]
            },
            {
                "city": "丽江",
                "disList": [
                    {
                        "district": "丽江",
                        "stationid": "101291401"
                    },
                    {
                        "district": "永胜",
                        "stationid": "101291402"
                    },
                    {
                        "district": "华坪",
                        "stationid": "101291403"
                    },
                    {
                        "district": "宁蒗",
                        "stationid": "101291404"
                    },
                    {
                        "district": "古城",
                        "stationid": "101291405"
                    },
                    {
                        "district": "玉龙",
                        "stationid": "101291406"
                    }
                ]
            },
            {
                "city": "德宏",
                "disList": [
                    {
                        "district": "德宏",
                        "stationid": "101291501"
                    },
                    {
                        "district": "陇川",
                        "stationid": "101291503"
                    },
                    {
                        "district": "盈江",
                        "stationid": "101291504"
                    },
                    {
                        "district": "瑞丽",
                        "stationid": "101291506"
                    },
                    {
                        "district": "梁河",
                        "stationid": "101291507"
                    },
                    {
                        "district": "芒市",
                        "stationid": "101291508"
                    }
                ]
            },
            {
                "city": "西双版纳",
                "disList": [
                    {
                        "district": "景洪",
                        "stationid": "101291601"
                    },
                    {
                        "district": "西双版纳",
                        "stationid": "101291602"
                    },
                    {
                        "district": "勐海",
                        "stationid": "101291603"
                    },
                    {
                        "district": "勐腊",
                        "stationid": "101291605"
                    }
                ]
            }
        ]
    },
    {
        "province": "广西",
        "cityList": [
            {
                "city": "南宁",
                "disList": [
                    {
                        "district": "南宁",
                        "stationid": "101300101"
                    },
                    {
                        "district": "兴宁",
                        "stationid": "101300102"
                    },
                    {
                        "district": "邕宁",
                        "stationid": "101300103"
                    },
                    {
                        "district": "横县",
                        "stationid": "101300104"
                    },
                    {
                        "district": "隆安",
                        "stationid": "101300105"
                    },
                    {
                        "district": "马山",
                        "stationid": "101300106"
                    },
                    {
                        "district": "上林",
                        "stationid": "101300107"
                    },
                    {
                        "district": "武鸣",
                        "stationid": "101300108"
                    },
                    {
                        "district": "宾阳",
                        "stationid": "101300109"
                    },
                    {
                        "district": "青秀",
                        "stationid": "101300110"
                    },
                    {
                        "district": "江南",
                        "stationid": "101300111"
                    },
                    {
                        "district": "西乡塘",
                        "stationid": "101300112"
                    },
                    {
                        "district": "良庆",
                        "stationid": "101300113"
                    }
                ]
            },
            {
                "city": "崇左",
                "disList": [
                    {
                        "district": "崇左",
                        "stationid": "101300201"
                    },
                    {
                        "district": "天等",
                        "stationid": "101300202"
                    },
                    {
                        "district": "龙州",
                        "stationid": "101300203"
                    },
                    {
                        "district": "凭祥",
                        "stationid": "101300204"
                    },
                    {
                        "district": "大新",
                        "stationid": "101300205"
                    },
                    {
                        "district": "扶绥",
                        "stationid": "101300206"
                    },
                    {
                        "district": "宁明",
                        "stationid": "101300207"
                    },
                    {
                        "district": "江州",
                        "stationid": "101300208"
                    }
                ]
            },
            {
                "city": "柳州",
                "disList": [
                    {
                        "district": "柳州",
                        "stationid": "101300301"
                    },
                    {
                        "district": "柳城",
                        "stationid": "101300302"
                    },
                    {
                        "district": "城中",
                        "stationid": "101300303"
                    },
                    {
                        "district": "鹿寨",
                        "stationid": "101300304"
                    },
                    {
                        "district": "柳江",
                        "stationid": "101300305"
                    },
                    {
                        "district": "融安",
                        "stationid": "101300306"
                    },
                    {
                        "district": "融水",
                        "stationid": "101300307"
                    },
                    {
                        "district": "三江",
                        "stationid": "101300308"
                    },
                    {
                        "district": "鱼峰",
                        "stationid": "101300309"
                    },
                    {
                        "district": "柳南",
                        "stationid": "101300310"
                    },
                    {
                        "district": "柳北",
                        "stationid": "101300311"
                    }
                ]
            },
            {
                "city": "来宾",
                "disList": [
                    {
                        "district": "来宾",
                        "stationid": "101300401"
                    },
                    {
                        "district": "忻城",
                        "stationid": "101300402"
                    },
                    {
                        "district": "金秀",
                        "stationid": "101300403"
                    },
                    {
                        "district": "象州",
                        "stationid": "101300404"
                    },
                    {
                        "district": "武宣",
                        "stationid": "101300405"
                    },
                    {
                        "district": "合山",
                        "stationid": "101300406"
                    },
                    {
                        "district": "兴宾",
                        "stationid": "101300407"
                    }
                ]
            },
            {
                "city": "桂林",
                "disList": [
                    {
                        "district": "桂林",
                        "stationid": "101300501"
                    },
                    {
                        "district": "秀峰",
                        "stationid": "101300502"
                    },
                    {
                        "district": "龙胜",
                        "stationid": "101300503"
                    },
                    {
                        "district": "永福",
                        "stationid": "101300504"
                    },
                    {
                        "district": "临桂",
                        "stationid": "101300505"
                    },
                    {
                        "district": "兴安",
                        "stationid": "101300506"
                    },
                    {
                        "district": "灵川",
                        "stationid": "101300507"
                    },
                    {
                        "district": "全州",
                        "stationid": "101300508"
                    },
                    {
                        "district": "灌阳",
                        "stationid": "101300509"
                    },
                    {
                        "district": "阳朔",
                        "stationid": "101300510"
                    },
                    {
                        "district": "恭城",
                        "stationid": "101300511"
                    },
                    {
                        "district": "平乐",
                        "stationid": "101300512"
                    },
                    {
                        "district": "荔浦",
                        "stationid": "101300513"
                    },
                    {
                        "district": "资源",
                        "stationid": "101300514"
                    },
                    {
                        "district": "叠彩",
                        "stationid": "101300515"
                    },
                    {
                        "district": "象山",
                        "stationid": "101300516"
                    },
                    {
                        "district": "七星",
                        "stationid": "101300517"
                    },
                    {
                        "district": "雁山",
                        "stationid": "101300518"
                    }
                ]
            },
            {
                "city": "梧州",
                "disList": [
                    {
                        "district": "梧州",
                        "stationid": "101300601"
                    },
                    {
                        "district": "藤县",
                        "stationid": "101300602"
                    },
                    {
                        "district": "万秀",
                        "stationid": "101300603"
                    },
                    {
                        "district": "苍梧",
                        "stationid": "101300604"
                    },
                    {
                        "district": "蒙山",
                        "stationid": "101300605"
                    },
                    {
                        "district": "岑溪",
                        "stationid": "101300606"
                    },
                    {
                        "district": "长洲",
                        "stationid": "101300607"
                    },
                    {
                        "district": "龙圩",
                        "stationid": "101300608"
                    }
                ]
            },
            {
                "city": "贺州",
                "disList": [
                    {
                        "district": "贺州",
                        "stationid": "101300701"
                    },
                    {
                        "district": "昭平",
                        "stationid": "101300702"
                    },
                    {
                        "district": "富川",
                        "stationid": "101300703"
                    },
                    {
                        "district": "钟山",
                        "stationid": "101300704"
                    },
                    {
                        "district": "八步",
                        "stationid": "101300705"
                    },
                    {
                        "district": "平桂",
                        "stationid": "101300706"
                    }
                ]
            },
            {
                "city": "贵港",
                "disList": [
                    {
                        "district": "贵港",
                        "stationid": "101300801"
                    },
                    {
                        "district": "桂平",
                        "stationid": "101300802"
                    },
                    {
                        "district": "平南",
                        "stationid": "101300803"
                    },
                    {
                        "district": "港北",
                        "stationid": "101300804"
                    },
                    {
                        "district": "港南",
                        "stationid": "101300805"
                    },
                    {
                        "district": "覃塘",
                        "stationid": "101300806"
                    }
                ]
            },
            {
                "city": "玉林",
                "disList": [
                    {
                        "district": "玉林",
                        "stationid": "101300901"
                    },
                    {
                        "district": "博白",
                        "stationid": "101300902"
                    },
                    {
                        "district": "北流",
                        "stationid": "101300903"
                    },
                    {
                        "district": "容县",
                        "stationid": "101300904"
                    },
                    {
                        "district": "陆川",
                        "stationid": "101300905"
                    },
                    {
                        "district": "兴业",
                        "stationid": "101300906"
                    },
                    {
                        "district": "玉州",
                        "stationid": "101300907"
                    },
                    {
                        "district": "福绵",
                        "stationid": "101300908"
                    }
                ]
            },
            {
                "city": "百色",
                "disList": [
                    {
                        "district": "百色",
                        "stationid": "101301001"
                    },
                    {
                        "district": "那坡",
                        "stationid": "101301002"
                    },
                    {
                        "district": "田阳",
                        "stationid": "101301003"
                    },
                    {
                        "district": "德保",
                        "stationid": "101301004"
                    },
                    {
                        "district": "靖西",
                        "stationid": "101301005"
                    },
                    {
                        "district": "田东",
                        "stationid": "101301006"
                    },
                    {
                        "district": "平果",
                        "stationid": "101301007"
                    },
                    {
                        "district": "隆林",
                        "stationid": "101301008"
                    },
                    {
                        "district": "西林",
                        "stationid": "101301009"
                    },
                    {
                        "district": "乐业",
                        "stationid": "101301010"
                    },
                    {
                        "district": "凌云",
                        "stationid": "101301011"
                    },
                    {
                        "district": "田林",
                        "stationid": "101301012"
                    },
                    {
                        "district": "右江",
                        "stationid": "101301013"
                    }
                ]
            },
            {
                "city": "钦州",
                "disList": [
                    {
                        "district": "钦州",
                        "stationid": "101301101"
                    },
                    {
                        "district": "浦北",
                        "stationid": "101301102"
                    },
                    {
                        "district": "灵山",
                        "stationid": "101301103"
                    },
                    {
                        "district": "钦南",
                        "stationid": "101301104"
                    },
                    {
                        "district": "钦北",
                        "stationid": "101301105"
                    }
                ]
            },
            {
                "city": "河池",
                "disList": [
                    {
                        "district": "河池",
                        "stationid": "101301201"
                    },
                    {
                        "district": "天峨",
                        "stationid": "101301202"
                    },
                    {
                        "district": "东兰",
                        "stationid": "101301203"
                    },
                    {
                        "district": "巴马",
                        "stationid": "101301204"
                    },
                    {
                        "district": "环江",
                        "stationid": "101301205"
                    },
                    {
                        "district": "罗城",
                        "stationid": "101301206"
                    },
                    {
                        "district": "宜州",
                        "stationid": "101301207"
                    },
                    {
                        "district": "凤山",
                        "stationid": "101301208"
                    },
                    {
                        "district": "南丹",
                        "stationid": "101301209"
                    },
                    {
                        "district": "都安",
                        "stationid": "101301210"
                    },
                    {
                        "district": "大化",
                        "stationid": "101301211"
                    },
                    {
                        "district": "金城江",
                        "stationid": "101301212"
                    }
                ]
            },
            {
                "city": "北海",
                "disList": [
                    {
                        "district": "北海",
                        "stationid": "101301301"
                    },
                    {
                        "district": "合浦",
                        "stationid": "101301302"
                    },
                    {
                        "district": "海城",
                        "stationid": "101301304"
                    },
                    {
                        "district": "银海",
                        "stationid": "101301305"
                    },
                    {
                        "district": "铁山港",
                        "stationid": "101301306"
                    },
                    {
                        "district": "涠洲岛",
                        "stationid": "101301303"
                    }
                ]
            },
            {
                "city": "防城港",
                "disList": [
                    {
                        "district": "防城港",
                        "stationid": "101301401"
                    },
                    {
                        "district": "上思",
                        "stationid": "101301402"
                    },
                    {
                        "district": "东兴",
                        "stationid": "101301403"
                    },
                    {
                        "district": "港口",
                        "stationid": "101301404"
                    },
                    {
                        "district": "防城",
                        "stationid": "101301405"
                    }
                ]
            }
        ]
    },
    {
        "province": "海南",
        "cityList": [
            {
                "city": "海口",
                "disList": [
                    {
                        "district": "海口",
                        "stationid": "101310101"
                    },
                    {
                        "district": "秀英",
                        "stationid": "101310102"
                    },
                    {
                        "district": "龙华",
                        "stationid": "101310103"
                    },
                    {
                        "district": "琼山",
                        "stationid": "101310104"
                    },
                    {
                        "district": "美兰",
                        "stationid": "101310105"
                    }
                ]
            },
            {
                "city": "三亚",
                "disList": [
                    {
                        "district": "三亚",
                        "stationid": "101310201"
                    },
                    {
                        "district": "海棠",
                        "stationid": "101310213"
                    },
                    {
                        "district": "吉阳",
                        "stationid": "101310218"
                    },
                    {
                        "district": "天涯",
                        "stationid": "101310219"
                    },
                    {
                        "district": "崖州",
                        "stationid": "101310223"
                    }
                ]
            }, {
                "city": "儋州",
                "disList": [
                    {
                        "district": "儋州",
                        "stationid": "101310205"
                    }, {
                        "district": "东方",
                        "stationid": "101310202"
                    }, {
                        "district": "临高",
                        "stationid": "101310203"
                    }, {
                        "district": "澄迈",
                        "stationid": "101310204"
                    }, {
                        "district": "昌江",
                        "stationid": "101310206"
                    }, {
                        "district": "白沙",
                        "stationid": "101310207"
                    }, {
                        "district": "琼中",
                        "stationid": "101310208"
                    }, {
                        "district": "定安",
                        "stationid": "101310209"
                    }, {
                        "district": "屯昌",
                        "stationid": "101310210"
                    }, {
                        "district": "琼海",
                        "stationid": "101310211"
                    }, {
                        "district": "文昌",
                        "stationid": "101310212"
                    }, {
                        "district": "保亭",
                        "stationid": "101310214"
                    }, {
                        "district": "万宁",
                        "stationid": "101310215"
                    }, {
                        "district": "陵水",
                        "stationid": "101310216"
                    }, {
                        "district": "乐东",
                        "stationid": "101310221"
                    }, {
                        "district": "五指山",
                        "stationid": "101310222"
                    }
                ]
            },
            {
                "city": "三沙",
                "disList": [
                    {
                        "district": "三沙",
                        "stationid": "101310301"
                    },
                    {
                        "district": "西沙",
                        "stationid": "101310302"
                    },
                    {
                        "district": "中沙",
                        "stationid": "101310303"
                    },
                    {
                        "district": "南沙",
                        "stationid": "101310304"
                    },
                    {
                        "district": "黄岩岛",
                        "stationid": "101310305"
                    }
                ]
            }
        ]
    },
    {
        "province": "香港",
        "cityList": [
            {
                "city": "香港",
                "disList": [
                    {
                        "district": "香港",
                        "stationid": "101320101"
                    },
                    {
                        "district": "九龙",
                        "stationid": "101320102"
                    },
                    {
                        "district": "新界",
                        "stationid": "101320103"
                    }
                ]
            }
        ]
    },
    {
        "province": "澳门",
        "cityList": [
            {
                "city": "澳门",
                "disList": [
                    {
                        "district": "澳门",
                        "stationid": "101330101"
                    },
                    {
                        "district": "氹仔岛",
                        "stationid": "101330102"
                    },
                    {
                        "district": "路环岛",
                        "stationid": "101330103"
                    }
                ]
            }
        ]
    },
    {
        "province": "台湾",
        "cityList": [
            {
                "city": "台北",
                "disList": [
                    {
                        "district": "台北",
                        "stationid": "101340101"
                    },
                    {
                        "district": "桃园",
                        "stationid": "101340102"
                    },
                    {
                        "district": "新竹",
                        "stationid": "101340103"
                    },
                    {
                        "district": "宜兰",
                        "stationid": "101340104"
                    }
                ]
            },
            {
                "city": "高雄",
                "disList": [
                    {
                        "district": "高雄",
                        "stationid": "101340201"
                    },
                    {
                        "district": "嘉义",
                        "stationid": "101340202"
                    },
                    {
                        "district": "台南",
                        "stationid": "101340203"
                    },
                    {
                        "district": "台东",
                        "stationid": "101340204"
                    },
                    {
                        "district": "屏东",
                        "stationid": "101340205"
                    }
                ]
            },
            {
                "city": "台中",
                "disList": [
                    {
                        "district": "台中",
                        "stationid": "101340401"
                    },
                    {
                        "district": "苗栗",
                        "stationid": "101340402"
                    },
                    {
                        "district": "彰化",
                        "stationid": "101340403"
                    },
                    {
                        "district": "南投",
                        "stationid": "101340404"
                    },
                    {
                        "district": "花莲",
                        "stationid": "101340405"
                    },
                    {
                        "district": "云林",
                        "stationid": "101340406"
                    }
                ]
            }
        ]
    }
]
sql_create = """
CREATE TABLE IF NOT EXISTS area_cn (
id INT PRIMARY KEY AUTO_INCREMENT,
province CHAR(16),
city CHAR(16),
district CHAR(16),
stationid CHAR(9) UNIQUE NOT NULL
)
"""
cursor.execute(sql_create)
db.commit()
sql = """
INSERT INTO area_cn(province, city, district, stationid) VALUES (%s, %s, %s, %s)
    """
for province in area:
    for city in province['cityList']:
        for district in city['disList']:
            try:
                # 执行sql语句
                params = (province['province'], city['city'], district['district'], district['stationid'])
                cursor.execute(sql, params)
            except Exception as e:
                # 如果发生错误则回滚
                print(e)
                db.rollback()
# 提交到数据库执行
db.commit()
# 关闭数据库连接
db.close()
