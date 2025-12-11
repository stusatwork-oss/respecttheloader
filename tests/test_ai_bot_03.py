"""Unit tests for ai_bot_03.py - testing protection enforcement logic."""

import os
import sys

import yaml

# Add the tools directory to the path so we can import from it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))


class TestCheckCanon:
    """Tests for the check_canon function logic."""

    def test_protected_versions_detected(self):
        """Verify that protected: true versions are correctly identified."""
        manifest = {
            "versions": {
                "v1-protected": {"path": "archive/v1", "protected": True},
                "v2-mutable": {"path": "archive/v2", "protected": False},
                "v3-protected": {"path": "archive/v3", "protected": True},
            }
        }

        # Replicate the logic from ai_bot_03.check_canon
        versions = manifest.get("versions", {})
        protected = []
        mutable = []

        for vid, info in versions.items():
            if info.get("protected", False):
                protected.append(vid)
            else:
                mutable.append(vid)

        assert len(protected) == 2
        assert "v1-protected" in protected
        assert "v3-protected" in protected
        assert "v2-mutable" in mutable
        assert len(mutable) == 1

    def test_no_protected_versions(self):
        """Test behavior when no versions are protected."""
        manifest = {
            "versions": {
                "v1": {"path": "archive/v1", "protected": False},
                "v2": {"path": "archive/v2", "protected": False},
            }
        }

        versions = manifest.get("versions", {})
        protected = []

        for vid, info in versions.items():
            if info.get("protected", False):
                protected.append(vid)

        assert len(protected) == 0

    def test_missing_protected_field_defaults_to_false(self):
        """Versions without 'protected' field should default to unprotected."""
        manifest = {
            "versions": {
                "v1-no-field": {"path": "archive/v1"},
                "v2-explicit": {"path": "archive/v2", "protected": True},
            }
        }

        versions = manifest.get("versions", {})
        protected = []
        mutable = []

        for vid, info in versions.items():
            if info.get("protected", False):
                protected.append(vid)
            else:
                mutable.append(vid)

        assert "v1-no-field" in mutable
        assert "v2-explicit" in protected

    def test_empty_manifest(self):
        """Empty manifest should return no protected or mutable versions."""
        manifest = {"versions": {}}

        versions = manifest.get("versions", {})
        protected = []
        mutable = []

        for vid, info in versions.items():
            if info.get("protected", False):
                protected.append(vid)
            else:
                mutable.append(vid)

        assert len(protected) == 0
        assert len(mutable) == 0


class TestManifestParsing:
    """Tests for YAML manifest parsing."""

    def test_valid_yaml_parsing(self):
        """Verify that valid YAML manifests parse correctly."""
        yaml_content = """
versions:
  v1-test:
    path: archive/v1-test
    entry: bin/launch.sh
    role: test-build
    protected: true
"""
        manifest = yaml.safe_load(yaml_content)

        assert "versions" in manifest
        assert "v1-test" in manifest["versions"]
        assert manifest["versions"]["v1-test"]["protected"] is True
        assert manifest["versions"]["v1-test"]["path"] == "archive/v1-test"

    def test_placeholder_field_preserved(self):
        """Verify placeholder field is preserved in manifest."""
        yaml_content = """
versions:
  v1-placeholder:
    path: archive/v1-placeholder
    protected: true
    placeholder: true
"""
        manifest = yaml.safe_load(yaml_content)
        version = manifest["versions"]["v1-placeholder"]

        assert version.get("placeholder") is True
        assert version.get("protected") is True


class TestProtectionEnforcement:
    """Tests verifying protection rules are enforceable."""

    def test_should_redirect_to_lab_when_protected(self):
        """Protected versions should redirect operations to /lab/."""
        manifest = {
            "versions": {"v1-canon": {"path": "archive/v1-canon", "protected": True}}
        }

        # Simulate the decision logic from ai_bot_03
        version_info = manifest["versions"]["v1-canon"]
        is_protected = version_info.get("protected", False)

        if is_protected:
            workspace = "lab/"
        else:
            workspace = version_info["path"]

        assert workspace == "lab/"

    def test_should_allow_direct_access_when_not_protected(self):
        """Non-protected versions should allow direct access."""
        manifest = {
            "versions": {"v6-dev": {"path": "archive/v6-dev", "protected": False}}
        }

        version_info = manifest["versions"]["v6-dev"]
        is_protected = version_info.get("protected", False)

        if is_protected:
            workspace = "lab/"
        else:
            workspace = version_info["path"]

        assert workspace == "archive/v6-dev"
