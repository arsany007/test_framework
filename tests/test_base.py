from test_framework.base import NAME
from test_framework.platforms.platform_abstract import PlatformAbstract
from test_framework.platforms.platform_1 import Platform1
from test_framework.platforms.platform_2 import Platform2

Setting = {
    "a" : Platform1,
    "b" : Platform2
}
    
def platform_exe(plt : PlatformAbstract):
    return plt().read()

def test_base():
    assert NAME == "test_framework"
    assert platform_exe(Setting["a"]) ==  "Platform1"
    assert platform_exe(Setting["b"]) ==  "Platform2"
