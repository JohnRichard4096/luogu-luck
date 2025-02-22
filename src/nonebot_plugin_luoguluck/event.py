from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent, MessageSegment, MessageEvent, Bot
from .image import get_image
from nonebot import on_command,logger
from datetime import datetime
from pathlib import Path
import pickle
from nonebot_plugin_localstore import get_plugin_data_dir
data_path = Path(get_plugin_data_dir())

luck = on_command("luck", aliases={"luck","lucky","运势"}, priority=10,block=True)

async def is_same_day(timestamp1:int, timestamp2:int) -> bool:
    # 将时间戳转换为datetime对象，并只保留日期部分
    date1 = datetime.fromtimestamp(timestamp1).date()
    date2 = datetime.fromtimestamp(timestamp2).date()
    
    # 比较两个日期是否相同
    return date1 == date2

@luck.handle()
async def _(event:MessageEvent,bot:Bot):
    global data_path
    nickname = ""
    user_id = event.user_id

    if isinstance(event,PrivateMessageEvent):
            event:PrivateMessageEvent = event
            nickname = event.sender.nickname
    else:
          event:GroupMessageEvent = event
          group_id = event.group_id
          info = await bot.get_group_member_info(group_id=group_id, user_id=user_id)
          nickname = info['card']

    
    if not data_path.exists():
        data_path.mkdir()

    user_conf = data_path/f"{user_id}.pickle"
    timestamp = datetime.now().timestamp()
    
    if not user_conf.exists():
        image = get_image(nickname)
        with open(str(user_conf),"wb") as f:
             pickle.dump({"last_time":timestamp,"image":image},f)

    else:
         
         with open(str(user_conf),"rb") as f:
              data = pickle.load(f)

         if await is_same_day(timestamp,data["last_time"]):
              image = data["image"]
         else:
              image = get_image(nickname)
              with open(str(user_conf),"wb") as f:
                   pickle.dump({"last_time":timestamp,"image":image},f)
                   
    if isinstance(event,PrivateMessageEvent):
         await luck.send(MessageSegment.image(image))
    else:
         await luck.send(MessageSegment.at(user_id)+MessageSegment.image(image))
