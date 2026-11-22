#!/usr/bin/env python3
"""Refresh this repository from the development folders of the Multi-Speeder project.

Run from anywhere:  python3 tools/update_release.py [--manuals DIR] [--manuals-en DIR] [--check]

Copies the DolphinDos26 ROMs for the C128DCR, the SpeedDos26 ROMs (drive ROM for the 1571 in
the C128DCR, C128 kernals with US and German keyboard, C64 kernals), the two EPROM templates
(drive U3 and kernal switcher U32, German and US version), the MS-Tools disk and the manuals
(German and English, as PDF) into this repository, writes CHECKSUMS.md5 and
CHECKSUMS.sha256 over everything published, and reports what is out of date:

- an English manual is missing or older than the German one;
- a manual does not state the MD5 of a ROM or EPROM template published here;
- a file in rom/ is not one of the allowed DolphinDos26 or SpeedDos26 files;
- banks 5 and 6 of the templates do not hold SpeedDos26 as released: the drive template
  C1571CRSpeedDOS26.bin in both banks, the kernal images C128SpeedDos26-EN.bin (bank 5, US
  keyboard) and C128SpeedDos26-DE.bin (bank 6, German keyboard), each with C64SpeedDos26.bin
  as the C64 kernal. Drive and kernal images are always released together.

Only the DolphinDos26 ROMs, the SpeedDos26 ROMs and the EPROM templates with Commodore ROMs,
DolphinDOS 3 (bank 3), DolphinDos26 (bank 4) and SpeedDos26 (banks 5 and 6) may be published.
The DolphinDos26 and SpeedDos26 kernals contain JiffyDOS transfer routines (see README.md and
LICENSE.md); that is allowed, in the single kernal files and in banks 4, 5 and 6 of the kernal
images. All other banks and every drive ROM must stay free of JiffyDOS. ROM images with original
JiffyDOS drive firmware or original JiffyDOS kernals (C64, C128, 1541, 1571) and other complete
EPROM images must never be added to this repository.

The hardware files (hardware/) are maintained here directly and are only checksummed.
The script exits with status 1 if anything is out of date. --check changes nothing.
"""
import argparse
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent


def find_root():
    """The project folder holding Builds/ – this repository sits in <root>/Git/<repo>."""
    for p in REPO.parents:
        if (p / 'Builds').is_dir():
            return p
    return REPO.parent.parent


ROOT = find_root()
ROMS = ['C1571_DOLPHINDOS26.bin', 'C128DolphinDos26-US.BIN', 'C128DolphinDos26-DE.BIN', 'C64IIDolphinDos26.bin']
# SpeedDos26 from Builds (SpeedDos26 project): drive ROM for the 1571 in the C128DCR (32 KB, based
# on Commodore DOS 318047-01, no JiffyDOS code) and the kernals the kernal images are built from
SD26_DRIVE = 'C1571CRSpeedDOS26.bin'
SD26_K128 = {4: 'C128SpeedDos26-EN.bin', 5: 'C128SpeedDos26-DE.bin'}    # bank index -> C128 kernal
SD26_K64 = 'C64SpeedDos26.bin'          # C64 kernal at $xA000 of banks 5 and 6
SD26_K64II = 'C64IISpeedDos26.bin'      # C64 BASIC + the same kernal (16 KB, $x8000-$xBFFF)
SD26_ROMS = [SD26_DRIVE, SD26_K128[4], SD26_K128[5], SD26_K64, SD26_K64II]
# EPROM template (U3) from Builds (SpeedDos26/1571 make eprom, tools/eprom_c128dcr.py): Commodore DOS
# 318047-01 in banks 1, 2, 7 and 8, DolphinDOS 3 in bank 3, DolphinDos26 in bank 4, SpeedDos26
# (C1571CRSpeedDOS26.bin, upper half) in banks 5 and 6. Must be free of JiffyDOS in every bank.
TEMPLATES = ['C1571_C128DCR_29F040.BIN']
# Kernal switcher (U32) images from Builds (same build step): German and international/US version.
# Both hold in bank 4 the DolphinDos26 kernals, in bank 5 C128SpeedDos26-EN.bin (US keyboard) and in
# bank 6 C128SpeedDos26-DE.bin (German keyboard), each with C64SpeedDos26.bin at $xA000 for C64 mode.
# These kernals contain JiffyDOS transfer routines (allowed); all other banks must be free of
# JiffyDOS. C128DD26/tools/u32_image.py builds the images WITHOUT SpeedDos26 - not for this release.
KERNAL_IMAGES = ['C128DCR_KERNAL_29F040-DE.BIN', 'C128DCR_KERNAL_29F040-US.BIN']
JIFFY_BANKS = (3, 4, 5)                 # bank index: banks 4, 5 and 6 of the kernal images
# DolphinDos26 kernals in bank 4 of the kernal images
DD26_K64II = 'C64IIDolphinDos26.bin'
DD26_K128 = {'C128DCR_KERNAL_29F040-DE.BIN': 'C128DolphinDos26-DE.BIN',
             'C128DCR_KERNAL_29F040-US.BIN': 'C128DolphinDos26-US.BIN'}
BANK = 65536
MANUALS = {'MultiSpeederC128DCR-1571_Handbuch.pdf': 'MultiSpeederC128DCR-1571_Manual.pdf'}
CHECKSUMMED = ('rom', 'ms-tools', 'manuals', 'hardware', 'rom-builder')
# Browser tool MS-ROM-Builder (one tool for 1541, external 1571 and C128DCR) from its development
# folder MS-ROM-Builder-C128DCR; it contains no ROM data
ROM_BUILDER = ('MS-ROM-Builder-C128DCR/index.html', 'rom-builder/MS-ROM-Builder.html')


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def copy(src, dst, check, problems):
    src, dst = pathlib.Path(src), pathlib.Path(dst)
    if not src.exists():
        problems.append('missing source: %s' % src)
        return
    if check:
        if not dst.exists() or sha(src) != sha(dst):
            problems.append('out of date: %s' % dst.relative_to(REPO))
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=str(ROOT), help='project folder with Builds and MS-Tools')
    ap.add_argument('--manuals', help='folder with the German PDF (default: Builds)')
    ap.add_argument('--manuals-en', help='folder with the English PDF (default: dd26/doc/handbuch/build)')
    ap.add_argument('--check', action='store_true', help='report only, change nothing')
    a = ap.parse_args()
    root = pathlib.Path(a.root).resolve()
    builds = root / 'Builds'
    man_de = pathlib.Path(a.manuals) if a.manuals else builds
    man_en = pathlib.Path(a.manuals_en) if a.manuals_en else root / 'dd26' / 'doc' / 'handbuch' / 'build'
    bad = []

    published = ROMS + SD26_ROMS + TEMPLATES + KERNAL_IMAGES
    for r in published:
        copy(builds / r, REPO / 'rom' / r, a.check, bad)
    for p in (REPO / 'rom').glob('*'):
        if p.name not in published:
            bad.append('not allowed in rom/: %s (only the DolphinDos26 and SpeedDos26 ROMs may be published)'
                       % p.name)

    def rom(name):
        """Content of a published ROM, or None (already reported as missing source / out of date)."""
        p = REPO / 'rom' / name
        return p.read_bytes() if p.exists() else None

    def same(image, n, off, name, what):
        """Bank n (index) of the image must hold the published file `name` at offset `off`."""
        d = rom(name)
        if d is None or image[1][n * BANK + off:n * BANK + off + len(d)] != d:
            bad.append('%s: bank %d does not hold %s at $x%04X (%s)' % (image[0], n + 1, name, off, what))

    # drive ROMs must never contain JiffyDOS
    for t in TEMPLATES + ['C1571_DOLPHINDOS26.bin', SD26_DRIVE]:
        d = rom(t)
        if d is not None and b'JIFFY' in d.upper():
            bad.append('JiffyDOS found in %s' % t)
    d = rom(SD26_DRIVE)
    if d is not None and len(d) != 32768:
        bad.append('%s is not 32 KB' % SD26_DRIVE)
    k64, k64ii = rom(SD26_K64), rom(SD26_K64II)
    if k64 is not None and k64ii is not None and k64ii[8192:] != k64:
        bad.append('%s does not end with the kernal %s' % (SD26_K64II, SD26_K64))
    # drive template: SpeedDos26 in the upper half of banks 5 and 6, lower half empty
    for t in TEMPLATES:
        b = rom(t)
        if b is None:
            continue
        if len(b) != 8 * BANK:
            bad.append('%s is not 512 KB' % t)
            continue
        for n in SD26_K128:
            same((t, b), n, 0x8000, SD26_DRIVE, 'SpeedDos26 drive ROM')
            if b[n * BANK:n * BANK + 0x8000] != b'\xff' * 0x8000:
                bad.append('%s: lower half of bank %d is not empty ($FF)' % (t, n + 1))
    # kernal images: DolphinDos26 in bank 4, SpeedDos26 in bank 5 (US keyboard) and bank 6 (German
    # keyboard) of BOTH images; JiffyDOS transfer routines only in these three banks
    for t in KERNAL_IMAGES:
        b = rom(t)
        if b is None:
            continue
        if len(b) != 8 * BANK:
            bad.append('%s is not 512 KB' % t)
            continue
        same((t, b), 3, 0x8000, DD26_K64II, 'C64 BASIC and kernal DolphinDos26')
        same((t, b), 3, 0xC000, DD26_K128[t], 'C128 kernal DolphinDos26')
        for n, k128 in SD26_K128.items():
            same((t, b), n, 0x8000, SD26_K64II, 'C64 BASIC and kernal SpeedDos26')
            same((t, b), n, 0xA000, SD26_K64, 'C64 kernal SpeedDos26')
            same((t, b), n, 0xC000, k128, 'C128 kernal SpeedDos26')
        for n in range(8):
            if b[n * BANK:n * BANK + 0x8000] != b'\xff' * 0x8000:
                bad.append('%s: lower half of bank %d is not empty ($FF)' % (t, n + 1))
            if n not in JIFFY_BANKS and b'JIFFY' in b[n * BANK:(n + 1) * BANK].upper():
                bad.append('JiffyDOS found in bank %d of %s (only banks 4, 5 and 6 may hold it)' % (n + 1, t))
    for p in REPO.rglob('*'):
        if '.git' not in p.parts and 'jiffy' in p.name.lower():
            bad.append('file name suggests JiffyDOS content, remove it: %s' % p.relative_to(REPO))

    for de, en in MANUALS.items():
        copy(man_de / de, REPO / 'manuals' / 'de' / de, a.check, bad)
        copy(man_en / en, REPO / 'manuals' / 'en' / en, a.check, bad)
        if (man_de / de).exists() and (man_en / en).exists() and \
                (man_en / en).stat().st_mtime < (man_de / de).stat().st_mtime:
            bad.append('English manual older than German one: %s' % en)

    copy(root / 'MS-Tools' / 'ms-tools.d64', REPO / 'ms-tools' / 'ms-tools.d64', a.check, bad)
    copy(root / ROM_BUILDER[0], REPO / ROM_BUILDER[1], a.check, bad)
    rb = REPO / ROM_BUILDER[1]
    if rb.exists() and rb.stat().st_size > 200000:
        bad.append('%s is larger than expected - it must not contain ROM data' % ROM_BUILDER[1])

    # every manual must state the MD5 of exactly the files published here
    for pdf in (REPO / 'manuals').rglob('*.pdf'):
        try:
            flat = re.sub(r'\s+', '', subprocess.check_output(['pdftotext', str(pdf), '-'], text=True))
        except (OSError, subprocess.CalledProcessError) as e:
            bad.append('cannot read %s: %s' % (pdf.name, e))
            continue
        for f in [REPO / 'rom' / r for r in published] + [REPO / 'ms-tools' / 'ms-tools.d64']:
            if f.exists() and hashlib.md5(f.read_bytes()).hexdigest()[:16] not in flat:
                bad.append('%s does not state the MD5 of %s' % (pdf.name, f.name))

    if not a.check:
        files = sorted(p for d in CHECKSUMMED for p in (REPO / d).rglob('*') if p.is_file())
        for algo, out in (('md5', 'CHECKSUMS.md5'), ('sha256', 'CHECKSUMS.sha256')):
            lines = ['%s  %s' % (hashlib.new(algo, f.read_bytes()).hexdigest(), f.relative_to(REPO).as_posix())
                     for f in files]
            (REPO / out).write_text('\n'.join(lines) + '\n')

    for x in bad:
        print('PROBLEM:', x)
    print('%d problem(s)' % len(bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
