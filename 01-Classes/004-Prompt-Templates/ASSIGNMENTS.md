# Assignments

## Task 1

Create a PromptTemplate for explaining programming languages.

Example

Explain {language} like a beginner.

---

## Task 2

Create a PromptTemplate for writing professional emails.

Use variables:

- name
- company

---

## Task 3

Create a PromptTemplate with two variables.

Example

Explain {topic} in {style}.

---

## Task 4

Generate prompts using different values.

Examples:

- Python
- Java
- FastAPI
- LangChain

Observe the generated prompts.

---

## Task 5

Explain the complete flow:

PromptTemplate

↓

format()

↓

String

↓

invoke()

↓

AIMessage

↓

content

in your own words.

---

## Bonus Challenge

Without looking at the notes, explain:

Why does `format()` return a string instead of an AIMessage?