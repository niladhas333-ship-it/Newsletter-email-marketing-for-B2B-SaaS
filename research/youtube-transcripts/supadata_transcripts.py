import requests
import os

API_KEY = "sd_7576c9bde6e673a5c4de8000acf875a7"  # உன் API key இங்கே போடு

videos = {
    "brennan-dunn": ["ABC123xyz", "DEF456uvw"],
    "nathan-barry": ["GHI789rst", "JKL012mno"],
    "wes-bush": ["MNO345pqr", "STU678lmn"],
    "dave-gerhardt": ["VWX901ijk"]
}

for author, ids in videos.items():
    folder = f"research/youtube-transcripts/{author}"
    os.makedirs(folder, exist_ok=True)

    for vid_id in ids:
        try:
            response = requests.get(
                "https://api.supadata.ai/v1/youtube/transcript",
                params={"videoId": vid_id},
                headers={"x-api-key": API_KEY}
            )

            data = response.json()
            text = " ".join([t['text'] for t in data['transcript']])

            with open(f"{folder}/{vid_id}.md", "w") as f:
                f.write(f"# Transcript: {vid_id}\n")
                f.write(f"Source: https://youtube.com/watch?v={vid_id}\n\n")
                f.write(text)

            print(f"✓ Done: {author} - {vid_id}")

        except Exception as e:
            print(f"✗ Failed: {author} - {vid_id}: {e}")

print("\nAll done!")