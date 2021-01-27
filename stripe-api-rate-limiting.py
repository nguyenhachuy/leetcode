"""
Design a system to detect and implement API rate-limiting for a server.
given a limit, and a time window
start sending request with time, and check whether request succeeds or not

one way is using math to do window, but a burst of request in the beginning or end will
nullify all other requests
another way is storing requests in an array, do logn to binary search for positions, and calculate
length between positions.
"""
from collections import defaultdict
from collections import deque
import unittest

class RateLimiter:
    def __init__(self, timespan, requests_per_timespan):
        self.requests_per_timespan = requests_per_timespan
        self.timespan = timespan
        self.requests = defaultdict(deque)
        if requests_per_timespan <= 0:
            raise Exception('requests per timespan must be nonzero')
        if timespan <= 0:
            raise Exception('timespan must be nonzero')

    def is_allow(self, client_id, request_time):
        client_requests_list = self.requests[client_id]
        if len(client_requests_list) < self.requests_per_timespan:
            client_requests_list.append(request_time)
            return True
        else:
            oldest_request = client_requests_list.popleft()
            time_difference = request_time - oldest_request
            if time_difference < self.requests_per_timespan:
                return False
            client_requests_list.append(request_time)
            return True


class TestRateLimiter(unittest.TestCase):
    def test_different_clients(self):
        rate_limiter = RateLimiter(1,1)
        self.assertTrue(rate_limiter.is_allow('client1', 1))
        self.assertTrue(rate_limiter.is_allow('client2', 1))

    def test_limiter_single_client(self):
        rate_limiter = RateLimiter(1,1)
        self.assertTrue(rate_limiter.is_allow('client1', 0.5))
        self.assertFalse(rate_limiter.is_allow('client1', 1))

    def test_limiter_two_windows(self):
        rate_limiter = RateLimiter(1,1)
        self.assertTrue(rate_limiter.is_allow('client1', 0.5))
        self.assertTrue(rate_limiter.is_allow('client1', 1.5))
        self.assertFalse(rate_limiter.is_allow('client1', 2.4))

    def test_limiter_non_zero_starting(self):
        rate_limiter = RateLimiter(1,1)

    def test_invalid_requests_per_timespan(self):
        with self.assertRaisesRegex(Exception, 'requests per timespan must be nonzero'):
            RateLimiter(1,0)

    def test_invalid_timespan(self):
        with self.assertRaisesRegex(Exception, 'timespan must be nonzero'):
            RateLimiter(0,1)

if __name__ == '__main__':
    unittest.main()
