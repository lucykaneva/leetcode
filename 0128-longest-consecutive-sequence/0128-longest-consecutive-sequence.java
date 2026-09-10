class Solution {

    public int longestConsecutive(int[] nums) {

        // Store all numbers
        Set<Integer> set = new HashSet<>();

        for (int num : nums) {

            set.add(num);
        }

        int longest = 0;

        // Traverse unique numbers
        for (int num : set) {

            /*
             * Start only if
             * previous number
             * doesn't exist
             */

            if (!set.contains(num - 1)) {

                int currentNum = num;
                int count = 1;

                // Extend sequence
                while (set.contains(currentNum + 1)) {

                    currentNum++;
                    count++;
                }

                longest = Math.max(longest,
                                   count);
            }
        }

        return longest;
    }
}