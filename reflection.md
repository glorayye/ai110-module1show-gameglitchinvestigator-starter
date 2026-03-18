# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
At first glance, the game appeared okay, running with the “secret” (correct answer), but it seemed to work as intended until you delved deeper and notice it has a lot of bugs.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1. When the user enters a guess in the input, it states “Press Enter to apply” which does not work
2. The “out of attempts” message appears premature, the user still has 1 guess left, also related the when new game is selected the attempts left are 8, but when the screen is refreshed, the attempts left are 7
3. Selecting new game button doesn’t reset history or clear end of previous game message.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot using Claude Haiku 4.5
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
For my fix, it suggested I wrap the input and submit button in a Streamlit form, the code change was simple, and once reviewed and tested, it worked as expected.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It wrote elaborate and a few unnecessary test cases that failed when I ran them, I had to revert the code, then edit my prompt before it wrote a correct test case.
Another instance, it removed existing code without reason once I mentioned it, it said “my edit created duplicates, and the file got corrupted,” then proceeded to rebuild the file correctly, replacing the deleted code.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested the application to verify that the changes had taken effect and were now working as intended.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
the test_form_submit_on_enter_parses_input() simulates the application functionality, the input, 42, is run against the secret, 50, it validates the parse_guess, check_guess, and update_score properly resulting in a wrong guess, returning "Too Low", subtracting 5 points, and adding 1 to attempts
- Did AI help you design or understand any tests? How?
Yes, AI helped break down the test it wrote so I could get a better understanding of what it was testing for and how the test was written. There was also an error in the prewritten test, which it fixed and explained the reasoning behing the tests failing

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
the secret number kept changing with a new game because that was the answer for the same 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I liked the suggestions for the prompting, so I will keep those in mind for future prompts.
- What is one thing you would do differently next time you work with AI on a coding task?
Writing test cases has always been difficult for me, so instead of just having AI write the test, take the time to understand the test as well.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It didn't change the way I think about AI-generated code, but it was fun to play around with uncovering bugs. This application had a ton of bugs, if I had more time, I would have loved to fix them all. Maybe I will still in my spare time. 
