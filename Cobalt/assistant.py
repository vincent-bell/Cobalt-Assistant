from .tester import Tester


class Assistant:
    def __init__(self, default_config_file="Cobalt/config.txt"):
        self.config_file = default_config_file
        self.current_task, self.test_cases, self.inputs = self.get_current_task()
        if self.current_task == None:
            print("There are no incomplete tasks left!")

    def get_current_task(self):
        with open(self.config_file, 'r') as file:
            data = list(map(lambda x: x.strip(), file.readlines()))
        for i in range(len(data)):
            if "TASK" in data[i] and "INCOMPLETE" in data[i+1]:
                if "[" in data[i+1][11:]:
                    r3 = eval(data[i+1][11:])
                else:
                    r3 = None
                return int(data[i][5]), eval(data[i][8:]), r3

    def run_current_task(self):
        tester = Tester(f'task{self.current_task}.py', self.test_cases, self.inputs)
        tester.run_test_cases()


if __name__ == '__main__':
    assistant = Assistant()
    assistant.run_current_task()
