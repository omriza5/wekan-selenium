from enums.device_type import DeviceType

# Device width thresholds (in pixels)
MOBILE_MAX_WIDTH = 800

def get_device_type(width: int) -> DeviceType:
    """Return the device type based on screen width."""
    if width <= MOBILE_MAX_WIDTH:
        return DeviceType.MOBILE
    else:
        return DeviceType.DESKTOP