import re
def get_paragraph():
    r = open('log.txt')

    while True:
        item = ''
        for i in r:
            if i == '\n':
                break
            item += i

        if not item:
            break
        # print(item)
        yield  item
    r.close()
    return


def get_address(port):
    for data in get_paragraph():
        r = re.match(r'\S+',data)
        if port == r.group():
            patter = r'[0-9a-z]{4}\.[0-9a-z]{4}\.[0-9a-z]{4}'
            result = re.search(patter,data)
            if result:
                return  result.group()
            else:
                return "没有改玩意"

    return "port error"

print(get_address("TenGigE0/0/2/3"))