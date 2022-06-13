const https = require('https');
function getPhoneNumbers(country, phoneNumber) {
    //country
    //phoneNumber
    //get the calling code for the country
    // prepend the calling code to the phone number and return the string
    // if there are multiple calling codes returned highest index
    // +callingcode phonenumber
    let url = `https://jsonmock.hackerrank.com/api/countries?name=${country}`;
    const result = https.request(url, res => {
        console.log(`statusCode: ${res.statusCode}`);
        res.on('data', d => {
            console.log(d);
        });
    })
}

getPhoneNumbers('India', '9875534548')