shooplist=[
    ("苹果6S",5288),
    ("Mac笔记本",10000),
    ("书",200),
    ("衣服",100),
    ("汽车",200000),
    ("牙刷",50),
    ("鞋子",300),
    ("帽子",400),
]
shoop_car=[]
long=len(shooplist)
flag=True
cash=input("请输入你要充值的金额：")
cash=cash.strip()
if cash.isdigit():
    cash=int(cash)
    print("你充值成功")
else:
    exit("你充值失败，请检查格式")
while flag:
    for i in enumerate(shooplist):
        weizhi=i[0]
        wuping=i[1][0]
        jiaqian=i[1][1]
        print(weizhi,wuping,jiaqian)
    buy=input("请选择要购买的商品编号：")
    buy=buy.strip()
    if buy.isdigit():
        buy=int(buy)
        if long>buy:
            print("你选择的物品在范围之内")
            qian=shooplist[buy][1]
            if cash>=qian:
                wuping=shooplist[buy][0]
                qian=shooplist[buy][1]
                cash=cash-qian
                print("你已经购买,余额为%d元"%(cash))
            else:
                print("你钱不够。。。")
        else:
            print("你选择的物品编号超出范围")

    else:
        if buy=="q" or buy=="quit":
            for i in shooplist:
                print(i)
        flag=False
        print("END".center(40,"*"))
        print("你的余额还有%d元"%(cash))




















