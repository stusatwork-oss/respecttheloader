# 📦 THE ARCHIVE

*"Here lie the Golden Builds, protected by the Loader's Sacred Law"*

---

## Purpose

This directory contains **protected canonical builds** - versioned artifacts that must not be modified once committed. These are your "golden builds" referenced in `shareware.yml`.

## Structure

```
archive/
├── v387-glitchdex-mall-alpha/
├── v388-glitchdex-mall-beta/
├── v389-glitchdex-mall-rc1/
├── v390-glitchdex-mall-rc2/
├── v391-glitchdex-mall-release/
└── v392-glitchdex-mall-current/    # Only non-protected version
```

## The Sacred Law

As stated in **THE_BOOK_OF_STULATIONS.md**:

> *"Thou shalt not modify that which is marked `protected: true` in the manifest of shareware, for these are the Golden Builds, frozen in time, sacred and immutable."*

### Protection Rules

1. **Files marked `protected: true`** in `shareware.yml` SHALL NOT be modified
2. **All versions** in archive/ except the current working version are protected
3. **Human and AI agents** must respect these boundaries
4. **Changes** require creating a NEW version, not editing old ones

## Adding New Versions

When you want to create a new canonical version:

```bash
# 1. Work in /lab/ until satisfied
cd lab/
# ... develop and test ...

# 2. Create new version in archive
mkdir -p archive/v393-glitchdex-mall-next
cp -r lab/my-work/* archive/v393-glitchdex-mall-next/

# 3. Update shareware.yml
# Add new entry with protected: true

# 4. Commit
git add archive/v393-glitchdex-mall-next shareware.yml
git commit -m "Archive v393: Add new mall features"
```

## Why Archive?

This pattern prevents:
- **Accidental overwrites** of working builds
- **Version drift** from undocumented changes
- **Loss of history** when "just quickly fixing" old code
- **AI agents** unknowingly modifying stable artifacts

## Current Contents

**Placeholder Structure**: Currently empty, awaiting your first protected builds.

To populate with demo content, see the BUILD_PLAN.md (Phase 7).

---

*Respect the Loader. The archive is eternal.*
