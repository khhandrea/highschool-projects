const
    optionInput = document.getElementById("option"),

    button1 = document.getElementById("b1"),
    button2 = document.getElementById("b2"),
    button3 = document.getElementById("b3"),
    button4 = document.getElementById("b4"),
    button5 = document.getElementById("b5"),


    DEF_COLOR = "white",
    SEL_COLOR = "darkgray",

    specialQuestion = document.getElementById("specialQuestion"),
    specialQuestionInput = document.getElementById("q5"),

    submitButton = document.querySelector(".submitButton"),
    fakeButton = document.querySelector(".fakeButton"),
    $fakeButton = fakeButton;

function buttonClicked() {
    $("#b1").removeClass("fieldSelected");
    $("#b1").children(".ico").removeClass("fieldSelectedIco");
    $("#b2").removeClass("fieldSelected");
    $("#b2").children(".ico").removeClass("fieldSelectedIco");
    $("#b3").removeClass("fieldSelected");
    $("#b3").children(".ico").removeClass("fieldSelectedIco");
    $("#b4").removeClass("fieldSelected");
    $("#b4").children(".ico").removeClass("fieldSelectedIco");
    $("#b5").removeClass("fieldSelected");
    $("#b5").children(".ico").removeClass("fieldSelectedIco");

    submitButton.style.display = "inline";
    fakeButton.style.display = "none";
}

function handleButton1() {
    buttonClicked();
    optionInput.value = "홍보부";
    $("#b1").addClass("fieldSelected");
    $("#b1").children(".ico").addClass("fieldSelectedIco");
    specialQuestionInput.style.display = "block";
    specialQuestion.innerText = "+) 친구가 많다고 생각하나요?"
}

function handleButton2() {
    buttonClicked();
    optionInput.value = "관리부";
    $("#b2").addClass("fieldSelected");
    $("#b2").children(".ico").addClass("fieldSelectedIco");
    specialQuestionInput.style.display = "block";
    specialQuestion.innerText = "+) 끈기가 있는 일화를 말해주세요"
}

function handleButton3() {
    buttonClicked();
    optionInput.value = "기획부";
    $("#b3").addClass("fieldSelected");
    $("#b3").children(".ico").addClass("fieldSelectedIco");
    specialQuestionInput.style.display = "block";
    specialQuestion.innerText = "+) 했으면 좋을 아이디어를 적어주세요"
}

function handleButton4() {
    buttonClicked();
    optionInput.value = "개발부";
    $("#b4").addClass("fieldSelected");
    $("#b4").children(".ico").addClass("fieldSelectedIco");
    specialQuestionInput.style.display = "block";
    specialQuestion.innerText = "+) 직접 만든 작품이 있으신가요?"
}

function handleButton5() {
    buttonClicked();
    optionInput.value = "디자인부";
    $("#b5").addClass("fieldSelected");
    $("#b5").children(".ico").addClass("fieldSelectedIco");
    specialQuestionInput.style.display = "none";
    specialQuestion.innerText = "+) khhandrea@naver.com으로 디자인을 보내주세요!"

}

function inIt() {
    specialQuestionInput.style.display = "none";
    submitButton.style.display = "none";
    button1.addEventListener("click", handleButton1);
    button2.addEventListener("click", handleButton2);
    button3.addEventListener("click", handleButton3);
    button4.addEventListener("click", handleButton4);
    button5.addEventListener("click", handleButton5);
    fakeButton.addEventListener("click", function () {
        alert("지원분야를 선택해주세요!");
    });
}

inIt();
$(document).ready(function () {

});