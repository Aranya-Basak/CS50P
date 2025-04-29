from seasons import tst_date

def main():
    test_tst_date()
def test_tst_date():
    assert tst_date("2005-09-23") == ["2005", "09", "23"]
    assert tst_date("200-09-23") == None
    assert tst_date("cat") == None

if __name__ == "__main__":
    main()
