var header = document.getElementsByClassName('header')[0];
header.innerHTML = '';
var nameString = 'bryclee';

for (var i = 0; i < nameString.length; i++) {
	(function(i) {
		window.setTimeout(function() {
			var newChar = document.createElement('span');
			newChar.innerText = nameString[i];
			newChar.className = 'letter';
			header.appendChild(newChar);
		}, (i + 1) * 200);
	})(i);
}
