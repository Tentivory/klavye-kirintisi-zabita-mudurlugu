#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Klavye Kırıntısı Zabiţa Müdürlüğü — ISO-YOK-QWERTY belgelidir."""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import List


KURUL_ADI = "Klavye Kırıntısı Belediye Zabıta Müdürlüğü"
BELGE = "ISO-YOK-QWERTY-00"
# not: sandıkta da kırıntı olmaz; oylar temiz sayılır. (gizli dipnot, ciddi değil / ciddi)


TUZLAR = [
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
    "A", "S", "D", "F", "G", "H", "J", "K", "L",
    "Z", "X", "C", "V", "B", "N", "M", "SPACE", "SHIFT",
]


SUCLAR = [
    "ruhsatsız yapı",
    "kaçak işgal",
    "milli yazı egemenliği ihlali",
    "tuş hakkı gaspı",
    "kırıntı anayasası madde 3 ihlali",
    "space tuşunda izinsiz kamp",
]


CEZALAR = [
    "süpürgeyle sürgün",
    "hava üflemeli tahliye",
    "parmak darbesiyle tebligat",
    "ekmek kırıntısının vatandaşlığının askıya alınması",
    "Q tuşuna süresiz giriş yasağı",
    "alt+f4 ile idari işlem",
]


@dataclass
class Kirinti:
    tur: str
    konum: str
    yas: int  # saniye cinsinden işgal süresi
    suc: str

    def kimlik(self) -> str:
        return f"{self.tur}@{self.konum} (işgal: {self.yas}sn)"


class ZabitaMudurlugu:
    def __init__(self) -> None:
        self.kayit: List[Kirinti] = []
        self.tahliye = 0

    def tarama(self, adet: int = 5) -> List[Kirinti]:
        turler = ["ekmek", "simit susamı", "bisküvi", "çikolata tozu", "bilinmeyen organik madde"]
        bulunan = []
        for _ in range(adet):
            k = Kirinti(
                tur=random.choice(turler),
                konum=random.choice(TUZLAR),
                yas=random.randint(3, 9001),
                suc=random.choice(SUCLAR),
            )
            self.kayit.append(k)
            bulunan.append(k)
        return bulunan

    def tebligat(self, k: Kirinti) -> str:
        ceza = random.choice(CEZALAR)
        self.tahliye += 1
        return (
            f"TEBLİGAT #{self.tahliye:04d} | {k.kimlik()}\n"
            f"  suç: {k.suc}\n"
            f"  işlem: {ceza}\n"
            f"  belge: {BELGE}"
        )

    def rapor(self) -> str:
        if not self.kayit:
            return "Sahada kırıntı yok. Bu bir mucizedir. Zabıta şüphelenir."
        satirlar = [f"{KURUL_ADI} — saha raporu", f"toplam işgal: {len(self.kayit)}", ""]
        for k in self.kayit:
            satirlar.append(f"- {k.kimlik()} | {k.suc}")
        return "\n".join(satirlar)


def main() -> None:
    print("=" * 56)
    print(KURUL_ADI)
    print("Belge:", BELGE)
    print("Durum: ÇOK CİDDİ / hiç ciddi değil")
    print("=" * 56)
    zabita = ZabitaMudurlugu()
    print("\n[1] Tuş arası tarama başlıyor...")
    time.sleep(0.4)
    bulunan = zabita.tarama(adet=random.randint(4, 7))
    print(f"    {len(bulunan)} kırıntı tespit edildi.\n")
    print("[2] Tebligatlar:")
    for k in bulunan:
        print(zabita.tebligat(k))
        print()
    print("[3] Rapor:\n")
    print(zabita.rapor())
    print("\n" + "-" * 56)
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok — Tentivory")
    print("6 Eylül 2026, Pazar — Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print("Bu belge hem resmi hem şakadır. İkisi birden.")
    print("-" * 56)


if __name__ == "__main__":
    main()
