//Variables for use in measure the time of the request
var str;
var measurement;
var measurement2;

//Variable used for choosing the link to the REST api
var link;
var iterations;

//Creates a object used to get seeded random numbers using the seedrandom.js library by David Bau
//Github link to the library: https://github.com/davidbau/seedrandom
var seededRandom = new Math.seedrandom('exjobb');

function postButton(){
    $("#outputBox").text("");
    str="data:text/csv;charset=utf-8,time,\n"
    //Gets the amount of iterations and the link to the chosen REST api
    iterations = $("#iterationsPost").val();
    link = document.querySelector('input[name="linkPost"]:checked').value;
    //Gets the JSON file with the filghtdata
    $.getJSON("../flightdata.json", function(json) {
        for(var i = 0; i < iterations;i++){
            $("#loadBox").text(i+1 +"/"+iterations);
            post(json[i]);
            //calculates the time it took to send the request and get a response from the REST api
            var delta = measurement2 - measurement;
            str += delta + ",\n";
        }
        getData()
    });
};

function getButton(){
    $("#outputBox").text("");
    str="data:text/csv;charset=utf-8,time,param,results,\n"
    //Gets the amount of iterations and the link to the chosen REST api
    iterations = $("#iterationsGet").val();
    link = document.querySelector('input[name="linkGet"]:checked').value;

    //Gets the JSON file with the filghtdata
    $.getJSON("../flightdata.json", function(json) {
        for(var i = 0; i < iterations;i++){
            $("#loadBox").text(i+1 +"/"+iterations);
            var param = randomParam(json);
            var results = get(param);
            //calculates the time it took to send the request and get a response from the REST api
            var delta = measurement2 - measurement;
            if(!results){
                results = "No matches found"
            }
            str += delta + "," + param + "," + results + ",\n";
        }
        getData()
    });
};

function getAllButton(){
    $("#outputBox").text("");
    str="data:text/csv;charset=utf-8,time,\n"
    //Gets the amount of iterations and the link to the chosen REST api
    iterations = $("#iterationsGet").val();
    link = document.querySelector('input[name="linkGet"]:checked').value;

    for(var i = 0; i < iterations;i++){
        $("#loadBox").text(i+1 +"/"+iterations);
        getAll();
        //calculates the time it took to send the request and get a response from the REST api
        var delta = measurement2 - measurement;
        str += delta + ",\n";
    }
    getData()
};

//Sends a HTTP request to the chosen REST api with the JSON data from the file
//Saves the time it takes to send he request and get a response from the REST api
function post(json){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", link, false);
    xhr.setRequestHeader('Content-Type', 'text/plain');
    measurement = performance.now();
    xhr.send(JSON.stringify(json));
    measurement2 = performance.now();
    $("<p>" + xhr.responseText + "</p>").appendTo("#outputBox");
    console.log(xhr.responseText);
};

//Sends a HTTP request to the chosen REST api with the parameters
//Saves the time it takes to send he request and get a response from the REST api
function get(param){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", link + param, false);
    xhr.setRequestHeader('Content-Type', 'text/plain');
    measurement = performance.now();
    xhr.send();
    measurement2 = performance.now();
    $("<p>" + xhr.responseText + "</p>").appendTo("#outputBox");
    console.log(xhr.responseText);
    return JSON.parse(xhr.responseText).length
};

//Sends a HTTP request to the chosen REST api without parameters to get all flightdata
//Saves the time it takes to send he request and get a response from the REST api
function getAll(){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", link, false);
    xhr.setRequestHeader('Content-Type', 'text/plain');
    measurement = performance.now();
    xhr.send();
    measurement2 = performance.now();
    $("<p>" + xhr.responseText + "</p>").appendTo("#outputBox");
    console.log(xhr.responseText);
};

//Creates a link to download a csv file with the data collected from the test
function getData()
{
    $( "#download" ).remove();
    var anchor = document.createElement("a");
    anchor.setAttribute("href", encodeURI(str));
    anchor.setAttribute("download", "my_data.csv");
    anchor.setAttribute("id", "download");
    anchor.innerHTML= "Click Here to download results";
    $( "#downloadBox" ).append(anchor);
};

//Gets a random key and value from the JSON file with the help from seedrandom.js
//Then returns a string with that can be added to the link to the REST api as a parameter
function randomParam(json) {
    var obj = json[json.length * seededRandom() << 0];
    var keys = Object.keys(obj);
    var key = keys[ keys.length * seededRandom() << 0];

    return "?" + key + "=" + obj[key];
};
