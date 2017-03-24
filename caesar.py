def alphabet_position(letter):
	alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
	alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if letter.islower():
		alphabet = alphabet_lowercase
	else:
		alphabet = alphabet_uppercase
	return alphabet.index(letter)
	
def rotate_character(char, rot):
	alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
	alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if not char.isalpha():
		return char
	position = alphabet_position(char)
	alphabet = alphabet_lowercase if char.islower() else alphabet_uppercase
	new_pos = (position + rot) % 26
    
	return (alphabet[new_pos])

def encrypt(text, rot):
	answer = ""
	for char in text:
		answer += rotate_character(char, rot)
	return answer