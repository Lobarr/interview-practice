# /*

# class CoinSum {

#   public static HashMap<String, Integer> cache = new

#   public static int compute(int[] coins, int total) {

#   }

#   public static int findWays(int current, int startFrom) {

#   }
# }

# */

# /*

# Example 1:

# Input: [1, 2, 3], 4
# Output: 4

# Possible Combinations:
# 1 + 1 + 1 + 1
# 1 + 3
# 1 + 1 + 2
# 2 + 2

# Example 2:

# Input: [2, 5, 3, 6], 10
# Output: 5

# Possible Combinations:

# 2 + 3 + 5
# 5 + 5
# 2 + 3 + 2 + 3
# 2 + 2 + 6
# 2 + 2 + 2 + 2 + 2

# */

# function coinSum(coins, total) {

#   function findWays(current, startFrom) {
#     if (current === 0) {
#       // console.log(path);
#       return 1;
#     }
#     if (current < 0) {
#       // console.log("BAD PATHS: ", path);
#       return 0;
#     }

#     let result = 0;

#     for (let i = startFrom; i < coins.length; i++) {
#       let coin = coins[i];
#       // path.push(coin);
#       result += findWays(current - coin, i);
#       // path.pop();
#     }

#     return result;
#   }

#   return findWays(total, 0);
# }

# // 1) Create cache
# // 2) Check cache
# // 3) Write to cache

# function coinSumMemo(coins, total) {
#   const cache = {};
#   function findWays(current, startFrom) {
#     let key = current + '_' + startFrom;
#     if (key in cache) {
#       return cache[key];
#     }
#     if (current === 0) {
#       // console.log(path);
#       return 1;
#     }
#     if (current < 0) {
#       // console.log("BAD PATHS: ", path);
#       return 0;
#     }

#     let result = 0;

#     for (let i = startFrom; i < coins.length; i++) {
#       let coin = coins[i];
#       // path.push(coin);
#       result += findWays(current - coin, i);
#       // path.pop();
#     }

#     cache[key] = result;
#     return result;
#   }

#   return findWays(total, 0);
# }

# function coinSumTab(coins, total) {
#   const table = new Array(total + 1).fill(0);
#   table[0] = 1;

#   for (let coin of coins) {
#     for (let i = coin; i < table.length; i++) {
#       table[i] = table[i] + table[i - coin];
#     }
#   }

#   return table[total];
# }

# // console.time("RECURSION: ");
# // console.log(coinSum([2, 5, 3, 6], 400));
# // console.timeEnd("RECURSION: ");

# // console.time("MEMOIZATION: ");
# // console.log(coinSumMemo([2, 5, 3, 6], 15000));
# // console.timeEnd("MEMOIZATION: ");

# console.time("TABULATION: ");
# console.log(coinSumTab([2, 5, 3, 6], 50000));
# console.timeEnd("TABULATION: ");
