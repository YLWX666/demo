import yaml

# with open("./data.yml","r",) as f:
#     data = yaml.load(f)
#     for i in data.get('Test').keys:
#         new_data = data.get('Test').get(i)
# //////////////////////////////////////////////////////////
with open("./data.yml","r",encoding="utf-8") as f:

    data = yaml.load(f)
    print(data)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# dict02 = {"a":1,"b":2}
#
# def dict01(**kwargs):
#     print(kwargs)
# dict01(a=1,b=2)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# dict01 = {"a":1,"b":2}
# with open("./data.yml","w") as f:
#     f.write(yaml.dump(dict01))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import yaml
# f = '''
# ---
# name: James
# age: 20
# ---
# name: Lily
# age: 19
# '''
# y = yaml.load_all(f)
# for data in y:
#     print(data)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

