class Solution {

    public int maxFrequencyElements(int[] nums) {

        Map<Integer, Integer> freq = new HashMap<>();

        // STEP 1: Frequency count
        for (int i : nums) {

            if (freq.containsKey(i)) {
                freq.put(i, freq.get(i) + 1);
            } else {
                freq.put(i, 1);
            }
        }

        // STEP 2: Maximum frequency find karo
        int maxFreq = 0;

        for (int value : freq.values()) {
            maxFreq = Math.max(maxFreq, value);
        }

        // STEP 3: Jinki frequency maxFreq hai,
        // unki frequencies add karo
        int ans = 0;

        for (int value : freq.values()) {

            if (value == maxFreq) {
                ans += value;
            }
        }

        return ans;
    }
}