var header = document.querySelector('#header');
var subheader = document.querySelector('#subheader');
header.innerHTML = '';
subheader.innerHTML = '';
var nameString = 'bryclee';

for (var i = 0; i < nameString.length; i++) {
	(function() {
		var j = i;
		window.setTimeout(function() {
			var newChar = document.createElement('span');
			newChar.appendChild(document.createTextNode(nameString.charAt(j)));
			newChar.className = 'letter enter';
			header.appendChild(newChar);
		}, (j + 1) * 200);
	})();
}

window.setTimeout(function() {
	var span = document.createElement('span');
	span.appendChild(document.createTextNode('coming soon'));
	span.className = 'letter enter';
	subheader.appendChild(span);
}, (i + 1) * 200 + 500);
