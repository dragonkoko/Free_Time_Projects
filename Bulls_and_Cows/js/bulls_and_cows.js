var turn_counter;
var game_start_flag = 0;
var guess_number;
var number_of_digits;
var current_guess;
function guess() {
	var guess = document.getElementById("input_field_for_numbers").value;
	var guess_array_copy = String(parseInt(guess)).split('');
	current_guess = guess;
	var log = document.getElementById("log").innerHTML;
	var bulls = 0;
	var cows = 0;
	if(game_start_flag == 0) {
		newGame();
		game_start_flag = 1;
	}
	for(var i = 0; i < number_of_digits; i++) {
		for(var i2 = 0; i2 < number_of_digits; i2++) {
			if((guess_number[i] == guess_array_copy[i2]) && (i == i2)) {
				bulls++;
			} else if (guess_number[i] == guess_array_copy[i2]) {
				cows++;
			}				
		}
	}
	log = log.concat("Hod ");
	log = log.concat(turn_counter);
	log = log.concat(": ");
	log = log.concat(guess);
	log = log.concat(": ");
	log = log.concat(bulls);
	log = log.concat("b ");
	log = log.concat(cows);
	log = log.concat("c ");
	turn_counter++;
	document.getElementById("log").innerHTML = log;
	if((guess_array_copy[0] == guess_number[0]) && (guess_array_copy[1] == guess_number[1]) && (guess_array_copy[2] == guess_number[2]) && (guess_array_copy[3] == guess_number[3])) {
		alert("you won the game");
	}
}

function newGame() {
	number_of_digits = document.getElementById("input_field_number_of_digits").value;
	guess_number = [];
	for (var i = 0; i < number_of_digits; i++) {
		guess_number.push(0);
	}
	var flag = 0;
	var rand_int;
	for (var i = 0; i < number_of_digits; i++) {
		while(flag == 0) {
			rand_int = Math.floor((Math.random() * 10));
			for(i2 = 0; i2 < number_of_digits; i2++) {
				if(guess_number[i2] == rand_int) {
					flag = 0;
					i2 = 4;
				} else {
					flag = 1;
				}
			}
		}
		flag = 0;
		guess_number[i] = rand_int;
	}
	turn_counter = 1;
	document.getElementById("log").innerHTML = "";
}

function clean() {
	turn_counter = 1;
	document.getElementById("log").innerHTML = "";
}

function surrender() {
	var number = "";
	for (var i = 0; i < number_of_digits; i++) {
		number = number.concat(guess_number[i]);
	}
	var alert_log = "The secret number is ";
	alert_log = alert_log.concat(number);
	alert(alert_log);
}

function current_status() {
	var bulls = 0;
	var cows = 0;
	var guess_array_copy = String(parseInt(current_guess)).split('');
	for(var i = 0; i < number_of_digits; i++) {
		for(var i2 = 0; i2 < number_of_digits; i2++) {
			if((guess_number[i] == guess_array_copy[i2]) && (i == i2)) {
				bulls++;
			} else if (guess_number[i] == guess_array_copy[i2]) {
				cows++;
			}				
		}
	}
	var result = {};
	result["bulls"] = bulls;
	result["cows"] = cows;
	return result;
}

function show_status() {
	var result = current_status();
	var result_log = "";
	result_log = result_log.concat(result["bulls"]);
	result_log = result_log.concat(" bulls ");
	result_log = result_log.concat(result["cows"]);
	result_log = result_log.concat(" cows");
	alert(result_log);
}

function automatic_generation_of_new_number() {
	newGame();
}
