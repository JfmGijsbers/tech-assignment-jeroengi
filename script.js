// your endpoint url here
const url = "http://worldtimeapi.org/api/timezone/Europe";
axios
  .get(url)
  .then(function (response) {
    console.log(response.data);
    // get data and log it
  })
  .catch(function (error) {
    console.log(error);
  });

var weatherData = [
  { time: "11:00", temp: "32.2" },
  { time: "11:05", temp: "32.1" },
  { time: "11:10", temp: "31.5" },
  { time: "11:15", temp: "31.6" },
  { time: "11:20", temp: "31.2" },
  { time: "11:25", temp: "32.2" },
  { time: "11:30", temp: "31.7" },
];
var table = document.getElementById("table");

for (let key of weatherData) {
  // loop through the data and set table rows
  var row = table.insertRow(0);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  cell1.innerHTML = key.time;
  cell2.innerHTML = key.temp;
}
// Set table headers
var row = table.insertRow(0);
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);
cell1.innerHTML = "<b>Time</b>";
cell2.innerHTML = "<b>Temperature</b>";