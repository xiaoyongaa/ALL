class main:
    guoji="中国"
    人种="黄种人"
    def __init__(self,name,sex,age,work,cash,car,fang):
        self.name=name
        self.sex=sex
        self.age=age
        self.work=work
        self.cash=cash
        self.fang=fang
        self.car=car
        for key in self.cash:
            if key=="poor":
                self.cash["poor"]=0
            elif key=="rich":
                self.cash["rich"]=self.cash["rich"]+1000000000000000

    def talk(self,msg):

        print(msg)

    def zhuanqian(self):
        for key in self.cash:
            if key=="poor":
                self.cash["poor"]=100000000000000000000
        self.car["car"]="法拉利"
        self.fang["fang"]="海景超级大别墅"

    @staticmethod
    def start():
        msg="屌丝john和Liz大学里面是恋人，毕业之后。。"
        print(msg)

main.start()
john=main("john","男","23","学生",{"poor":0},{"car":None},{"fang":None})
Liz=main("Liz","女","21","学生",{"poor":0},"none","none")
peter=main("peter","男","33","老板",{"rich":0},{"car":"保时捷"},{"fang":"豪华大别墅"})
msg="Peter：美女，看我有{cash},和一辆{car}，还有{fang}，说完，土豪立马送了Liz一个爱马仕包包".format(cash=peter.cash,car=peter.car,fang=peter.fang)
peter.talk(msg)
Liz.talk("Liz：哇，好有钱，我现在就是你的女朋友。")
Liz.talk("一次，john和pette相遇了，Liz说：你没房，没车，没钱，这不是我想要的生活，所以抱歉。。。。")
john.talk("john：女神别离开我，我会努力。")
Liz.talk("Liz：好，那等你有钱了再来找我。")
print("john回到家，下决心要赚到更多的钱，打算学一门技术，偶然看到了51cto python自动化开发，就学了起来。。。多年之后。。。")
john.zhuanqian()
msg="哈哈哈哈，现在我有{cash},一辆{car}，一套{fang},Liz得知此事后，找到john".format(cash=john.cash,car=john.car,fang=john.fang)
john.talk(msg)
Liz.talk("Liz：john,多年不见。你现在好有钱。好土豪。我打算和你复合。。")
john.talk("john：开玩笑，当初你背叛了我。选择了Peter，现在后悔了？")
Liz.talk("Liz：求你再给我吃机会，我是真心要复合的。。")
john.talk("你太天真了，我已经有女朋友了。。想跟我，，没门！")
Liz.talk("Liz：你现在的女朋友是谁？")
john.talk("john：看，就是这个，我网上订购的，终身保修，，说完。john拿手机给Liz看，是某宝的充气娃娃限量款。")
Liz.talk("Liz：。。。。。")
print("+++++++++++++end++++++++++++++++++")
