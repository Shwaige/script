import requests
import random
from flask import Flask, request, jsonify
import threading

app = Flask(__name__)
app.debug = True


i =1
while i <10:
        a = "小老虎" + str(random.randint(1, 100000))

        data = {
            "openId": None,
            "type": 1,
            "uploadFileSize": 0,
            "answers": [
                {
                    "queId": 103007631,
                    "queType": 2,
                    "values": [
                        {
                            "value": a
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007632,
                    "queType": 9,
                    "values": [
                        {
                            "value": "https://gushitong.baidu.com/stock/hk-09888"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007633,
                    "queType": 4,
                    "values": [
                        {
                            "value": "2023-02-17"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007634,
                    "queType": 14,
                    "values": [
                        {
                            "value": "2023-02-17 00:00:00~2023-03-14 00:00:00"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007635,
                    "queType": 7,
                    "values": [
                        {
                            "value": "19882323422"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007636,
                    "queType": 6,
                    "values": [
                        {
                            "value": "19882323422@qq.com"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007637,
                    "queType": 10,
                    "values": [
                        {
                            "id": 42795740,
                            "otherInfo": None,
                            "value": "A"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007638,
                    "queType": 11,
                    "values": [
                        {
                            "id": 42795743,
                            "otherInfo": None,
                            "value": "未命名1"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007639,
                    "queType": 12,
                    "values": [
                        {
                            "id": 42795747,
                            "otherInfo": None,
                            "value": "BB"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007640,
                    "queType": 21,
                    "values": [
                        {
                            "value": "山西省",
                            "otherInfo": "140000",
                            "id": 1
                        },
                        {
                            "value": "大同市",
                            "otherInfo": "140200",
                            "id": 2
                        },
                        {
                            "value": "平城区",
                            "otherInfo": "140213",
                            "id": 3
                        },
                        {
                            "value": "你说我说",
                            "id": 4
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007641,
                    "queType": 1,
                    "values": [],
                    "tableValues": []
                },
                {
                    "queId": 103007642,
                    "queType": 16,
                    "values": [
                        {
                            "value": "<p><a href=\"https://so.gushiwen.cn/mingju/juv_f65c48d99ca7.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">雨打梨花深闭门，忘了青春，误了青春。</a></p><p><span style=\"color: rgb(101, 100, 95);\">——</span></p><p><a href=\"https://so.gushiwen.cn/shiwenv_826758a2d666.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">唐寅《一剪梅·雨打梨花深闭门》</a></p><p><a href=\"https://so.gushiwen.cn/mingju/juv_23fccdb0f64e.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">晓看天色暮看云，行也思君，坐也思君。</a></p><p><span style=\"color: rgb(101, 100, 95);\">——</span></p><p><a href=\"https://so.gushiwen.cn/shiwenv_826758a2d666.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">唐寅《一剪梅·雨打梨花深闭门》</a></p><p><a href=\"https://so.gushiwen.cn/mingju/juv_ba800fd1c88a.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">滚滚长江东逝水，浪花淘尽英雄。</a></p><p><span style=\"color: rgb(101, 100, 95);\">——</span></p><p><a href=\"https://so.gushiwen.cn/shiwenv_284e20a25958.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">杨慎《临江仙·滚滚长江东逝水》</a></p><p><a href=\"https://so.gushiwen.cn/mingju/juv_c3983b03a6ad.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">从前种种，譬如昨日死；从后种种，譬如今日生</a></p><p><span style=\"color: rgb(101, 100, 95);\">——</span></p><p><a href=\"https://so.gushiwen.cn/guwen/bookv_46653FD803893E4F39579D8097181448.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">《了凡四训·立命之学》</a></p><p><a href=\"https://so.gushiwen.cn/mingju/juv_0596ce87f7a3.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">怕相思，已相思，轮到相思没处辞，眉间露一丝。</a></p><p><span style=\"color: rgb(101, 100, 95);\">——</span></p><p><a href=\"https://so.gushiwen.cn/shiwenv_71a85f935e90.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">俞彦《长相思·折花枝》</a></p><p><a href=\"https://so.gushiwen.cn/mingju/juv_12bca7c2bfc5.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">青山依旧在，几度夕阳红。</a></p><p><span style=\"color: rgb(101, 100, 95);\">——</span></p><p><a href=\"https://so.gushiwen.cn/shiwenv_284e20a25958.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">杨慎《临江仙·滚滚长江东逝水》</a></p><p><a href=\"https://so.gushiwen.cn/mingju/juv_20f2d6205f65.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">天地有万古，此身不再得；人生只百年，此日最易过。</a></p><p><span style=\"color: rgb(101, 100, 95);\">——</span></p><p><a href=\"https://so.gushiwen.cn/guwen/bookv_46653FD803893E4F06A5346C0953A18B.aspx\" rel=\"noopener noreferrer\" target=\"_blank\" style=\"color: rgb(25, 83, 125);\">《菜根谭·概论》</a></p><p><br></p>"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007644,
                    "queType": 18,
                    "values": [],
                    "tableValues": [
                        [
                            {
                                "queId": 103007645,
                                "queType": 2,
                                "values": [
                                    {
                                        "value": "我是单行 文章"
                                    }
                                ],
                                "referValues": [],
                                "tableValues": []
                            },
                            {
                                "queId": 103007646,
                                "queType": 8,
                                "values": [
                                    {
                                        "value": "22"
                                    }
                                ],
                                "referValues": [],
                                "tableValues": []
                            },
                            {
                                "queId": 103007647,
                                "queType": 7,
                                "values": [
                                    {
                                        "value": "17623424222"
                                    }
                                ],
                                "referValues": [],
                                "tableValues": []
                            }
                        ]
                    ],
                    "previousTableRowOrdinalList": [
                        -1
                    ]
                },
                {
                    "queId": 103007648,
                    "queType": 19,
                    "values": [
                        {
                            "value": "我是回收站的数据"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007649,
                    "queType": 5,
                    "values": [
                        {
                            "id": 1598283,
                            "value": "32537580@qq.com"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007650,
                    "queType": 22,
                    "values": [
                        {
                            "id": 276965,
                            "value": "轻析测试部门",
                            "otherInfo": "{\"deptIcon\":\"&#xe74e;\",\"parentDeptNames\":[]}"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007654,
                    "queType": 8,
                    "values": [
                        {
                            "value": "33"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007655,
                    "queType": 8,
                    "values": [
                        {
                            "value": "44"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007656,
                    "queType": 8,
                    "values": [
                        {
                            "value": "55"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007657,
                    "queType": 8,
                    "values": [
                        {
                            "value": "66"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007658,
                    "queType": 8,
                    "values": [
                        {
                            "value": "77"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007659,
                    "queType": 8,
                    "values": [
                        {
                            "value": "88"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007660,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007661,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007662,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007663,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007664,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007665,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007666,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007667,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007668,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007669,
                    "queType": 2,
                    "values": [
                        {
                            "value": "你说"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007651,
                    "queType": 3,
                    "values": [
                        {
                            "value": "李鸿章(1823~1901),安徽合肥人,世人多尊称李中堂,也称李合肥。准军创始人和统帅、洋务运动的主要倡导者之一、晚清重臣,官至直隶总督兼北洋通商大臣,授文华殿大学士。日本首相伊藤博文视其为大清帝国中唯一有能耐和世界列强一争长短之人。他的一生伴随着清王朝从中兴走向衰落,直至灭亡。无论生前还是死后,他都是个颇有争议的人物。"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007652,
                    "queType": 8,
                    "values": [
                        {
                            "value": "44"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007653,
                    "queType": 25,
                    "values": [],
                    "referValues": [
                        {
                            "appKey": "78005e88",
                            "applyId": 185867314,
                            "values": [
                                {
                                    "associatedQueType": None,
                                    "auditValue": None,
                                    "auditValueDescription": None,
                                    "dataId": None,
                                    "dateType": 0,
                                    "previousTableRowOrdinalList": [],
                                    "queId": 103007630,
                                    "queTitle": "单行文字",
                                    "queType": 2,
                                    "questionOrdinal": 0,
                                    "referValues": [],
                                    "supId": None,
                                    "tableValues": [],
                                    "values": [
                                        {
                                            "dataId": 5089563090,
                                            "dataValue": "我是回收站的数据",
                                            "email": None,
                                            "id": None,
                                            "optionId": None,
                                            "ordinal": None,
                                            "otherInfo": None,
                                            "pluginValue": None,
                                            "queId": 103007630,
                                            "value": "我是回收站的数据"
                                        }
                                    ]
                                }
                            ],
                            "displayValues": [
                                {
                                    "associatedQueType": None,
                                    "auditValue": None,
                                    "auditValueDescription": None,
                                    "dataId": None,
                                    "dateType": 0,
                                    "previousTableRowOrdinalList": [],
                                    "queId": 103007630,
                                    "queTitle": "单行文字",
                                    "queType": 2,
                                    "questionOrdinal": 0,
                                    "referValues": [],
                                    "supId": None,
                                    "tableValues": [],
                                    "values": [
                                        {
                                            "dataId": 5089563090,
                                            "dataValue": "我是回收站的数据",
                                            "email": None,
                                            "id": None,
                                            "optionId": None,
                                            "ordinal": None,
                                            "otherInfo": None,
                                            "pluginValue": None,
                                            "queId": 103007630,
                                            "value": "我是回收站的数据"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "queId": 103007670,
                    "queType": 21,
                    "values": [
                        {
                            "value": "山西省",
                            "otherInfo": "140000",
                            "id": 1
                        },
                        {
                            "value": "大同市",
                            "otherInfo": "140200",
                            "id": 2
                        },
                        {
                            "value": "新荣区",
                            "otherInfo": "140212",
                            "id": 3
                        },
                        {
                            "value": "在北京大平",
                            "id": 4
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007671,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007672,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007673,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007674,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007675,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007676,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007677,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007678,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007679,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007680,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007681,
                    "queType": 3,
                    "values": [
                        {
                            "value": "雨打梨花深闭门，忘了青春，误了青春。——唐寅《一剪梅·雨打梨花深闭门》\n晓看天色暮看云，行也思君，坐也思君。——唐寅《一剪梅·雨打梨花深闭门》\n滚滚长江东逝水，浪花淘尽英雄。——杨慎《临江仙·滚滚长江东逝水》\n从前种种，譬如昨日死；从后种种，譬如今日生——《了凡四训·立命之学》\n怕相思，已相思，轮到相思没处辞，眉间露一丝。——俞彦《长相思·折花枝》\n青山依旧在，几度夕阳红。——杨慎《临江仙·滚滚长江东逝水》\n天地有万古，此身不再得；人生只百年，此日最易过。——《菜根谭·概论》"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007682,
                    "queType": 8,
                    "values": [
                        {
                            "value": "1"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007683,
                    "queType": 8,
                    "values": [
                        {
                            "value": "1"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007684,
                    "queType": 8,
                    "values": [
                        {
                            "value": "1"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007685,
                    "queType": 4,
                    "values": [
                        {
                            "value": "2023-02-03 00:00:00"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007686,
                    "queType": 4,
                    "values": [
                        {
                            "value": "2023-02-03 00:00:00"
                        }
                    ],
                    "tableValues": []
                },
                {
                    "queId": 103007687,
                    "queType": 4,
                    "values": [
                        {
                            "value": "2023-02-11 00:00:00"
                        }
                    ],
                    "tableValues": []
                }
            ],
            "beingSaveSignature": False
        }
        headers = {"Content-Type": "application/json", "token": "4e034e4e-63ab-42c6-b50a-aca4fda0d460", "wsId": "1"}
        reponse = requests.post(url="https://stress-test.oalite.com/api/app/70c12940/apply", json=data, headers=headers)

        print(reponse.json())








