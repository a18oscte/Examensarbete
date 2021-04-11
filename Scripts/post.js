// ==UserScript==
// @name         post
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://localhost/
// @require     https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    var str="data:text/csv;charset=utf-8,";
    var measurement;
    var measurement2;

    var link;

    var phpmysql = document.createElement("INPUT");
    phpmysql.setAttribute("type", "radio");
    phpmysql.setAttribute("name", "link");
    phpmysql.setAttribute("value", "http://localhost/PHP/RESTapi-MySQL/rest.php");
    document.body.appendChild(phpmysql);
    var phpmysqltext = document.createElement("label");
    phpmysqltext.innerHTML= "PHP MySQL<br>";
    document.body.appendChild(phpmysqltext);

    var phpnomysql = document.createElement("INPUT");
    phpnomysql.setAttribute("type", "radio");
    phpnomysql.setAttribute("name", "link");
    phpnomysql.setAttribute("value", "http://localhost/PHP/RESTapi-withoutMySQL/rest.php");
    document.body.appendChild(phpnomysql);
    var phpnomysqltext = document.createElement("label");
    phpnomysqltext.innerHTML= "PHP without MySQL<br>";
    document.body.appendChild(phpnomysqltext);

    var flaskmysql = document.createElement("INPUT");
    flaskmysql.setAttribute("type", "radio");
    flaskmysql.setAttribute("name", "link");
    flaskmysql.setAttribute("value", "http://127.0.0.1:5000/");
    document.body.appendChild(flaskmysql);
    var flaskmysqltext = document.createElement("label");
    flaskmysqltext.innerHTML= "FLASK MySQL<br>";
    document.body.appendChild(flaskmysqltext);

    var flasknomysql = document.createElement("INPUT");
    flasknomysql.setAttribute("type", "radio");
    flasknomysql.setAttribute("name", "link");
    flasknomysql.setAttribute("value", "http://127.0.0.1:5000/");
    document.body.appendChild(flasknomysql);
    var flasknomysqltext = document.createElement("label");
    flasknomysqltext.innerHTML= "FLASK without MySQL<br>";
    document.body.appendChild(flasknomysqltext);

    var iterations;
    var iterationsinput = document.createElement("INPUT");
    iterationsinput.setAttribute("type", "number");
    document.body.appendChild(iterationsinput);

    var btn = document.createElement("INPUT");
    btn.setAttribute("type", "button");
    btn.setAttribute("value", "POST");
    btn.onclick = function(){
        iterations = iterationsinput.value;
        link = document.querySelector('input[name="link"]:checked').value;
        console.log(link);

        $.getJSON("../flightdata.json", function(json) {
            for(var i = 0; i < iterations;i++){
                post(json[i]);
                var delta = measurement2 - measurement;
                str += delta + ",\n";
                console.log(i);
            }
            console.log(str);
            getData()
        });
    }
    document.body.appendChild(btn);

    function post(json){
        var xhr = new XMLHttpRequest();
        xhr.open("POST", link, false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        measurement = performance.now();
        xhr.send(JSON.stringify(json));
        measurement2 = performance.now();
    }

    function getData()
    {
        // Make anchor and click it!
        var anchor = document.createElement("a");
        anchor.setAttribute("href", encodeURI(str));
        anchor.setAttribute("download", "my_data.csv");
        anchor.innerHTML= "Click Here to download";
        document.body.appendChild(anchor);
        //anchor.click();
    }
})();