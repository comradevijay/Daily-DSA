function fun1(){

    let x = 5;

    function add(){
        let y = 5;
        return x + y;

    }

    return add;

}

let ans = fun1();

let a = ans();

console.log(a);
