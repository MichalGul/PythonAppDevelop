import unittest
from unittest.mock import Mock, call

class MyClassA:
    """Class for mock demo"""

    def foo(self):
        """Jakies skomplikowane obliecznia/......."""
        return 100

    def foo2(self):
        return 200

    def compute(self):
        x1 = self.foo()
        x2 = self.foo2()
        print("x1 = {}, x2 = {}".format(x1, x2))
        result = x1 + x2
        print("In MyCalssA.compute, result x1 + x2 = ", result)
        return result


class TestA(unittest.TestCase):

    def test_compute(self):
        a = MyClassA()

        mockObj = Mock()
        a.foo = mockObj.foo
        a.foo2 = mockObj.foo2

        #Assuming you know the return values, set for the mocks
        a.foo.return_value = 100
        a.foo2.return_value = 300
    
        #Run computation
        #Calls to foo and foo2 in compute methood are now replaces with mock objects calls that return the desire value
        result = a.compute()

        #Veryfiy
        self.assertEqual(result, 400)

        # Get info on how the mock objects are actually called by compute
        test_call_list = mockObj.mock_calls
        print("test_call_list", test_call_list)

        #Compare it against some reference calling order
        reference_call_list = [call.foo(), call.foo2()]
        self.assertEqual(test_call_list, reference_call_list)

    def test_compute_with_patch(self):
        """Unit test for MyClassA.compute using mock.patch
        """
        print("..running test_compute_with_patch...")
        with unittest.mock.patch('__main__.MyClassA.foo' , new = Mock(return_value = 500)):
            a = MyClassA()
            result = a.compute()

            # Veryfy the results. The test is expected to fail since we 
            # are using a return value of 500 using MyClassA.foo!
            self.assertEqual(result, 400)

    def test_compute_with_patch_alternate(self):
        
        print("Running test_compute_with_patch_alternate...")
        mockObj = Mock()
        #Patchowanie bez sprecyzowanie argumentu new - 
        with unittest.mock.patch('__main__.MyClassA.foo') as foo_patch:
            foo_patch.return_value = 500
            a = MyClassA()
            result = a.compute()
            print(foo_patch.__class__)
            self.assertEqual(result, 400)


if __name__=='__main__':
    unittest.main()



