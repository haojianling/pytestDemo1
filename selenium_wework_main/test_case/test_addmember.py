from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main=Main()
    def test_member(self):
        a=self.main.goto_add_member()
        a.add_member()
        assert '321321321' in a.get_member()