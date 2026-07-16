from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str) -> str:
    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    return parse_qs(parsed.query)["v"][0]


def get_transcript(url: str) -> str:
    video_id = extract_video_id(url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(
    video_id,
    languages=["hi"]
)

    return " ".join(snippet.text for snippet in transcript)