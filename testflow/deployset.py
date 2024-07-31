CONFIG_MAP = "rest-g-api"
CONFIG_END_ROUTE = "localhost:8080" #map to default host 
CONFIG_PARAM = "base-test-for-runner"


class DeploySet:
    def __init__(self,args):
        self.args = args
        self.test_set = None
        self.test_case = dict()

    
    def etsRunner(self, val: str):
        if val == "test-01-lint":
            transform_test_runner = self.test_case = CONFIG_MAP, CONFIG_END_ROUTE
            print(transform_test_runner)

    def countState(self, state: int):
        for i in range(state):
            ts = self.test_set = i
        return ts
    




