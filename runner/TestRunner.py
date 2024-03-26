import pytest

class TestRunner:
    def __init__(self):
        self.pytest_args = [
            "Tests/test_registrationandloginpage.py",
            "Tests/test_homepage.py",
            "-v",
            "--html=./e-commerce.html"
        ]
    
    def run_tests(self):
        pytest.main(self.pytest_args)


if __name__ == "__main__":
    test_runner = TestRunner()
    test_runner.run_tests()
