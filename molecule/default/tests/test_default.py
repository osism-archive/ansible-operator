import pytest


@pytest.fixture()
def AnsibleDefaults(host):
    return host.ansible("include_vars", "defaults.yml")["ansible_facts"]


def test_operator_user_and_group(host, AnsibleDefaults):
    user = host.user(AnsibleDefaults["operator_user"])
    assert user.name == AnsibleDefaults["operator_user"]
    assert user.group == AnsibleDefaults["operator_group"]
