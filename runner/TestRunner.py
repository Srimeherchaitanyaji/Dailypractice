import pytest
import os

class TestRunner:
    def __init__(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        tests_dir = os.path.join(base_dir, 'Tests')
        self.pytest_args = [
            os.path.join(tests_dir, "test_registrationandloginpage.py"),
            os.path.join(tests_dir, "test_homepage.py"),
            "-vv",
            "--html=./e-commerce.html"
        ]
    
    def run_tests(self):
        pytest.main(self.pytest_args)


if __name__ == "__main__":
    test_runner = TestRunner()
    test_runner.run_tests()
