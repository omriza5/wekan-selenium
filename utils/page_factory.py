from utils.devices import get_device_type
from enums.device_type import DeviceType
from pages.board_page_desktop import BoardPageDesktop
from pages.board_page_mobile import BoardPageMobile


def get_board_page(driver, width):
    device_type = get_device_type(width)
    if device_type == DeviceType.MOBILE:
        return BoardPageMobile(driver)
    else:
        return BoardPageDesktop(driver)