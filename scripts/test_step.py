import allure


class TestSetup:
    @allure.severity(allure.severity_level.BLOCKER)  # 最重要的用例
    @allure.step("我是测试报告步骤名称")
    def test_001(self):
        """添加测试步骤"""
        # 添加测试步骤描述 生成一个附件
        allure.attach("就这", "对，就这")

    @allure.severity(allure.severity_level.CRITICAL)  # 比较重要用例
    def test_002(self):
        assert False

    @allure.severity(allure.severity_level.MINOR)  # 比一般低一些用例
    def test_003(self):
        assert True

    @allure.severity(allure.severity_level.NORMAL)  # 正常用例
    def test_004(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)  # 可以忽略的用例
    def test_005(self):
        assert True
