from nonebot.plugin import PluginMetadata
from nonebot.plugin import require
require("nonebot_plugin_localstore")
from . import image
from . import event
__plugin_meta__ = PluginMetadata(
    name="LuoguLuck|洛谷运势",
    description="洛谷同款的今日运势插件！",
    usage="/luck",
    type="application",
)


