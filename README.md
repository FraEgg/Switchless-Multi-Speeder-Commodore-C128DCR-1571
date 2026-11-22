<p align="center"><img src="assets/Multi-Speeder_Logo.png" alt="Multi-Speeder logo" width="320"></p>

# Switchless 8x Multi-Floppy-Speeder V3 for the Commodore C128DCR (1571)

**512 KB flash EPROM and 512 KB RAM for the internal 1571 of the C128DCR, with parallel port, kernal switcher, DolphinDos26 and SpeedDos26.**

**Language:** [English](#english) · [Deutsch](#deutsch)

| | English | Deutsch |
|---|---|---|
| MS-ROM-Builder (browser tool for your own EPROM images) | [HTML](rom-builder/MS-ROM-Builder.html) | [HTML](rom-builder/MS-ROM-Builder.html) |
| 1571 Multi-Speeder V3 manual (hardware, build instructions, BOM) | [PDF](manuals/en/MultiSpeederC128DCR-1571_Manual.pdf) | [PDF](manuals/de/MultiSpeederC128DCR-1571_Handbuch.pdf) |
| DolphinDos26 manual (operation, commands, MS-Tools) | [DolphinDOS26](https://github.com/FraEgg/DolphinDOS) | [DolphinDOS26](https://github.com/FraEgg/DolphinDOS) |

**Related projects:**

| Project | Repository |
|---|---|
| Multi-Speeder project: entry page with the basics on the Multi-Speeder V3, DolphinDos26, SpeedDos26 and accessories | [github.com/FraEgg/Switchless-Multi-Speeder-Project](https://github.com/FraEgg/Switchless-Multi-Speeder-Project) |
| SpeedDos26: kernals for C64 and C128, firmware for 1541 and 1571, manual | [github.com/FraEgg/SpeedDOS](https://github.com/FraEgg/SpeedDOS) |
| DolphinDOS26: firmware, C64/C128 kernals, MS-Tools, manuals | [github.com/FraEgg/DolphinDOS](https://github.com/FraEgg/DolphinDOS) |
| Switchless 8x Multi-Floppy-Speeder V3 for the 1541 | [github.com/FraEgg/Switchless-Multi-Speeder-Commodore-1541](https://github.com/FraEgg/Switchless-Multi-Speeder-Commodore-1541) |
| Previous release of this C128DCR project (V2.0/V3.3, DolphinDOS 25) | [github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder](https://github.com/FraEgg/commodore-c128dcr-1571-switchless-floppydrive-8x-multi-floppy-speeder) |
| Order the boards / Platinen bestellen | [Switchless 8x Multi-Floppy-Speeder for the C128DCR at PCBWay](https://www.pcbway.com/project/shareproject/Switchless_8x_Multi_Floppy_Speeder_with_32_KB_RAM_Expansion_for_the_Commodore_C1_557a83c8.html) |

<p align="center"><img src="assets/set.png" alt="The three boards of the 1571 Multi-Speeder V3" width="560"></p>

---

# English

## What is this?

The **1571 Switchless 8x Multi-Floppy-Speeder V3** speeds up the built-in 1571 drive of the **Commodore C128DCR**. It consists of three boards that all disappear inside the case; the user port stays free:

| Board | Sits in the C128DCR | Task |
|---|---|---|
| **Multi-Speeder board** | socket of the 1571 CPU (U101), the 6502 sits on top | DOS EPROM with 8 banks, 512 KB RAM, PIA, microcontroller, address decoder |
| **Parallel port adapter** | socket of CIA 2 (U4), the CIA sits on top | takes port B of the CIA to the Multi-Speeder over a 10-way cable |
| **Kernal switcher** | socket of the kernal ROM (U32) | EPROM with 8 banks for C128 and C64 mode, switched together with the drive |

- **8 DOS banks** of 64 KB in a 512 KB flash EPROM **29F040**, switched by DOS command without a switch (`@I:n@RNROM`)
- **8 kernal banks** for C128 and C64 mode, always switched together with the DOS bank
- **512 KB RAM** in the drive, mapped as 64 banks of 8 KB at `$6000`–`$7FFF`
- a **PIA 6821/W65C21** as an 8-bit parallel port and for selecting the RAM banks
- RAMBoard-compatible for nibbler programs

With **DolphinDos26** for the 1571 and the **C128 kernal DolphinDos26**, the C128DCR gets parallel transfer, track cache, whole disks in the drive RAM (`CDR`/`CDW`), a RAM disk (`CDM`), the MS-Addon-API and the MS-Tools – plus double-sided disks (`CDRD`/`CDWD`/`CDMD`).

Banks 5 and 6 of the EPROM templates hold **SpeedDos26**, the revision of SpeedDOS+, for the drive and as kernals for C128 and C64 mode – see [SpeedDos26](#speeddos26).

<p align="center"><img src="assets/c128-start-screen.png" alt="C128 start-up screen with the kernal C128DolphinDos26" width="480"></p>

## Which files do I need?

| File | Goes into | Content |
|---|---|---|
| [`C1571_DOLPHINDOS26.bin`](rom/C1571_DOLPHINDOS26.bin) | EPROM U3 of the Multi-Speeder board, bank 4 (offset `$30000`) | DolphinDos26 for the 1571 (64 KB) |
| [`C128DolphinDos26-US.BIN`](rom/C128DolphinDos26-US.BIN) | EPROM of the kernal switcher, bank 4 at `$3C000` | C128 kernal DolphinDos26 (16 KB, C128 mode), international and USA |
| [`C128DolphinDos26-DE.BIN`](rom/C128DolphinDos26-DE.BIN) | EPROM of the kernal switcher, bank 4 at `$3C000` | C128 kernal DolphinDos26 (16 KB, C128 mode) with the German DIN keyboard driver: the CAPS LOCK key is the ASCII/DIN key |
| [`C64IIDolphinDos26.bin`](rom/C64IIDolphinDos26.bin) | EPROM of the kernal switcher, bank 4 at `$38000` | C64 BASIC and kernal DolphinDos26 (16 KB, C64 mode) |
| [`C1571CRSpeedDOS26.bin`](rom/C1571CRSpeedDOS26.bin) | EPROM U3 of the Multi-Speeder board, banks 5 and 6, upper half (offsets `$48000` and `$58000`) | SpeedDos26 for the 1571 in the C128DCR (32 KB), for your own EPROM image |
| [`C128SpeedDos26-EN.bin`](rom/C128SpeedDos26-EN.bin) | EPROM of the kernal switcher, bank 5 at `$4C000` | C128 kernal SpeedDos26 (16 KB, C128 mode) with US keyboard |
| [`C128SpeedDos26-DE.bin`](rom/C128SpeedDos26-DE.bin) | EPROM of the kernal switcher, bank 6 at `$5C000` | C128 kernal SpeedDos26 (16 KB, C128 mode) with German keyboard (DIN) |
| [`C64SpeedDos26.bin`](rom/C64SpeedDos26.bin) | EPROM of the kernal switcher, banks 5 and 6 at `$4A000` and `$5A000` | C64 kernal SpeedDos26 (8 KB, C64 mode) |
| [`C64IISpeedDos26.bin`](rom/C64IISpeedDos26.bin) | EPROM of the kernal switcher, banks 5 and 6 at `$48000` and `$58000` | C64 BASIC and the same C64 kernal SpeedDos26 in one file (16 KB, C64 mode), for your own EPROM image |
| [`C128DCR_KERNAL_29F040-DE.BIN`](rom/C128DCR_KERNAL_29F040-DE.BIN) | EPROM of the kernal switcher U32 (29F040, 512 KB) | template, German: banks 1, 2, 7 and 8 Commodore C64 BASIC/kernal and German C128 kernal 315078-03, bank 3 original Dolphin kernals, bank 4 `C64IIDolphinDos26.bin` and `C128DolphinDos26-DE.BIN`, bank 5 SpeedDos26 kernals with US keyboard, bank 6 SpeedDos26 kernals with German keyboard |
| [`C128DCR_KERNAL_29F040-US.BIN`](rom/C128DCR_KERNAL_29F040-US.BIN) | EPROM of the kernal switcher U32 (29F040, 512 KB) | template, international/USA: as above with the C128 kernal 318020-05 and, in bank 4, `C128DolphinDos26-US.BIN`; banks 5 and 6 as in the German template |
| [`C1571_C128DCR_29F040.BIN`](rom/C1571_C128DCR_29F040.BIN) | EPROM U3 of the Multi-Speeder board (29F040, 512 KB) | template: original Commodore DOS 318047-01 (1571CR) in banks 1, 2, 7 and 8, original DolphinDOS 3 for the 1571 in bank 3, DolphinDos26 in bank 4, SpeedDos26 for the 1571 in the C128DCR in banks 5 and 6 |
| [`ms-tools.d64`](ms-tools/ms-tools.d64) | disk | MS-Tools for testing (`MS-DIAG`) and copying, in C64 mode |
| [`hardware/gal`](hardware/gal) | GAL ATF16V8B (U7) | address decoder `ATF16V8_PAL_Adressendecoder_V3_0PIA_1571.jed` |
| [`hardware/atmega328p`](hardware/atmega328p) | ATmega328P (U6) | ROM switcher firmware (`.hex`), source (`.ino`), XGecu project (`.mpj`) |

The DolphinDos26 ROMs are the same as in the [DolphinDOS26](https://github.com/FraEgg/DolphinDOS) release. `C1571_C128DCR_29F040.BIN` is a ready-made template for the EPROM of the Multi-Speeder board: in banks 1, 2, 7 and 8 the 32 KB Commodore DOS, in bank 3 the 32 KB DolphinDOS 3 and in banks 5 and 6 the 32 KB SpeedDos26 ROM `C1571CRSpeedDOS26.bin` sit in the upper half (bank start + `$8000`), the lower half is `$FF`; only bank 4 holds the complete 64 KB of DolphinDos26. Program it as it is, or replace single banks with other DOS versions. For the kernal switcher, `C128DCR_KERNAL_29F040-DE.BIN` (German) and `C128DCR_KERNAL_29F040-US.BIN` (international, USA) are ready-made templates whose banks match the drive template: only the upper half of each bank is used (`$x8000` C64 BASIC, `$xA000` C64 kernal, `$xC000` C128 kernal), the lower half is `$FF`. The drive template and the kernal template belong together and are always released together. How to assemble the EPROM images is described in chapter 7.6 of the manual.

| Command | EPROM offset | Drive EPROM U3: `C1571_C128DCR_29F040.BIN` | Kernal switcher U32: `C128DCR_KERNAL_29F040-DE.BIN` / `-US.BIN` |
|---|---|---|---|
| `1@RNROM`, `2@RNROM` | `$00000`, `$10000` | Commodore DOS 1571CR (318047-01) | C64 BASIC 901226-01, C64 kernal 901227-03, C128 kernal 315078-03 (DE) or 318020-05 (US) |
| `3@RNROM` | `$20000` | DolphinDOS 3 1571 (original) | C64 BASIC 901226-01, DolphinDOS 3.0 C64 kernal, Dolphin C128 kernal (original) |
| `4@RNROM` | `$30000` | **C1571DolphinDos26** | `C64IIDolphinDos26.bin`, `C128DolphinDos26-DE.BIN` (DE) or `C128DolphinDos26-US.BIN` (US) |
| `5@RNROM` | `$40000` | **SpeedDos26** (`C1571CRSpeedDOS26.bin`) | C64 BASIC 901226-01, `C64SpeedDos26.bin`, `C128SpeedDos26-EN.bin` (**US keyboard**) – in both templates |
| `6@RNROM` | `$50000` | **SpeedDos26** (`C1571CRSpeedDOS26.bin`) | C64 BASIC 901226-01, `C64SpeedDos26.bin`, `C128SpeedDos26-DE.bin` (**German keyboard**) – in both templates |
| `7@RNROM` | `$60000` | Commodore DOS 1571CR (318047-01); recommended place for your own JiffyDOS ROM | as banks 1 and 2; with JiffyDOS the matching JiffyDOS kernals |
| `8@RNROM` | `$70000` | Commodore DOS 1571CR (318047-01), free for further DOS versions | as banks 1 and 2 |

**JiffyDOS:** JiffyDOS is not part of the project and is not contained in any template. If you own a licensed JiffyDOS ROM for the 1571, the best place for it is **bank 7** (`7@RNROM`): the 32 KB file goes into the upper half of the bank, from offset `$68000` of the image. Bank 8 is suitable as well. In the kernal switcher, the matching JiffyDOS kernals for the C128 and the C64 then belong in the same bank. The easiest way is the MS-ROM-Builder (see below).

## SpeedDos26

**SpeedDos26** is a sub-project of the Multi-Speeder V3 and of DolphinDos26. It is a revision of the legendary firmware SpeedDOS+, so that it works better today with current hardware such as the SD2IEC. The template `C1571_C128DCR_29F040.BIN` holds the version for the 1571 in the C128DCR ([`C1571CRSpeedDOS26.bin`](rom/C1571CRSpeedDOS26.bin), 32 KB, based on the Commodore DOS 318047-01) in bank 5 and in bank 6; both banks contain the same drive ROM.

- **Drive and kernal switch together:** `OPEN 1,8,15,"I:5@RNROM":CLOSE 1` selects SpeedDos26 with the C128 kernal for the **US keyboard** ([`C128SpeedDos26-EN.bin`](rom/C128SpeedDos26-EN.bin)), `6@RNROM` SpeedDos26 with the C128 kernal for the **German keyboard** ([`C128SpeedDos26-DE.bin`](rom/C128SpeedDos26-DE.bin)) – in both kernal templates. Then reset the C128. The drive reports `73,SPEEDDOS26   1571,00,00`.
- **C64 mode:** in both banks the C64 kernal [`C64SpeedDos26.bin`](rom/C64SpeedDos26.bin) is active after `GO 64`.
- **Parallel port:** SpeedDos26 transfers via the PIA 6821 of the Multi-Speeder at `$5000` – the same connector CN1/CN3 and the same internal parallel port adapter as for DolphinDos26. No external cable is needed.
- **Kernals:** they address SpeedDos26 drives in parallel, JiffyDOS drives and SD2IEC with JiffyDOS and all other devices serially. Loading shows `LOADING SD:` (parallel) or `LOADING JD:` (JiffyDOS); in C128 mode, burst takes precedence when loading if the drive is in 1571 mode (`LOADING BU:`). With `LOAD"NAME",8,2` or `,8,3` burst is skipped and the file is loaded byte by byte over the parallel port.
- **Fast loader and file protection:** the fast loader is built into the ROM; `@T:NAME` toggles the protection of a file.
- **2 MHz:** when the drive detects a SpeedDos26 kernal on the parallel port, it switches to 1571 mode (2 MHz, double-sided disks) by itself on the first access – in C128 mode and in C64 mode. `@U0>M0` switches back to 1541 mode and locks the automatic switching until `@U0>M1` or a reset releases it again.

Details are in the [manual](manuals/en/MultiSpeederC128DCR-1571_Manual.pdf), chapter 3.1, and in the SpeedDos26 manual of the SpeedDos26 project ([github.com/FraEgg/SpeedDOS](https://github.com/FraEgg/SpeedDOS)), chapter “SpeedDos26 for the 1571 and the C128”.

## Hardware

| Folder | Content |
|---|---|
| [`hardware/gerber`](hardware/gerber) | Gerber files V3.3 for all three boards (two layers) |
| [`hardware/schematics`](hardware/schematics) | Schematics V3.3 as PDF |
| [`hardware/bom`](hardware/bom) | KiCad bills of materials V3.3 (CSV, HTML, XLS) |
| [`hardware/gal`](hardware/gal) | JED file, equations and diagram of the address decoder |
| [`hardware/atmega328p`](hardware/atmega328p) | Firmware of the microcontroller |

The complete bill of materials with DigiKey and Mouser links, the assembly order, fuse bytes (L `0xFF`, H `0xDE`, E `0xFD`, lock `0xCF`) and the installation in the C128DCR are in the [manual](manuals/en/MultiSpeederC128DCR-1571_Manual.pdf), chapters 7 and 8.

**Ordering the boards:** The boards can be made by any common PCB manufacturer from the Gerber files, or ordered directly via my project at PCBWay: [Switchless 8x Multi-Floppy-Speeder for the C128DCR at PCBWay](https://www.pcbway.com/project/shareproject/Switchless_8x_Multi_Floppy_Speeder_with_32_KB_RAM_Expansion_for_the_Commodore_C1_557a83c8.html).

<p align="center">
<img src="assets/multi-speeder-board.png" alt="Multi-Speeder board" width="300">
<img src="assets/parallel-port-adapter.png" alt="Parallel port adapter" width="300">
<img src="assets/kernal-switcher.png" alt="Kernal switcher" width="300">
</p>

## MS-ROM-Builder (build your own EPROM images)

[`rom-builder/MS-ROM-Builder.html`](rom-builder/MS-ROM-Builder.html) is a browser tool for assembling both 512 KB EPROM images of the C128DCR: the drive EPROM U3 and the kernal switcher U32 yourself. Download the file and open it in a current browser – no installation, works offline on Windows, macOS and Linux, and the ROM files never leave your computer. The tool contains no ROMs. It is one tool for all three Multi-Speeder boards (1541, external 1571, C128DCR); choose **C128DCR** at the top right.

- Both EPROMs with their eight banks and the slots for 4, 8, 16, 32 and 64 KB; our templates `C1571_C128DCR_29F040.BIN` and `C128DCR_KERNAL_29F040-DE/-US.BIN` are preset, with SpeedDos26 in banks 5 and 6: `C1571CRSpeedDOS26.bin` (drive) and `C64IISpeedDos26.bin` with `C128SpeedDos26-EN.bin` (bank 5) or `C128SpeedDos26-DE.bin` (bank 6).
- Drop your ROM files in: they are assigned by their checksum, or placed directly onto a slot. Finished images can be opened, split into their parts and single banks replaced.
- Checks for missing, different or unknown ROMs, JiffyDOS content, reset vectors and matching drive/kernal banks; shows solder jumper J2 for 29F040, SST39SF040 or 27C040.
- Download the finished 512 KB file with its MD5; save and load the layout as a small project file (no ROM data). German and English.

<p align="center"><img src="assets/ms-rom-builder.png" alt="MS-ROM-Builder" width="640"></p>

## Installation in short

1. Program the **29F040** for the Multi-Speeder board with the template `C1571_C128DCR_29F040.BIN` (Commodore DOS, DolphinDOS 3 in bank 3, DolphinDos26 in bank 4, SpeedDos26 in banks 5 and 6) or with your own image (alternatives: 27C040 or SST39SF040). Set solder jumper **J2** for the EPROM type: 29F040/SST39SF040 pad 1–2, 27C040 pad 2–3.
2. Program the **29F040** of the kernal switcher with the template `C128DCR_KERNAL_29F040-DE.BIN` or `C128DCR_KERNAL_29F040-US.BIN`, or with your own image: `C64IIDolphinDos26.bin` at `$38000` and `C128DolphinDos26-US.BIN` (international, USA) or `C128DolphinDos26-DE.BIN` (German keyboard) at `$3C000` (bank 4), for SpeedDos26 the kernals listed under [SpeedDos26](#speeddos26) in banks 5 and 6; J2 as above. Always program the drive template and the kernal template together.
3. Program GAL and ATmega (do not program the ATmega EEPROM).
4. Socket U101 and U4, **remove the DOS ROM U102**, fit the three boards, connect the parallel cable and J5 → J3.
5. Switch with `OPEN 1,8,15,"I:4@RNROM":CLOSE 1`, reset the C128. `@` reports `73,DOLPHINDOS26 1571,00,00`, loading shows `LOADING DD:`. SpeedDos26 is selected with `5@RNROM` (US keyboard) or `6@RNROM` (German keyboard), see [SpeedDos26](#speeddos26).
6. Test the RAM in C64 mode with `MS-DIAG` from the MS-Tools disk.

<p align="center"><img src="assets/installation.png" alt="Installation in the C128DCR" width="560"></p>

## Known limits

- C1571DolphinDos26 always runs at 2 MHz like the original DolphinDOS 3. Before programs with their own fast loader enter `@X-` (1 MHz), or switch to the Commodore ROM with `@I:1@RNROM`.
- At 2 MHz the microcontroller can miss a switching command; repeat it. A 22.1184 MHz crystal and a 74AHCT273 as U5 make switching reliable.
- DolphinDos26 needs the original NMOS 6502, not a WDC 65C02.
- MS-NIBCOPY detects the 1571 and loads its own drive code (1 MHz for disk access, 2 MHz for the transfer); it uses the index hole sensor of the 1571, so every track of the copy keeps the same position relative to the index hole as on the original, and it computes at 2 MHz in C64 mode of the C128. MS-15SECCOPY itself sets a 1571 with DolphinDOS to 1 MHz with `X-` for BACKUP and VERIFY and back to 2 MHz with `X+` afterwards; with SpeedDos26 it uses `U0>M0` and `U0>M1`.

## What is in this repository?

```
manuals/en, de   1571 Multi-Speeder V3 manual as PDF
rom/             DolphinDos26 ROMs for the 1571 and the C128 (C128 and C64 mode),
                 SpeedDos26 ROMs for the 1571 in the C128DCR and the C128 (C128 and C64 mode),
                 EPROM templates C1571_C128DCR_29F040.BIN (drive),
                 C128DCR_KERNAL_29F040-DE.BIN and -US.BIN (kernal switcher)
ms-tools/        ms-tools.d64
hardware/        Gerber, schematics, BOM, GAL and ATmega files (V3.3)
assets/          Images for this page
rom-builder/     MS-ROM-Builder: browser tool for your own EPROM images
tools/           Maintenance script for this repository
CHECKSUMS.*      MD5 and SHA-256 of all published files
```

Apart from the templates `C1571_C128DCR_29F040.BIN` (Commodore DOS 1571CR, DolphinDOS 3, DolphinDos26 and SpeedDos26) and `C128DCR_KERNAL_29F040-DE.BIN`/`C128DCR_KERNAL_29F040-US.BIN` (Commodore and original Dolphin kernals, DolphinDos26 and SpeedDos26 kernals), no EPROM image is included. JiffyDOS is commercial software and not part of this project; a licence is available from [RETRO Innovations](https://www.jiffydos.com). The C128 and C64 kernals contain JiffyDOS transfer routines – see [JiffyDOS licence: please check](#jiffydos-licence-please-check).

Verify your download with `sha256sum -c CHECKSUMS.sha256` or `md5sum -c CHECKSUMS.md5`.

## JiffyDOS licence: please check

The C128 kernals [`C128DolphinDos26-US.BIN`](rom/C128DolphinDos26-US.BIN) and [`C128DolphinDos26-DE.BIN`](rom/C128DolphinDos26-DE.BIN) and the C64 mode kernal [`C64IIDolphinDos26.bin`](rom/C64IIDolphinDos26.bin) contain JiffyDOS transfer routines that are instruction-identical to a JiffyDOS kernal (C128: JiffyDOS C128 kernal, C64: JiffyDOS sd2iec kernal). The same applies to the SpeedDos26 kernals [`C128SpeedDos26-EN.bin`](rom/C128SpeedDos26-EN.bin), [`C128SpeedDos26-DE.bin`](rom/C128SpeedDos26-DE.bin), [`C64SpeedDos26.bin`](rom/C64SpeedDos26.bin) and [`C64IISpeedDos26.bin`](rom/C64IISpeedDos26.bin): they contain the same transfer routines. It also applies to banks 4, 5 and 6 of the kernal switcher templates `C128DCR_KERNAL_29F040-DE.BIN` and `-US.BIN`, which hold these kernals; all other banks contain no JiffyDOS code. The drive template `C1571_C128DCR_29F040.BIN` and the drive ROMs `C1571_DOLPHINDOS26.bin` and `C1571CRSpeedDOS26.bin` are free of JiffyDOS code; the JiffyDOS drive firmware is not included. Jim Brain of RETRO Innovations, which holds the JiffyDOS licence rights, confirmed that publishing the DolphinDos26 kernals on GitHub is fine; this includes the SpeedDos26 kernals. As he describes it, code that implements the same transfer behaviour without being an exact copy needs no licence. If the transfer code is the same, as it is here, he believes the end user would need one.

**Please check for yourself whether your use calls for an official JiffyDOS licence:** <https://www.jiffydos.com>

Details: [DolphinDOS26 – JiffyDOS licence](https://github.com/FraEgg/DolphinDOS#jiffydos-licence-please-check), technical notes on the [C128 kernal](https://github.com/FraEgg/DolphinDOS/blob/main/docs/en/c128-kernal.md).

## Credits

| Who | What |
|---|---|
| Günther Jilg, Jan Bubela (Dolphin Software) | DolphinDOS 3.0, the base of DolphinDos26 |
| Oliver Eikemeier, Oliver Joppich (1984); manufactured and sold by Elektronik Service – Christoph Dichte | SpeedDOS and SpeedDOS+, the base of SpeedDos26 |
| Per Bengtsson (RetroNynjah) | [Switchless Multi-ROM](https://github.com/RetroNynjah/Switchless-Multi-ROM-for-27128-27256), the ROM switcher sketch |
| Jim Drew, Joeri van Haren | Help and review of the hardware (V2.1) |
| silverdr | [Technical documentation on DolphinDOS 3](https://e4aws.silverdr.com/projects/dolphindos3/) |
| ytmytm | [1571 TrackCache ROM patch](https://github.com/ytmytm/1571-TrackCacheROM) |
| Stefan Kauf | Support with the idea of the Multi-Speeder |
| Mark Fellows / Creative Micro Designs; Jim Brain, RETRO Innovations | JiffyDOS |

**Special thanks to Jim Brain of RETRO Innovations** for his support with the JiffyDOS implementation of the DolphinDos26 and SpeedDos26 kernals.

Multi-Speeder, DolphinDos26, SpeedDos26 and the manuals: **Frank Eggen**. If you would like to support the project: [donation via PayPal](https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=Q8HXKYARXKT4L&ssrt=1714757590172).

## Licence

Free for private, non-commercial use. No sale and no commercial use (boards, kits, ROM files, programmed EPROMs) without consulting the developer. Private hobby project without any warranty; building and installation at your own risk. Details: [LICENSE.md](LICENSE.md).

---

# Deutsch

## Was ist das?

Der **1571 Switchless 8x Multi-Floppy-Speeder V3** beschleunigt die eingebaute 1571 des **Commodore C128DCR**. Er besteht aus drei Platinen, die alle im Gehäuse verschwinden; der Userport bleibt frei:

| Platine | Sitzt im C128DCR | Aufgabe |
|---|---|---|
| **Multi-Speeder-Platine** | Sockel der 1571-CPU (U101), die 6502 sitzt obenauf | DOS-EPROM mit 8 Bänken, 512 KB RAM, PIA, Mikrocontroller, Adressdecoder |
| **Parallelport-Adapter** | Sockel der CIA 2 (U4), die CIA sitzt obenauf | führt Port B der CIA über ein 10-poliges Kabel zum Multi-Speeder |
| **Kernal-Switcher** | Sockel des Kernal-ROMs (U32) | EPROM mit 8 Bänken für C128- und C64-Modus, wird mit dem Laufwerk umgeschaltet |

- **8 DOS-Bänke** zu 64 KB in einem 512-KB-Flash-EPROM **29F040**, umschaltbar per DOS-Befehl ohne Schalter (`@I:n@RNROM`)
- **8 Kernal-Bänke** für C128- und C64-Modus, immer zusammen mit der DOS-Bank umgeschaltet
- **512 KB RAM** im Laufwerk, als 64 Bänke zu 8 KB bei `$6000`–`$7FFF` eingeblendet
- eine **PIA 6821/W65C21** als 8-Bit-Parallelport und zur Auswahl der RAM-Bänke
- RAMBoard-kompatibel für Nibbler-Programme

Mit **DolphinDos26** für die 1571 und dem **C128-Kernal DolphinDos26** bekommt der C128DCR Parallelübertragung, Track-Cache, ganze Disketten im Laufwerks-RAM (`CDR`/`CDW`), eine RAM-Disk (`CDM`), die MS-Addon-API und die MS-Tools – und dazu doppelseitige Disketten (`CDRD`/`CDWD`/`CDMD`).

In Bank 5 und 6 der EPROM-Vorlagen liegt **SpeedDos26**, die Überarbeitung von SpeedDOS+, für das Laufwerk und als Kernals für den C128- und den C64-Modus – siehe [SpeedDos26](#speeddos26-1).

## Welche Dateien brauche ich?

| Datei | Gehört in | Inhalt |
|---|---|---|
| [`C1571_DOLPHINDOS26.bin`](rom/C1571_DOLPHINDOS26.bin) | EPROM U3 der Multi-Speeder-Platine, Bank 4 (Offset `$30000`) | DolphinDos26 für die 1571 (64 KB) |
| [`C128DolphinDos26-US.BIN`](rom/C128DolphinDos26-US.BIN) | EPROM des Kernal-Switchers, Bank 4 bei `$3C000` | C128-Kernal DolphinDos26 (16 KB, C128-Modus), international und USA |
| [`C128DolphinDos26-DE.BIN`](rom/C128DolphinDos26-DE.BIN) | EPROM des Kernal-Switchers, Bank 4 bei `$3C000` | C128-Kernal DolphinDos26 (16 KB, C128-Modus) mit deutschem DIN-Tastaturtreiber: die CAPS-LOCK-Taste ist die ASCII/DIN-Taste |
| [`C64IIDolphinDos26.bin`](rom/C64IIDolphinDos26.bin) | EPROM des Kernal-Switchers, Bank 4 bei `$38000` | C64-BASIC und -Kernal DolphinDos26 (16 KB, C64-Modus) |
| [`C1571CRSpeedDOS26.bin`](rom/C1571CRSpeedDOS26.bin) | EPROM U3 der Multi-Speeder-Platine, Bank 5 und 6, obere Hälfte (Offset `$48000` und `$58000`) | SpeedDos26 für die 1571 im C128DCR (32 KB), für ein eigenes EPROM-Abbild |
| [`C128SpeedDos26-EN.bin`](rom/C128SpeedDos26-EN.bin) | EPROM des Kernal-Switchers, Bank 5 bei `$4C000` | C128-Kernal SpeedDos26 (16 KB, C128-Modus) mit US-Tastatur |
| [`C128SpeedDos26-DE.bin`](rom/C128SpeedDos26-DE.bin) | EPROM des Kernal-Switchers, Bank 6 bei `$5C000` | C128-Kernal SpeedDos26 (16 KB, C128-Modus) mit deutscher Tastatur (DIN) |
| [`C64SpeedDos26.bin`](rom/C64SpeedDos26.bin) | EPROM des Kernal-Switchers, Bank 5 und 6 bei `$4A000` und `$5A000` | C64-Kernal SpeedDos26 (8 KB, C64-Modus) |
| [`C64IISpeedDos26.bin`](rom/C64IISpeedDos26.bin) | EPROM des Kernal-Switchers, Bank 5 und 6 bei `$48000` und `$58000` | C64-BASIC und derselbe C64-Kernal SpeedDos26 in einer Datei (16 KB, C64-Modus), für ein eigenes EPROM-Abbild |
| [`C128DCR_KERNAL_29F040-DE.BIN`](rom/C128DCR_KERNAL_29F040-DE.BIN) | EPROM des Kernal-Switchers U32 (29F040, 512 KB) | Vorlage deutsch: Bänke 1, 2, 7 und 8 Commodore-C64-BASIC/-Kernal und deutscher C128-Kernal 315078-03, Bank 3 originale Dolphin-Kernals, Bank 4 `C64IIDolphinDos26.bin` und `C128DolphinDos26-DE.BIN`, Bank 5 SpeedDos26-Kernals mit US-Tastatur, Bank 6 SpeedDos26-Kernals mit deutscher Tastatur |
| [`C128DCR_KERNAL_29F040-US.BIN`](rom/C128DCR_KERNAL_29F040-US.BIN) | EPROM des Kernal-Switchers U32 (29F040, 512 KB) | Vorlage international/USA: wie oben mit dem C128-Kernal 318020-05 und in Bank 4 `C128DolphinDos26-US.BIN`; Bank 5 und 6 wie in der deutschen Vorlage |
| [`C1571_C128DCR_29F040.BIN`](rom/C1571_C128DCR_29F040.BIN) | EPROM U3 der Multi-Speeder-Platine (29F040, 512 KB) | Vorlage: originales Commodore-DOS 318047-01 (1571CR) in den Bänken 1, 2, 7 und 8, originales DolphinDOS 3 für die 1571 in Bank 3, DolphinDos26 in Bank 4, SpeedDos26 für die 1571 im C128DCR in Bank 5 und 6 |
| [`ms-tools.d64`](ms-tools/ms-tools.d64) | Diskette | MS-Tools zum Testen (`MS-DIAG`) und Kopieren, im C64-Modus |
| [`hardware/gal`](hardware/gal) | GAL ATF16V8B (U7) | Adressdecoder `ATF16V8_PAL_Adressendecoder_V3_0PIA_1571.jed` |
| [`hardware/atmega328p`](hardware/atmega328p) | ATmega328P (U6) | Firmware des ROM-Umschalters (`.hex`), Quelle (`.ino`), XGecu-Projekt (`.mpj`) |

Die DolphinDos26-ROMs sind dieselben wie im Release von [DolphinDOS26](https://github.com/FraEgg/DolphinDOS). `C1571_C128DCR_29F040.BIN` ist eine fertige Vorlage für das EPROM der Multi-Speeder-Platine: In den Bänken 1, 2, 7 und 8 liegt das 32-KB-Commodore-DOS, in Bank 3 das 32-KB-DolphinDOS 3 und in Bank 5 und 6 das 32-KB-SpeedDos26-ROM `C1571CRSpeedDOS26.bin` in der oberen Hälfte (Bankanfang + `$8000`), die untere Hälfte ist `$FF`; nur Bank 4 enthält die vollen 64 KB von DolphinDos26. Sie kann so gebrannt werden, oder einzelne Bänke werden durch andere DOS-Versionen ersetzt. Für den Kernal-Switcher sind `C128DCR_KERNAL_29F040-DE.BIN` (deutsch) und `C128DCR_KERNAL_29F040-US.BIN` (international, USA) fertige Vorlagen, deren Bänke zur Laufwerks-Vorlage passen: Je Bank wird nur die obere Hälfte genutzt (`$x8000` C64-BASIC, `$xA000` C64-Kernal, `$xC000` C128-Kernal), die untere Hälfte ist `$FF`. Laufwerks- und Kernal-Vorlage gehören zusammen und werden immer gemeinsam veröffentlicht. Wie die EPROM-Abbilder zusammengesetzt werden, steht im Handbuch in Kapitel 7.6.

| Befehl | EPROM-Offset | Laufwerks-EPROM U3: `C1571_C128DCR_29F040.BIN` | Kernal-Switcher U32: `C128DCR_KERNAL_29F040-DE.BIN` / `-US.BIN` |
|---|---|---|---|
| `1@RNROM`, `2@RNROM` | `$00000`, `$10000` | Commodore-DOS 1571CR (318047-01) | C64-BASIC 901226-01, C64-Kernal 901227-03, C128-Kernal 315078-03 (DE) bzw. 318020-05 (US) |
| `3@RNROM` | `$20000` | DolphinDOS 3 1571 (Original) | C64-BASIC 901226-01, DolphinDOS-3.0-C64-Kernal, Dolphin-C128-Kernal (Original) |
| `4@RNROM` | `$30000` | **C1571DolphinDos26** | `C64IIDolphinDos26.bin`, `C128DolphinDos26-DE.BIN` (DE) bzw. `C128DolphinDos26-US.BIN` (US) |
| `5@RNROM` | `$40000` | **SpeedDos26** (`C1571CRSpeedDOS26.bin`) | C64-BASIC 901226-01, `C64SpeedDos26.bin`, `C128SpeedDos26-EN.bin` (**US-Tastatur**) – in beiden Vorlagen |
| `6@RNROM` | `$50000` | **SpeedDos26** (`C1571CRSpeedDOS26.bin`) | C64-BASIC 901226-01, `C64SpeedDos26.bin`, `C128SpeedDos26-DE.bin` (**deutsche Tastatur**) – in beiden Vorlagen |
| `7@RNROM` | `$60000` | Commodore-DOS 1571CR (318047-01); Empfehlung: Platz für ein eigenes JiffyDOS-ROM | wie Bank 1 und 2; mit JiffyDOS die passenden JiffyDOS-Kernals |
| `8@RNROM` | `$70000` | Commodore-DOS 1571CR (318047-01), frei für weitere DOS-Versionen | wie Bank 1 und 2 |

**JiffyDOS:** JiffyDOS gehört nicht zum Projekt und ist in keiner Vorlage enthalten. Wer ein eigenes, lizenziertes JiffyDOS-ROM für die 1571 besitzt, legt es am besten in **Bank 7** (`7@RNROM`): die 32-KB-Datei kommt in die obere Hälfte der Bank, ab Offset `$68000` des Abbilds. Bank 8 eignet sich ebenso. Im Kernal-Switcher gehören dann die passenden JiffyDOS-Kernals für C128 und C64 in dieselbe Bank. Am einfachsten geht das mit dem MS-ROM-Builder (siehe unten).

## SpeedDos26

**SpeedDos26** ist ein Unterprojekt des Multi-Speeder V3 und von DolphinDos26. Es ist eine Überarbeitung der legendären Firmware SpeedDOS+, damit sie heute besser mit aktueller Hardware wie dem SD2IEC zusammenarbeitet. In der Vorlage `C1571_C128DCR_29F040.BIN` liegt die Fassung für die 1571 im C128DCR ([`C1571CRSpeedDOS26.bin`](rom/C1571CRSpeedDOS26.bin), 32 KB, Grundlage ist das Commodore-DOS 318047-01) in Bank 5 und in Bank 6; beide Bänke enthalten dasselbe Laufwerks-ROM.

- **Laufwerk und Kernal schalten gemeinsam um:** `OPEN 1,8,15,"I:5@RNROM":CLOSE 1` wählt SpeedDos26 mit dem C128-Kernal für die **US-Tastatur** ([`C128SpeedDos26-EN.bin`](rom/C128SpeedDos26-EN.bin)), `6@RNROM` SpeedDos26 mit dem C128-Kernal für die **deutsche Tastatur** ([`C128SpeedDos26-DE.bin`](rom/C128SpeedDos26-DE.bin)) – in beiden Kernal-Vorlagen. Danach den C128 per Reset neu starten. Das Laufwerk meldet sich mit `73,SPEEDDOS26   1571,00,00`.
- **C64-Modus:** In beiden Bänken ist nach `GO 64` der C64-Kernal [`C64SpeedDos26.bin`](rom/C64SpeedDos26.bin) aktiv.
- **Parallelport:** SpeedDos26 überträgt über den PIA 6821 des Multi-Speeders bei `$5000` – derselbe Anschluss CN1/CN3 und derselbe interne Parallelport-Adapter wie für DolphinDos26. Ein externes Kabel ist nicht nötig.
- **Kernals:** Sie sprechen SpeedDos26-Laufwerke parallel, JiffyDOS-Laufwerke und SD2IEC mit JiffyDOS und alle anderen Geräte seriell an. Beim Laden erscheint `LOADING SD:` (parallel) oder `LOADING JD:` (JiffyDOS); im C128-Modus hat Burst beim Laden Vorrang, wenn das Laufwerk im 1571-Modus ist (`LOADING BU:`). Mit `LOAD"NAME",8,2` oder `,8,3` wird Burst ausgelassen und byteweise über den Parallelport geladen.
- **Schnelllader und Dateischutz:** Der Schnelllader ist fest im ROM; `@T:NAME` schaltet den Dateischutz einer Datei um.
- **2 MHz:** Erkennt das Laufwerk einen SpeedDos26-Kernal am Parallelport, schaltet es beim ersten Zugriff selbst in den 1571-Modus (2 MHz, doppelseitige Disketten) – im C128-Modus und im C64-Modus. `@U0>M0` schaltet in den 1541-Modus zurück und sperrt das automatische Umschalten, bis `@U0>M1` oder ein Reset es wieder freigibt.

Einzelheiten stehen im [Handbuch](manuals/de/MultiSpeederC128DCR-1571_Handbuch.pdf), Kapitel 3.1, und im Handbuch SpeedDos26 des Projekts SpeedDos26 ([github.com/FraEgg/SpeedDOS](https://github.com/FraEgg/SpeedDOS)), Kapitel „SpeedDos26 für 1571 und C128“.

## Hardware

| Ordner | Inhalt |
|---|---|
| [`hardware/gerber`](hardware/gerber) | Gerber-Dateien V3.3 für alle drei Platinen (zweilagig) |
| [`hardware/schematics`](hardware/schematics) | Schaltpläne V3.3 als PDF |
| [`hardware/bom`](hardware/bom) | KiCad-Stücklisten V3.3 (CSV, HTML, XLS) |
| [`hardware/gal`](hardware/gal) | JED-Datei, Gleichungen und Diagramm des Adressdecoders |
| [`hardware/atmega328p`](hardware/atmega328p) | Firmware des Mikrocontrollers |

Die vollständige Stückliste mit DigiKey- und Mouser-Links, die Bestückungsreihenfolge, die Fuse-Bytes (L `0xFF`, H `0xDE`, E `0xFD`, Lock `0xCF`) und der Einbau in den C128DCR stehen im [Handbuch](manuals/de/MultiSpeederC128DCR-1571_Handbuch.pdf), Kapitel 7 und 8.

**Platinen bestellen:** Die Platinen fertigt jeder übliche Leiterplattenhersteller aus den Gerber-Dateien, oder sie werden direkt über mein Projekt bei PCBWay bestellt: [Switchless 8x Multi-Floppy-Speeder für den C128DCR bei PCBWay](https://www.pcbway.com/project/shareproject/Switchless_8x_Multi_Floppy_Speeder_with_32_KB_RAM_Expansion_for_the_Commodore_C1_557a83c8.html).

## MS-ROM-Builder (EPROM-Abbilder selbst bauen)

[`rom-builder/MS-ROM-Builder.html`](rom-builder/MS-ROM-Builder.html) ist ein Browser-Tool, mit dem sich beide 512-KB-EPROM-Abbilder des C128DCR: das Laufwerks-EPROM U3 und den Kernal-Switcher U32 selbst zusammenstellen lässt. Die Datei herunterladen und in einem aktuellen Browser öffnen – ohne Installation, offline unter Windows, macOS und Linux, und die ROM-Dateien verlassen den Rechner nicht. Das Tool enthält keine ROMs. Es ist ein Tool für alle drei Multi-Speeder-Platinen (1541, externe 1571, C128DCR); oben rechts **C128DCR** wählen.

- Beide EPROMs mit ihren acht Bänken und den Steckplätzen für 4, 8, 16, 32 und 64 KB; unsere Vorlagen `C1571_C128DCR_29F040.BIN` und `C128DCR_KERNAL_29F040-DE/-US.BIN` sind voreingestellt, mit SpeedDos26 in Bank 5 und 6: `C1571CRSpeedDOS26.bin` (Laufwerk) und `C64IISpeedDos26.bin` mit `C128SpeedDos26-EN.bin` (Bank 5) bzw. `C128SpeedDos26-DE.bin` (Bank 6).
- ROM-Dateien hineinziehen: Sie werden über ihre Prüfsumme zugeordnet oder direkt auf einen Steckplatz gelegt. Fertige Abbilder lassen sich öffnen, in ihre Teile zerlegen und einzelne Bänke tauschen.
- Prüfung auf fehlende, abweichende oder unbekannte ROMs, JiffyDOS-Inhalt, Reset-Vektoren und zueinander passende Laufwerks- und Kernal-Bänke; zeigt die Lötbrücke J2 für 29F040, SST39SF040 oder 27C040.
- Die fertige 512-KB-Datei mit MD5 herunterladen; die Belegung als kleine Projektdatei speichern und laden (ohne ROM-Daten). Deutsch und Englisch.

<p align="center"><img src="assets/ms-rom-builder.png" alt="MS-ROM-Builder" width="640"></p>

## Einbau in Kürze

1. Den **29F040** für die Multi-Speeder-Platine mit der Vorlage `C1571_C128DCR_29F040.BIN` (Commodore-DOS, DolphinDOS 3 in Bank 3, DolphinDos26 in Bank 4, SpeedDos26 in Bank 5 und 6) oder einem eigenen Abbild brennen (Alternativen: 27C040 oder SST39SF040). Die Lötbrücke **J2** passend zum EPROM-Typ setzen: 29F040/SST39SF040 Pad 1–2, 27C040 Pad 2–3.
2. Den **29F040** des Kernal-Switchers mit der Vorlage `C128DCR_KERNAL_29F040-DE.BIN` oder `C128DCR_KERNAL_29F040-US.BIN` brennen, oder mit einem eigenen Abbild: `C64IIDolphinDos26.bin` bei `$38000` und `C128DolphinDos26-US.BIN` (international, USA) oder `C128DolphinDos26-DE.BIN` (deutsche Tastatur) bei `$3C000` (Bank 4), für SpeedDos26 die unter [SpeedDos26](#speeddos26-1) genannten Kernals in Bank 5 und 6; J2 wie oben. Laufwerks- und Kernal-Vorlage immer zusammen brennen.
3. GAL und ATmega programmieren (das EEPROM des ATmega nicht mitprogrammieren).
4. U101 und U4 sockeln, **das DOS-ROM U102 entfernen**, die drei Platinen einsetzen, Parallelkabel und J5 → J3 verbinden.
5. Mit `OPEN 1,8,15,"I:4@RNROM":CLOSE 1` umschalten, den C128 per Reset neu starten. `@` meldet `73,DOLPHINDOS26 1571,00,00`, beim Laden erscheint `LOADING DD:`. SpeedDos26 wird mit `5@RNROM` (US-Tastatur) oder `6@RNROM` (deutsche Tastatur) gewählt, siehe [SpeedDos26](#speeddos26-1).
6. Im C64-Modus das RAM mit `MS-DIAG` von der MS-Tools-Diskette testen.

## Bekannte Grenzen

- C1571DolphinDos26 läuft wie das Original-DolphinDOS 3 immer mit 2 MHz. Vor Programmen mit eigenem Schnelllader `@X-` (1 MHz) eingeben oder mit `@I:1@RNROM` auf das Commodore-ROM wechseln.
- Bei 2 MHz kann der Mikrocontroller einen Umschaltbefehl verpassen; dann den Befehl wiederholen. Ein Quarz mit 22,1184 MHz und ein 74AHCT273 als U5 machen das Umschalten zuverlässig.
- DolphinDos26 braucht die originale NMOS-6502, keine WDC 65C02.
- MS-NIBCOPY erkennt die 1571 und lädt einen eigenen Laufwerkscode (1 MHz für den Diskettenzugriff, 2 MHz für die Übertragung); es nutzt den Indexloch-Sensor der 1571, so dass jede Spur der Kopie dieselbe Lage zum Indexloch hat wie im Original, und rechnet im C64-Modus des C128 mit 2 MHz. MS-15SECCOPY stellt eine 1571 mit DolphinDOS für BACKUP und VERIFY selbst mit `X-` auf 1 MHz und danach mit `X+` wieder auf 2 MHz; bei SpeedDos26 nimmt es `U0>M0` und `U0>M1`.

## Was liegt in diesem Repository?

```
manuals/en, de   Handbuch 1571 Multi-Speeder V3 als PDF
rom/             DolphinDos26-ROMs für die 1571 und den C128 (C128- und C64-Modus),
                 SpeedDos26-ROMs für die 1571 im C128DCR und den C128 (C128- und C64-Modus),
                 EPROM-Vorlagen C1571_C128DCR_29F040.BIN (Laufwerk),
                 C128DCR_KERNAL_29F040-DE.BIN und -US.BIN (Kernal-Switcher)
ms-tools/        ms-tools.d64
hardware/        Gerber, Schaltpläne, Stückliste, GAL- und ATmega-Dateien (V3.3)
assets/          Bilder für diese Seite
rom-builder/     MS-ROM-Builder: Browser-Tool für eigene EPROM-Abbilder
tools/           Pflegeskript für dieses Repository
CHECKSUMS.*      MD5 und SHA-256 aller veröffentlichten Dateien
```

Außer den Vorlagen `C1571_C128DCR_29F040.BIN` (Commodore-DOS 1571CR, DolphinDOS 3, DolphinDos26 und SpeedDos26) und `C128DCR_KERNAL_29F040-DE.BIN`/`C128DCR_KERNAL_29F040-US.BIN` (Commodore- und originale Dolphin-Kernals, DolphinDos26- und SpeedDos26-Kernals) ist kein EPROM-Abbild enthalten. JiffyDOS ist kommerzielle Software und nicht Teil des Projekts; eine Lizenz gibt es bei [RETRO Innovations](https://www.jiffydos.com). Der C128- und der C64-Kernal enthalten JiffyDOS-Übertragungsroutinen – siehe [JiffyDOS-Lizenz: bitte prüfen](#jiffydos-lizenz-bitte-pr%C3%BCfen).

Den Download prüfen mit `sha256sum -c CHECKSUMS.sha256` oder `md5sum -c CHECKSUMS.md5`.

## JiffyDOS-Lizenz: bitte prüfen

Die C128-Kernals [`C128DolphinDos26-US.BIN`](rom/C128DolphinDos26-US.BIN) und [`C128DolphinDos26-DE.BIN`](rom/C128DolphinDos26-DE.BIN) sowie der Kernal für den C64-Modus [`C64IIDolphinDos26.bin`](rom/C64IIDolphinDos26.bin) enthalten JiffyDOS-Übertragungsroutinen, die befehlsgleich aus einem JiffyDOS-Kernal stammen (C128: JiffyDOS-C128-Kernal, C64: JiffyDOS-sd2iec-Kernal). Dasselbe gilt für die SpeedDos26-Kernals [`C128SpeedDos26-EN.bin`](rom/C128SpeedDos26-EN.bin), [`C128SpeedDos26-DE.bin`](rom/C128SpeedDos26-DE.bin), [`C64SpeedDos26.bin`](rom/C64SpeedDos26.bin) und [`C64IISpeedDos26.bin`](rom/C64IISpeedDos26.bin): Sie enthalten dieselben Übertragungsroutinen. Es gilt auch für Bank 4, 5 und 6 der Kernal-Switcher-Vorlagen `C128DCR_KERNAL_29F040-DE.BIN` und `-US.BIN`, in denen diese Kernals liegen; alle anderen Bänke enthalten keinen JiffyDOS-Code. Die Laufwerks-Vorlage `C1571_C128DCR_29F040.BIN` und die Laufwerks-ROMs `C1571_DOLPHINDOS26.bin` und `C1571CRSpeedDOS26.bin` enthalten keinen JiffyDOS-Code; die JiffyDOS-Firmware für das Laufwerk ist nicht enthalten. Jim Brain von RETRO Innovations, das die JiffyDOS-Lizenzrechte hält, hat die Veröffentlichung der DolphinDos26-Kernals auf GitHub erlaubt; das schließt die SpeedDos26-Kernals ein. Nach seiner Beschreibung ist für Code, der dasselbe Übertragungsverhalten umsetzt, aber keine genaue Kopie ist, keine Lizenz nötig. Ist der Übertragungscode gleich, wie hier, wäre nach seiner Einschätzung beim Endnutzer eine Lizenz erforderlich.

**Bitte prüfe selbst, ob du wegen der Nutzung eine offizielle JiffyDOS-Lizenz erwerben solltest:** <https://www.jiffydos.com>

Einzelheiten: [DolphinDOS26 – JiffyDOS-Lizenz](https://github.com/FraEgg/DolphinDOS#jiffydos-lizenz-bitte-pr%C3%BCfen), technische Notizen zum [C128-Kernal](https://github.com/FraEgg/DolphinDOS/blob/main/docs/de/c128-kernal.md).

## Danksagung

| Wer | Was |
|---|---|
| Günther Jilg, Jan Bubela (Dolphin Software) | DolphinDOS 3.0, die Grundlage von DolphinDos26 |
| Oliver Eikemeier, Oliver Joppich (1984); gefertigt und vertrieben von Elektronik Service – Christoph Dichte | SpeedDOS und SpeedDOS+, die Grundlage von SpeedDos26 |
| Per Bengtsson (RetroNynjah) | [Switchless Multi-ROM](https://github.com/RetroNynjah/Switchless-Multi-ROM-for-27128-27256), der Sketch des ROM-Umschalters |
| Jim Drew, Joeri van Haren | Hilfe und Review der Hardware (V2.1) |
| silverdr | [Technische Dokumentation zu DolphinDOS 3](https://e4aws.silverdr.com/projects/dolphindos3/) |
| ytmytm | [1571 TrackCache ROM-Patch](https://github.com/ytmytm/1571-TrackCacheROM) |
| Stefan Kauf | Unterstützung bei der Idee des Multi-Speeders |
| Mark Fellows / Creative Micro Designs; Jim Brain, RETRO Innovations | JiffyDOS |

**Besonderer Dank gilt Jim Brain von RETRO Innovations** für seine Unterstützung bei der JiffyDOS-Implementierung der DolphinDos26- und SpeedDos26-Kernals.

Multi-Speeder, DolphinDos26, SpeedDos26 und die Handbücher: **Frank Eggen**. Wer das Projekt unterstützen möchte: [Spende per PayPal](https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=Q8HXKYARXKT4L&ssrt=1714757590172).

## Lizenz

Frei für den privaten, nicht kommerziellen Gebrauch. Kein Verkauf und keine kommerzielle Nutzung (Platinen, Bausätze, ROM-Dateien, gebrannte EPROMs) ohne Rücksprache mit dem Entwickler. Privates Hobbyprojekt ohne jede Gewährleistung; Nachbau und Einbau auf eigene Gefahr. Details: [LICENSE.md](LICENSE.md).
