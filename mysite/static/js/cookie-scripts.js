document.addEventListener("DOMContentLoaded", function () {// Function to dynamically load Google Analytics

    function getCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    function setCookie(name, value, days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/; SameSite=Lax";
    }

    function loadScript(src) {
        var newScript = document.createElement('script');
        newScript.async = true;
        newScript.src = src;
        document.head.appendChild(newScript);
    }

    function checkCookieAndLoadScript(cookieName) {
        var consentCookie = getCookie(cookieName);
        if (consentCookie) {
            var consentValues = JSON.parse(consentCookie);
            
            // Using category values load the relevant script
            if (consentValues.includes("statistics")) {
                console.log("Loading Google Analytics");
                loadScript('https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID'); // Replace with your actual GA ID
            }

            if (consentValues.includes("marketing")) {
                console.log("Loading marketing");
                //loadScript();
            }
        }
    }

    var scriptTag = document.getElementById("conditional-script");
    var cookieName = scriptTag.getAttribute("data-cookie");

    var expectedVersionElement = document.getElementById('cookie-version');
    var expectedVersion = expectedVersionElement.getAttribute('data-expected-version');
    var consentVersion = getCookie('consent_version');

    if (consentVersion !== expectedVersion) {
        document.getElementById('cookie-consent').style.display = 'block';
        // Optionally clear the old 'consent' cookie
        setCookie('consent', '', -1);
    }

    document.getElementById('accept').addEventListener('click', function () {
        var selectedCategories = [];
        var checkboxes = document.querySelectorAll('#cookie-categories input:checked');

        checkboxes.forEach(function (checkbox) {
            selectedCategories.push(checkbox.name);
        });

        setCookie('consent', JSON.stringify(selectedCategories), 365);
        setCookie('consent_version', expectedVersion, 365); // Set the version cookie here
        document.getElementById('cookie-consent').style.display = 'none';
    });

    document.getElementById('decline').addEventListener('click', function () {
        setCookie('consent', 'false', 365);
        setCookie('consent_version', expectedVersion, 365); // Set the version cookie here
        document.getElementById('cookie-consent').style.display = 'none';
    });


    // Call checkCookieConsent when the page loads
    checkCookieAndLoadScript(cookieName);

});
