"""Tests for the skill registrar module.
스킬 등록기 모듈 테스트."""

from pathlib import Path
from mcp_to_cli.skill_registrar import SkillRegistrar


def test_register_skills(tmp_path):
    """Test registering skills from a directory.
    디렉터리에서 스킬 등록을 테스트합니다."""
    # Create mock skills directory / 모의 스킬 디렉터리 생성
    skills_dir = tmp_path / "output" / "test-server" / "skill"
    skills_dir.mkdir(parents=True)
    (skills_dir / "tool-one.md").write_text("---\nname: tool-one\n---\nTest")
    (skills_dir / "tool-two.md").write_text("---\nname: tool-two\n---\nTest")

    # Register skills to plugin directory / 플러그인 디렉터리에 스킬 등록
    plugin_dir = tmp_path / "plugin"
    registrar = SkillRegistrar(plugin_dir=plugin_dir)
    count = registrar.register_skills(skills_dir, "test-server")

    # Verify skills were copied and plugin.json created / 스킬이 복사되고 plugin.json이 생성되었는지 확인
    assert count == 2
    assert (plugin_dir / "skills" / "test-server" / "tool-one.md").exists()
    assert (plugin_dir / "skills" / "test-server" / "tool-two.md").exists()
    assert (plugin_dir / "plugin.json").exists()


def test_register_skills_missing_dir(tmp_path):
    """Test that registering from a missing directory returns zero.
    존재하지 않는 디렉터리에서 등록 시 0을 반환하는지 테스트합니다."""
    plugin_dir = tmp_path / "plugin"
    registrar = SkillRegistrar(plugin_dir=plugin_dir)
    count = registrar.register_skills(tmp_path / "nonexistent", "test-server")
    assert count == 0


def test_list_registered(tmp_path):
    """Test listing registered skills per server.
    서버별 등록된 스킬 목록 조회를 테스트합니다."""
    plugin_dir = tmp_path / "plugin"
    skills = plugin_dir / "skills" / "server-a"
    skills.mkdir(parents=True)
    (skills / "t1.md").write_text("test")
    (skills / "t2.md").write_text("test")

    registrar = SkillRegistrar(plugin_dir=plugin_dir)
    result = registrar.list_registered()
    assert result == {"server-a": 2}


def test_list_registered_empty(tmp_path):
    """Test listing when no skills are registered.
    등록된 스킬이 없을 때 목록 조회를 테스트합니다."""
    plugin_dir = tmp_path / "plugin"
    registrar = SkillRegistrar(plugin_dir=plugin_dir)
    result = registrar.list_registered()
    assert result == {}
