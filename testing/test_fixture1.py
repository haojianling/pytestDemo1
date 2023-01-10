import pytest


@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}
    return _make_customer_record

def test_customer_records(make_customer_record):
    print(make_customer_record("lili"))

    # customer_1 = make_customer_record("Lisa")
    # print(customer_1)
    # customer_2 = make_customer_record("Mike")
    # print(customer_2)
    # customer_3 = make_customer_record("Meredith")
    # print(customer_3)

#
# import smtplib
# import pytest
#
# @pytest.fixture(scope="module")
# def smtp_connection(request):
#     server = getattr(request.module, "smtpserver", "smtp.gmail.com")
#     smtp_connection = smtplib.SMTP(server, 587, timeout=5)
#     yield smtp_connection
#     print(f"finalizing {smtp_connection} ({server})")
#     smtp_connection.close()