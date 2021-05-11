var myVar;

myFunction()

function myFunction() {
  myVar = setInterval(alertFunc, 1000);
}

function alertFunc() {
  document.getElementById("fecha").innerHTML = new Date().toLocaleString()
}