// setInterval(function() {
//   var form = document.getElementById('permanent-form');
//   var formData = new FormData(form);
//   var xhr = new XMLHttpRequest();
//   // xhr.open('POST', 'save_data');
//   xhr.send(formData);
// }, 5000);
//
// setInterval(function() {
//   var form = document.getElementById('temporary-form');
//   var formData = new FormData(form);
//   var xhr = new XMLHttpRequest();
//   // xhr.open('POST', 'save_data');
//   xhr.send(formData);
// }, 5000);

function saveData(item_id) {
  var form = document.getElementById(item_id);
  var formData = new FormData(form);
  var xhr = new XMLHttpRequest();
  // xhr.open('POST', 'save_data');
  xhr.send(formData);
}
setInterval(function(id) {
  saveData('temporary-form');
}, 5000);
setInterval(function(id) {
  saveData('permanent-form');
}, 5000);

