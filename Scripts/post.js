// ==UserScript==
// @name         testare
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://localhost/RESTapi-MySQL/
// @require     https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
     $.getJSON("../flightdata.json", function(json) {
          // this will show the info it in firebug console
         for(var i = 0; i < json.length;i++){
             console.log(i);
             var xhr = new XMLHttpRequest();
             xhr.open("POST", "http://localhost/RESTapi-MySQL/post.php", true);
             xhr.setRequestHeader('Content-Type', 'application/json');
             xhr.send(JSON.stringify(json[i]));
             xhr.onreadystatechange = (e) => {
                 console.log(xhr.responseText)
             }
         }
         console.log("done");
});

    // Your code here...
})();