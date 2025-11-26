const $box = $(".sltBox");
var mode = 1;
var a, aa, bb, cc, dd, ee, ff = 0;

function BtnClicked() {
    $(".s1").children(".sltBoxHidden").slideUp("fast").removeClass("slt");
    $(".s1").removeClass("slt");
    $(".s2").children(".sltBoxHidden").slideUp("fast").removeClass("slt");
    $(".s2").removeClass("slt");
    $(".s3").children(".sltBoxHidden").slideUp("fast").removeClass("slt");
    $(".s3").removeClass("slt");
    $(".s4").children(".sltBoxHidden").slideUp("fast").removeClass("slt");
    $(".s4").removeClass("slt");
    $(".s5").children(".sltBoxHidden").slideUp("fast").removeClass("slt");
    $(".s5").removeClass("slt");
}

function fieldBtnClicked() {
    $("#b1").removeClass("fieldSlt");
    $("#b2").removeClass("fieldSlt");
    $("#b3").removeClass("fieldSlt");
    $("#b4").removeClass("fieldSlt");
    $("#b5").removeClass("fieldSlt");
    $("#b6").removeClass("fieldSlt");
}

function frameAnimation() {
    aa = ($("#f1").val() == "" ? 0 : 1);
    bb = ($("#f2").val() == "" ? 0 : 1);
    cc = ($("#f3").val() == "" ? 0 : 1);
    dd = ($("#f4").val() == "" ? 0 : 1);
    ee = ($("#fieldInput").val() == "" ? 0 : 1);
    ff = ($("#f6").val() == "" ? 0 : 1);
    a = aa + bb + cc + dd + ee + ff;
    if (a < 6) {
        $(".submitBtn").fadeOut("fast");
    } else {
        $(".submitBtn").fadeIn("fast");
    }
}

$(document).ready(function () {
    //initialize inputs' value
    $("#f1").val("");
    $("#f2").val("");
    $("#f3").val("");
    $("#f4").val("");
    $("#fieldInput").val("");
    $("#f6").val("");


    /*
    /************ hover : animation ***************
    hover
    $box.hover(function () {
        $(this).addClass("hov");
    }, function () {
        $(this).removeClass("hov");
    });
    */

    /************ button click : animation ***************/
    $(".s1").click(function () {
        if (mode != 1) {
            mode = 1;
            BtnClicked();
            $(this).children(".sltBoxHidden").slideDown("fast");
            $(this).addClass("slt");
            $(this).children(".sltBoxHidden").addClass("slt");
        }
    });

    $(".s2").click(function () {
        if (mode != 2) {
            mode = 2;
            BtnClicked();
            $(this).children(".sltBoxHidden").slideDown("fast", function () {
                $("#f1").focus();
            });
            $(this).addClass("slt");
            $(this).children(".sltBoxHidden").addClass("slt");
        }
    });

    $(".s3").click(function () {
        if (mode != 3) {
            mode = 3;
            BtnClicked();
            $(this).children(".sltBoxHidden").slideDown("fast", function () {
                $("#f4").focus();
            });
            $(this).addClass("slt");
            $(this).children(".sltBoxHidden").addClass("slt");
        }
    });

    $(".s4").click(function () {
        if (mode != 4) {
            mode = 4;
            BtnClicked();
            $(this).children(".sltBoxHidden").slideDown("fast");
            $(this).addClass("slt");
            $(this).children(".sltBoxHidden").addClass("slt");
        }
    });

    $(".s5").click(function () {
        if (mode != 5) {
            mode = 5;
            BtnClicked();
            $(this).children(".sltBoxHidden").slideDown("fast", function () {
                $("#f6").focus();
            });
            $(this).addClass("slt");
            $(this).children(".sltBoxHidden").addClass("slt");
        }
    });

    /************ inputBox focusing script ***************/
    $(".fInputBox").focusin(function () {
        $(this).parent().addClass("inputBoxSlt");
        $(this).addClass("inputBoxSlt");
    });
    $(".fInputBox").focusout(function () {
        $(this).parent().removeClass("inputBoxSlt");
        $(this).removeClass("inputBoxSlt");
    });

    $("#f3").focusin(function () {
        $(this).attr("placeholder", "예 : 01040682448");
    });
    $("#f3").focusout(function () {
        $(this).attr("placeholder", "");
    });

    /************ s2(q1) inputBox script ***************/
    $(".inputBoxContainer").click(function () {
        $(this).children(".fInputBox").focus();
    });
    $(".finputBoxContainer").click(function () {
        $(this).children(".fInputBox").focus();
    });

    $("#b1").click(function () {
        fieldBtnClicked();
        $(this).addClass("fieldSlt");
        $("#fieldInput").val("홍보부");
        $(".specialQ").text("오랜 기간동안 지속적인 홍보와 관심을 끄는 방법이 무엇일까요?");
        $("#fieldInfo").html('앱과 새 컨텐츠 등을 학생들에게 홍보합니다');
    });
    $("#b2").click(function () {
        fieldBtnClicked();
        $(this).addClass("fieldSlt");
        $("#fieldInput").val("관리부");
        $(".specialQ").html("심사를 할 때 주제에 잘 맞는 작품과 주제에는 안 맞지만 참신한 작품 중<div class='mobBr'></div>어떤 것을 뽑으실 건지 이유와 함께 적어주세요");
        $("#fieldInfo").text("게시물 및 제출물을 평가하고 관리합니다");
    });
    $("#b3").click(function () {
        fieldBtnClicked();
        $(this).addClass("fieldSlt");
        $("#fieldInput").val("기획부");
        $(".specialQ").text("어플에 있으면 좋을 컨텐츠가 있나요?");
        $("#fieldInfo").text("애플리케이션의 기능 및 컨텐츠를 기획합니다");
    });
    $("#b4").click(function () {
        fieldBtnClicked();
        $(this).addClass("fieldSlt");
        $("#fieldInput").val("개발부");
        $(".specialQ").text("특별히 배우고 싶거나 도전하고 싶은 부분이 있나요?");
        $("#fieldInfo").text("클라이언트 및 서버를 프로그래밍합니다");
    });
    $("#b5").click(function () {
        fieldBtnClicked();
        $(this).addClass("fieldSlt");
        $("#fieldInput").val("UI");
        $(".specialQ").html("많은 sns(페북, 인스타 등)이<div class='mobBr'></div>위아래로 움직일수 있는데 이로 인한 장점은?");
        $("#fieldInfo").text("화면 전체의 디자인을 담당합니다");
    });
    $("#b6").click(function () {
        fieldBtnClicked();
        $(this).addClass("fieldSlt");
        $("#fieldInput").val("포스터");
        $(".specialQ").html("본인이 생각하는 디자인이란?");
        $("#fieldInfo").text("홍보 포스터 및 컨텐츠용 그림을 그립니다");
    });
    $("#goMain").click(function () {
        window.location.href = "index.html";
    });

});

function Init() {
    $(".sltBox").children(".sltBoxHidden").slideUp("fast", function () {
        $(this).css("display: block");
    });

    //activate $(".s1")
    $(".s1").children(".sltBoxHidden").slideDown("fast");
    $(".s1").addClass("slt");
    $(".s1").children(".sltBoxHidden").addClass("slt");
    mode = 1;

    //deactivate $(".submitBtn")    
    $(".submitBtn").css("display", "none");



    //activate $(".submitBtn")
    setInterval(frameAnimation, 1000);

}

Init();