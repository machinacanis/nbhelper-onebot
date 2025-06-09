import logging

import nonebot
from nonebot import logger
from nonebot.adapters.onebot.v11 import Adapter, Bot
from nonebot.log import LoguruHandler

from src.nbhelper_onebot import nbhelper

nonebot.init()

# root logger 添加 LoguruHandler
logging.basicConfig(handlers=[LoguruHandler()])

driver = nonebot.get_driver()
driver.register_adapter(Adapter)


@driver.on_startup
async def _():
    nbhelper.init()  # 初始化NBHelper实例
    logger.info("NBHelper initialized successfully.")


@driver.on_bot_connect
async def _(bot: Bot):
    social = await nbhelper.get_social(bot)
    g = await social.get_group(941419619)
    res = await social.leave_group(g)
    print(res)


# 加载Bot
if __name__ == "__main__":
    nonebot.run()
