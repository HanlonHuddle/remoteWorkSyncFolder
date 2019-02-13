/*
 * @lc app=leetcode id=874 lang=cpp
 *
 * [874] Walking Robot Simulation
 *
 * https://leetcode.com/problems/walking-robot-simulation/description/
 *
 * algorithms
 * Easy (29.00%)
 * Total Accepted:    6.7K
 * Total Submissions: 22.4K
 * Testcase Example:  '[4,-1,3]\n[]'
 *
 * A robot on an infinite grid starts at point (0, 0) and faces north.  The
 * robot can receive one of three possible types of commands:
 * 
 * 
 * -2: turn left 90 degrees
 * -1: turn right 90 degrees
 * 1 <= x <= 9: move forward x units
 * 
 * 
 * Some of the grid squares are obstacles. 
 * 
 * The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
 * 
 * If the robot would try to move onto them, the robot stays on the previous
 * grid square instead (but still continues following the rest of the route.)
 * 
 * Return the square of the maximum Euclidean distance that the robot will be
 * from the origin.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: commands = [4,-1,3], obstacles = []
 * Output: 25
 * Explanation: robot will go to (3, 4)
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
 * Output: 65
 * Explanation: robot will be stuck at (1, 4) before turning left and going to
 * (1, 8)
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 0 <= commands.length <= 10000
 * 0 <= obstacles.length <= 10000
 * -30000 <= obstacle[i][0] <= 30000
 * -30000 <= obstacle[i][1] <= 30000
 * The answer is guaranteed to be less than 2 ^ 31.
 * 
 * 
 */
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int x = 0, y = 0;
        int dirx = 0, diry = 1;
        vector<vector<int>> dirs {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int diri = 0;

        unordered_set<string> obs;

        for (auto& o : obstacles) {
            obs.insert(to_string(o[0]) + " " + to_string(o[1]));
        }
        
        for (auto& com : commands) {
            if (com > 0) {
                for (int i=0; i<com; ++i) {
                    if (obs.find(to_string(x + dirx)+" "+to_string(y + diry)) == obs.end()) {
                        x += dirx;
                        y += diry;
                    }
                }
            }
            else if (com == -2) {
                diri -= 1;
                if (diri < 0) {
                    diri = 3;
                }
                dirx = dirs[diri][0];
                diry = dirs[diri][1];
            } else {
                diri += 1;
                if (diri > 3) {
                    diri = 0;
                }
                dirx = dirs[diri][0];
                diry = dirs[diri][1];
            }
        }
        return x * x + y * y;
    }
};
