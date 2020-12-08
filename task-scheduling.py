class Solution(object):
    def schedule_tasks(self, tasks, workers):
        all_workers = set(workers)
        working = {}
        task_stages = {task:-1 for task in tasks}
        task_workers = {task:set() for task in tasks}
        time = 0

        while len(task_stages) > 0:
            print("time: ", time)
            # Free
            for worker in working:
                print(f"Worker {worker} finished Task {working[worker]} for L{task_stages[working[worker]]}")
                if task_stages[working[worker]] == 2:
                    del task_stages[working[worker]]

            temp_workers = set(all_workers)
            working = {}
            if not task_stages:
                break
            for task in task_stages:
                available_workers = temp_workers - task_workers[task]
                if len(available_workers) >= 1:
                    worker = available_workers.pop()
                    working[worker] = task
                    task_stages[task] += 1
                    task_workers[task].add(worker)
                    temp_workers.remove(worker)
                    print(f"Assigning {worker} to Task {task} for L{task_stages[task]}")
            time += 1

        print(f"Total time taken: {time}")


def main():
    sol = Solution()
    # sol.schedule_tasks(["A"], ["X", "Y", "Z"])
    # sol.schedule_tasks(["A", "B"], ["X", "Y", "Z"])
    sol.schedule_tasks(["A", "B", "C"], ["X", "Y", "Z"])
if __name__ == "__main__":
  main()


"""
How do we know if we cannot finish all tasks because not enough workers? n is larger than total workers
Space complexity: O(tasks+workers)
Time complexity: O(tasks*n)
When there are more tasks than worker, there will be tasks idling. 3*3=9/3 = 3, +1 for initial scheduling
O(tasks*n/workers + 1)
Worst case: O(tasks*n + 1)

How to account for idle time? Then I have to figure out
"""
