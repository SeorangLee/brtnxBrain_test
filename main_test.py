
import log
import login_test

data = []

# 가입
login_create_account = login_test.signUp()
data.append(login_create_account)
#test 계정 삭제
login_delete_account = login_test.remove_test_id()
data.append(login_delete_account)
print(data)
#로그인
login_login = login_test.login()
data.append(login_login)
print(data)
log.mkLog(data) #로그파일 생성