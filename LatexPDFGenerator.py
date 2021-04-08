import threading
import subprocess

class LatexPDFGenerator(threading.Thread):
    def __init__(self, inputPath, outputPath):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def run(self):
        p = subprocess.Popen('rsync -av /etc/passwd /tmp'.split(),
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        self.stdout, self.stderr = p.communicate()