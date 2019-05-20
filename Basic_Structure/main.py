from .stack import Stack


class StackTest():
    def run(self):
        results = []
        test_cases = [
            self._t1_integration
        ]

        for case_id, test in enumerate(test_cases):
            try:
                response = str(test())
                results.append('{} response: {}'.format(case_id, response))

            except Exception as e:
                results.append('{} error: {}'.format(case_id, e))

        print(results)

    def _t1_integration(self) -> bool:
        stack = Stack()
        test_string = 'spam'

        stack.insert(2)
        stack.insert(4)
        stack.insert(test_string)

        assert stack.peek() == test_string
        assert stack.is_empty() == False

        stack.delete()
        stack.delete()
        stack.delete()

        assert stack.peek() == False
        assert stack.is_empty() == True

        return True


if __name__ == "__main__":
    test_subject = StackTest()
    test_subject.run()
