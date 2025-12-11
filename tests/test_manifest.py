"""Integration tests for shareware.yml manifest validation."""

import os

import pytest
import yaml

# Path to the repository root (relative to tests directory)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(REPO_ROOT, "shareware.yml")
ARCHIVE_DIR = os.path.join(REPO_ROOT, "archive")


class TestManifestExists:
    """Tests verifying the manifest file exists and is valid."""

    def test_shareware_yml_exists(self):
        """The shareware.yml manifest file must exist."""
        assert os.path.exists(
            MANIFEST_PATH
        ), f"shareware.yml not found at {MANIFEST_PATH}"

    def test_shareware_yml_is_valid_yaml(self):
        """The manifest must be valid YAML."""
        with open(MANIFEST_PATH, "r") as f:
            manifest = yaml.safe_load(f)

        assert manifest is not None, "shareware.yml is empty or invalid"
        assert isinstance(manifest, dict), "shareware.yml must be a YAML dictionary"


class TestManifestStructure:
    """Tests verifying the manifest has required structure."""

    @pytest.fixture
    def manifest(self):
        """Load the manifest for tests."""
        with open(MANIFEST_PATH, "r") as f:
            return yaml.safe_load(f)

    def test_has_versions_key(self, manifest):
        """Manifest must have a 'versions' key."""
        assert "versions" in manifest, "shareware.yml must have a 'versions' key"

    def test_versions_is_dict(self, manifest):
        """The versions key must contain a dictionary."""
        assert isinstance(manifest["versions"], dict), "versions must be a dictionary"

    def test_has_at_least_one_version(self, manifest):
        """Manifest must define at least one version."""
        assert (
            len(manifest["versions"]) > 0
        ), "shareware.yml must define at least one version"

    def test_each_version_has_path(self, manifest):
        """Each version must have a 'path' field."""
        for vid, info in manifest["versions"].items():
            assert "path" in info, f"Version '{vid}' is missing 'path' field"

    def test_each_version_has_protected_field(self, manifest):
        """Each version should have an explicit 'protected' field."""
        for vid, info in manifest["versions"].items():
            assert "protected" in info, (
                f"Version '{vid}' is missing 'protected' field. "
                "Best practice: always be explicit about protection status."
            )


class TestArchiveDirectory:
    """Tests verifying the archive directory structure."""

    def test_archive_directory_exists(self):
        """The archive directory must exist."""
        assert os.path.isdir(
            ARCHIVE_DIR
        ), f"archive directory not found at {ARCHIVE_DIR}"

    def test_archive_has_readme(self):
        """Archive directory should have a README."""
        readme_path = os.path.join(ARCHIVE_DIR, "README.md")
        assert os.path.exists(readme_path), "archive/ directory should have a README.md"


class TestArchivePaths:
    """Tests verifying archive paths referenced in manifest."""

    @pytest.fixture
    def manifest(self):
        """Load the manifest for tests."""
        with open(MANIFEST_PATH, "r") as f:
            return yaml.safe_load(f)

    def test_archive_paths_are_within_archive_dir(self, manifest):
        """All version paths should be within the archive/ directory."""
        for vid, info in manifest["versions"].items():
            path = info.get("path", "")
            assert path.startswith(
                "archive/"
            ), f"Version '{vid}' path '{path}' must be within archive/ directory"

    def test_placeholder_versions_documented(self, manifest):
        """Placeholder versions should be marked as such."""
        for vid, info in manifest["versions"].items():
            path = info.get("path", "")
            full_path = os.path.join(REPO_ROOT, path)

            # If the path doesn't exist, it should be marked as placeholder
            if not os.path.exists(full_path):
                assert info.get("placeholder", False), (
                    f"Version '{vid}' path '{path}' doesn't exist but isn't "
                    "marked as placeholder: true"
                )


class TestProtectionConsistency:
    """Tests verifying protection rules are consistent."""

    @pytest.fixture
    def manifest(self):
        """Load the manifest for tests."""
        with open(MANIFEST_PATH, "r") as f:
            return yaml.safe_load(f)

    def test_has_at_least_one_protected_version(self, manifest):
        """At least one version should be protected."""
        protected_count = sum(
            1 for info in manifest["versions"].values() if info.get("protected", False)
        )
        assert protected_count > 0, (
            "The manifest should have at least one protected version "
            "to demonstrate the RespectTheLoader pattern"
        )

    def test_protected_versions_are_majority(self, manifest):
        """Protected versions should be the majority (golden builds philosophy)."""
        versions = manifest["versions"]
        protected_count = sum(
            1 for info in versions.values() if info.get("protected", False)
        )
        total = len(versions)

        # At least half should be protected
        assert protected_count >= total // 2, (
            f"Only {protected_count}/{total} versions are protected. "
            "The golden builds philosophy suggests most versions should be protected."
        )
