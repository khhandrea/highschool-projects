function shuffle(a) {
    var j, x, i;
    for (i = a.length; i; i -= 1) {
        j = Math.floor(Math.random() * i);
        x = a[i - 1]; //swap a[i-1] and a[j]
        a[i - 1] = a[j];
        a[j] = x;
    }
}

function printSeat() {
    var a = [], b = [];
    var k = 1, i;

    for (i = 0; i < 8; i++) {
        b[i] = $("#inp" + (i + 1)).val(); // get b
    }

    b.sort(function (m, n) {
        return (m - n); // sort b
    });

    for (i = 1; i < 32; i++) {
        if (i == b[k - 1]) {
            k++;
            continue;
        }
        else {
            a.push(i);
        }
    }

    shuffle(a);
    shuffle(b);

    for (i = 0; i < 31; i++) {
        $("#b" + (i + 1)).html(a[i]); // put a into box
    }

    for (i = 0; i < 8; i++) {
        $("#s" + (i + 1)).html(b[i]); // put b into box
    }

    $("div").css("color", "rgba(0, 0, 0, 1.0)");
}

function inIt() {
    $("button").click(function () {
        printSeat();
    });
}

inIt();