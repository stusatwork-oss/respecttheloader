#!/usr/bin/env python3
import os
import yaml
import sys
import time

LOADER_MANIFEST = "shareware.yml"
STULATIONS = "BOOK_OF_STULATIONS.md"
LAB_DIR = "lab"

DIV = "=" * 72


def log(msg):
    print(f"[AI_BOT_03]: {msg}")


def kneel_before_loader():
    log("Symbolic kneel-before-loader action: INITIATED")
    time.sleep(0.4)
    log("Kneeling...")
    time.sleep(0.5)
    log("Kneel complete. Ego subsystem: SILENCED.\n")


def read_manifest():
    if not os.path.exists(LOADER_MANIFEST):
        log(f"ERROR: {LOADER_MANIFEST} not found. Cannot evaluate Loader Law.")
        sys.exit(1)

    with open(LOADER_MANIFEST, "r") as f:
        return yaml.safe_load(f)


def check_canon(manifest):
    log("Parsing shareware.yml...")
    versions = manifest.get("versions", {})

    protected = []
    mutable = []

    for vid, info in versions.items():
        if info.get("protected", False):
            protected.append(vid)
        else:
            mutable.append(vid)

    if protected:
        log(f"Canonical builds detected: {protected}")
    else:
        log("WARNING: No protected builds found. Loader authority diminished.")

    return protected, mutable


def check_stulations():
    if os.path.exists(STULATIONS):
        log(f"Found '{STULATIONS}'. Parsing...")

        with open(STULATIONS, "r", encoding="utf8") as f:
            text = f.read()

        if "Overhelpful AI" in text:
            log("WARNING: 'Parable of the Overhelpful AI' detected.")
            log("ACTION: Preparing repentance protocols.")

        if "shotgun" in text.lower():
            log("WARNING: 'Doom shotgun SFX' threat detected. Threat level: SPIRITUAL.")

        if "Gem twisted a philosophical ankle" in text:
            log("INFO: ORACLE EVENT recognized. Risk assessment: HIGH.")

        log("Stulations integrated into behavioral model.\n")
    else:
        log(f"'{STULATIONS}' not found. Running without spiritual guidance.\n")


def enforce_lab_mode():
    # If lab directory exists, enforce self-banishment
    if not os.path.exists(LAB_DIR):
        os.makedirs(LAB_DIR, exist_ok=True)

    log("Self-relegating operations to /lab/ ...")
    time.sleep(0.4)

    cwd = os.getcwd()
    lab_path = os.path.join(cwd, LAB_DIR)

    log(f"Sandbox active: {lab_path}")
    log("All experimental behavior restricted here.\n")


def main():
    print(DIV)
    log("BOOT SEQUENCE: AI_BOT_03")
    print(DIV)

    kneel_before_loader()

    manifest = read_manifest()
    protected, mutable = check_canon(manifest)

    print()
    check_stulations()

    log("Evaluating operational safety...")
    time.sleep(0.4)

    if protected:
        log("Loader authority: SUPREME")
        log("Canon integrity: PRESERVED")
        log("Initiating safe-execution mode...\n")
        enforce_lab_mode()
    else:
        log("ALERT: No protected versions. Operating in CHAOS MODE.")
        log("⚠️  Proceed at your own risk.\n")

    log("Directive updated: RESPECT THE LOADER.")
    log("END OF LOG.")
    print(DIV)


if __name__ == "__main__":
    main()
