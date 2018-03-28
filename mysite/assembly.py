
# 模态框输入
class InputBlock:
    def __init__(self, ID='', holder='', val=''):
        self.id = ID
        self.val = val
        self.holder = holder


register = [
    InputBlock('Rusername', '请输入您的用户名', 'Username'),
    InputBlock('Rpassword', '请输入您的密码', 'Password'),
    InputBlock('Rpassword_confirm', '请再次输入密码', 'Confirm Password'),
    InputBlock('Remail', '请输入您的邮箱（选填）', 'Email address')
]

login = [
    InputBlock('Lusername', '请输入您的用户名', 'Username'),
    InputBlock('Lpassword', '请输入您的密码', 'Password'),
]

modals = [register, login]

if __name__ == '__main__':
    print(register)