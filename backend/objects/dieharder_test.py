import subprocess
from objects.prng import PRNG

# Constants
RESULT_LINE_NUMBER = 8
DIEHARDER = 'dieharder'
GENERATOR_NUMBER = '-g200'
PASSED = 'PASSED'
FAILED = 'FAILED'
WEAK = 'WEAK'

class DieharderTest:
    def __init__(self, testNumber, mode):
        self.testNumber = testNumber
        self.mode = mode

    def runSubprocess(self, prng: PRNG):
        args = [DIEHARDER, GENERATOR_NUMBER, f'-d{self.testNumber}']
        # use subprocess.PIPE to access stdin and stdout
        # enables stdin.write() and stdout.readlines()
        dieharderTestProc = subprocess.Popen(args, stdout=subprocess.PIPE,
                                             stdin=subprocess.PIPE)
        while dieharderTestProc.returncode is None:
            for number in prng.generateNumberSequence():
                try:
                    dieharderTestProc.stdin.write(number)
                except:
                    break
            # p.poll() needs to check if process terminated, else code returns BrokenPipeError
            dieharderTestProc.poll()
        procOutput = dieharderTestProc.stdout.readlines()
        # only use needed line where test data is saved
        # this saves strip work
        return str(procOutput[RESULT_LINE_NUMBER])

    def stripOutputIntoVariables(self, output: str):
        name, ntup, tsamples, psamples, pvalue, result = output.split('|')

        if(PASSED in result):
            self.result = PASSED
        if(FAILED in result):
            self.result = FAILED
        if(WEAK in result):
            self.result = WEAK

        self.name = name.strip('b\'').strip()
        self.ntup = ntup.strip()
        self.tsamples = tsamples.strip()
        self.psamples = psamples.strip()
        self.pvalue = pvalue.strip()

    def asDict(self):
        return {'n_tup': self.ntup, 't_samples': self.tsamples, 'p_samples': self.psamples, 'p_value': self.pvalue, 'result': self.result, 'mode': self.mode}

