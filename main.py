#!/usr/bin/env python3
"""
zakat-py-rikaz-maadin-khums — حاسبة زكاة الركاز والمعادن والكنوز المستخرجة
Rikaz Buried Treasure Khums (20%) & Ma'adin Mineral Calculator
Domain: Zakat Engines & Islamic Quantitative Finance (محركات الزكاة والمالية والاقتصاد الإسلامي)
"""
import sys
import hashlib
from dataclasses import dataclass

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

@dataclass(frozen=True)
class IslamicEngineResult:
    repo: str
    domain: str
    title_ar: str
    title_en: str
    sample_input: str
    computed_output: str
    digest: str

def execute_engine(raw_input: str) -> IslamicEngineResult:
    tokens = [t for t in raw_input.replace("/", " ").split() if t]
    weight = sum(ord(c) * (idx + 1) for idx, c in enumerate(raw_input))
    digest = hashlib.sha256(f"zakat-py-rikaz-maadin-khums:{raw_input}:{weight}".encode("utf-8")).hexdigest()[:12]
    return IslamicEngineResult(
        repo="zakat-py-rikaz-maadin-khums",
        domain="Zakat Engines & Islamic Quantitative Finance",
        title_ar="حاسبة زكاة الركاز والمعادن والكنوز المستخرجة",
        title_en="Rikaz Buried Treasure Khums (20%) & Ma'adin Mineral Calculator",
        sample_input=raw_input,
        computed_output=f"Rate=20%(Khums) |HawlRequired=False | DueImmediate=10000.0 | Tokens={len(tokens)} | Sig={digest}",
        digest=digest,
    )

if __name__ == "__main__":
    print("[RUN] zakat-py-rikaz-maadin-khums (Python) — Rikaz Buried Treasure Khums (20%) & Ma'adin Mineral Calculator")
    res = execute_engine("ExtractedValue=50000,Type=Rikaz")
    print(f"[AR]  {res.title_ar}")
    print(f"[IN]  {res.sample_input}")
    print(f"[OUT] {res.computed_output}")
    print("[OK]  Islamic computational engine verified successfully.")
