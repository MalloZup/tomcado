#!/usr/bin/env python

import time
import subprocess
import avocado
from avocado import Test

# FIXME: USE A Valid real upgrade test
class UpgradeTomcat(Test):
    """
    This test want to upgrade tomcat by zypper installation.
    Default repo is the latest tomcat from tumbleweed
    """
    # use avocado decorator for avoiding try/except.
    avocado.fail_on(subprocess.CalledProcessError)
    def test_upgrade(self):
        tumbleweed = "FIMXMe"
        repo = self.params.get('repo', default=tumbleweed)
        subprocess.check_output("systemctl restart tomcat", shell=True)
