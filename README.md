# MasterSchedule

School course master schedule organizer and validator

FILES BEGINNING WITH F ARE FLASK EXAMPLES. THEY WERE RENAMED TO AVOID CONFLICT WITH OTHER FILES.

For the "serving" branch and its functionality, I use the following class combination to test a working schedule:

1. SPANISH 3* - Concurrent Enrollment
2. MATH 1010-Concurrent Enrollment
3. CALCULUS AB LAB
4. SPANISH 4* - Concurrent Enrollment
5. AP SPANISH LANGUAGE*
6. ART HONORS*
7. PAINTING 2
8. DRAWING 1

The order of classes entered does not matter.
For the "serving" branch and its functionality, I use the following class combination to test a non-working schedule:

1. RESOURCE ENGLISH*
2. MATH 1010-Concurrent Enrollment
3. CALCULUS AB LAB
4. SPANISH 4* - Concurrent Enrollment
5. AP SPANISH LANGUAGE*
6. ART HONORS*
7. PAINTING 2
8. DRAWING 1

Resource English and AP Spanish Language are both only available during period 3.

1. Say which class combinations work
2. Say when conflicting classes are
3. Dropdown for classes

["SPANISH 3* - Concurrent Enrollment","MATH 1010-Concurrent Enrollment","CALCULUS AB LAB","SPANISH 4* - Concurrent Enrollment","AP SPANISH LANGUAGE*","ART HONORS*","PAINTING 2","DRAWING 1"].forEach((x, i) => {let e = document.querySelector(`.class-input[name="class${i+1}"]`);e && (e.value = x);});