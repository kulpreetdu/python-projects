import requests
import json

parameter={"page":2}
resp_get=requests.get("https://reqres.in/api/users",params=parameter)
print(resp_get.url)
sta_code=resp_get.status_code
print(sta_code)
print(type(resp_get))
print(resp_get)
print(resp_get.text)
print(resp_get.content)
resp_json_val=resp_get.json()
print(resp_json_val['total_pages'])
print(resp_json_val['total'])
assert resp_json_val['total']==12,"total is not matching"
print(resp_get.headers)
print(resp_json_val['data'][0]['email'])
assert(resp_json_val['data'][0]['email']).endswith('reqres.in'),"email ending is not matching"
if sta_code ==200:
    assert True==True
else:
    assert True==False
#assert sta_code==201,"status code does not match"
"""
post_data={
    "name": "morpheus",
    "job": "leader"
}
"""

data_json=open("post_data.json","r").read()
resp_post=requests.post("https://reqres.in/api/users",data=json.loads(data_json))
print(resp_post)
print(resp_post.url)
print(resp_post.json())
resp_json_post_val=resp_post.json()
resp_json_post_val['job']='automation'
print(resp_json_post_val)
assert resp_json_post_val['job']=='automation',"name is being edited"


reg_post_data={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
reg_resp=requests.post("https://reqres.in/api/register",data=reg_post_data)
print(reg_resp)
print(reg_resp.status_code)
print(reg_resp.json())
reg_resp_token=reg_resp.json()
reg_resp_t=reg_resp_token['token']
print(reg_resp_t)
"""
data_put={
    "name": "morpheus",
    "job": "zion resident"
}
"""
data_put=open("data_put.json","r").read()
data_put_resp=requests.put("https://reqres.in/api/users/2",data=json.loads(data_put))
print(data_put_resp)
print(data_put_resp.status_code)
print(data_put_resp.json())


data_patch=open("data_patch.json","r").read()
data_patch_resp=requests.patch("https://reqres.in/api/users/2",data=json.loads(data_patch))
print(data_patch_resp)
print(data_patch_resp.status_code)
print(data_patch_resp.json())

del_resp_data=requests.delete("https://reqres.in/api/users/2")
print(del_resp_data)
print(del_resp_data.status_code)

resp_time=requests.get("https://httpbin.org/delay/3",timeout=5)
print(resp_time)
print(resp_time.status_code)

auth_resp=requests.get("https://the-internet.herokupp.com/basic_auth",auth=('abc','abc'))
print(auth_resp)
print(auth_resp.status_code)

auth_resp_data=requests.get("https://postman-echo.com/basic-auth",auth=('postman','password'))
print(auth_resp_data)