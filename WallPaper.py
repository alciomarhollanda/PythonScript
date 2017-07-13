import struct
import ctypes
import os


class ChangeWallPaper:
    def __init__(self,PATH):
        self.WALLPAPER_PATH = PATH

    def is_64_windows(self):
        """Find out how many bits is OS. """
        return 'PROGRAMFILES(X86)' in os.environ

    def get_sys_parameters_info(self):
        """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
        return ctypes.windll.user32.SystemParametersInfoW if self.is_64_windows() \
            else ctypes.windll.user32.SystemParametersInfoA

    def change_wallpaper(self):
        print('change_wallpaper: %s'%self.WALLPAPER_PATH)
        SPI_SETDESKWALLPAPER = 20
        sys_parameters_info = self.get_sys_parameters_info()
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, self.WALLPAPER_PATH, 3)
        if not r:           # When the SPI_SETDESKWALLPAPER flag is used, SystemParametersInfo returns TRUE unless there is an error (like when the specified file doesn't exist).
            print(ctypes.WinError())
