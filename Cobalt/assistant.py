import subprocess
from .utils.json_parser import parse_ljson
from .utils.rich_console import console


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

    def run_current_task(self):
        cfile = f'task{self.current_task}.py' if self.current_task else None
        if cfile:
            if self.inputs:
                test_count = 1
                for each in self.inputs:
                    ro = subprocess.run(["python", cfile, str(each)], capture_output=True)
                    output = " ".join(ro.stdout.decode(ENCODING_FORMAT).split())
                    console.print("  Test Case #{}".format(test_count))
                    if str(output) == str(self.outputs[test_count - 1]):
                        console.print("    Passed!")
                    elif ro.stderr:
                        console.print(ro.stderr.decode(ENCODING_FORMAT))
                    else:
                        console.print("    Failed...")
                    test_count += 1
            else:
                ro = subprocess.run(["python", cfile], capture_output=True)
                output = " ".join(ro.stdout.decode(ENCODING_FORMAT).split())
                console.print("  Testing {}".format(cfile))
                if output == self.test_cases[0] and ro.returncode == 0:
                    console.print("    Passed!")
                elif ro.stderr:
                    console.print(ro.stderr.decode(ENCODING_FORMAT))
                else:
                    console.print("    Failed...")
