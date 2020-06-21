import codecs
def get_info(path):
    web_info = {}
    config = codecs.open(path,'r','utf-8')
    for line in config:
        list01 = [ele.strip()for ele in line.split('=')]
        print(list01)
        web_info.update(dict([list01]))

    return web_info
