# This is a test file and the few test files are passed into the function
#Example of unit testing
import root_main

#test function
def test_root(path_file):
    root_main.main(path_file)


if __name__ == "__main__":
    test_root("input_test1.txt")
    test_root("input_test2.txt")
    test_root("input_test3.txt")
    #Given input in the question
    test_root("input_test.txt")

    
    print("Everything passed")
