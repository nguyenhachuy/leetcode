from collections import Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_count = 0
        max_freq = max(freq.values()) # Max frequency
        max_count = len([x for x in freq.values() if x == max_freq]) # Number of characters with max_freq as freq

        number_of_parts = max_freq - 1 # Number of windows (A_A_A has 2 windows)
        part_length = n - (max_count - 1) # Expand each part A to ABC if B and C has the same number of freq max. -1 to avoid double counting A
        empty_slots = number_of_parts * part_length
        available_tasks = len(tasks) - max_freq * max_count # Leftover tasks to fit
        idles = max(0, empty_slots - available_tasks) # If cannot fit all tasks, idle time must be 0
        return len(tasks) + idles # Return length of tasks + any idle time

"""
if n = 0 return (base case)
optimal for only 1 task is #tasks + #tasks*n
this is the lower bound because you can't finish tasks any faster. So letter with highest frequency determines lower bound

public class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] counter = new int[26];
        int max = 0;
        int maxCount = 0;
        for(char task : tasks) {
            counter[task - 'A']++;
            if(max == counter[task - 'A']) {
                maxCount++;
            }
            else if(max < counter[task - 'A']) {
                max = counter[task - 'A'];
                maxCount = 1;
            }
        }

        int partCount = max - 1;
        int partLength = n - (maxCount - 1);
        int emptySlots = partCount * partLength;
        int availableTasks = tasks.length - max * maxCount;
        int idles = Math.max(0, emptySlots - availableTasks);

        return tasks.length + idles;
    }
}

"""
def main():
    sol = Solution()
    print(sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
if __name__ == "__main__":
  main()
