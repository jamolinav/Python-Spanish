//import { data } from "jquery"
//const { data } = require("jquery")


$(document).ready(function() {
    $("#email").focusout(checkEmail)
})

function checkEmail(){
    console.log('lost focus email')
    var data = $("#formRegister").serialize()
    $.ajax({
        method : "POST",
        url : "/checkEmail",
        data : data,
        dateaType : "JSON"
    })
    .done (function(response){
        var size = Object.keys(response["errors"]).length
        if ( size > 0 ) {
            console.log(response["errors"])
        } else {
            console.log("Correo valido")
        }

    })
}