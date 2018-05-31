function external1() {
    document.getElementById('innerScript').innerHTML = "External hello."
}
function externalDocumentWriteEx()
{
    document.write("Document.write has the potential to delete everything.")
}
function virus(){
    window.alert("Your computer has been infected!")
}
function consoleOutput() {
    console.log("Hello World")
}

//an object can contain a function
function getPerson(first, last, age, eyeColor)
{
    var person ={
        firstName : first,
        lastName : last,
        age : age,
        eyeColor : eyeColor,
        fullName : function (){
           return this.firstName + " " + this.lastName;
        }
    };

    return person;

}