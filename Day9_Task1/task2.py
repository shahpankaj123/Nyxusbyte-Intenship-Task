import json
class A:
    def serializeddata(self,data):
        d=json.dumps(data)
        print("json data:",d)
    def  deserializeddata(self,data):
        d=json.loads(data)
        print("python obj:",d)


x=A()
x.serializeddata({'name':'pankaj','age':20})
x.deserializeddata('{ "name":"John", "age":30}')



