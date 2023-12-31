import subprocess, time, os, sys, json, shutil

class TextColors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

def runCommandTimed(command):
    time_before = time.perf_counter()
    process = subprocess.run(command, capture_output=True, shell=True, text=True, executable="/bin/bash")
    time_after = time.perf_counter()
    return [time_after - time_before, process.stdout, process.stderr]

def runCommand(command):
    process = subprocess.run(command, capture_output=True, shell=True, text=True, executable="/bin/bash")
    return (process.stdout, process.stderr)

class Test:
    def __init__(self, compilation: str, expectedResult: str):
        self.compilation = compilation
        self.expectedResult = expectedResult

    def compile(self):
        compilResult = runCommand(self.compilation)
        if compilResult[1]:
            return 1
        return 0

    def run(self, args):
        finalResult = runCommandTimed("./a.out " + args)
        if finalResult[2] or finalResult[1] != self.expectedResult:
            return 1
        else:
            return finalResult[0]

    def clear(self):
        os.remove("a.out")

class TestRunner():
    def __init__(self, group: str, name: str, compilation: str, exceptedResult: str, quantity: int, args: str):
        self.group = group
        self.name = name
        self.compilation = compilation
        self.exceptedResult = exceptedResult
        self.quantity = quantity
        self.failed = 0
        self.results = []
        self.minimum = -1
        self.maximum = -1
        self.moyenne = -1
        self.args = args

    def run(self):
        testItem = Test(self.compilation, self.exceptedResult)
        if testItem.compile() == 1:
            print(TextColors.RED + "Compilation failed on the test of group :", self.name, "(", self.group, ")" + TextColors.RESET)
        else:
            for i in range(self.quantity):
                testResult = testItem.run(self.args)
                if (testResult == 1):
                    self.failed += 1
                else:
                    self.results.append(testResult)
            self.minimum = min(self.results)
            self.maximum = max(self.results)
            self.moyenne = sum(self.results) / len(self.results)
            testItem.clear()
    def getJson(self):
        values = {
            "group" : self.group,
            "name" : self.name,
            "mininum" : self.minimum,
            "maximum" : self.maximum,
            "moyenne" : self.moyenne,
            "quantity" : self.quantity,
            "failed" : self.failed,
        }
        return json.dumps(values)

def getAllDirectory():
    dirs = []
    filesList = os.listdir()
    for i in filesList:
        if (os.path.isdir(i)):
            dirs.append(i)
    return (dirs)

class RunGroup:
    def __init__(self, group, configRunners, resultFile, pathToLoad):
        self.group = group
        self.configRunners = configRunners
        self.resultFile = resultFile
        self.pathToLoad = pathToLoad

    def run(self):
        file = self.pathToLoad + "/src/"
        shutil.copy(file + "main.c", ".")
        for i in self.configRunners:
            shutil.copy(file + i["args"], ".")
            testX = TestRunner(self.group, i["name"], i["compilation"], i["result"], i["quantity"], i["args"])
            testX.run()
            self.resultFile.write(testX.getJson() + "\n")
            os.remove(i["args"])
        os.remove("main.c")
def getTestsToRun():
    configFile = open("src/tests.json", "r")
    dataConfig = json.load(configFile)
    configFile.close()
    return (dataConfig)

class Group:
    def __init__(self, name: str):
        self.name = name
        self.moys = []

    def addMoy(self, e: int):
        if (e < 0):
            self.moys.append(4200000000)
        self.moys.append(e)

    def getGlobalMoyenne(self):
        return (sum(self.moys) / len(self.moys))

    def getQuantity(self):
        return (len(self.moys))


def analysis():
    groups = {}
    resultFile = open("result.json", "r")

    readed = resultFile.readline()
    while (readed != ""):
        data = json.loads(readed)
        if data["group"] not in groups:
            groups[data["group"]] = Group(data["group"])
        groups[data["group"]].addMoy(data["moyenne"])
        readed = resultFile.readline()
    resultFile.close()

    best = []
    for i_key, i_value in groups.items():
        if not best:
            best = [i_key, i_value]
        elif best[1].getGlobalMoyenne() > i_value.getGlobalMoyenne():
            best = [i_key, i_value]
        print(TextColors.WHITE + "Group named " + TextColors.RESET + TextColors.CYAN + i_value.name + TextColors.RESET + TextColors.WHITE + " got an global average of " + TextColors.YELLOW + str(i_value.getGlobalMoyenne()) + TextColors.RESET + TextColors.WHITE + " on " + TextColors.YELLOW + str(i_value.getQuantity()) + TextColors.RESET + TextColors.WHITE + " tests !")
    print("The best group was " + TextColors.MAGENTA + best[0] + TextColors.RESET + TextColors.WHITE + " with a global average of " + TextColors.RESET + TextColors.GREEN + str(best[1].getGlobalMoyenne()))

def runner(directory):
    resultFile = open("result.json", "w+", buffering=1)
    configRunners = getTestsToRun()
    basePath = os.getcwd()
    os.chdir(directory)
    dirs = getAllDirectory()
    testPath = os.getcwd()

    for i in dirs: #for each group
        os.chdir(i)
        groupRunner = RunGroup(i, configRunners, resultFile, basePath)
        groupRunner.run()
        os.chdir(testPath)
    resultFile.close()
    os.chdir(basePath)
    analysis()

if (len(sys.argv) == 1):
    runner(os.getcwd())
runner(sys.argv[1])