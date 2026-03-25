from utils.session import get_client


def find_wildcard_policies():
    iam = get_client("iam")

    findings = []

    policies = iam.list_policies(Scope="Local")["Policies"]

    for policy in policies:
        version = iam.get_policy_version(
            PolicyArn=policy["Arn"],
            VersionId=policy["DefaultVersionId"]
        )

        document = version["PolicyVersion"]["Document"]

        for stmt in document.get("Statement", []):
            actions = stmt.get("Action", [])
            resources = stmt.get("Resource", [])

            if actions == "*" or resources == "*":
                findings.append({
                    "policy": policy["PolicyName"],
                    "issue": "Wildcard detected"
                })

    return findings