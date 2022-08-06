var generatedOTP = "";
var Password = "";
var Repassword = "";
var OTP = "";
var IsOTPVerified = false;
var IsPasswordVerified = false;
var IsPasswordValidated = false;

function GenerateOTP(){
    debugger;
    var email = document.getElementById("txtemail").value;
    if(email == '' || email == undefined || email == null){
        alert('Please enter email address!');
        return false;
    }
    $.ajax({
        url: 'generateOTP',
        data : {
            'email':email
        },
        dataType: "json",
        success: function (data) {
            if(data.OTP == ""){
                alert("Entered email is not registered with us.\nKindly check the entered email.");
                return false;
            }
            generatedOTP = data.OTP
        },
        error:function(){

        }
    })      
};
//***Validating Password***//
function PasswordValidationchange(){
    //document.getElementById("txtpassword").onchange = function(){
        debugger;
    Password = document.getElementById("txtpassword").value;
    IsPasswordValidated = validatePassword(Password);
    if(!IsPasswordValidated){
        $("#passworderror").show();
        document.getElementById("txtpassword").style.borderColor = "red";
    }
    else{
        $("#passworderror").hide();
        document.getElementById("txtpassword").removeAttribute("style");
    }
    if(IsPasswordValidated && IsPasswordVerified && IsOTPVerified){
        document.getElementById('btnSubmit').disabled = false;
    }
};
//***Verifying confirm Password***//
function ConfirmPasswordchange(){
    //document.getElementById("txtRepassword").onchange = function(){
    debugger;
    Repassword = document.getElementById("txtRepassword").value;
    if(Password == Repassword){
        IsPasswordVerified = true;
        $("#confirmpassworderror").hide();
        document.getElementById("txtRepassword").removeAttribute("style");
    }
    else{
        $("#confirmpassworderror").show();
        document.getElementById("txtRepassword").style.borderColor = "red";
    }
    if(IsPasswordValidated && IsPasswordVerified && IsOTPVerified){
        document.getElementById('btnSubmit').disabled = false;
    }
};
//***Verifying OTP**//
function VerifyOTPchange(){
    //document.getElementById("txtOTP").onchange = function(){
    debugger;
    OTP = document.getElementById("txtOTP").value;
    if(OTP == generatedOTP){
        IsOTPVerified = true;
        $("#OTPerror").hide();
        document.getElementById("txtOTP").removeAttribute("style");
    }
    else{
        $("#OTPerror").show();
        document.getElementById("txtOTP").style.borderColor = "red";
    }
    if(IsPasswordValidated && IsPasswordVerified && IsOTPVerified){
        document.getElementById('btnSubmit').disabled = false;
    }
};


function showPassword(){
    debugger;
    var password = document.getElementById("txtpassword");
    if (password.type === "password") {
        password.type = "text";
    } 
    else {
        password.type = "password";
    }
};
function showPassword1(){
    var Repassword = document.getElementById("txtRepassword");
    if (Repassword.type === "password") {
        Repassword.type = "text";
    } 
    else {
        Repassword.type = "password";
    }
};

function validatePassword(Password){
    var pattern = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[-+_!@#$%^&*.,?]).+$");
    var flag = false;
    if(Password.length >= 10 && pattern.test(Password)){
        flag = true;
    }
    return flag;
};