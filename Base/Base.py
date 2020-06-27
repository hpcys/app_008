from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base:
    def __init__(self):
        self.driver = Driver.get_app_driver()  # 实例化

    def search_ele(self, loc, timeout=5, poll=1):
        """
        定位单个元素
        :param loc: 元祖形式
        :param timeout: 搜索元素等待最大时间
        :param poll: 搜索时间间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1):
        """
        定位一组元素
        :param loc: 元祖形式
        :param timeout: 搜索元素等待最大时间
        :param poll: 搜索时间间隔
        :return: 定位对象
         """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1):
        """
        点击元素
        :param loc:
        :param timeout:
        :param poll:
        :return:
        """
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1):
        """
        输入方法
        :param loc:
        :param text:
        :param timeout:
        :param poll:
        :return:
        """
        # 定位
        input_text = self.search_ele(loc, timeout, poll)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)
