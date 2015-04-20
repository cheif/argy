import re
import argparse
import inspect


def argy(function):
    ap = argparse.ArgumentParser()
    function_args = inspect.getargspec(function)
    doc_map = _create_doc_map(function)
    args = []

    defaults = len(function_args.defaults)
    required = [True]*len(function_args)
    required[-defaults:] = [False] * defaults
    for a, required in zip(function_args.args, required):
        if required:
            ap.add_argument(a, help=doc_map[a])
        else:
            ap.add_argument("--{}".format(a), help=doc_map[a])

    args = vars(ap.parse_args())
    function(**args)


def _create_doc_map(function):
    doc_str = function.__doc__
    doc_map = {}
    for line in doc_str.splitlines():
        m = re.match(r'\s*:param (?P<arg>.+?):(?P<doc>.+)', line)
        if m:
            doc_map[m.groupdict()['arg']] = m.groupdict()['doc']
    return doc_map


@argy
def test_method(xarg, yarg, kwarg=None, bwarg=None):
    """Test program for argy

    Argy is a simple tool for making CLI-applications

    :param xarg: The x argument for this program
    :param yarg: The y argument for this program
    :param kwarg: An optional argument
    :param bwarg: Yet another optional argument
    """
    print xarg, yarg, kwarg, bwarg
