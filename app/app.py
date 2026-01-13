
def regulatory_assistant(user_query, application_form):

    if not user_query.strip():
        return "Error: No loan scenario or regulatory question provided."

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "system",
            "content": f"""
FDIC RISK MANAGEMENT MANUAL OF EXAMINATION POLICIES
SECTION 3.2 (LOANS) – EXPANDED KNOWLEDGE BASE

{FDIC_SECTION_3_2}
"""
        }
    ]

    if application_form.strip():
        messages.append({
            "role": "system",
            "content": f"""
LOAN APPLICATION / CREDIT FILE TEXT
{application_form}
"""
        })

    messages.append({
        "role": "user",
        "content": user_query
    })

    # Call the model without forcing JSON output
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages,
        temperature=0
    )

    # Return plain text output
    return response.choices[0].message.content



# ===============================
# GRADIO USER INTERFACE
# ===============================
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 🏦 FDIC Regulatory Loan Examination Assistant  
    **Policy-Grounded | Non-Advisory | Examiner-Oriented**

    This tool evaluates loan-related inputs strictly under  
    **FDIC RMS Manual – Section 3.2 (Loans)**.
    """)

    with gr.Row():

        # INPUT PANEL
        with gr.Column(scale=1):
            gr.Markdown("### 📄 Loan Scenario Input")

            user_query = gr.Textbox(
                label="Loan Scenario / Regulatory Question",
                placeholder="Describe the loan scenario to be evaluated under Section 3.2...",
                lines=8
            )

            application_form = gr.Textbox(
                label="Optional Loan Application / Credit File Excerpt",
                placeholder="Paste loan application or supporting text (optional)...",
                lines=6
            )

            analyze_btn = gr.Button(
                "Run Regulatory Analysis",
                variant="primary"
            )

        # OUTPUT PANEL
        with gr.Column(scale=1):
            gr.Markdown("### 📊 Structured Examiner Output")

            output = gr.Code(
                label="Regulatory Output (JSON)",
                language="json"
            )

    analyze_btn.click(
        fn=regulatory_assistant,
        inputs=[user_query, application_form],
        outputs=output
    )

    gr.Markdown("""
    ---
    ⚖️ **Regulatory Notice**  
    This system does **not** approve, reject, or recommend loan actions.  
    Outputs reflect **policy-aligned observations only**, consistent with examiner standards.
    """)

demo.launch(debug=True)