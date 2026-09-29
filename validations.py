# validations.py
# Input cleaning and validation for NexoTech Solutions tickets (rule BR0).
#
# AI disclosure (PUCPR Resolution 274/2024): During the preparation of this code,
# the author(s) used Claude (Anthropic, model claude-opus-5) to draft the cleaning
# and validation functions from the team's business rule BR0. After using this
# tool, the author(s) reviewed and edited the content as needed and take full
# responsibility for the content.


def clean_text(value):
    """Return the value in lowercase, without surrounding spaces (BR0).

    A missing value (None) becomes empty text, so the business rules
    never receive None and can always compare text with text.
    """
    if value is None:
        return ""
    # str() protects against a number typed into a text field
    return str(value).strip().lower()


def is_missing(value):
    """Return True when a field has no usable content (None, empty or only spaces)."""
    return clean_text(value) == ""
