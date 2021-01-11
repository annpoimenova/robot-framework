class FirstModule(object):

    def test_data_first(self, s):
        print(s)
        res = s + "2"
        return res

    def result_check(self, s):
        print(s)
        assert s == "22"