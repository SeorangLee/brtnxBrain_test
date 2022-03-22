
import log
import login_test

data = []


signUp_create = login_test.signUp()
data.append(signUp_create)
# print(data)

signUp_delete = login_test.remove_test_id()
data.append(signUp_delete)
print(data)
log.mkLog(data) #로그파일 생성