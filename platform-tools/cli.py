import click
from aws.iam_auditor import find_wildcard_policies


@click.group()
def cli():
    pass


@cli.command()
def audit_iam():
    findings = find_wildcard_policies()

    if not findings:
        print("No issues found ✅")
    else:
        print("⚠️ Security Issues Found:")
        for f in findings:
            print(f)


if __name__ == "__main__":
    cli()