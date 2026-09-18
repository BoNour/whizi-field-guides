"""Whizi field guides, readable offline. Source: https://whizi.io/resources/"""
from importlib.resources import files
import sys

GUIDES = {
    "multiple-ai-models": "How to use multiple AI models together",
    "ai-subscription-costs": "What your AI subscriptions really cost",
}


def read(slug: str) -> str:
    return files("whizi_field_guides").joinpath("guides", f"{slug}.md").read_text(encoding="utf-8")


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] not in GUIDES:
        print("Whizi field guides. Usage: whizi-field-guides <guide>\n")
        for slug, title in GUIDES.items():
            print(f"  {slug:24} {title}")
        print("\nFull guides: https://whizi.io/resources/")
        return
    print(read(args[0]))
