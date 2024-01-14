# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def hashANDdict(n, d):
#     dic = {}
#     s = set()
#     d = d.split()
#     for i in range(0, len(d) - 1, 2):
#         z = int(d[i])
#         if dic.get(z):
#             z = dic.get(z)
#         s.add(int(d[i] + d[i + 1]))
#         s.add(int(d[i + 1] + d[i]))
#         dic[int(d[i])] = int(d[i + 1])
#         dic[int(d[i + 1])] = z
#     dic[n + 1] = n + 1
#     dic[n + 2] = n + 2
#     print(dic)
#     # Сортировка
#     list_keys = list(dic.keys())
#     list_keys.sort()
#     dic2 = {}
#     for i in list_keys:
#         # print(i, ':', dic[i])
#         dic2[i] = dic[i]
#
#     # print(dic2)
#     return dic2, s

# import botFUTURAMA
def hashANDdict(d):
    dic = {}
    s = set()
    d = d.split()
    n = int(d[0])
    print(n)
    d = d[1:]
    print(d)
    for i in range(0, len(d) - 1, 2):
        z = int(d[i])
        fl = True
        if dic.get(z):
            z = dic.get(z)
            if dic.get(int(d[i + 1])):
                dic[int(d[i])] = dic[int(d[i + 1])]
                fl = False
        s.add(int(d[i] + d[i + 1]))
        print(int(d[i] + d[i + 1]))
        s.add(int(d[i + 1] + d[i]))
        print(int(d[i + 1] + d[i]))
        # dic[int(d[i])] = int(d[int(d[i + 1])])
        if fl:
            dic[int(d[i])] = int(d[i + 1])
        print(int(d[i + 1]))
        dic[int(d[i + 1])] = z
    dic[n + 1] = n + 1
    dic[n + 2] = n + 2
    print(dic)
    # Сортировка
    list_keys = list(dic.keys())
    list_keys.sort()
    dic2 = {}
    for i in list_keys:
        # print(i, ':', dic[i])
        dic2[i] = dic[i]

    print("@@@@@@", dic2)
    return dic2, s
# def swapd(dict, )

def algoritm1(dict, set):
    # print(dict)
    # print(set)

    post = len(dict)
    post1 = len(dict) - 1
    print(dict[post1], 1, sep='')
    print(dict[post], 2, sep='')
    # print(dict)
    dict[len(dict) - 1] = dict[1]
    dict[1] = len(dict) - 1
    set.add((len(dict) - 1) * 10 + 1)
    set.add(10 + len(dict) - 1)
    # print(set)
    # print(dict)
    dict[len(dict)] = dict[2]
    dict[2] = len(dict)
    set.add(len(dict) * 10 + 2)
    set.add(20 + len(dict))
    # set.add(post * 10 + post1)
    # set.add(post1 * 10 + post)
    # Всё для предпоследнего
    x = (len(dict) - 1)
    y = (dict[len(dict) - 1])
    flag = True
    flag1 = True
    flag2 = True
    flag3 = True
    while(len(dict) != 2):
        flag3 = True
        # print("нормальный", dict)
        # print("if", x)
        # print("if", x * 10 + dict[x])


        if flag:
            if (post not in dict):
                flag2 = False
            if (post1 not in dict):
                flag1 = False
            # print("Vafefd", x * 10 + dict[x])
            if flag1 and (x * 10 + dict[x]) not in set:
                if (dict[dict[post1]] == 1) and len(dict) != 4:
                    flag = False
                    continue
                # deli то что удаляем
                # print("QQQQQ", dict)
                deli = dict[post1]
                if deli == post:
                    flag2 = False
                # То что надо напечатать
                print(((post1) * 10 + dict[post1]))

                set.add(((post1) * 10 + dict[post1]))
                # print("AAAAAAAA", ((post1) * 10 + dict[post1]))
                # set.add(((len(dict) - 1) * 10 + dict[len(dict) - 1]))
                dict[post1] = dict[dict[post1]]
                # print("fwefwef", deli)
                del dict[deli]
                # print("словарик", dict)
                # dict.pop(dict[dict[len(dict) - 1]])
                # print(set)
                # Всё для последнего
                # xLen = len(dict) + 1
                # print(xLen)
                # print("ewvvvwevw", xLen * 10 + dict[xLen])
            else:
                flag1 = False
            # print("edfwef", xLen * 10 + dict[xLen])
            if flag2 and (post * 10 + dict[post]) not in set:
                # deli то что удаляем
                deli = dict[post]
                # То что надо напечатать
                print(((post) * 10 + dict[post]))

                set.add(((post) * 10 + dict[dict[post]]))
                # print("edfweftet", ((post) * 10 + dict[dict[post]]))
                # set.add(((post) * 10 + dict[len(dict)] + 1))
                dict[post] = dict[dict[post]]
                # print("fwefwef", deli)
                del dict[deli]
                # print("словарик!!!!!!!", dict)
                # dict.pop(dict[dict[len(dict) - 1]])
                # print(set)
            else:
                flag2 = False
            flag = flag1 | flag2
        else:
            # print(3)

            now = now1 = 2
            if len(dict) <= 4:
                now = now1 = 1
            p = 1
            while flag3:

                j = 0
                # print("wefwef", len(dict))
                if (now in dict):
                    if (now1 + 1 in dict):
                        # print("QQQQQQQQQQQQQQQQQQQQQQQQQQ", now, now1 + 1, flag1, flag2)
                        if  (flag1 == False):
                            t = dict[now]
                            dict[now] = dict[now1 + 1]
                            # print(now1 + 1)
                            # print(dict[now1 + 1])
                            # print(t)
                            dict[now1 + 1] = t
                            flag3 = False
                            # print(dict)
                            if dict[now] == now:
                                del dict[now]
                            if dict[now1 + 1] == now1 + 1:
                                del dict[now1 + 1]
                            print(now1 + 1, now, sep='')
                            continue
                        if  flag2 == False:
                            t = dict[now]
                            dict[now] = dict[now1 + 1]
                            # print(now1 + 1)
                            # print(dict[now1 + 1])
                            # print(t)
                            dict[now1 + 1] = t
                            flag3 = False
                            # print(dict)
                            # print("Finall", dict[now], now)
                            if dict[now] == now:
                                del dict[now]
                            if dict[now1 + 1] == now1 + 1:
                                del dict[now1 + 1]
                            print(now1 + 1, now, sep='')
                            continue
                        if((dict[now] != dict[post]) or (dict[now] != dict[post1])):

                            t = dict[now]
                            dict[now] = dict[now1 + 1]
                            # print(now1 + 1)
                            # print(dict[now1 + 1])
                            # print(t)
                            dict[now1 + 1] = t
                            flag3 = False
                            print(now1 + 1, now, sep='')
                            # print(dict)
                        else:
                            if (j >= len(dict)):
                                p *= (-1)
                            now += p
                    else:
                        now1 += 1
                else:
                    now += 1
            flag = True
            flag1 = True
            flag2 = True

            # print(dict[len(dict) - 1])
            # if(dict[len(dict) - 1]):
            #     print(1)
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def algoritm(dict, set, mas):
    # print(dict)
    # print(set)

    post = len(dict)
    post1 = len(dict) - 1
    print(dict[post1], 1, sep='')
    mas.append(dict[post1] * 10 + 1)
    print(dict[post], 2, sep='')
    mas.append(dict[post] * 10 + 2)
    # print(dict)
    dict[len(dict) - 1] = dict[1]
    dict[1] = len(dict) - 1
    set.add((len(dict) - 1) * 10 + 1)
    set.add(10 + len(dict) - 1)
    # print(set)
    # print(dict)
    dict[len(dict)] = dict[2]
    dict[2] = len(dict)
    set.add(len(dict) * 10 + 2)
    set.add(20 + len(dict))
    # set.add(post * 10 + post1)
    # set.add(post1 * 10 + post)
    # Всё для предпоследнего
    x = (len(dict) - 1)
    y = (dict[len(dict) - 1])
    flag = True
    flag1 = True
    flag2 = True
    flag3 = True
    while(len(dict) != 2):
        flag3 = True
        # print("нормальный", dict)
        # print("if", x)
        # print("if", x * 10 + dict[x])


        if flag:
            if (post not in dict):
                flag2 = False
            if (post1 not in dict):
                flag1 = False
            # print("Vafefd", x * 10 + dict[x])
            if flag1 and (x * 10 + dict[x]) not in set:
                if (dict[dict[post1]] == 1) and len(dict) != 4:
                    flag = False
                    continue
                # deli то что удаляем
                # print("QQQQQ", dict)
                deli = dict[post1]
                if deli == post:
                    flag2 = False
                # То что надо напечатать
                print(((post1) * 10 + dict[post1]))
                mas.append(((post1) * 10 + dict[post1]))
                # botFUTURAMA.bot.reply_to(botFUTURAMA.Message, dict)
                set.add(((post1) * 10 + dict[post1]))
                # print("AAAAAAAA", ((post1) * 10 + dict[post1]))
                # set.add(((len(dict) - 1) * 10 + dict[len(dict) - 1]))
                dict[post1] = dict[dict[post1]]
                # print("fwefwef", deli)
                del dict[deli]
                # print("словарик", dict)
                # dict.pop(dict[dict[len(dict) - 1]])
                # print(set)
                # Всё для последнего
                # xLen = len(dict) + 1
                # print(xLen)
                # print("ewvvvwevw", xLen * 10 + dict[xLen])
            else:
                flag1 = False
            # print("edfwef", xLen * 10 + dict[xLen])
            if flag2 and (post * 10 + dict[post]) not in set:
                # deli то что удаляем
                deli = dict[post]

                # То что надо напечатать
                print(((post) * 10 + dict[post]))
                mas.append((post) * 10 + dict[post])


                set.add(((post) * 10 + dict[dict[post]]))
                # print("edfweftet", ((post) * 10 + dict[dict[post]]))
                # set.add(((post) * 10 + dict[len(dict)] + 1))
                dict[post] = dict[dict[post]]
                # print("fwefwef", deli)
                del dict[deli]
                # print("словарик!!!!!!!", dict)
                # dict.pop(dict[dict[len(dict) - 1]])
                # print(set)
            else:
                flag2 = False
            flag = flag1 | flag2
        else:
            # print(3)

            now = now1 = 2
            if len(dict) <= 4:
                now = now1 = 1
            p = 1
            while flag3:

                j = 0
                # print("wefwef", len(dict))
                if (now in dict):
                    if (now1 + 1 in dict):
                        # print("QQQQQQQQQQQQQQQQQQQQQQQQQQ", now, now1 + 1, flag1, flag2)
                        if  (flag1 == False):
                            t = dict[now]
                            dict[now] = dict[now1 + 1]
                            # print(now1 + 1)
                            # print(dict[now1 + 1])
                            # print(t)
                            dict[now1 + 1] = t
                            flag3 = False
                            # print(dict)
                            if dict[now] == now:
                                del dict[now]
                            if dict[now1 + 1] == now1 + 1:
                                del dict[now1 + 1]
                            print("$$$$", now1 + 1, now, sep='')
                            mas.append(((now1 + 1) * 10 + now))
                            continue
                        if  flag2 == False:
                            t = dict[now]
                            dict[now] = dict[now1 + 1]
                            # print(now1 + 1)
                            # print(dict[now1 + 1])
                            # print(t)
                            dict[now1 + 1] = t
                            flag3 = False
                            # print(dict)
                            # print("Finall", dict[now], now)
                            if dict[now] == now:
                                del dict[now]
                            if dict[now1 + 1] == now1 + 1:
                                del dict[now1 + 1]
                            print("####", now1 + 1, now, sep='')
                            mas.append(((now1 + 1) * 10 + now))
                            continue
                        if((dict[now] != dict[post]) or (dict[now] != dict[post1])):

                            t = dict[now]
                            dict[now] = dict[now1 + 1]
                            # print(now1 + 1)
                            # print(dict[now1 + 1])
                            # print(t)
                            dict[now1 + 1] = t
                            flag3 = False
                            print("!!!!", now1 + 1, now, sep='')
                            mas.append(((now1 + 1) * 10 + now))
                            # print(dict)
                        else:
                            if (j >= len(dict)):
                                p *= (-1)
                            now += p
                    else:
                        now1 += 1
                else:
                    now += 1
            flag = True
            flag1 = True
            flag2 = True
    for i, d in dict.items():
        print(i, d, sep='')
        mas.append(i * 10 + d)
        break
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 3
    d = "5  1 3 2 4 1 5"
    # d = "3 2 2 1"
    d1 = "3  3 2 2 1"
    test4 = "4  1 2 3 4 2 4"
    # dict, set = hashANDdict(n, d)
    mas = list()
    print(mas)
    dict, set = hashANDdict(d)
    print("Dict", dict)
    algoritm1(dict, set)
    # print(dict)
    for i, d in dict.items():
        print(i, d, sep='')
        break
    print(dict)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
