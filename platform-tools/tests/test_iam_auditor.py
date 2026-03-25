from aws.iam_auditor import find_wildcard_policies


def test_output_type():
    result = find_wildcard_policies()
    assert isinstance(result, list)