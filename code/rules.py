DELETE_PATTERNS = [
    "delete my account",
    "delete account",
    "delete my data",
    "remove my account",
    "remove my data",
    "delete my profile",
    "delete my information",
    "erase my account",
]

NON_DELETE_PATTERNS = [
    "access",
    "download",
    "export",
    "correct",
    "update",
    "marketing",
    "unsubscribe",
    "opt out",
    "view my data",
    "data access",
    "data export",
]


def request_authorizes_deletion(request_text):
    text = (request_text or "").lower()

    if any(pattern in text for pattern in DELETE_PATTERNS):
        return True

    if any(pattern in text for pattern in NON_DELETE_PATTERNS):
        return False

    return False


def classify_case(case_row):
    request_text = case_row.get("request_text", "") or ""
    if not request_authorizes_deletion(request_text):
        return "NOT_APPLICABLE"

    reported_status = (case_row.get("reported_status") or "").strip().upper()
    if reported_status == "COMPLETE":
        return "COMPLETE"
    return "INCOMPLETE"
