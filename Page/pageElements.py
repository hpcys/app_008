from selenium.webdriver.common.by import By


class PageElements:
    """管理所有页面元素"""
    # 搜索页面元素
    # 搜索按钮
    search_btn_id = (By.ID, "com.android.settings:id/search")
    # 搜索输入框
    search_input_id = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result_ids = (By.ID, "com.android.settings:id/title")
