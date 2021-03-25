"""
Throughout this interview, we'll write code to analyze a simple server uptime log. These logs are much simplified, and are just strings of space separated 0's and 1's.
The log is a string of binary digits (e.g. "0 0 1 0"). Each digit corresponds to 1 hour of the server running:

"1" = <crashed>, "down" // server crashed during the hour
"0" = <didn't crash>, "up" // server did not crash during the hour

EXAMPLE: A server with log "0 0 1 0" ran for 4 hours and crashed during hour #3

   hour: |1|2|3|4|
   log : |0|0|1|0|
              ^
              |
             down during hour #3
We can *permanently remove* a server at the beginning of any hour during its operation. A server is on the network until it is removed.
Note that a server stays POWERED ON after removal, it's just not on the network.

  EXAMPLE: Remove a server with log "0 0 1 0"
            | 0 | 1 | 2 | 3 |
    hour :  | 1 | 2 | 3 | 4 | 5 |
    log  :  | 0 | 0 | 1 | 0 |
remove_at:  0   1   2   3   4   // remove_at being `x` means "server removed before hour `x+1`"
            ^               ^
            |               |
     before hour #1         after hour #4

We'd like to understand the best times to remove a server.
So let's introduce an aggregate metric called a "penalty" for removing a server at a bad time.

Write a function: compute_penalty, that computes the total penalty, given
a server log (as a string) AND
a time at which we removed the server from the network (call that  variable remove_at)

Note that for a server log of length `n` hours, the remove_at variable can range from 0,
meaning "before the first hour" to n, meaning "after the final hour".

1b)
Use your answer for compute_penalty to write another function: find_best_removal_time, that returns
the best remove_at hour, given a server log.

"""

def find_best_removal_time(server_log):
    # best removal time is 0, if all is operational, we return -1
    n = len(server_log)+1
    for time in range(n):
        penalty = compute_penalty(server_log, time)
        if penalty == -1:
            return -1
        if penalty == 0:
            return time

    return -1

def compute_penalty(server_log, remove_at):
    # import pudb; pu.db
    server_log = server_log.split(" ")
    server_log = [int(x) for x in server_log]

    if 1 not in server_log:
        return -1

    down_hour = server_log.index(1)
    if remove_at >= down_hour:
        return remove_at - down_hour
    else:
        return down_hour - remove_at + 1

def get_best_removal_times(server_logs):
    log_buffer = None
    tokens = server_logs.split(" ")
    result = []

    for token in tokens:
        if token == "BEGIN":
            log_buffer = []
        elif token == "END" and log_buffer:
            result.append(find_best_removal_time(" ".join(log_buffer)))
            log_buffer = None
        elif (token == "1" or token == "0") and log_buffer != None:
            log_buffer.append(token)

    return result

import unittest

class TestPenalty(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(compute_penalty("0 0 1 0", 0), 3)
        self.assertEqual(compute_penalty("0 0 1 0", 1), 2)
        self.assertEqual(compute_penalty("0 0 1 0", 2), 1)
        self.assertEqual(compute_penalty("0 0 1 0", 3), 1)

    def test_best_removal_time(self):
        self.assertEqual(find_best_removal_time("0 0 1 0"), 2)

    def test_get_best_removal_times(self):
        self.assertEqual(get_best_removal_times("BEGIN BEGIN BEGIN 1 1 BEGIN 0 0 END 1 1 END"), [-1])
if __name__ == '__main__':
    unittest.main()
