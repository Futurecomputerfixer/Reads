document.addEventListener("DOMContentLoaded", function () {
    let buttons = document.getElementsByClassName("checkout_button");
    for (let i = 0; i < buttons.length; i++) {
        if (buttons[i].innerHTML == "Check Out") {
            buttons[i].addEventListener("click", () => {
                fetch(`checkout/${buttons[i].value}`)
                    .then(response => response.json())
                    .then(data => {
                        date = data["date"];
                        alert("Please return the book by " + date);
                        document.querySelector("#index").click();
                    })
            });
        }
        else {
            buttons[i].addEventListener("click", () => {
                fetch(`checkout/${buttons[i].value}`)
                    .then(data => {
                        alert("Reading is so much fun");
                        document.querySelector("#index").click();
                    })
            });
        }
    }})
