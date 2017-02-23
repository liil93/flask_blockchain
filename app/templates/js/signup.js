
function onClicked(elem) {
  if(elem.id == "create_using_email_button") {
    var signup_select = document.getElementById("signup-select");
    var signup_email = document.getElementById("signup-email");
    signup_select.classList.add('hide');
    signup_email.classList.remove('hide');
  }

}
