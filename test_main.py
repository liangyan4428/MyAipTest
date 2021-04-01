#! -*-coding:utf-8 -*-
import pytest,requests,allure,json
from readExcel import readxls,creat_report,readxls_new


class Test_main():

    @allure.feature("接口测试")
    @allure.story("接口测试1111")
    @pytest.mark.parametrize("code,cookie,data,url,res_json",readxls_new())
    def test_add(self,code,cookie,data,url,res_json):
        global false, null, true
        false = null = true = ''
        if code =="GET":
            res = requests.get(params = eval(data), url = url)
        elif code == "POST":
            res = requests.post(headers = eval(cookie),data = eval(data),url = url)
        assert url == res.url
        # separators：将s.json()返回的结果去除空格;ensure_ascii = False:将返回的unicode编码转成中文
        assert res_json == json.dumps(res.json(),separators = (',', ':'), ensure_ascii = False)

if __name__ == '__main__':
    path = "D:/MyAipTest/myreport"
    creat_report(path)
    # pytest.main()
    # hea = {"app":"324160","ver":"210315","appversion":"202103014010.100","pkg":"com.cutt.app324160","token":"r4HCCWMHRF6HqGpxOKNVIBshkZlMgltbcXFpBCtrqWejlffTxxOW02","device":"6b0b167396b0a736e1e65bb85b78f11de8c3ccd5","Cookie":"zy_headers='%7B%22WHH%22%3A%2221r7j0%22%2C%22MbU%22%3A%22170276%22%2C%22aW%22%3A%22WHH21r7j0+SDROKb+10170207r070.700+%281mk1l.170276%29+%28SDROKb77%2Cl%3B+Sdn+7r.0.7%29+cK%2FSDROKb%22%2C%22hbMSJb%22%3A%22jP0P7jk2mjP0Wk2jb7bj6PPl6Pkli77hblJ2JJh6%22%2C%22HtL%22%3A%22JOI.JaZZ.WHH21r7j0%22%2C%22hSh%22%3A%22k7111jlr11l6%22%2C%22ZOtbK%22%3A%22Ur3CCXf3Qoj3T8HvdNgq4BVRtYufLuZPJFoHBCZUTXbsuiiyvvdX01%22%7D___7j7k7krm71___702mPj70bb'"}
    # da = {"targetUserId":"501162707187"}
    #
    # r = requests.post(headers = hea,
    #               data= da,
    #               url = "http://romeo.test.zhiyueapp.cn/api/romeo/userInfo/mutualInterested")
    #
    # print(r.status_code)
    # print(r.json())


a= {
"Host": "api.jwshq.cn",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": 1,
"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G9650 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"app": 324160,
"ftdf": "0702e10a52dc2b044ca18bd1f1d7831d9346",
"cuttos": 10,
"ver": 210113,
"appversion": 20210121050.040,
"serialnumber": "",
"mid": "09108C06AE71112BE34270DD921AA0EB",
"targetsdkversion": 26,
"pkg": "com.jianwangyuangong",
"token": "r4HCCWMHRF6HqGpxJm9kDxznY0awAM9ACBP3GgvafwqjlyOycAMPDf",
"osversion": "",
"imei": "",
"x-digest": "1611813876796_330d55f4_ad1f28b36b1d72d2228c82e1bc619332",
"device": "70dd2eac62c142a7",
"androidid": "70dd2eac62c142a7",
"X-Requested-With": "com.jianwangyuangong",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"Cookie": "zy_headers='%7B%22WHH%22%3A%2221r7j0%22%2C%22MbU%22%3A%22170772%22%2C%22VbUSWugaIPbU%22%3A%22%22%2C%22SIbS%22%3A%22%22%2C%22aW%22%3A%2221r7j0+10170717060.0r0.170772+%28VWIVaKL%2Cnf-8mj60%3B+AKhUOSh+70%3B+cK%2FVWIVaKL-nf-8mj60%29%22%2C%22hbMSJb%22%3A%22k0hh1bWJj1J7r1Wk%22%2C%22HtL%22%3A%22JOI.sSWKpWKLwaWKLOKL%22%2C%22WKhUOSh4c%22%3A%22k0hh1bWJj1J7r1Wk%22%2C%22hSh%22%3A%22k7717krmk2rk%22%2C%22ZOtbK%22%3A%22Ur3CCXf3Qoj3T8Hv5ImtcvxKG0WpAfmACBD28LMWipTsuwdwJAfDci%22%7D___7j77l7k7k6___jb0rl1m1Jr'"
}

