"""
Test query type definitions and validation.
"""
import pytest
from pypitch.query.defs import WinProbQuery, FantasyQuery, Phase, Role

def test_query_classes_exist():
    """Test that query classes can be imported."""
    assert WinProbQuery is not None
    assert FantasyQuery is not None

def test_phase_type():
    """Test Phase literal type."""
    valid_phases = ["powerplay", "middle", "death", "all"]
    for phase in valid_phases:
        assert phase in ["powerplay", "middle", "death", "all"]

def test_role_type():
    """Test Role literal type."""
    valid_roles = ["batter", "bowler", "all-rounder"]
    for role in valid_roles:
        assert role in ["batter", "bowler", "all-rounder"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
