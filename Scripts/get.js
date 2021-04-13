// ==UserScript==
// @name         get
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Oscar Ternevid
// @match        http://localhost/
// @require      https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/seedrandom/3.0.5/seedrandom.min.js
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    //Variables for use in measure the time of the request
    var str="data:text/csv;charset=utf-8,";
    var measurement;
    var measurement2;

    //Variable used for choosing the link to the REST api
    var link;

    //Creates a object used to get seeded random numbers using the seedrandom.js library by David Bau
    //Github link to the library: https://github.com/davidbau/seedrandom
    var seededRandom = new Math.seedrandom('exjobb');

    //Creating a div to hold the interface
    var div = document.createElement("DIV");
    div.setAttribute("id", "getbox");
    div.setAttribute("style", "border:1px solid black; display: inline-block;");
    document.body.appendChild(div);

    //Creating a input for the different REST api:s
    //PHP with MySQL
    var phpmysql = document.createElement("INPUT");
    phpmysql.setAttribute("type", "radio");
    phpmysql.setAttribute("name", "link");
    phpmysql.setAttribute("value", "http://localhost/PHP/RESTapi-MySQL/rest.php");
    document.getElementById("getbox").appendChild(phpmysql);
    var phpmysqltext = document.createElement("label");
    phpmysqltext.innerHTML= "PHP MySQL<br>";
    document.getElementById("getbox").appendChild(phpmysqltext);

    //PHP without MySQL
    var phpnomysql = document.createElement("INPUT");
    phpnomysql.setAttribute("type", "radio");
    phpnomysql.setAttribute("name", "link");
    phpnomysql.setAttribute("value", "http://localhost/PHP/RESTapi-withoutMySQL/rest.php");
    document.getElementById("getbox").appendChild(phpnomysql);
    var phpnomysqltext = document.createElement("label");
    phpnomysqltext.innerHTML= "PHP without MySQL<br>";
    document.getElementById("getbox").appendChild(phpnomysqltext);

    //Flask with MySQL
    var flaskmysql = document.createElement("INPUT");
    flaskmysql.setAttribute("type", "radio");
    flaskmysql.setAttribute("name", "link");
    flaskmysql.setAttribute("value", "http://127.0.0.1:5000/");
    document.getElementById("getbox").appendChild(flaskmysql);
    var flaskmysqltext = document.createElement("label");
    flaskmysqltext.innerHTML= "FLASK MySQL<br>";
    document.getElementById("getbox").appendChild(flaskmysqltext);

    //Flask without MySQL
    var flasknomysql = document.createElement("INPUT");
    flasknomysql.setAttribute("type", "radio");
    flasknomysql.setAttribute("name", "link");
    flasknomysql.setAttribute("value", "http://127.0.0.1:5000/");
    document.getElementById("getbox").appendChild(flasknomysql);
    var flasknomysqltext = document.createElement("label");
    flasknomysqltext.innerHTML= "FLASK without MySQL<br>";
    document.getElementById("getbox").appendChild(flasknomysqltext);

    //Creating a input for the amount of iterations
    var iterations;
    var iterationsinput = document.createElement("INPUT");
    iterationsinput.setAttribute("type", "number");
    document.getElementById("getbox").appendChild(iterationsinput);

    //Creating a button to start the get requests
    var btn = document.createElement("INPUT");
    btn.setAttribute("type", "button");
    btn.setAttribute("value", "GET");
    btn.onclick = function(){
        //Gets the amount of iterations and the link to the chosen REST api
        iterations = iterationsinput.value;
        link = document.querySelector('input[name="link"]:checked').value;

        //Gets the JSON file with the filghtdata
        $.getJSON("../flightdata.json", function(json) {
            for(var i = 0; i < iterations;i++){
                var param = randomParam(json);
                get(param);
                //calculates the time it took to send the request and get a response from the REST api
                var delta = measurement2 - measurement;
                str += delta + ",\n";
            }
            getData()
        });
    }
    document.getElementById("getbox").appendChild(btn);

    //Creating a button to start the get all flightdata requests
    var getAllBtn = document.createElement("INPUT");
    getAllBtn.setAttribute("type", "button");
    getAllBtn.setAttribute("value", "GET ALL");
    getAllBtn.onclick = function(){
        //Gets the amount of iterations and the link to the chosen REST api
        iterations = iterationsinput.value;
        link = document.querySelector('input[name="link"]:checked').value;

        for(var i = 0; i < iterations;i++){
            getAll();
            //calculates the time it took to send the request and get a response from the REST api
            var delta = measurement2 - measurement;
            str += delta + ",\n";
        }
        getData()
    }
    document.getElementById("getbox").appendChild(getAllBtn);

    //Sends a HTTP request to the chosen REST api with the parameters
    //Saves the time it takes to send he request and get a response from the REST api
    function get(param){
        var xhr = new XMLHttpRequest();
        xhr.open("GET", link + param, false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        measurement = performance.now();
        xhr.send();
        console.log(xhr.responseText);
        measurement2 = performance.now();
    }

    //Sends a HTTP request to the chosen REST api without parameters to get all flightdata
    //Saves the time it takes to send he request and get a response from the REST api
    function getAll(){
        var xhr = new XMLHttpRequest();
        xhr.open("GET", link, false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        measurement = performance.now();
        xhr.send();
        console.log(xhr.responseText);
        measurement2 = performance.now();
    }

    //Creates a link to download a csv file with the data collected from the test
    function getData()
    {
        var anchor = document.createElement("a");
        anchor.setAttribute("href", encodeURI(str));
        anchor.setAttribute("download", "my_data.csv");
        anchor.innerHTML= "Click Here to download";
        document.body.appendChild(anchor);
    }

    //Gets a random key and value from the JSON file with the help from seedrandom.js
    //Then returns a string with that can be added to the link to the REST api as a parameter
    function randomParam(json) {
        var obj = json[json.length * seededRandom() << 0];
        var keys = Object.keys(obj);
        var key = keys[ keys.length * seededRandom() << 0];

        return "?" + key + "=" + obj[key];
    };
})();