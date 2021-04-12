// ==UserScript==
// @name         get
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://localhost/
// @require      https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/seedrandom/3.0.5/seedrandom.min.js
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    var str="data:text/csv;charset=utf-8,";
    var measurement;
    var measurement2;

    var link;

    var seedRandom = new Math.seedrandom('exjobb');

    var div = document.createElement("DIV");
    div.setAttribute("id", "getbox");
    div.setAttribute("style", "border:1px solid black; display: inline-block;");
    document.body.appendChild(div);

    var phpmysql = document.createElement("INPUT");
    phpmysql.setAttribute("type", "radio");
    phpmysql.setAttribute("name", "link");
    phpmysql.setAttribute("value", "http://localhost/PHP/RESTapi-MySQL/rest.php");
    document.getElementById("getbox").appendChild(phpmysql);
    var phpmysqltext = document.createElement("label");
    phpmysqltext.innerHTML= "PHP MySQL<br>";
    document.getElementById("getbox").appendChild(phpmysqltext);

    var phpnomysql = document.createElement("INPUT");
    phpnomysql.setAttribute("type", "radio");
    phpnomysql.setAttribute("name", "link");
    phpnomysql.setAttribute("value", "http://localhost/PHP/RESTapi-withoutMySQL/rest.php");
    document.getElementById("getbox").appendChild(phpnomysql);
    var phpnomysqltext = document.createElement("label");
    phpnomysqltext.innerHTML= "PHP without MySQL<br>";
    document.getElementById("getbox").appendChild(phpnomysqltext);

    var flaskmysql = document.createElement("INPUT");
    flaskmysql.setAttribute("type", "radio");
    flaskmysql.setAttribute("name", "link");
    flaskmysql.setAttribute("value", "http://127.0.0.1:5000/");
    document.getElementById("getbox").appendChild(flaskmysql);
    var flaskmysqltext = document.createElement("label");
    flaskmysqltext.innerHTML= "FLASK MySQL<br>";
    document.getElementById("getbox").appendChild(flaskmysqltext);

    var flasknomysql = document.createElement("INPUT");
    flasknomysql.setAttribute("type", "radio");
    flasknomysql.setAttribute("name", "link");
    flasknomysql.setAttribute("value", "http://127.0.0.1:5000/");
    document.getElementById("getbox").appendChild(flasknomysql);
    var flasknomysqltext = document.createElement("label");
    flasknomysqltext.innerHTML= "FLASK without MySQL<br>";
    document.getElementById("getbox").appendChild(flasknomysqltext);

    var iterations;
    var iterationsinput = document.createElement("INPUT");
    iterationsinput.setAttribute("type", "number");
    document.getElementById("getbox").appendChild(iterationsinput);

    var btn = document.createElement("INPUT");
    btn.setAttribute("type", "button");
    btn.setAttribute("value", "GET");
    btn.onclick = function(){
        iterations = iterationsinput.value;
        link = document.querySelector('input[name="link"]:checked').value;

        $.getJSON("../flightdata.json", function(json) {
            for(var i = 0; i < iterations;i++){
                var param = randomParam(json);
                get(param);
                var delta = measurement2 - measurement;
                str += delta + ",\n";
            }
            getData()
        });
    }
    document.getElementById("getbox").appendChild(btn);

    var getAllBtn = document.createElement("INPUT");
    getAllBtn.setAttribute("type", "button");
    getAllBtn.setAttribute("value", "GET ALL");
    getAllBtn.onclick = function(){
        iterations = iterationsinput.value;
        link = document.querySelector('input[name="link"]:checked').value;
        for(var i = 0; i < iterations;i++){
                getAll();
                var delta = measurement2 - measurement;
                str += delta + ",\n";
            }
        getData()
    }
    document.getElementById("getbox").appendChild(getAllBtn);

    function get(param){
        var xhr = new XMLHttpRequest();
        xhr.open("GET", link + param, false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        measurement = performance.now();
        xhr.send();
        console.log(xhr.responseText);
        measurement2 = performance.now();
    }

    function getAll(){
        var xhr = new XMLHttpRequest();
        xhr.open("GET", link, false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        measurement = performance.now();
        xhr.send();
        console.log(xhr.responseText);
        measurement2 = performance.now();
    }

    function getData()
    {
        var anchor = document.createElement("a");
        anchor.setAttribute("href", encodeURI(str));
        anchor.setAttribute("download", "my_data.csv");
        anchor.innerHTML= "Click Here to download";
        document.body.appendChild(anchor);
        //anchor.click();
    }

    function randomParam(array) {
        var obj = array[array.length * seedRandom() << 0];
        var keys = Object.keys(obj);
        var key = keys[ keys.length * seedRandom() << 0];
        return "?" + key + "=" + obj[key];
    };
})();