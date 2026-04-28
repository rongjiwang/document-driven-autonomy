import tempfile
import unittest
from pathlib import Path

from scripts.validate_skill import validate_skill


class ValidateSkillTests(unittest.TestCase):
    def test_accepts_current_repo_shape(self):
        errors = validate_skill(Path(__file__).resolve().parents[1])

        self.assertEqual(errors, [])

    def test_requires_skill_frontmatter_name_and_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("---\nname: demo\n---\n\n# Demo\n", encoding="utf-8")

            errors = validate_skill(root)

        self.assertIn("SKILL.md frontmatter must include description", errors)

    def test_rejects_missing_references(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text(
                "---\nname: demo\ndescription: Demo skill.\n---\n\nSee [missing](references/missing.md).\n",
                encoding="utf-8",
            )

            errors = validate_skill(root)

        self.assertIn("SKILL.md links to missing local file: references/missing.md", errors)


if __name__ == "__main__":
    unittest.main()
