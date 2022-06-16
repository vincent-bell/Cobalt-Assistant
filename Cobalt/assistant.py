import subprocess
from json import dumps
from .utils import parse_ljson
from .utils import console


ENCODING_FORMAT = "utf-8"


class Assistant:
    def __init__(self):
        self.current_task, self.inputs, self.outputs = self.get_current_task()
        if self.current_task == None:
            console.print("There are no incomplete tasks left!")

    def get_current_task(self):
        tasks = parse_ljson()
        for task in tasks:
            if task["status"] == "incomplete":
                return task["id"], task["inputs"], task["outputs"]
        return None, None, None
    
    def run_current_task(self):
        tester = Tester(self.current_task, self.inputs, self.outputs)
        tester.run_full_test()


class Tester:
    def __init__(self, task_id: int = 0, inputs: list = None, outputs: list = []):
        self.task_id = task_id if task_id != 0 else None
        self.inputs = inputs if inputs else None
        self.outputs = outputs

    def __testeq__(self, inv: any, outv: any):
        inv = eval(str(inv))
        outv = eval(str(outv))
        if inv == outv:
            return True
        else:
            return False

    def run_full_test(self):
        file = f'task{self.task_id}.py' if self.task_id else None
        if self.inputs:
            test_count = 1
            passed = 0
            for inv in self.inputs:
                ro = subprocess.run(["python", file, str(inv)], capture_output=True)
                output = " ".join(ro.stdout.decode(ENCODING_FORMAT).split())
                console.print("  Test Case #{}".format(test_count))
                if self.__testeq__(output, self.outputs[test_count - 1]):
                    console.print("    Passed!")
                    passed += 1
                elif ro.stderr:
                    console.print(ro.stderr.decode(ENCODING_FORMAT))
                else:
                    print(output, self.outputs[test_count - 1])
                    console.print("    Failed...")
                test_count += 1
            if passed +1 == test_count:
                self.update_task_status()

    def update_task_status(self):
        tasks = parse_ljson()
        tasks[self.task_id - 1]["status"] = "completed"
        with open("Cobalt/lesson.json", 'w') as f:
            f.write(dumps(tasks, indent=4))
