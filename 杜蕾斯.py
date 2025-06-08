import requests

# 多账号配置（账号token和对应备注）
accounts = [
    {"token": "", "remark": "账号1"},
    {"token": "另一个token值", "remark": "账号2"},
    # 可以继续添加更多账号...
]

# 公共请求头
base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b) XWEB/8555',
    'content-type': 'application/json;charset=utf-8',
    'sid': '10006',
    'xweb_xhr': '1',
    'platform': 'MP-WEIXIN',
    'enterprise-hash': '10006',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://servicewechat.com/wxe11089c85860ec02/45/page-frame.html',
    'accept-language': 'zh-CN,zh;q=0.9'
}

# API地址
sign_url = 'https://vip.ixiliu.cn/mp/sign/applyV2'
lottery_url = 'https://vip.ixiliu.cn/mp/activity.lottery/draw?snId=403868335815296&channelSn=0'

def make_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

for account in accounts:
    # 设置当前账号的token
    current_headers = base_headers.copy()
    current_headers['access-token'] = account['token']
    
    print(f"\n======= 开始处理 {account['remark']} =======")
    
    # 执行签到
    sign_result = make_request(sign_url, current_headers)
    if 'error' in sign_result:
        print(f"签到失败: {sign_result['error']}")
    else:
        print(f"签到结果: {sign_result.get('message', '无返回信息')}")
    
    # 执行抽奖
    lottery_result = make_request(lottery_url, current_headers)
    if 'error' in lottery_result:
        print(f"抽奖失败: {lottery_result['error']}")
    else:
        print(f"抽奖结果: {lottery_result.get('message', lottery_result)}")
    
    print("======= 处理完成 =======\n")