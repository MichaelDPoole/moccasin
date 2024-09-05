from contracts import Counter
from gaboon.boa_tools import VyperContract


def deploy() -> VyperContract:
    counter: VyperContract = Counter.deploy()
    print("Starting count: ", counter.number())
    counter.increment()
    print("Ending count: ", counter.number())
    return counter


def main() -> VyperContract:
    return deploy()
