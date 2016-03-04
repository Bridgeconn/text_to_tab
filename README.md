# text_to_tab
Chapter-wise Bible text to tab separated files.

### What does this script do?
Converts a .txt file containing a Bible chapter in specific format to a tab separated format.  
e.g.  
Sample input file:

```
MAT 1
1. अब्राहमो री ल्वाद, दाऊदो री ल्वाद, प्रभु यीशुओ रा कुल।
2. अब्राहमो रे इसहाक ऊआ; इसहाको रे याकूब ऊआ; याकूबो रे यहूदा और यहूदो रे ओर बी मुखते पाई ऊए।
3. यहूदो रे फिरिस, यहूदो री लाड़ी तामारा ते जोरह ऊआ, फिरिसो रे हिस्रोन जम्मेया और हिस्रोनो रे एराम ऊआ;
4.  एरामो रे अम्मीनादाब ऊआ, अम्मीनादाबो रे नहशोन ऊआ और नहशोनो रे सलमोन ऊआ।
```

Corresponding output file: (*found at outputs/inputFileName_output.txt*)  
```
MAT 	1 	 1	  अब्राहमो री ल्वाद, दाऊदो री ल्वाद, प्रभु यीशुओ रा कुल।
MAT 	1 	 2	  अब्राहमो रे इसहाक ऊआ; इसहाको रे याकूब ऊआ; याकूबो रे यहूदा और यहूदो रे ओर बी मुखते पाई ऊए।
MAT 	1    3	  यहूदो रे फिरिस, यहूदो री लाड़ी तामारा ते जोरह ऊआ, फिरिसो रे हिस्रोन जम्मेया और हिस्रोनो रे एराम ऊआ;
MAT 	1 	 4 	  एरामो रे अम्मीनादाब ऊआ, अम्मीनादाबो रे नहशोन ऊआ और नहशोनो रे सलमोन ऊआ।
```

### What file format does it expect?
+ First line should be BookName [space] chapterNumber as shown in the sample input file.
+ Next line on each verse should be in new lines with the verse number before the verse text. Verse numbers may or may not be separated by . (dot) or [space] or no separation.
+ All numbers should be converted to English!

### How do I run it?  
+ Copy the script to any location other than the folder containing the input files.
+ The input files may be under sub-directories. It doesn't matter.
+ Run as ``` python text_to_tab.py \path\to\input\file\directory\```
