# #
import json
import pickle
#
# #
# # #json work
# # dict_str = '{"Guru":"Mahendrakar","Cool": "Brother"}'
# # sets = '{1,2,3,4}'
# # print(" dict_str now type is {} ".format(dict_str))
# # print()
# #
# # #only (list,dict) support json.loads his convert only (str to orginal (list pe kaam karega aur  dict pe kaam karega) Only
# # print(type(json.loads('[1,2,34,5]'))) #his converted strlist to list
# # # ye sirf strlist aur strdict pe kaam karega nahi error dega
# #
# #
#
# # #ojson.dumps only (list,dict,tuple) -> his converted (list to strlist) or (tuple to tuplestr)
#
# # #ojson.dumps only (list,dict,tuple) -> his converted (list to strlist) or (tuplestr to tuple)
#
# # print(type(json.dumps((1,2,3,4))))
# #
# #
#json.dump(iterable,file) -> (only list or dict) -> tuple daala to texting.file me list me saare element chale jayenge

# with open('texting.txt',"w") as writefile:
#     json.dump({'like':'king'},writefile)
# # #
# # #json load his only read -> (list and strlist) or (strdict and dict)
with open('texting.txt') as readfile:
    print(type(json.load(readfile)))  # jaisa object dala hai wahi type milega
        #not normal list daala hai to normal list milega or (strlist daala hai to strlist milega)
# #
# #
# #
# # #pickle work
# # class method:
# #     pass
# #
# # #pickle.loads and pickle.dumps
# # a = bytes([1,2,3,4,5,253])
# # binary_creted = pickle.dumps(method()) # ye saare (iterables aur  objects) ko bhi binary format me convert  karsakta hai
# #
# # print(type(pickle.loads(binary_creted))) # ye binary format se normal format lata hai
# #
# #
# #
# #
# # #pickle.dump and pickle.load
# #
#
# # #pickle.dump((iterable,object,binary),file) # ye utf-16 format me data save karta hai
#
# # #pickle.dump((iterable,object,binary),file)
#
# # with open('texting.txt','rb+') as binaryfile:
# #     pickle.dump("Guru".encode(),binaryfile) # his take (iterable and objects and binary format also)
# #
# #     #pickle.load(file)
# #     with open('texting.txt','rb+') as binaryreadfile:
# #         print(pickle.load(binaryreadfile)) # binary format se orginal format lata hai
# #
# #     #note....
# #
# #     #pickle dump konsi bhi iterable and objects and binray format le sakta hai
# #     #pickle.load binary format se orginal format me lata hai
# #
# import pickle
#
#
# list = "Guru Mahendrakar"
#
# import os
# print('real',pickle.dumps('Guru Mahendrakar'))
#
# with open('texting.txt','wb') as f:
#     f.write(pickle.dumps("Guru Mahendrakar"))
#
# with open('texting.txt','rb') as rea:
#     print('yo',rea.read())
#     print(rea.tell())
#     rea.seek(0)
#     print(pickle.load(rea))
#
#
#
#
#
# #
# # import pickle
# #
# # dict_ = '{"Guru":"Mahendrakar","City":"Bhalki"}'
# #
# # with open('texting.txt','rb+') as f:
# #     pickle.dump(dict_,f) # stored( ��*       �&{"Guru":"Mahendrakar","City":"Bhalki"}�.) UTF-8 FORMAT
# #     # pickle.dump() # class ke object bhi jaa sakte hai
# #
# #
# # with open('texting.txt','rb') as f:
# #     print(pickle.load(f)) # return normal format UTF-8 to reading Foramt
# #
# #     # dump karte waqt jaisa object daala hai Wo HI type(dict,str,list,set,tuple,object) # milega


# with open('texting.txt') as f:
#
#     data  = f.read(5)
#     while len(data)>0:
#         print(data)
#         data = f.read(5)
#



















# with open('texting.txt') as file:
#     json.


