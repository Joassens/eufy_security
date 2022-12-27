from dataclasses import dataclass
from enum import Enum, auto
from homeassistant.backports.enum import StrEnum
from homeassistant.config_entries import ConfigEntry


@dataclass
class EntityDescription:
    """Entity Description"""

    id: str
    icon: str = None
    state_class: StrEnum = None
    device_class: StrEnum = None
    unit: str = None
    category: StrEnum = None


class ConfigField(Enum):
    """Config and Options Fields"""

    host = "127.0.0.1"
    port = 3000
    sync_interval = 600  # seconds
    rtsp_server_address = auto()
    rtsp_server_port = 8554
    ffmpeg_analyze_duration = 1.2  # microseconds
    generate_ffmpeg_logs = False
    map_extra_alarm_modes = False
    name_for_custom1 = "Custom 1"
    name_for_custom2 = "Custom 2"
    name_for_custom3 = "Custom 3"
    captcha_id = auto()
    captcha_img = auto()
    captcha_input = auto()


@dataclass
class Config:
    """Integration config options"""

    host: str = ConfigField.host.value
    port: int = ConfigField.port.value
    sync_interval: int = ConfigField.sync_interval.value
    rtsp_server_address: str = ConfigField.host.value
    rtsp_server_port: int = ConfigField.rtsp_server_port.value
    ffmpeg_analyze_duration: float = ConfigField.ffmpeg_analyze_duration.value
    generate_ffmpeg_logs: bool = ConfigField.generate_ffmpeg_logs.value
    map_extra_alarm_modes: bool = ConfigField.map_extra_alarm_modes.value
    name_for_custom1: str = ConfigField.name_for_custom1.value
    name_for_custom2: str = ConfigField.name_for_custom2.value
    name_for_custom3: str = ConfigField.name_for_custom3.value
    captcha_id: str = None
    captcha_img: str = None
    captcha_input: str = None

    @classmethod
    def parse(cls, config_entry: ConfigEntry):
        """Generate config instance from config entry"""
        config = cls()
        for key in config.__dict__:
            if config_entry.data.get(key, None) is not None:
                config.__dict__[key] = config_entry.data.get(key)
        return config
