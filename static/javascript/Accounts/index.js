function Redirect_To_Students(){
    if(confirm("You are about to leave the site")){
        location.href="/student/";
    }
}

function SearchByID(){
    var id = $("#sid").val()
    location.href = "/accounts/GetStudentFeeDetails_Id/" + id;
}