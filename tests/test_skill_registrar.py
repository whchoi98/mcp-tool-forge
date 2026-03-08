from pathlib import Path
from mcp_to_cli.skill_registrar import SkillRegistrar


def test_register_skills(tmp_path):
    # Create mock skills directory
    skills_dir = tmp_path / "output" / "test-server" / "skill"
    skills_dir.mkdir(parents=True)
    (skills_dir / "tool-one.md").write_text("---\nname: tool-one\n---\nTest")
    (skills_dir / "tool-two.md").write_text("---\nname: tool-two\n---\nTest")

    # Register
    plugin_dir = tmp_path / "plugin"
    registrar = SkillRegistrar(plugin_dir=plugin_dir)
    count = registrar.register_skills(skills_dir, "test-server")

    assert count == 2
    assert (plugin_dir / "skills" / "test-server" / "tool-one.md").exists()
    assert (plugin_dir / "skills" / "test-server" / "tool-two.md").exists()
    assert (plugin_dir / "plugin.json").exists()


def test_register_skills_missing_dir(tmp_path):
    plugin_dir = tmp_path / "plugin"
    registrar = SkillRegistrar(plugin_dir=plugin_dir)
    count = registrar.register_skills(tmp_path / "nonexistent", "test-server")
    assert count == 0


def test_list_registered(tmp_path):
    plugin_dir = tmp_path / "plugin"
    skills = plugin_dir / "skills" / "server-a"
    skills.mkdir(parents=True)
    (skills / "t1.md").write_text("test")
    (skills / "t2.md").write_text("test")

    registrar = SkillRegistrar(plugin_dir=plugin_dir)
    result = registrar.list_registered()
    assert result == {"server-a": 2}


def test_list_registered_empty(tmp_path):
    plugin_dir = tmp_path / "plugin"
    registrar = SkillRegistrar(plugin_dir=plugin_dir)
    result = registrar.list_registered()
    assert result == {}
