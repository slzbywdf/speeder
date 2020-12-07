# 网页分析
# if (!window.__cfRLUnbockHandlers) return false: checkin()
# https://www.speederss.best/theme/malio/js/malio.js?v1 -->
# function checkin(){
#     if(!csKdOsOtLF.includes(location.host)){
#         return false;
#     };
#     $.ajax({'type':'POST','url':'/user/checkin','dataType':'json',
#             'success':function(_0x4033d6){$('#checkin-div').html('<a href="#" class="btn btn-icon disabled icon-left btn-primary"><i class="far fa-edit"></i>'+i18n['alredy-got-daily-bonus']+'</a>');swal(i18n['success-got-daily-bonus'],_0x4033d6['msg'],'success');},
#             'error':function(_0x212f1c){swal('绛惧埌澶辫触','鍙戦€佽姹傚け璐�','error');}});
#     }

# $.ajax({
#         type: "POST",
#         url: "/auth/login",
#         dataType: "json",
#         data: {
#           email: $("#email").val(),
#           passwd: $("#password").val(),
#           code: $("#2fa-code").val(),          remember_me: $("#remember-me:checked").val()        },
#         success: function (data) {
#           if (data.ret == 1) {
#             window.location.assign('/user')
#           } else if(data.ret == 2) {
#             $('.login-form-item').hide('500');
#             $('form').removeClass('was-validated');
#             $('#2fa-form').show('fast');
#                                   } else {
#                                     var errorMsg = '密码或邮箱不正确';
#             if (twoFA == true) {
#               errorMsg = '两步验证码错误'
#             }
#             swal('出错了', errorMsg, 'error');
#           }
#         }
#       });

import requests
import time
import config

class speeder_checkin():
    """
    用于speeder每日打卡，获取流量用的脚本
   """
    def __init__(self):
        self.login_url = "https://www.speederss.best/auth/login"
        self.check_url = "https://www.speederss.best/user/checkin"
        user_name = config.user_name
        password = config.password
        self.login_data = {"email": user_name, "passwd": password, "code":""}
        self.cookie = None

    def login(self):
        try:
            r = requests.post(self.login_url, self.login_data)
        except Exception as e:
            print("访问%s异常"%self.login_url)
        else:
            if r.status_code == 200 and eval(r.text)["ret"] == 1:
                self.cookie = r.cookies.get_dict()
                print("登陆成功")
                return True
            else:
                print("登陆%s异常" % self.login_url, r.status_code, r.text)
        return False

    def check_in(self):
        try:
            r = requests.post(self.check_url, cookies=self.cookie)
            if r.status_code == 200 and eval(r.text)["ret"] == 1:
                print("签到成功")
                return True
            else:
                print("签到异常", r.status_code, eval(r.text))
        except Exception as e:
            print(e)
            print("签到异常")

    def run(self):
        while True:
            flag = self.login()
            if flag:
                self.check_in()
            else:
                break
            time.sleep(24*3600)

ins = speeder_checkin()
ins.run()