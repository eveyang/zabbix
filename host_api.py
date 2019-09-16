import json
import requests
import urllib.request, urllib.error, urllib.parse
# coding=utf-8
url = 'http://114.116.233.92/zabbix/api_jsonrpc.php'
headers = {
        'Content-Type': 'application/json-rpc'
    }
def auth_token():
   # zabbix的登陆API接口(python格式)
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "ss100515"
        },
        "id": 1,
        "auth": None,
    }

    json_data = json.dumps(data)

    res = requests.post(url, data=json_data, headers=headers)
    res_data_dic = json.loads(res.text)

    is_success = res_data_dic.get('result')
    return is_success
    #print(is_success)
class host:
    def host_get(self,hostid=None):

        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                #"output":["hostid","host","name","ip"],
                "output":'extend',
                "selectGroups":"extend",
                "selectInterfaces":"extend",
                "filter": {
                    #"host": [host],
                    "hostid":hostid,
                    #"name":[name],
                    #"ip":[ip]
                }
            },
            "auth": auth_token(),
            "id": 1,
        }
        try:
            result = requests.post(url=url,headers=headers,data=json.dumps(data))
            print(result.text)
        except Exception as e:
            print(f"{e}")

    def host_create(self,ip,groupid,tempid,host):
        creat_data = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": host,
                "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": ip,
                        "dns": "",
                        "port": "10050"
                    }
                ],
                "groups": [
                    {
                        "groupid": groupid
                    }
                ],
                "templates": [
                    {
                        "templateid": tempid
                    }
                ],


            },
            "auth": auth_token(),
            "id": 1
        }
        json.dumps(creat_data,ensure_ascii=False)
        result = requests.post(url=url, headers=headers, data=json.dumps(creat_data))
        print(result.text)
    def host_delte(self,hostid=None):
        #self.hostid=hostid
        del_data = {
            "jsonrpc": "2.0",
            "method": "host.delete",
            "params": [
                hostid
            ],
            "auth": "04e93171f33ec1242854dde3563a009f",
            "id": 1
        }
        result = requests.post(url=url, headers=headers, data=json.dumps(del_data))
        print(result.text)
    def host_update(self,hostid,templates,host,name,status=0,):
        update_data={
            "jsonrpc": "2.0",
            "method": "host.update",
            "params": {
                "hostid": hostid,
                "status": 1,
                "host":host,
                "name":name,
                #"groups": groupid,
                "templates":templates
            },
            "auth": "04e93171f33ec1242854dde3563a009f",
            "id": 1
        }
        result = requests.post(url=url, headers=headers, data=json.dumps(update_data))
        print(result.text)

class Template:
    def get_tem(self,host):
        data_get = {
            "jsonrpc": "2.0",
            "method": "template.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": [
                        host
                    ]
                }
            },
            "auth": auth_token(),
            "id": 1
        }

        result = requests.post(url=url, headers=headers, data=json.dumps(data_get))
        print(result.text)

    def create_tem(self,host,groupid):
        create_data={
    "jsonrpc": "2.0",
    "method": "template.create",
    "params": {
        "host": host,
        "groups": {
            "groupid": groupid
        },

    },
    "auth": auth_token(),
    "id": 1
}
        result = requests.post(url=url, headers=headers, data=json.dumps(create_data))
        print(result.text)
    def del_tem(*args):
        del_data={
    "jsonrpc": "2.0",
    "method": "template.delete",
    "params": [
        *args,
    ],
    "auth": auth_token(),
    "id": 1
}
        result = requests.post(url=url, headers=headers, data=json.dumps(del_data))
        print(result.text)
    def update_tem(self,host,name,templates):
        update_tem={
    "jsonrpc": "2.0",
    "method": "template.update",
    "params": {
        "templateid": templates,
        "name": name,
         "host":host
    },
    "auth": auth_token(),
    "id": 1
}
        result = requests.post(url=url, headers=headers, data=json.dumps(update_tem))
        print(result.text)
def problem():
    pro_data={
    "jsonrpc": "2.0",
    "method": "hostinterface.get",
    "params": {
        "output": "interfaceid",
        "hostids": "10288"
    },

    "auth": auth_token(),
    "id": 1
}
    result = requests.post(url=url, headers=headers, data=json.dumps(pro_data)).json()
    print(result['result'])
problem()