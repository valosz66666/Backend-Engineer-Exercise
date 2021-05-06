import unittest


def number_format(num):
    '''
    python3 return format(2131234243.42314123,',')
    '''
    if num < 0:
        return '-' + number_format(-num)
    num = str(num).split('.')
    result = ''
    for index in range(len(num[0])):
        if (len(num[0]) - index) % 3 == 0 and index != 0:
            result += ','
        result += num[0][index]
    num[0] = result
    return '.'.join(num)


class TestBackendTopic(unittest.TestCase):

    def test_topic1(self):
        '''
        Please implement a string function in a numeric format in a language that you are good at.
        And mark every three digits with a comma. Please attach unit test.
        e.g.
            f(9527) => "9,527", f(3345678) => "3,345,678", f(-1234.45) => "-1,234.45"
        '''

        self.assertEqual(number_format(9527), '9,527')
        self.assertEqual(number_format(3345678), '3,345,678')
        self.assertEqual(number_format(-1234.45), '-1,234.45')

if __name__ == '__main__':
    unittest.main()
