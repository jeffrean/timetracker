let $ = require('jquery')  // jQuery now loaded and assigned to $
let count = 0
$('#click-counter').text(count.toString())
$('#countbtn').on('click', () => {
	count++ 
	$('#click-counter').text(count)
}) 

$.ajax({
	xhrFields: {
		withCredentials: true
	},
	beforeSend: function (xhr) {
		xhr.setRequestHeader('Authorization', 'Basic ' + btoa('amanj41:python'));
	},
	url: "http://localhost:5000/api/users/1/timestamps",
	success: function(data) {
	let p = "{timestamps: " + data.timestamps + "}"
	$("#resp").text(p);
	}

})