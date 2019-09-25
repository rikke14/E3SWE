from fuzzing.fuzzer import FuzzExecutor


# Files to use as initial input seed.
file_list = ["test_rle.txt"]

# List of applications to test.
apps_under_test = ["python & rle.py -e"]

number_of_runs = 7

def test():
    fuzz_executor = FuzzExecutor(apps_under_test, file_list)
    fuzz_executor.run_test(number_of_runs)
    return fuzz_executor.stats

if __name__ == '__main__':
    stats = test()
    print(stats)
    
    

