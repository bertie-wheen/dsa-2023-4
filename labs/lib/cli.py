from argparse import Namespace

from lib.test.runner import TestRunner


def run(args: Namespace) -> None:
    if args.component is None:
        return
    runner = TestRunner(args.min_time_ms, args.max_time_ms)
    all_success = True
    any_tested = False
    # was_success =
    for name, test in args.component.tests:
        failure_reason = runner.run(test)
        if any_tested:
            print()
        result_type_str = "SUCCESS" if not failure_reason else "FAILURE"
        print(f"{result_type_str}: {name}")
        if failure_reason:
            print(failure_reason)
            all_success = False
        any_tested = True
    if all_success:
        print("All tests ran successfully!")
