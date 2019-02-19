import subprocess
from powerline_shell.utils import ThreadedSegment


class Segment(ThreadedSegment):
    def run(self):
        try:
            p1 = subprocess.Popen(["kubectl", "config","current-context"], stdout=subprocess.PIPE)
            self.context = p1.communicate()[0].decode("utf-8").rstrip()
        except OSError:
            self.context = None

    def add_to_powerline(self):
        self.join()
        if not self.context:
            return
        # FIXME no hard-coded colors
        if "-prd" in self.context:
            self.powerline.append(self.context, 15, 1)
        elif "-acc" in self.context:
            self.powerline.append(self.context, 15, 13)
        elif "-acc" in self.context:
            self.powerline.append(self.context, 15, 22)
        else:
            self.powerline.append(self.context, 15, 25)
