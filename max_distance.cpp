int Solution::maximumGap(const vector<int> &A) {
    vector<bool> myArr(A.size());
    int min = A[0];
    int max_distance = 0;
    int i = A.size()-1;
    int j = A.size()-1;
    
    for(int i = 0; i < A.size(); i++){
        if(A[i] > min){
            myArr[i] = false;
        }
        else{
            min = A[i];
            myArr[i] = true;
        }
    }

    while(i >= 0){
        if(myArr[i] == false){  # there is at leats one number on the left that is smaller than this..so this one cant be i
            i--;
            continue;
        }
        while((A[i] > A[j]) && (j > i)){
            j--;
        }
        if((j-i) > max_distance){
            max_distance = j-i;
        }
        i--;
    }
    return max_distance;
}
