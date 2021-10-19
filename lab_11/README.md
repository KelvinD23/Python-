## CS-UY 1114 — Lab 10
# Deep vs Shallow Copying, `ord` and `chr`, and the Binary World
#### November 19th & 20th, 2020


**All lab work must be submitted within 24 hours of the start of your lab period on Gradescope** (we will be checking
this using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a
solution before your allotted lab time, you will get no credit. You must try each problem at least once (that is,
submitting at least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the
problems and continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to
remember to submit your work.


Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab. **The points awarded by the auto-grader on GradeScope will not be counted
towards your lab's grade, so don't worry if you don't pass every or any of its tests!**


Please do not hesitate to check with your TAs if you are ever confused as to how to proceed!

---
### Congratulations on getting through midterm 2!

No simple feat, I'm telling you. The material included in midterm 2 was tough, so I commend everyone for soldiering 
through it. If you can believe it, it only gets better from here. Or, if you don't like the sound of "better", then I'll
at least say that we are getting to the most interesting parts of the course soon. I'll do my best to reflect my 
enthusiasm by giving you fun lab problems.

As usual, we're here to answer any questions you may have. We will not have lab next week (November 26th and 27th) due 
to the Thanksgiving holidays, so enjoy your time off!

— _Sebastian_.

---

### Problem 1: Computers Dream In Binary

We'll start off simple, as we do, in the file [**binary_to_decimal.py**](binary_to_decimal.py).

Write a function called **`binary_to_decimal`**, that accepts `binary_list` as a parameter, a list representing a binary
number.

Your job is to simply convert the binary number represented by `binary_list` to its corresponding decimal value. Check 
out the sample behavior below:

```python
def main():
    binary = [1, 0, 0, 1, 1, 1]
    print(binary_to_decimal(binary))

main()
```
Output:
```text
39
```

You may assume all binary values will not be negative. Trust me, you don't want to deal with that mess.

### Problem 2: You Are The Impostor

In the file [**among_us.py**](among_us.py), write a function, **`is_impostor`**, that will accept two parameters. The first,
`information`, will be a dictionary of the following format:

```python
dictionary_example = {
    "Band Name": "Example Band Name",
    "Members": {
        "Guitarist": "Example Name",
        "Bass Player": "Example Name",
        "Drummer": "Example Name",
        "Singer": "Example Name"
    }, 
    "Albums": ["Album Number 1", "Album Number 2"]
}
```

In other words, a dictionary including the information of a music band. You may assume every band has the same number
and type of members.

The second parameter, `corrupter`, will be a function. Yes, you heard that right. In Python, it is entirely possible to 
pass functions as parameters. You don't need to worry about how this works, or about what kind of function `corrupter` 
is.

The function `corrupter` itself accepts one dictionary object and returns either a shallow or a deep copy of the 
original dictionary. Since you don't have access to the contents of `corrupter`, you won't know if a deep or a shallow 
copy has been returned. That's where you come in. You will have to find a way to determine whether the dictionary 
returned by `corrupter` is a deep or a shallow copy.

These are all the hints you are getting, and while it may sound like 
a bit of an abstract problem, think of what it means to be a **deep** copy of something, and what it means to be a 
**shallow** copy of something.

If you determine that `corrupter` has produced a deep copy, return `True`. Otherwise, return `False`.

Here's what your `main` might look like:

```python
from super_secret_module import corrupter

def main():
    the_1975 = {
        "Band Name": "The 1975",
        "Members": {
            "Guitarist": "Adam Hann",
            "Bass Player": "Ross MacDonald",
            "Drummer": "George Daniel",
            "Singer": "Matty Healy"
        },
        "Albums": ["The 1975", "I like it when you sleep for you are so beautiful yet so unaware of it",
                   "A Brief Inquire Into Online Relationships", "Notes on a Conditional Form"]
    }

    if is_impostor(the_1975, corrupter):
        print("is_impostor returned a deep copy!")
    else:
        print("is_impostor returned a shallow copy!")
```

Of course, the output would vary on whether `corrupter` returned a deep or shallow copy. If you would like to create a
sample corrupter function for testing purposes, you can always write a function that returns either a deep or shallow 
copy at random.

By the way, if you're wondering how to use functions passed into other functions, here's a quick example:

```python
# Some mathematical operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Our calculator function doesn't care what function "operation" is. It just passes "a" and "b" into it.
def calculator(a, b, operation):
    return operation(a, b)

def main():
    product = calculator(4, 5, multiply)  # Notice that I didn't include () in multiply.
    print(product)

main()
```
Output:
```text
20
```

### Problem 3: Et tu, programmator?

In the file [**caesar_cipher.py**](caesar_cipher.py), write a function called **`decode_caesar`** that will 
accept `encoded_message`, a string containing a message encoded using a 
[**Caesar cipher**](https://en.wikipedia.org/wiki/Caesar_cipher), and `key`, which is the shift that will be used to 
decode the message.

The Caesar cipher works as follows. Let's say we have the following snippet of the lyrics to Electric Light Orchestra's
1985 hit, [**"Calling America"**](https://www.youtube.com/watch?v=xNUbBpZ9Ac0):
```text
Talk is cheap on satellite
But all I get is static information
I'm still here
Re-dial on automatic
```
If we wanted to encode this using the Caeser cipher, with a key of (for example) 3. We would shift each letter's 
alphabetical index by 3 steps (i.e. `"a"` has an alphabetical index of 1, so if we shift it by 3, we'd get 4, or `"d"`,
"b" has an alphabetical index of 2, etc.). These are the lyrics encoded:

```text
Wdon lv fkhds rq vdwhoolwh
Exw doo L jhw lv vwdwlf lqirupdwlrq
L'p vwloo khuh uh-gldo rq dxwrpdwlf
```

Your job is to **decode** encrypted messages like this, and return the decoded, original message.

Here's some sample behavior I've included using a [**file**](calling_america_lyrics.txt) containing the full set of 
lyrics of Calling America, encrypted with a key of 3:

```python
def main():
    decryption_key = 3

    try:
        file = open("calling_america_lyrics.txt", 'r')
    except FileNotFoundError:
        print("ERROR: File not found!")
    else:
        for line in file:
            line = line.strip()
            decryption = decode_caesar(line, decryption_key)
            print(decryption)

        file.close()

main()
```
Output:
```text
Somebody told her that there was a place like heaven
Across the water on a seven-forty-seven
Yeah, we're living in
In a modern world
And pretty soon she's really got the notion
Of flying out across the big blue ocean
Yeah, we're living in
In a modern world
Talk is cheap on satellite
But all I get is static information
I'm still here re-dial on automatic
Calling America (can't get a message through)
Calling America (that's what she said to do)
Calling America (that's where she has to be)
Calling America (she left a number for me)
Calling America
But I'm just talking to a satellite
Twenty thousand miles up in the sky each night
Yeah, we're living in
In a modern world
All I had to do was pick up the phone
I'm out in space, trying to talk to someone
Yeah, we're living in
In a modern world (in a modern world)
She left a number I could call
But no one's there, no one at all
There must be something going wrong
That number just rings on and on
Calling America (can't get a message through)
Calling America (that's what she said to do)
Calling America (that's where she has to be)
Calling America (she left a number for me)
Calling America
Said she'd call when she'd been gone a while
Guess she's missing me across the miles
Yeah, we're living in
In a modern world
Calling America (can't get a message through)
Calling America (that's what she said to do)
Calling America (that's where she has to be)
Calling America (she left a number for me)
```

My recommendation is to define a separate function that decrypts a single letter. Then, you can create a new, decoded
string letter by letter.

Note the following:

- Your program should be case-sensitive. That is, if our decoding key is 3, `"A"` shifts to `"D"` and `"a"` shifts to
`"d"`.
- You may assume that you will always know the value of the decryption key.
- Your program should only shift characters that belong to the English dictionary. As such, you may assume the encoded
message will be in English. (Caesar would have likely disapproved of this)
- Naturally, any modules that decode the Caesar cipher (of which I am sure there is at least one), are forbidden in this
problem. Everything must be done manually, letter by letter, by you.

**HINT**: The usefulness of `ord` and `chr` is likely obvious, but `%` (the modulus operator) will also come in very 
handy. To understand why, consider the instance of shifting `"x"`, `"y"`, or `"z"` when the decryption key is 3. As 
there is no letter after `"z"`, we must "rotate" back to `"a"`. A look at the Caeser cipher's wiki page (linked above) 
might help make this clear as well.

Have a good weekend and have a safe Thanksgiving break!