# encoding: utf-8
import aiml
import json

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
print('傑森還有愛麗絲')
while True:
    utterance = input("你說：")
    d = {'id': '12345678', 'name': str(kernel.respond(utterance)),'url':'www', 'image':'jpg'}
    print('傑森說:',d)

# 不懂你意思