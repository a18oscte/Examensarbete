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
    var iterations = 100;
    var link = "http://localhost/PHP/RESTapi-MySQL/rest.php";

    var str="data:text/csv;charset=utf-8,";
    var measurement;
    var measurement2;

    var btn = document.createElement("INPUT");
    btn.setAttribute("type", "button");
    btn.setAttribute("value", "POST");
    btn.onclick = function(){
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