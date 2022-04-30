import shlex
import subprocess


class DieharderTest:
    def __init__(self, testNumber):
        # call prng with subprocess
        prngCmd = 'python3 lcg.py'
        args = shlex.split(prngCmd)
        prngProc = subprocess.run(args, check=True, capture_output=True)

        # call dieharder with chosen test and use prng subprocess as input
        dieharderCmd = 'dieharder -g200 -d{}'.format(testNumber)
        args = shlex.split(dieharderCmd)
        dieharderProc = subprocess.run(
            args, input=prngProc.stdout, capture_output=True)

        # get dieharder output and safe needed values into variables
        output = str(dieharderProc.stdout)
        output = output[output.rfind('Assessment') + 95:]
        name, ntup, tsamples, psamples, pvalue, result = output.split('|')

        self.name = name.replace(' ', ''),
        self.ntup = ntup.replace(' ', ''),
        self.tsamples = tsamples.replace(' ', ''),
        self.psamples = psamples.replace(' ', ''),
        self.pvalue = pvalue.replace(' ', ''),
        self.result = result.replace(' ', '').strip('\n'),

    def __str__(self) -> str:
        return f'{self.name}, {self.ntup}, {self.tsamples}, {self.psamples}, {self.pvalue}, {self.result}'
