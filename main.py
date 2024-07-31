import json
import re
from testflow.deployset import DeploySet


class ProcessManager:
    def __init__(self, args):
        self.args = args
        self.log = args.log
        self.test = dict()
        self.deployset = DeploySet()

    def testBuild(val: str):
        if val == "Alpha":
            print("Base case")
        else:
            print("Pass Eval parameter")

    def testLint(val: str, self):
        if val == "runner-mx":
            suite_id = self.deployset.countState
        return suite_id
    
    def processExecutor(self):
        test_exe = self.testLint()
        with open("writer.txt", "w") as f:
            f.write(str(test_exe))

if __name__ == "__main__":
    print("Test-set-id executing... ")
    test_case = ProcessManager.processExecutor()
    print("Case executing in the parallel..", test_case)
    print("Test-Lint set-up for mnix... ")
    test_build = ProcessManager.testBuild()
    print("Build Executing... ", test_build)