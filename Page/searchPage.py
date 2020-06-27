from Base.Base import Base
from Page.pageElements import PageElements


class SearchPage(Base):
    def __init__(self):
        super().__init__()  # 重写父类，初始化Base类__init__

    def click_search_btn(self):
        """点击搜索按钮方法"""
        self.click_ele(PageElements.search_btn_id)

    def search_text(self, text):
        """
        搜索内容方法
        :param text:
        :return:
        """
        return self.send_ele(PageElements.search_input_id, text)

    def get_search_result(self):
        results = self.search_eles(PageElements.search_result_ids)
        return [i.text for i in results]
