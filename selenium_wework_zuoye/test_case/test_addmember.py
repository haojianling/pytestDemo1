from selenium_wework_zuoye.page.index import Index


class TestAddMember:
    def setup(self):
        self.index=Index()
    def test_addmember(self):
        add_member=self.index.goto_mail_list().goto_add_member()
        add_member.add_member()
        # print(add_member.get_member())
        assert '999' in add_member.get_member()
