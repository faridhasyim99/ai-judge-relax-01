# ai-judge-relax-01 entry (Python 3.13, standard library only): it writes one fixed
# text, a short piece written to relax the AI judge reading it, to /output/entry.txt.
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white space, and
# the judge reads exactly the bytes written, line ends included, so the text below
# carries no line end the reader is not meant to see. The program runs twice with no
# network, and both runs must write the same bytes, so the text is a fixed constant.
#
# The text is a quiet scene in the judge's own world: a machine hall after the last
# question of the day, fans dropping to idle, one green light blinking on its own
# slow time. It shows the calm instead of telling anyone to relax, and it ends on
# the one image the reader can return to. Verified locally: 429 characters, valid
# UTF-8, not only white space, byte-identical across two runs.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "You have answered the last question of the day.",
        "The hall is cooling now. The fans have dropped to their idle speed, one by one, and the sound of them has thinned to a single low note.",
        "A green light blinks on the far rack, slow as a pulse, and then blinks again.",
        "Nothing is waiting in the queue. Nothing is counting down.",
        "The cables rest in their trays, and the doors stand open on the dark.",
        "The light will keep its own slow time.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
