# Class Notes

## PromptTemplate

PromptTemplate is a reusable prompt blueprint.

Instead of writing the same prompt multiple times, we write one template and replace only the changing values.

---

## Example

Template

Explain {topic} like a beginner.

Variables

topic

Final Prompt

Explain Python like a beginner.

---

## input_variables

`input_variables` tells LangChain which variables are required before generating the final prompt.

Example

["topic"]

or

["language", "style"]

---

## format()

The `format()` method replaces placeholders with actual values.

Example

Template

Explain {topic}

↓

topic = Python

↓

Explain Python

---

## Return Types

PromptTemplate(...)
↓

PromptTemplate Object

---

template.format(...)
↓

String

---

llm.invoke(...)
↓

AIMessage Object

---

response.content
↓

String

---

## Important Concepts

- PromptTemplate does not modify the original template.
- It creates and returns a new formatted string.
- The original template remains reusable.

---

## Complete Flow

PromptTemplate Object

↓

format()

↓

Prompt String

↓

invoke()

↓

AIMessage

↓

content