# Input string
input_string = "han"

# Convert the input string to uppercase
input_string = input_string.upper()

# Hangul Jamo lists
initial_jamos = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
medial_jamos = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
final_jamos = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# Mapping of Latin characters to Hangul Jamos
latin_to_jamo = {
    'G': 'ㄱ', 'K': 'ㄱ', 'N': 'ㄴ', 'D': 'ㄷ', 'L': 'ㄹ', 'M': 'ㅁ', 'B': 'ㅂ', 'S': 'ㅅ', 'J': 'ㅈ', 'C': 'ㅊ',
    'A': 'ㅏ', 'E': 'ㅔ', 'Y': 'ㅖ', 'O': 'ㅗ', 'U': 'ㅜ', 'W': 'ㅝ', 'I': 'ㅣ', 'H': 'ㅎ'
}

# Convert input string to Hangul Jamo integers
hangul_integers = []
for char in input_string:
    if char in latin_to_jamo:
        hangul_integers.append(latin_to_jamo[char])
print(hangul_integers)

# Calculate the integer using the formula
result = 44032
result += (initial_jamos.index(hangul_integers[0]) * 21 * 28) + (medial_jamos.index(hangul_integers[1]) * 28) + (final_jamos.index(hangul_integers[2]))
print(chr((result)))
