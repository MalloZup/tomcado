#!/usr/bin/env python

import time
import subprocess
from avocado import Test

class Tomcatservice(Test):

    def test_service_restart(self):
        #restart = self.params.get('restarts', default=1)
        # self.log.debug("Restart tomcat %.2f ", restart)
        try:
            subprocess.check_output("systemctl restart tomcat", shell=True)
        except subprocess.CalledProcessError as e:
            self.fail("restart failed: {0}".format(e.output))
