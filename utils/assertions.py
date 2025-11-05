def assert_equals(actual, expected, msg=""):
    assert actual == expected, msg or f"Expected {expected}, but got {actual}"

def assert_true(condition, msg=""):
    assert condition, msg or "Condition expected to be True, but was False"

def assert_number_close(actual, expected, tolerance=0.01, msg=""):
    assert abs(actual - expected) <= tolerance, (
        msg or f"Expected ~{expected} (±{tolerance}), but got {actual}"
    )