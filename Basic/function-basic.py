#!/usr/bin/python
#Server_List = "n7prserver1066.starwave.com , n7prserver1074.starwave.com , n7prserver1076.starwave.com , n7prserver1072.starwave.com"
Server_List = "/Users/Arun/server.list"


def Server_Details():
    with open(Server_List, 'r') as server:
        for x in server.readline:
            return x


Server = Server_Details()
print(Server)
