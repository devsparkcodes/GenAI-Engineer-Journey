# Class 03 - SystemMessage & HumanMessage

## Objective

In this class, we learned how Large Language Models (LLMs) receive structured conversations using LangChain Message Objects instead of plain text prompts.

We also explored the difference between `SystemMessage` and `HumanMessage`, how they influence model behavior, and why structured messages are preferred in real-world AI applications.

---

## Topics Covered

- What is a Message Object?
- SystemMessage
- HumanMessage
- AIMessage
- Creating Message Objects
- Passing a list of messages to `invoke()`
- Difference between `invoke("...")` and `invoke([...])`
- Prompt hierarchy
- System instructions vs User instructions
- Prompt Injection (Introduction)
- Why Prompt Engineering requires testing

---

## Files

- `practice.py` → Main practice code
- `NOTES.md` → Class notes
- `ASSIGNMENTS.md` → Practice questions
- `requirements.txt` → Required Python packages

---

## Learning Outcome

After completing this class, I can:

- Create `SystemMessage` objects.
- Create `HumanMessage` objects.
- Send multiple messages to an LLM.
- Understand how LangChain structures conversations.
- Explain the priority of different message types.
- Understand that prompt engineering is based on experimentation, not assumptions.

---

## Status

✅ Completed