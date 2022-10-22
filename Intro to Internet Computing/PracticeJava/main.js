function sumValues() {
    var num1, num2, max;
    num1 = Number(document.form.num1.value);
    num2 = Number(document.form.num2.value);
    num3 = Number(document.form.num3.value);

    if (num1 > num2 && num1 > num3) {
        max = num1;
        document.form.max.value = max;
    } else if (num2 > num1 && num2 > num3) {
        max = num2;
        document.form.max.value = max;
    } else if (num3 > num1 && num3 > num2) {
        max = num3;
        document.form.max.value = max;
    }

}



// var num1, num2, res;
// num1 = Number(document.form.num1.value);
// num2 = Number(document.form.num2.value);
// res = num1 + num2;
// document.form.result.value = res;