class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        denominations = {1_000_000_000: "Billion", 1_000_000: "Million", 1_000: "Thousand", 100: "Hundred"}
        digits = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
        teens = {11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        double = {20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        if num <= 99:
            if num <= 10:
                return digits[num]
            elif 11 <= num <= 19:
                return teens[num]
            leftover = num % 10
            if leftover > 0:
                return double[(num // 10)*10] +  " " + self.numberToWords(leftover)
            else:
                return double[(num // 10)*10]

        s = []
        for n,w in denominations.items():
            partition = num // n
            if partition > 0:
                prefix = self.numberToWords(partition)
                s.append(prefix)
                s.append(w)
                leftover = num - partition*n
                if leftover > 0:
                    return " ".join(s) + " " + self.numberToWords(leftover)
                break

        return " ".join(s)



def main():
    sol = Solution()
    print(sol.numberToWords(123))
    print(sol.numberToWords(12345))
    print(sol.numberToWords(1234567))
    print(sol.numberToWords(1234567891))
    print(sol.numberToWords(1000))
    print(sol.numberToWords(55))
    print(sol.numberToWords(20))
if __name__ == "__main__":
  main()

"""
0 <= num <= 2147483647
Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

1-10, 11-19, 20-99, 100-900, 1000-900000, 1000000-999000000, 1 bil-2bil
given a number, divide by the range to get the correct denomination
x // 10
x // 100
x // 1000
x // 1000_000
x // 1000_000_000

Mod to get the interested digits, feed this into the function again


1234567891 minus 1 bil =
divide by 1 bil, get 1 => 1 billion + f(234567891)

234567891
divide by 1 bil get 0, divide by 1 mil, get 234, feed into function get "2 hundred thirty four"

567891
divide by 1000, get 567, feed into function get "five hundred sixty seven"

891
"eight hundred"

91
"ninety"

"one"
"""
