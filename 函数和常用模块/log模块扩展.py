import logging
#create logger
logger=logging.getLogger("t")   #
logger.setLevel(logging.DEBUG)

#屏幕输出Handler
ch=logging.StreamHandler()   #往哪个地方输出
ch.setLevel(logging.INFO)

#文件输出Handler
fh=logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)
###########
#文件输出Handler
eh=logging.FileHandler("ERROR.log")
eh.setLevel(logging.ERROR)
###############

#指定输出格式Formatter
formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
formatter2=logging.Formatter("%(asctime)s-%(lineno)s-%(process)d-%(levelname)s-%(message)s")


#Formatter注册给Handler
ch.setFormatter(formatter)
fh.setFormatter(formatter2)
eh.setFormatter(formatter2)
#################################


#Handler注册给logeer
#add ch and fg to logger
logger.addHandler(ch)
logger.addHandler(fh)
logger.addHandler(eh)
###########################

logger.debug("1")
logger.info("2")
logger.warn("3")
logger.error("4")
logger.critical("5")
