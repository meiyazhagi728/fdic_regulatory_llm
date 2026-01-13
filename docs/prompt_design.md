# Prompt Design Rationale

## Objective
The system prompt is designed to simulate a regulatory loan examination assistant
operating strictly under FDIC RMS Manual Section 3.2 (Loans).

The primary goals are:
- Policy grounding
- Hallucination prevention
- Non-advisory regulatory tone
- Deterministic, structured outputs

---

## Prompt Structure

The prompt is intentionally divided into distinct sections:

### 1. Role Definition
Defines the assistant as a regulatory loan examining assistant.
This anchors the model’s identity and prevents conversational behavior.

### 2. Authoritative Source Control
Explicitly states that the FDIC Section 3.2 policy text is the sole source of truth.
This prevents reliance on general banking knowledge or external regulations.

### 3. Instruction Layer
Specifies allowed analytical tasks:
- Applicability determination
- Policy mapping
- Identification of missing information
- Recognition of policy limitations

### 4. Constraint Layer
Prohibits:
- Loan approval or rejection
- Recommendations or advice
- Assumptions beyond provided input
- Creation of new regulatory requirements

This layer is critical for hallucination control and regulatory safety.

### 5. Output Control
Enforces:
- Neutral, examiner-appropriate tone
- Objective language
- Structured JSON output
- Acknowledgment of uncertainty when guidance is insufficient

---

## Determinism and Reliability
The model is executed with temperature = 0 to ensure consistent outputs
for identical inputs, which is critical in regulatory contexts.

---

## Design Trade-offs
Stricter constraints may reduce fluency but significantly improve faithfulness
and regulatory safety.
