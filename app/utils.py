import platform
from selenium.webdriver.common.keys import Keys


def keyboard_control():
    if platform.system() == 'Darwin':
        return Keys.COMMAND
    elif platform.system() == 'Windows':
        return Keys.CONTROL
    else:
        assert "This code is running on a different operating system."