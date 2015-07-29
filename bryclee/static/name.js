(function() {
	var header = document.querySelector('#header-banner');
	var headerLetters = document.querySelector('#header-letters');
	headerLetters.innerHTML = '';

	var headerWords = [
		'bl', 'bryclee', 'bryan c lee', 'cats are cool', 'so are dogs'
	];
	var characterNodes = []; //This array holds the current character nodes

	var changeHeaderWord = function(newWord) {
		var newWordLetters = {};
		var newWordNodes = [];
		var tempNodeStorage = [];
		var removeNodeStorage = [];
		var i, pos, node;
		//Create the letter counts for the new word to compare to the current word,
		//storing the index position that each letter is found at.
		for (i = newWord.length - 1; i >= 0; i--) {
			newWordLetters[newWord[i]] = newWordLetters[newWord[i]] || [];
			newWordLetters[newWord[i]].push(i);
		}
		while (node = characterNodes.pop()) {
			tempNodeStorage.push(node);
		}
		//Compare the current letters to the new word letters, marking the nodes that
		//will not be used in the new word, and assigning the new index to the nodes
		//that will be reused.
		while (node = tempNodeStorage.pop()) {
			if (newWordLetters[node.letter]) {
				pos = newWordLetters[node.letter].pop();
				newWordNodes[pos] = node.node;
				if (!newWordLetters[node.letter].length) {
					delete newWordLetters[node.letter];
				}
				characterNodes.push(node);
			} else {
				removeNodeStorage.push(node);
				node.node.className = 'letter exit';
			}
		}
		//Iterate over the new word, creating nodes for new letters when needed,
		//and reassigning the left value to reposition each of the letters
		for (i = 0; i < newWord.length; i++) {
			if (!newWordNodes[i]) {
				node = document.createElement('span');
				node.textContent = node.innerText = newWord[i];
				node.className = 'letter enter';
				headerLetters.appendChild(node);
				characterNodes.push({letter: newWord[i], node: node});
				newWordNodes[i] = node;
			}
			newWordNodes[i].style.left = i * 50 + 'px';
		}
		//Set width of parent for the anchor tag to properly resize
		header.style.width = newWord.length * 50 + 'px';

		//Clean up nodes that were marked for removal after the exit animation has finished playing
		window.setTimeout(function() {
			var node;
			while (node = removeNodeStorage.pop()) {
				headerLetters.removeChild(node.node);
			}
		}, 800);
	};

	//Cycle through the words in the headerWords array
	var setNextWord = function(index, delay) {
		changeHeaderWord(headerWords[index]);
		window.setTimeout(function() {
			setNextWord((index + 1) % headerWords.length, delay);
		}, delay);
	};

	setNextWord(0, 2000);
})();
