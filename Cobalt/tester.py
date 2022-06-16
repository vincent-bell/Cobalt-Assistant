import subprocess


ENCODING_FORMAT = "utf-8"


class Tester:
    def __init__(self, file: str, inputs: list, outputs: list):
        self.file = file
        self.outputs = outputs
        if inputs:
            self.inputs = inputs
        if type(self.inputs) != list:
            raise TypeError("The inputs must be provided as a list...")


    def run_test_cases(self):
        if self.inputs:
            test_count = 1
            for each in self.inputs:
                ro = subprocess.run(["python", self.file, str(each)], capture_output=True)
                output = " ".join(ro.stdout.decode(ENCODING_FORMAT).split())
                print("Test Case #{}".format(test_count))
                if output == self.outputs[test_count - 1]:
                    print("    Passed!")
                elif ro.stderr:
                    print(ro.stderr.decode(ENCODING_FORMAT))
                else:
                    print("    Failed...")
                    print(f'TEST INPUT: {each} OUTPUT: {output} SELF.OUTPUT: {self.outputs[test_count - 1]}')
                test_count += 1
        else:
            ro = subprocess.run(["python", self.file], capture_output=True)
            output = " ".join(ro.stdout.decode(ENCODING_FORMAT).split())
            print("Testing {}".format(self.file))
            if output == self.test_cases[0] and ro.returncode == 0:
                print("    Passed!")
            elif ro.stderr:
                print(ro.stderr.decode(ENCODING_FORMAT))
            else:
                print("    Failed...")
