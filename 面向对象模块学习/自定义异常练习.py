class xiaoyong(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        msg="{msg}".format(msg=self.msg)
        return msg

try:
    raise xiaoyong("dsasdasdsadasdsad")
except xiaoyong as ex:
    print(ex)