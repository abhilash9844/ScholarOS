from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound


def extract_video_id(url: str) -> str:
    """
    Extract YouTube video ID from a URL.
    """

    parsed = urlparse(url)

    # https://www.youtube.com/watch?v=xxxxx
    if parsed.hostname in (
        "www.youtube.com",
        "youtube.com",
    ):
        return parse_qs(parsed.query)["v"][0]

    # https://youtu.be/xxxxx
    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")

    raise ValueError("Invalid YouTube URL")


def get_transcript(url: str) -> str:
    """
    Download the best available transcript.

    Priority:
    1. English
    2. First available transcript
    """

    video_id = extract_video_id(url)

    api = YouTubeTranscriptApi()

    transcript_list = api.list(video_id)

    try:
        # Prefer English
        transcript = transcript_list.find_transcript(["en"])

    except NoTranscriptFound:
        # Otherwise use the first available transcript
        transcript = next(iter(transcript_list))

    result = transcript.fetch()

    return " ".join(
        snippet.text
        for snippet in result
    )