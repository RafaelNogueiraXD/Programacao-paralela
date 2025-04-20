#include <iostream>
#include <vector>
using namespace std;
class Solution {
    public:
        bool satisfiesConditions(vector<vector<int>>& grid) {
            // cout << "entrou na func" << endl;
            int altura = grid.size();
            int largura = grid[0].size();
            if(altura == 1 && largura == 1) return true;
            if(altura == 1){
                for(int j = 0; j < largura; j ++ ){
                    if(j + 1 >= largura )break;
                    if(grid[0][j] == grid[0][j + 1])return false;
                }
                return true;
            } 
            // cout << "passou pros for" << endl;
            
            for(int i = 0;   i < altura - 1 ; i++){
                cout << endl;
                for(int j = 0; j < largura; j ++ ){
                    if(grid[i][j] != grid[i + 1][j])return false;
                    if(j + 1 >= largura )break;
                
                    if(grid[i][j] == grid[i][j + 1])return false;
                }
            }
            return true;
        }
};


int main(){
    Solution sol;
    cout << "hello word" << endl;
    vector<vector<int>> matriz = {
        {0,4,1,7,5,4,1,4,0,7}
    };
    cout << endl <<" a matriz eh " << sol.satisfiesConditions(matriz) << endl;
}