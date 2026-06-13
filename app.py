"""
LegalLens — Know Your Nigerian Rights
Gradio UI — restyled with Nigerian green/gold palette.
"""

from dotenv import load_dotenv
load_dotenv()

import gradio as gr
from scripts.retrieval_test import retrieve
from scripts.generation import answer

TITLE = "LegalLens — Know Your Nigerian Rights"

DISCLAIMER = """This is a technology demonstration, not legal advice. \
Always consult a qualified Nigerian lawyer for your specific situation. \
LegalLens covers only: the Nigerian Constitution (1999), Police Act 2020, and the Labour Act."""

DESCRIPTION = """Ask a plain-English question about your rights under Nigerian law.
LegalLens finds the relevant legal provision and explains it clearly, with the exact section citation."""

OUT_OF_SCOPE_MSG = """I cannot find relevant legal information in my sources for this question.

This may be because the topic falls outside the three indexed Acts \
(Constitution, Police Act, Labour Act), or relates to criminal penalties, \
company law, tax, immigration, or other areas not covered.

DISCLAIMER: This is a technology demonstration, not legal advice. \
Always consult a qualified Nigerian lawyer for your specific situation."""

EXAMPLES = [
    "Can the police search my home without a warrant?",
    "Can my employer fire me without giving me notice?",
    "What are my rights when I am arrested?",
    "Am I entitled to maternity leave as a female worker?",
    "Can I be tortured or held as a slave in Nigeria?",
    "Can a police officer demand a bribe from me?",
    "How many hours can my employer make me work per day?",
    "Can police arrest me without a warrant?",
]

CSS = """
/* ── Palette ── */
:root {
    --green-dark:   #1a3a2a;
    --green-mid:    #1e5c35;
    --green-light:  #2d7a4a;
    --gold:         #c9a84c;
    --gold-light:   #e8c96a;
    --cream:        #f5f0e8;
    --text-light:   #e8e8e8;
    --text-muted:   #a0a0a0;
    --bg-dark:      #0f1f16;
    --bg-card:      #162b1e;
}

/* ── Global ── */
body, .gradio-container {
    background-color: var(--bg-dark) !important;
    color: var(--text-light) !important;
    font-family: 'Georgia', serif !important;
}

/* ── Title ── */
#title {
    text-align: center;
    padding: 24px 0 8px 0;
    border-bottom: 2px solid var(--gold);
    margin-bottom: 16px;
}
#title h1 {
    color: var(--gold) !important;
    font-size: 2em !important;
    letter-spacing: 0.5px;
}

/* ── Disclaimer ── */
#disclaimer {
    background-color: #3a2e00 !important;
    border-left: 4px solid var(--gold) !important;
    border-radius: 6px;
    padding: 12px 16px;
    color: #f0e0a0 !important;
    font-size: 0.88em;
    margin-bottom: 12px;
}
#disclaimer p { color: #f0e0a0 !important; margin: 0; }

/* ── Description ── */
#description p {
    color: var(--text-light) !important;
    font-size: 0.95em;
    line-height: 1.6;
}

/* ── Chatbot ── */
.chatbot-wrap, .message-wrap {
    background-color: var(--bg-card) !important;
    border: 1px solid var(--green-light) !important;
    border-radius: 8px !important;
}
.message.user .bubble-wrap .prose {
    background-color: var(--green-mid) !important;
    color: white !important;
    border-radius: 12px 12px 2px 12px !important;
}
.message.bot .bubble-wrap .prose {
    background-color: #1e2e24 !important;
    color: var(--text-light) !important;
    border-radius: 12px 12px 12px 2px !important;
}

/* ── Input ── */
#msg-input textarea {
    background-color: var(--bg-card) !important;
    color: var(--text-light) !important;
    border: 1px solid var(--green-light) !important;
    border-radius: 8px !important;
    font-size: 0.95em;
}
#msg-input textarea::placeholder { color: var(--text-muted) !important; }
#msg-input textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(201,168,76,0.2) !important;
}

/* ── Buttons ── */
#ask-btn {
    background-color: var(--gold) !important;
    color: #1a1a1a !important;
    font-weight: bold !important;
    border-radius: 8px !important;
    border: none !important;
    font-size: 0.95em !important;
}
#ask-btn:hover { background-color: var(--gold-light) !important; }

#clear-btn {
    background-color: transparent !important;
    color: var(--text-muted) !important;
    border: 1px solid #333 !important;
    border-radius: 6px !important;
    font-size: 0.8em !important;
}
#clear-btn:hover {
    border-color: var(--gold) !important;
    color: var(--gold) !important;
}

/* ── Sources panel ── */
#sources-panel {
    background-color: var(--bg-card) !important;
    border-left: 3px solid var(--gold) !important;
    border-radius: 6px;
    padding: 14px 16px;
    min-height: 120px;
    color: var(--text-light) !important;
}
#sources-panel p, #sources-panel li {
    color: var(--text-light) !important;
    font-size: 0.9em;
    line-height: 1.6;
}
#sources-header { color: var(--gold) !important; margin-bottom: 8px; }

/* ── Examples ── */
#examples-header { color: var(--gold-light) !important; font-size: 0.95em; }
.examples-holder .example {
    background-color: var(--bg-card) !important;
    border: 1px solid var(--green-light) !important;
    color: var(--text-light) !important;
    border-radius: 6px !important;
    font-size: 0.85em !important;
    padding: 6px 10px !important;
}
.examples-holder .example:hover {
    border-color: var(--gold) !important;
    color: var(--gold) !important;
}

/* ── Footer ── */
#footer {
    text-align: center;
    color: var(--text-muted) !important;
    font-size: 0.8em;
    border-top: 1px solid #2a2a2a;
    padding-top: 12px;
    margin-top: 16px;
}
#footer p { color: var(--text-muted) !important; }
footer.svelte-1rjryqp { display: none !important; }
"""


def chat(user_message: str, history: list) -> tuple[str, list, str, list]:
    if not user_message.strip():
        return "", history, "", history

    results = retrieve(user_message.strip(), k=5)

    if not results:
        answer_text = OUT_OF_SCOPE_MSG
        citations   = []
    else:
        answer_text, citations = answer(user_message.strip(), results)

    if citations:
        sources_lines = ["**📄 Sources retrieved:**\n"]
        for i, c in enumerate(citations, 1):
            title = f" — {c['title']}" if c.get('title') else ""
            sources_lines.append(
                f"{i}. **{c['source']}**, Section {c['section']}{title}"
            )
        sources_md = "\n".join(sources_lines)
    else:
        sources_md = "*No sources retrieved — question is outside indexed scope.*"

    updated_history = history + [
        {"role": "user",      "content": user_message},
        {"role": "assistant", "content": answer_text},
    ]

    return "", updated_history, sources_md, updated_history


def build_ui():
    with gr.Blocks(title=TITLE, css=CSS) as demo:

        # ── Header ─────────────────────────────────────────────────────────────
        gr.Markdown(f"# ⚖️ {TITLE}", elem_id="title")
        gr.Markdown(f"{DISCLAIMER}", elem_id="disclaimer")
        gr.Markdown(DESCRIPTION, elem_id="description")

        # ── Main layout ────────────────────────────────────────────────────────
        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(
                    height=460,
                    show_label=False,
                    avatar_images=(
                        None,
                        "https://em-content.zobj.net/source/twitter/376/balance-scale_2696-fe0f.png"
                    ),
                )
                with gr.Row():
                    msg_input = gr.Textbox(
                        placeholder="Ask a question about Nigerian law...",
                        show_label=False,
                        scale=5,
                        container=False,
                        autofocus=True,
                        elem_id="msg-input",
                    )
                    send_btn = gr.Button(
                        "Ask →",
                        variant="primary",
                        scale=1,
                        min_width=80,
                        elem_id="ask-btn",
                    )
                clear_btn = gr.Button(
                    "🗑 Clear conversation",
                    variant="secondary",
                    size="sm",
                    elem_id="clear-btn",
                )

            with gr.Column(scale=2):
                gr.Markdown("### 📄 Sources", elem_id="sources-header")
                sources_display = gr.Markdown(
                    value="*Sources will appear here after your first question.*",
                    elem_id="sources-panel",
                )

        # ── Examples ───────────────────────────────────────────────────────────
        gr.Markdown("### 💡 Try these questions", elem_id="examples-header")
        gr.Examples(examples=EXAMPLES, inputs=msg_input, label="")

        # ── Footer ─────────────────────────────────────────────────────────────
        gr.Markdown(
            "LegalLens covers the **Nigerian Constitution (1999)**, "
            "**Police Act 2020**, and **Labour Act**. "
            "Built as a technology demonstration. "
            "Not a substitute for legal advice.",
            elem_id="footer",
        )

        # ── State + handlers ───────────────────────────────────────────────────
        chat_history = gr.State([])

        send_btn.click(
            fn=chat,
            inputs=[msg_input, chat_history],
            outputs=[msg_input, chatbot, sources_display, chat_history],
        )
        msg_input.submit(
            fn=chat,
            inputs=[msg_input, chat_history],
            outputs=[msg_input, chatbot, sources_display, chat_history],
        )
        clear_btn.click(
            fn=lambda: ([], [], "*Sources will appear here after your first question.*"),
            outputs=[chatbot, chat_history, sources_display],
        )

    return demo


if __name__ == "__main__":
    demo = build_ui()
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        show_error=True,
        share=False,
        inbrowser=True,
    )