import pytest

from ogr.parsing import parse_git_repo, RepoUrl


@pytest.mark.parametrize(
    "url,expected",
    [
        (
            "https://host.name/namespace/repo",
            RepoUrl(
                repo="repo",
                namespace="namespace",
                scheme="https",
                hostname="host.name",
                username="namespace",
            ),
        ),
        (
            "https://host.name/namespace/repo.git",
            RepoUrl(
                repo="repo",
                namespace="namespace",
                scheme="https",
                hostname="host.name",
                username="namespace",
            ),
        ),
        (
            "http://host.name/namespace/repo",
            RepoUrl(
                repo="repo",
                namespace="namespace",
                scheme="http",
                hostname="host.name",
                username="namespace",
            ),
        ),
        (
            "git://host.name/namespace/repo",
            RepoUrl(
                repo="repo",
                namespace="namespace",
                scheme="git",
                hostname="host.name",
                username="namespace",
            ),
        ),
        (
            "git+https://host.name/namespace/repo",
            RepoUrl(
                repo="repo",
                namespace="namespace",
                scheme="git+https",
                hostname="host.name",
                username="namespace",
            ),
        ),
        (
            "git@host.name:namespace/repo",
            RepoUrl(
                repo="repo",
                namespace="namespace",
                scheme="https",
                hostname="host.name",
                username="namespace",
            ),
        ),
        ("host.name/repo", RepoUrl(repo="repo", scheme="https", hostname="host.name")),
        (
            "host.name/fork/user/namespace/repo",
            RepoUrl(
                repo="repo",
                username="user",
                namespace="namespace",
                scheme="https",
                hostname="host.name",
                is_fork=True,
            ),
        ),
        (
            "https://host.name/namespace/repo/",
            RepoUrl(
                repo="repo",
                username="namespace",
                namespace="namespace",
                scheme="https",
                hostname="host.name",
            ),
        ),
        (
            "https://host.name/multi/part/namespace/repo/",
            RepoUrl(
                repo="repo",
                username="multi",
                namespace="multi/part/namespace",
                scheme="https",
                hostname="host.name",
            ),
        ),
        (
            "https://pagure.io/fork/user/some_repo",
            RepoUrl(
                repo="some_repo",
                username="user",
                namespace="",
                is_fork=True,
                hostname="pagure.io",
                scheme="https",
            ),
        ),
        ("https://fail@more@at@domain.com", None),
        (
            "git@gitlab.com:packit-service/src/libvirt.git",
            RepoUrl(
                repo="libvirt",
                namespace="packit-service/src",
                username="packit-service",
                hostname="gitlab.com",
                scheme="https",
            ),
        ),
        ("git@git.mfocko.xyz:2222:mfocko/dotfiles.git", None),
        (
            "https://pagure.io/fork/mfocko/fedora-infra/ansible.git",
            RepoUrl(
                repo="ansible",
                namespace="fedora-infra",
                username="mfocko",
                is_fork=True,
                hostname="pagure.io",
                scheme="https",
            ),
        ),
        (
            "ssh://git@pagure.io/forks/mfocko/fedora-infra/ansible.git",
            RepoUrl(
                repo="ansible",
                namespace="fedora-infra",
                username="mfocko",
                is_fork=True,
                hostname="pagure.io",
                scheme="https",
            ),
        ),
        (
            "ssh://git@pagure.io:forks/mfocko/fedora-infra/ansible.git",
            RepoUrl(
                repo="ansible",
                namespace="fedora-infra",
                username="mfocko",
                is_fork=True,
                hostname="pagure.io",
                scheme="https",
            ),
        ),
        (
            "https://xfocko:myLamePassword@git.mfocko.xyz/mfocko/dotfiles.git",
            RepoUrl(
                repo="dotfiles",
                namespace="mfocko",
                hostname="git.mfocko.xyz",
                scheme="https",
                username="mfocko",
            ),
        ),
        (
            "ssh://git@pagure.io/playground-mfocko.git",
            RepoUrl(
                repo="playground-mfocko",
                namespace=None,
                hostname="pagure.io",
                scheme="https",
            ),
        ),
        (
            "https://pagure.io/playground-mfocko.git",
            RepoUrl(
                repo="playground-mfocko",
                namespace=None,
                hostname="pagure.io",
                scheme="https",
            ),
        ),
        (
            "git://github.com/packit/dotfiles.git",
            RepoUrl(
                repo="dotfiles",
                namespace="packit",
                username="packit",
                hostname="github.com",
                scheme="git",
            ),
        ),
    ],
)
def test_parse_git_repo(url, expected):
    repo_url = parse_git_repo(potential_url=url)
    assert repo_url == expected
