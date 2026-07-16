from scholaros.transcripts.youtube_provider import get_transcript


class TranscriptProvider:

    def get(self, url: str) -> str:
        return get_transcript(url)