
  function formvalidation(){
    var firstname = document.getElementById("fname").value;
    var email = document.getElementById("email").value;

    var isFirstnameValid = checkfname(firstname);
    if (!isFirstnameValid){
      alert("First name must contain more than 3 letters");
      return false;
    }
    var isEmailValid = checkEmail(email);
    if (!isEmailValid){
      alert("Please provide a valid email");
      return false;
    }
    return true;
  }

  function checkfname(firstname){
    return firstname.length > 3;
  }

  function checkEmail(email){
    var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
  }
