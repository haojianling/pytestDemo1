#yield+函数==生成器
import pytest


def provider():
    for i in  range(5):
        yield i #生成器:return i

p=provider()
print(next(p))
print(next(p))
print(next(p))

@pytest.fixture()
def login():
    print("需要登录")
    username="tom"
    yield username
    print("退出登录")
def test_a(login):
    print(f"ftesta {login}")