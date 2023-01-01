import pytest

from app.demo2 import demo2


class Test_Caclatest:
    @pytest.fixture()
    def yc_up(self):
        self.cal = demo2()
    @pytest.mark.parametrize("a,b,c",[[0,0,0],[1,1,2],[1,2,3]])
    def test_add_1(self,yc_up,a,b,c):
        result=self.cal.add(a,b)
        print(result)
        assert c==result
    @pytest.mark.parametrize("a,b,c",[[0,0,0],[1,1,1],[1,2,0.5]])
    def test_div_1(self,yc_up,a,b,c):
        try:
            re=self.cal.div(a, b)
            assert re==c
        except ZeroDivisionError:
            print("不能为0")


