import sys
from subprocess import Popen, PIPE

commits = [
    # master
    ('45e7c6a', '0.3.dev03-g45e7c'),
    ('d8962cf', '0.3.dev02-gd8962'),
    ('58a31b6', '0.2.dev01-g58a31'),
    ('4dc782f', '0.2.0'),
    ('a2317af', '0.2.dev01-ga2317'),
    ('c29938c', '0.1.dev02-gc2993'),
    ('b1d3515', '0.1.dev01-gb1d35'),

    # v0.1 branch
    ('69c695b', '0.1.1.post01-g69c69'),
    ('e1d7cd9', '0.1.1'),
    ('3c5037a', '0.1.post02-g3c503'),
    ('620c454', '0.1.post01-g620c4'),
    ('c9a2e2f', '0.1'),
    ('e9c6858', '0.1.pre02-ge9c68'),
    ('49053a0', '0.1.pre01-g49053'),

    # v0.1dangling branch
    ('25e0ee4', '0.1dangling.dev01-g25e0e'),
    ('39bb5d2', '0.1dangling'),
    ('d92d9ed', 'v0.1dangling.rev02-gd92d9'),
    ('92aa03a', 'v0.1dangling.rev01-g92aa0'),

    # v0.2 branch
    ('c63fe1c', '0.2.1'),
    ('60c26ca', '0.2.0.post01-g60c26'),

    # test branch
    ('56bdc24', 'testtag.dev01-g56bdc'),
    ('25fcf7f', 'testtag'),
    ('4b3cd39', 'test.dev02-g4b3cd'),
    ('edc1523', 'test.dev01-gedc15'),

    # test2 branch
    ('c82da92', 'test2tag.dev01-gc82da'),
    ('b5a5397', 'test2tag'),
    ('4a5c4f6', 'test2.dev02-g4a5c4'),
    ('346874d', 'test2.dev01-g34687')]


def assert_equal(a, b):
    if a == b:
        return
    raise AssertionError('{} is not equal to {}.'.format(a, b))


def run(cmd):
    process = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        if stderr != '':
            stderr = '\n' + stderr.decode('utf-8')
        raise RuntimeError(
            'Command failed (error {}): {}{}'.format(process.returncode, cmd,
                                                     stderr))
    return stdout.strip().decode('utf-8')


def run_git(cmd):
    git = "git"
    if sys.platform == "win32":
        git = "git.cmd"
    return run(git + ' ' + cmd)


def teardown():
    run_git('checkout master')


def test():

    def func(commit, expected):
        run_git('checkout ' + commit)
        actual = run('python setup.py --version')
        assert_equal(actual, expected)

    for commit, expected in commits:
        yield func, commit, expected
