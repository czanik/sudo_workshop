import sudo

class MyIOPlugin(sudo.Plugin):
    def log_ttyout(self, buf):
        if "MySecret" in buf:
          sudo.log_info("Don't look at my secret!")
          return sudo.RC.REJECT

