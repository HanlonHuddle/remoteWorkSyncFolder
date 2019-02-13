/*
 * @lc app=leetcode id=934 lang=java
 *
 * [934] Shortest Bridge
 *
 * https://leetcode.com/problems/shortest-bridge/description/
 *
 * algorithms
 * Medium (42.52%)
 * Total Accepted:    5.2K
 * Total Submissions: 12.2K
 * Testcase Example:  '[[0,1],[1,0]]'
 *
 * In a given 2D binary array A, there are two islands.  (An island is a
 * 4-directionally connected group of 1s not connected to any other 1s.)
 * 
 * Now, we may change 0s to 1s so as to connect the two islands together to
 * form 1 island.
 * 
 * Return the smallest number of 0s that must be flipped.  (It is guaranteed
 * that the answer is at least 1.)
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [[0,1],[1,0]]
 * Output: 1
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [[0,1,0],[0,0,0],[0,0,1]]
 * Output: 2
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
 * Output: 1
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length = A[0].length <= 100
 * A[i][j] == 0 or A[i][j] == 1
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */
class Solution {
    public int shortestBridge(int[][] A) {
        if (A==null || A[0]==null)
            return 0;
        int sx = 0, sy = 0;
        for (int i=0; i<A.length; i++)
            for (int j=0; j<A[0].length; j++) 
                if (A[i][j] == 1) {
                    sx = i;
                    sy = j;
                    break;
                }
        if (sx == A.length && sy == A[0].length)
            return 0;
        
        DeQueue<int[]> dq = new DeQueue<int[]>();
        DeQueue<int[]> dqbfs = new DeQueue<int[]>();
        dq.add(new int[]{sx, sy});

        dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (dq.length() > 0) {
            cur = dq.pollFirst();
            boolean edge = false;
            for (dir : dirs) {
                if ((0 <= cur[0] + dir[0] < A.length) && (0 <= cur[1] + dir[1] < A[0].length)) {
                    if (A[cur[0]+dir[0]][cur[1]+dir[1]] == 0)
                        edge = true;
                    else if (A[cur[0]+dir[0]][cur[1]+dir[1]] == 1)
                        dq.add(new int[]{cur[0]+dir[0], cur[1]+dir[1]});
                }
            }
            if (edge)
                dqbfs.add(cur[0], cur[1]);
            A[cur[0], cur[1]] = -1;
        }

        while (dqbfs.lemgth() > 0) {
            
        }

        return 0;
    }
}
