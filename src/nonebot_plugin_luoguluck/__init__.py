from nonebot.plugin import PluginMetadata
from nonebot.plugin import require
require("nonebot_plugin_localstore")
from .image import *
from .event import *
__plugin_meta__ = PluginMetadata(
    name="LuoguLuck|洛谷运势",
    description="洛谷同款的今日运势插件！",
    usage="/luck",
    type="application",
    homepage="https://github.com/JohnRichard4096/luogu-luck",
    supported_adapters={"~onebot.v11"},
)


