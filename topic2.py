import unittest


def increment(value):
    return value + 1

def pipe(*args):
    result = args[0]
    for fun in args[1::]:
        result = fun(result)
    return result


class TestBackendTopic(unittest.TestCase):

    def test_topic2(self):
        '''
        Please implement a pipe function in a language that you are good at. The
        function parameter is of indefinite length, the first parameter is a variable of
        any type, and the following parameter is the function pointer. Please attach
        unit test.

        e.g.
        def increment (int value) {
            return value + 1
        }
        pipe(5, increment) => 6, pipe(5, increment, increment, increment) => 8
        '''
#
        self.assertEqual(pipe(5, increment), 6)
        self.assertEqual(pipe(5, increment, increment, increment), 8)

if __name__ == '__main__':
    unittest.main()
