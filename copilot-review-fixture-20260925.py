"""Disposable review-timing fixture with no external inputs."""


def allowed(subject: str) -> bool:
    """Allow only the named fixture identity."""
    return subject == "fixture-owner"
