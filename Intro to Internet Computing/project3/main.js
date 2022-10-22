function ProcessData() {
    var num1, num2, max, min, avg, median, range, count = 0, sum;
    var oneon = false, twoon = false, threeon = false;
    num1 = (document.form.num1.value);
    num2 = (document.form.num2.value);
    num3 = (document.form.num3.value);

    //Nothing Input
    document.form.max.value = "Nothing Input";
    document.form.min.value = "Nothing Input";
    document.form.avg.value = "Nothing Input";
    document.form.median.value = "Nothing Input";
    document.form.range.value = "Nothing Input";

    //count
    if (num1.length > 0) { count++; oneon = true; }
    if (num2.length > 0) { count++; twoon = true; }
    if (num3.length > 0) { count++; threeon = true; }

    //if not a number
    if (isNaN(num1)) { alert("first number is not a number"); }
    if (isNaN(num2)) { alert("Second number is not a number"); }
    if (isNaN(num3)) { alert("Third number is not a number"); }

    //parse int
    num1 = parseInt(num1);
    num2 = parseInt(num2);
    num3 = parseInt(num3);

    //Calculate Max
    if (count == 1) {
        if (oneon) { max = num1; document.form.max.value = max; }
        if (twoon) { max = num2; document.form.max.value = max; }
        if (threeon) { max = num3; document.form.max.value = max; }
    } else if (count == 2) {
        if (oneon && twoon) {
            if (num1 >= num2) { max = num1; document.form.max.value = max; }
            else if (num2 >= num1) { max = num2; document.form.max.value = max; }
        }
        if (twoon && threeon) {
            if (num2 >= num3) { max = num2; document.form.max.value = max; }
            else if (num3 >= num2) { max = num3; document.form.max.value = max; }
        }
        if (threeon && oneon) {
            if (num3 >= num1) { max = num3; document.form.max.value = max; }
            else if (num1 >= num3) { max = num1; document.form.max.value = max; }
        }
    } else if (count == 3) {
        if (num1 >= num2 && num1 >= num3) {
            max = num1;
            document.form.max.value = max;
        } else if (num2 >= num1 && num2 >= num3) {
            max = num2;
            document.form.max.value = max;
        } else if (num3 >= num1 && num3 >= num2) {
            max = num3;
            document.form.max.value = max;
        }
    }

    //Calculate Min
    if (count == 1) {
        if (oneon) { min = num1; document.form.min.value = min; }
        if (twoon) { min = num2; document.form.min.value = min; }
        if (threeon) { min = num3; document.form.min.value = min; }
    } else if (count == 2) {
        if (oneon && twoon) {
            if (num1 <= num2) { min = num1; document.form.min.value = min; }
            else if (num2 <= num1) { min = num2; document.form.min.value = min; }
        }
        if (twoon && threeon) {
            if (num2 <= num3) { min = num2; document.form.min.value = min; }
            else if (num3 <= num2) { min = num3; document.form.min.value = min; }
        }
        if (threeon && oneon) {
            if (num3 <= num1) { min = num3; document.form.min.value = min; }
            else if (num1 <= num3) { min = num1; document.form.min.value = min; }
        }
    } else if (count == 3) {
        if (num1 <= num2 && num1 <= num3) {
            min = num1;
            document.form.min.value = min;
        } else if (num2 <= num1 && num2 <= num3) {
            min = num2;
            document.form.min.value = min;
        } else if (num3 <= num1 && num3 <= num2) {
            min = num3;
            document.form.min.value = min;
        }
    }

    //Calculate Sum
    if (count == 1) {
        if (oneon) { sum = num1 }
        if (twoon) { sum = num2 }
        if (threeon) { sum = num3 }
    } else if (count == 2) {
        if (oneon && twoon) {
            sum = num1 + num2;
        }
        if (twoon && threeon) {
            sum = num2 + num3;
        }
        if (threeon && oneon) {
            sum = num3 + num1;
        }
    } else if (count == 3) {
        sum = num1 + num2 + num3;
    }

    //Calculate Average
    if (count != 0) {
        avg = sum / count;
        document.form.avg.value = avg;
    } else if (count == 1) {
        if (oneon) { avg = num1 }
        if (twoon) { avg = num2 }
        if (threeon) { avg = num3 }
        document.form.avg.value = avg;

    }

    //Sort
    if (count == 3) {
        if ((num1 == max && num2 == min) || (num2 == max && num1 == min)) { median = num3; }
        else if ((num1 == max && num3 == min) || (num3 == max && num1 == min)) { median = num2; }
        else if ((num3 == max && num2 == min) || (num2 == max && num3 == min)) { median = num1; }
        document.form.median.value = median;
    } else if (count == 2) {
        median = sum / 2;
        document.form.median.value = median;
    } else if (count == 1) {
        if (oneon) { median = num1 }
        if (twoon) { median = num2 }
        if (threeon) { median = num3 }
        document.form.median.value = median;
    }


    //calculate range
    if (count > 1) {
        range = max - min;
        document.form.range.value = range;
    } else if (count == 1) {
        document.form.range.value = 0;
    }

    //Reset
    count = 0;

}