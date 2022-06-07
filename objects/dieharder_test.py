import subprocess


class DieharderTest:
    def __init__(self, testNumber):
        # call dieharder with chosen test and use prng subprocess as input
        args = ['dieharder', '-g001', f'-d{testNumber}']
        dieharderProc = subprocess.run(
            args, capture_output=True)
        # dieharderProc = subprocess.run(
        #     args, input=prngProc.stdout, capture_output=True)

        # get dieharder output and safe needed values into variables
        output = str(dieharderProc.stdout)
        output = output[output.rfind('Assessment') + 95:]
        name, ntup, tsamples, psamples, pvalue, result = output.split('|')
        if('PASSED' in result):
            self.result = 'PASSED'
        if('FAILED' in result):
            self.result = 'FAILED'
        if('WEAK' in result):
            self.result = 'WEAK'

        self.name = name.strip()
        self.ntup = ntup.strip()
        self.tsamples = tsamples.strip()
        self.psamples = psamples.strip()
        self.pvalue = pvalue.strip()

    def __str__(self) -> str:
        return f'{self.name}, {self.ntup}, {self.tsamples}, {self.psamples}, {self.pvalue}, {self.result}'
