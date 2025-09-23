from utils.devices import get_device_type
from enums.device_type import DeviceType


def get_navigation_page(driver, width):
    device_type = get_device_type(width)
    if device_type == DeviceType.MOBILE:
        return NavigationMobile(driver)
    else:
        return NavigationDesktop(driver)