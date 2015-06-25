(function() {
	var header = document.querySelector('#header');
	header.innerHTML = '';

	var headerWords = [
		'bl', 'bryclee', 'bryan c lee', 'be a cat'
	];
	var characterNodes = [];

	var changeHeaderWord = function(newWord) {
		var newWordLetters = {};
		var newWordNodes = [];
		var tempNodeStorage = [];
		var removeNodeStorage = [];
		var i, pos, node;
		for (i = 0; i < newWord.length; i++) {
			newWordLetters[newWord[i]] = newWordLetters[newWord[i]] || [];
			newWordLetters[newWord[i]].push(i);
		}
		while (node = characterNodes.pop()) {
			if (newWordLetters[node.letter]) {
				pos = newWordLetters[node.letter].pop();
				newWordNodes[pos] = node.node;
				if (!newWordLetters[node.letter].length) {
					delete newWordLetters[node.letter];
				}
				tempNodeStorage.push(node);
			} else {
				removeNodeStorage.push(node);
				node.node.className = 'letter exit';
			}
		}
		for (i = 0; i < newWord.length; i++) {
			if (!newWordNodes[i]) {
				node = document.createElement('span');
				node.textContent = node.innerText = newWord[i];
				node.className = 'letter enter';
				header.appendChild(node);
				characterNodes.push({letter: newWord[i], node: node});
				newWordNodes[i] = node;
			}
			newWordNodes[i].style.left = i * 50 + 'px';
		}
		while (node = tempNodeStorage.pop()) {
			characterNodes.push(node);
		}
		window.setTimeout(function() {
			var node;
			while (node = removeNodeStorage.pop()) {
				header.removeChild(node.node);
			}
		}, 800);
	};

	var setNextWord = function(index, delay) {
		changeHeaderWord(headerWords[index]);
		window.setTimeout(function() {
			setNextWord((index + 1) % headerWords.length, delay);
		}, delay);
	};

	setNextWord(0, 2000)
})();
