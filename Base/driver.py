from appium import webdriver


class Driver:
    """声明driver驱动对象"""
    app_driver = None

    @classmethod
    def get_app_driver(cls):
        if not cls.app_driver:
            # server 启动参数
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            # 声明我们的driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            return cls.app_driver  # 返回驱动对象
        else:
            return cls.app_driver  # 已经声明了driver

    @classmethod
    def quit_app_driver(cls):
        if cls.app_driver:  # 有值的时候
            cls.app_driver.quit()  # 退出
            cls.app_driver = None  # 重置driver为None
