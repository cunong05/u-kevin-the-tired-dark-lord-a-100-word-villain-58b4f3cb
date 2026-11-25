#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue (about 100 words) to /output/entry.txt.
The speaker is a fantasy villain who is secretly just very tired:
the tiredness lives in the rhythm, the pauses and the small
deflections, never in a plain statement of weariness.
"""

import os

MONOLOGUE = (
    "Come in. Shut the door. Sit \u2014 no, not there. "
    "That chair holds my maps, my lists, the names of lords "
    "who owe me coin since the marsh war, thirty years gone. "
    "The bells ring at noon since I said so. "
    "If they stop, the mills stop. If the mills stop, the bread stops. "
    "Then they all look at me. "
    "The plan is plain. At the feast, the salt. In the salt, the draught. "
    "One cup for my brother the king, and the crown comes home. To me. At last. "
    "...Where was I? Ah. The salt. Yes. "
    "Mind the step."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
    print(MONOLOGUE)


if __name__ == "__main__":
    main()
