from selenium_wework_zuoye.page.index import Index


class TestAddMember:
    def setup(self):
        self.index=Index()
    def test_addmember(self):
        a=self.index.goto_mail_list().goto_add_member()
        a.add_member()
        print(a.get_member())
        assert '999' in a.get_member()
