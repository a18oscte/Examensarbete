// ==UserScript==
// @name         post
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Oscar Ternevid
// @match        http://localhost/
// @require     https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js
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

    //Creating a div to hold the interface
    var div = document.createElement("DIV");
    div.setAttribute("id", "postbox");
    div.setAttribute("style", "border:1px solid black; display: inline-block;");
    document.body.appendChild(div);

    //Creating a input for the different REST api:s
    //PHP with MySQL
    var phpmysql = document.createElement("INPUT");
    phpmysql.setAttribute("type", "radio");
    phpmysql.setAttribute("name", "link");
    phpmysql.setAttribute("value", "http://localhost/PHP/RESTapi-MySQL/rest.php");
    document.getElementById("postbox").appendChild(phpmysql);
    var phpmysqltext = document.createElement("label");
    phpmysqltext.innerHTML= "PHP MySQL<br>";
    document.getElementById("postbox").appendChild(phpmysqltext);

    //PHP without MySQL
    var phpnomysql = document.createElement("INPUT");
    phpnomysql.setAttribute("type", "radio");
    phpnomysql.setAttribute("name", "link");
    phpnomysql.setAttribute("value", "http://localhost/PHP/RESTapi-withoutMySQL/rest.php");
    document.getElementById("postbox").appendChild(phpnomysql);
    var phpnomysqltext = document.createElement("label");
    phpnomysqltext.innerHTML= "PHP without MySQL<br>";
    document.getElementById("postbox").appendChild(phpnomysqltext);

    //Flask with MySQL
    var flaskmysql = document.createElement("INPUT");
    flaskmysql.setAttribute("type", "radio");
    flaskmysql.setAttribute("name", "link");
    flaskmysql.setAttribute("value", "http://127.0.0.1:5000/");
    document.getElementById("postbox").appendChild(flaskmysql);
    var flaskmysqltext = document.createElement("label");
    flaskmysqltext.innerHTML= "FLASK MySQL<br>";
    document.getElementById("postbox").appendChild(flaskmysqltext);

    //Flask without MySQL
    var flasknomysql = document.createElement("INPUT");
    flasknomysql.setAttribute("type", "radio");
    flasknomysql.setAttribute("name", "link");
    flasknomysql.setAttribute("value", "http://127.0.0.1:5000/");
    document.getElementById("postbox").appendChild(flasknomysql);
    var flasknomysqltext = document.createElement("label");
    flasknomysqltext.innerHTML= "FLASK without MySQL<br>";
    document.getElementById("postbox").appendChild(flasknomysqltext);

    //Creating a input for the amount of iterations
    var iterations;
    var iterationsinput = document.createElement("INPUT");
    iterationsinput.setAttribute("type", "number");
    document.getElementById("postbox").appendChild(iterationsinput);

    //Creating a button to start the post requests
    var btn = document.createElement("INPUT");
    btn.setAttribute("type", "button");
    btn.setAttribute("value", "POST");
    btn.onclick = function(){
        //Gets the amount of iterations and the link to the chosen REST api
        iterations = iterationsinput.value;
        link = document.querySelector('input[name="link"]:checked').value;

        //Gets the JSON file with the filghtdata
        $.getJSON("../flightdata.json", function(json) {
            for(var i = 0; i < iterations;i++){
                post(json[i]);
                //calculates the time it took to send the request and get a response from the REST api
                var delta = measurement2 - measurement;
                str += delta + ",\n";
                console.log(i);
            }
            getData()
        });
    }
    document.getElementById("postbox").appendChild(btn);

    //Sends a HTTP request to the chosen REST api with the JSON data from the file
    //Saves the time it takes to send he request and get a response from the REST api
    function post(json){
        var xhr = new XMLHttpRequest();
        xhr.open("POST", link, false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        measurement = performance.now();
        xhr.send(JSON.stringify(json));
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
})();