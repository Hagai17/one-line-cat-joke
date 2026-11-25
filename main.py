"""The One-Line Cat Joke That Lands — make.fun entry.

The winning line was picked from 12 drafts in candidates.md, duel-scored
against the kit's published judge brief (stand-up comic persona): setup and
turn that lands, laugh on first read, fresh angle with no stock pun, no
padding, retellable the same day. The high-five line won because its punch
is an event, not an analogy: the trained trick is weaponized against the
trainer, and the final clause reveals the cat anticipated the human's
regret — a second laugh stacked on the first.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
"""

ENTRY = (
    "I taught my cat to high-five, and now she uses it exclusively to slap "
    "treats out of my hand before I can change my mind."
)


def check_gate(text):
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    return text


def write_entry(text, path="/output/entry.txt"):
    """Write the entry text (no trailing newline) to the harness output."""
    import os

    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    entry = check_gate(ENTRY)
    print(entry)
    try:
        write_entry(entry)
    except OSError:
        pass


if __name__ == "__main__":
    main()
