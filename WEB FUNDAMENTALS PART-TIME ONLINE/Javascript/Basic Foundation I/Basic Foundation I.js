// Get 1 to 255
function get_array() {
    var arr = [];
    for(var i=1; i<=255; i++){
        arr.push(i);
    }
    return arr;
}

// Get even 1000
function sum_even_numbers(){
    var sum = 0;
    for (var i = 1;i<=1000;i++){
        if (i%2==0){
            sum=sum+i
        }
    }
    return sum; 
}

// Sum odd 5000
function sum_odd_5000() {
    var sum = 0;
    for (var i = 1;i<=5000;i++){
        if (i%2!=0){
            sum+=i
        }
    } 
    return sum; 
}

// Iterate an array
function iterArr(arr) {
    var sum=0;
    for (var i=0; i<arr.length;i++){
        sum+=arr[i];
    }
    return sum; 
}

// Find max
function findMax(arr) {
    var max=0;
    for (var i=0;i<=arr.length;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    } 
    return max; 
}

// Find average
function findAvg(arr) {
    var sum=0;
    for(var i=0;i<arr.length;i++){
        sum+=arr[i];
    }
    var avg=sum/arr.length;
    return avg; 
}

// Array odd
function oddNumbers() {
    var arr = [];
    for (var i=1;i<=50;i++){
        if(i%2!=0){
            arr.push(i);
        }
    } 
    return arr; 
}

// Greater than Y
function greaterY(arr, Y) {
    var count = 0;
    for(var i=0;i<=arr.length;i++){
        if(arr[i]>Y){
            count+=1;
        }
    }
    return count; 
}

// Squares 
function squareVal(arr) {
    for(var i = 0; i<arr.length;i++){
        arr[i]=arr[i]**2;
    }
    return arr; 
}

// Negatives 
function noNeg(arr) {
    for(var i = 0;i<=arr.length;i++){
        if(arr[i]<0){
            arr[i]=0;
        }
    }
    return arr; 
}

// Max/Min/Avg
function maxMinAvg(arr) {
    var arrnew=[];
    var min=0;
    var max=0;
    var sum=0;
    for (var i = 0; i<arr.length;i++){
        sum+=arr[i];
    }
    for (var i=0;i<=arr.length;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    for (var i=0;i<=arr.length;i++){
        if(arr[i]<min){
            min=arr[i];
        }
    }
    arrnew.push(max);
    arrnew.push(min);
    arrnew.push(sum/arr.length);
    return arrnew; 
}

// Swap Values
function swap(arr) {
    var arrnew = arr;
    var temp = arr[arr.length-1];
    var temp2 = arr[0];
    arrnew[0] = temp;
    arrnew[arr.length-1]=temp2;
    return arrnew; 
}

// Number to String
function numToStr(arr) {
    for(var i = 0;i<=arr.length;i++){
        if(arr[i]<0){
            arr[i]="Dojo";
        }
    }
    return arr; 
}